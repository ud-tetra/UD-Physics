"""Exact block decomposition and outward-rounded first-loss certificate."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import json

from certified_interval import matrices, model_matrices
from stabilization_exact import add, eye, mm, sc, tr

BLOCKS = (
    ((F(3,2), 1), (1, 3), 1, 1),
    ((0, 0), (1, 0), 0, 2),
    ((0, 1), (1, 3), 0, 3),
)
DEGREE, STEPS = 28, 16
SCALE = 2**100
ZERO, ONE = (0, 0), (SCALE, SCALE)


def box(x):
    value = F(x)*SCALE
    return (value.numerator//value.denominator,
            -(-value.numerator//value.denominator))


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def times(a, b):
    values = [x*y for x, y in product(a, b)]
    return min(values)//SCALE, -(-max(values)//SCALE)


def mul(a, b):
    return tuple(plus(times(a[2*i], b[j]), times(a[2*i+1], b[j+2]))
                 for i in range(2) for j in range(2))


def fixed_pi():
    def atan(n):
        partial = sum(F((-1)**k, (2*k+1)*n**(2*k+1)) for k in range(32))
        return partial, partial+F(1,65*n**65)
    a, b = atan(5), atan(239)
    return box(16*a[0]-4*b[1])[0], box(16*a[1]-4*b[0])[1]


def trig_tables():
    pi = fixed_pi()
    pi_step = times(pi, box(F(1,STEPS)))
    assert F(22,7) < F(16,5)
    assert F(16,5)**81/factorial(81) < F(1,SCALE)
    tables = []
    for step in range(STEPS):
        theta = times(pi_step, box(step))
        power = ONE
        cosine, sine = ZERO, ZERO
        for k in range(81):
            term = times(power, box((-1)**(k//2)))
            if k % 2:
                sine = plus(sine, term)
            else:
                cosine = plus(cosine, term)
            power = times(times(power, theta), box(F(1,k+1)))
        cosine = plus(cosine, (-1,1))
        sine = plus(sine, (-1,1))
        power = ONE
        table = []
        for k in range(DEGREE):
            factor = times(power, box(F(1,factorial(k))))
            # kth derivative of cos/sin with respect to the step variable.
            table.append((times(factor,cosine),times(factor,sine)))
            cosine, sine = times(sine,box(-1)),cosine
            power = times(power,pi_step)
        tables.append(table)
    return tables, times(pi_step, box(F(1,2)))


def half_segment(rho, block, tables, time_step):
    bc, bs, cross, _ = block
    constants = [times(time_step,box(1-rho+rho*(F(x)+y)/2))
                 for x,y in zip(bc,bs)]
    cosines = [times(time_step,box(rho*(F(x)-y)/2)) for x,y in zip(bc,bs)]
    off = times(time_step,box(rho*F(cross,2)))
    negative = box(-1)
    tail = box(F(64,3*4**(DEGREE+1)))[1]
    result = (ONE,ZERO,ZERO,ONE)
    divisors = [box(F(1,k+1)) for k in range(DEGREE)]
    for table in tables:
        coeffs = []
        for k,(cosine,sine) in enumerate(table):
            a,b = [plus(constants[i] if k==0 else ZERO,times(cosines[i],cosine))
                   for i in range(2)]
            x = times(off,sine)
            coeffs.append((times(negative,x),times(negative,b),a,x))
        terms = [(ONE,ZERO,ZERO,ONE)]
        total = terms[0]
        for k in range(DEGREE):
            term = [ZERO]*4
            for j in range(k+1):
                term = list(map(plus,term,mul(coeffs[j],terms[k-j])))
            terms.append(tuple(times(y,divisors[k]) for y in term))
            total = tuple(map(plus,total,terms[-1]))
        result = mul(tuple(plus(v,(-tail,tail)) for v in total),result)
    return result


def verify_blocks():
    J,P,T = matrices()
    _,_,*hessians = model_matrices()
    hessians = [mm(mm(P,B),P) for B in hessians]
    frequencies = (F(19,256),F(35,64),F(3,64))
    basis = []
    for index,(a,block) in enumerate(zip(frequencies,BLOCKS)):
        Q = P
        for b in frequencies:
            if b != a:
                Q = sc(mm(Q,add(mm(T,T),sc(P,b))),1/(b-a))
        bc,bs,cross,count = block
        seeds = (Q if index==0 else mm(hessians[1],Q) if index==1
                 else mm(add(P,sc(hessians[0],-1)),Q))
        found = 0
        for seed in tr(seeds):
            v = seed
            for u in basis:
                dot = lambda x,y: sum(p*q for p,q in zip(x,y))
                v = [x-dot(v,u)/dot(u,u)*y for x,y in zip(v,u)]
            if not any(v):
                continue
            jv = [sum(x*y for x,y in zip(row,v)) for row in J]
            W = tr([v,jv])
            assert mm(J,W)==mm(W,[[0,-1],[1,0]])
            assert mm(tr(W),W)==sc(eye(2),sum(x*x for x in v))
            for B, reduced in zip(hessians, [[[bc[0],0],[0,bc[1]]],
                                            [[bs[0],0],[0,bs[1]]],
                                            [[0,cross],[cross,0]]]):
                assert mm(B,W)==mm(W,reduced)
            assert mm(P,W)==W
            basis.extend([v,jv])
            found += 1
        assert found==count
    assert len(basis)==12


def bernstein_weights(n):
    nodes = [F(i,n-1) for i in range(n)]
    columns = []
    for i,u in enumerate(nodes):
        power = [F(1)]
        for j,v in enumerate(nodes):
            if j==i:
                continue
            expanded = [F(0)]*(len(power)+1)
            for k,c in enumerate(power):
                expanded[k] -= v*c/(u-v)
                expanded[k+1] += c/(u-v)
            power = expanded
        columns.append([sum(power[k]*F(comb(j,k),comb(n-1,k)) for k in range(j+1))
                        for j in range(n)])
    return tr(columns)


def enclose(values, weights):
    out = []
    for row in weights:
        lo = hi = F(0)
        for w,v in zip(row,values):
            low,high = sorted((w*v[0],w*v[1]))
            lo += low/SCALE
            hi += high/SCALE
        out.append((lo,hi))
    return out


def run():
    verify_blocks()
    # Uniform analytic bounds used in the written proof.
    assert F(22,7)/2*F(17,4)<10
    assert F(11,4)**5<16**2
    assert F(11,4)**13<1024**2
    tables, dt = trig_tables()
    lo_mu, hi_mu = F(31,5), F(621,100)
    rho = lambda mu: mu/(mu+2)
    lower, upper = rho(lo_mu),rho(hi_mu)
    start = F(1,129)
    n, cells = 8, 24
    weights = bernstein_weights(n)
    derivative_cap = lambda k: 1024*F(55,7)**k/factorial(k)
    bounds = [None]*3
    for i,block in enumerate(BLOCKS):
        count = cells if i==2 else 25
        end = lower if i==2 else upper
        for cell in range(count):
            left = start+(end-start)*cell/count
            width = (end-start)/count
            nodes = [half_segment(left+width*F(k,n-1),block,tables,dt) for k in range(n)]
            error = derivative_cap(n)*width**n
            signs = (1,-1,1,1) if i==1 else (-1,-1,1,-1)
            for j,sgn in enumerate(signs):
                coefficients = enclose([u[j] for u in nodes],weights)
                margin = min(x[0] if sgn==1 else -x[1] for x in coefficients)-error
                assert margin>0,(i,cell,j,float(margin))
                bounds[i] = margin if bounds[i] is None else min(bounds[i],margin)
        print('Certified block',i+1,flush=True)

    width = upper-lower
    nodes = [half_segment(lower+width*F(k,n-1),BLOCKS[2],tables,dt) for k in range(n)]
    error = derivative_cap(n)*width**n
    for j,sgn in [(1,-1),(2,1),(3,-1)]:
        coefficients = enclose([u[j] for u in nodes],weights)
        assert min(x[0] if sgn==1 else -x[1] for x in coefficients)>error
    coefficients = enclose([u[0] for u in nodes],weights)
    derivative_error = (n*derivative_cap(n)*width**(n-1)
                        +derivative_cap(n+1)*width**n)
    slope = min((n-1)*(b[0]-a[1])/width
                for a,b in zip(coefficients,coefficients[1:]))-derivative_error
    assert slope>0
    assert F(nodes[0][0][1],SCALE)<0<F(nodes[-1][0][0],SCALE)
    assert min(bounds)>F(1,100000)
    assert slope>F(1,2)
    tight_lo, tight_hi = F(77511,12500), F(62009,10000)
    assert lo_mu < tight_lo < tight_hi < hi_mu
    a_lo = half_segment(rho(tight_lo),BLOCKS[2],tables,dt)[0]
    a_hi = half_segment(rho(tight_hi),BLOCKS[2],tables,dt)[0]
    assert F(a_lo[1],SCALE)<-F(1,10**7)
    assert F(a_hi[0],SCALE)>F(1,10**7)
    result = dict(evidence='EXACT_CONDITIONAL', stable_through=str(tight_lo),
                  first_loss_open_bracket=[str(tight_lo),str(tight_hi)],
                  monotonicity_bracket=[str(lo_mu),str(hi_mu)],
                  trigger='unique a=0 in the third reduced block, multiplicity three, half-return multiplier -1',
                  certified_sign_margin_floor='1/100000', bracket_da_drho_lower='1/2',
                  integration=dict(binary_fraction_bits=100,time_steps=STEPS,taylor_degree=DEGREE,
                                   interpolation_nodes=n,parameter_cells=[25,25,24,1]),
                  physical_promotion=0)
    Path(__file__).with_name('stability_boundary_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    run()
