"""Exact positive-energy scalar-heart/radial-shell model; standard library only."""
from fractions import Fraction as Q
from itertools import permutations, combinations
import json


def zeros(n,m): return [[Q(0) for _ in range(m)] for _ in range(n)]
def transpose(a): return list(map(list,zip(*a)))
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def mv(a,x): return [sum(v*w for v,w in zip(r,x)) for r in a]
def plus(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a): return [[c*x for x in r] for r in a]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def lap(edges):
    k=zeros(5,5)
    for i,j in edges:k[i][i]+=1;k[j][j]+=1;k[i][j]-=1;k[j][i]-=1
    return k

def stiffness(kh,ks,g,j):
    heart=zeros(5,5);heart[0][0]=1
    shell=eye(5);shell[0][0]=0
    return plus(plus(scale(kh,heart),scale(ks,shell)),plus(scale(g,lap([(0,i) for i in range(1,5)])),scale(j,lap(list(combinations(range(1,5),2))))))
def mass(ih,is_):
    m=zeros(5,5)
    for i in range(5):m[i][i]=ih if i==0 else is_
    return m

def padd(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def pmul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def det_poly(a):
    n=len(a);total=[Q(0)]
    for p in permutations(range(n)):
        term=[Q((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))]
        for i in range(n):term=pmul(term,a[i][p[i]])
        total=padd(total,term)
    return total

def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def volume(points):return abs(det3([[points[i][j]-points[0][j] for j in range(3)] for i in (1,2,3)])/6)


def main():
    # Coordinates (a,b,d1,d2,d3); d4=-d1-d2-d3. Coefficient identities prove all parameter cases.
    s=[[1,0,0,0,0],[0,1,1,0,0],[0,1,0,1,0],[0,1,0,0,1],[0,1,-1,-1,-1]]
    gram=[[1+int(i==j) for j in range(3)] for i in range(3)]
    for pars in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
        kh,ks,g,j=pars;transformed=mul(mul(transpose(s),stiffness(*pars)),s)
        expected=zeros(5,5);expected[0][0]=kh+4*g;expected[0][1]=expected[1][0]=-4*g;expected[1][1]=4*(ks+g)
        for i in range(3):
            for l in range(3):expected[i+2][l+2]=(ks+g+4*j)*gram[i][l]
        assert transformed==expected
    for ih,is_ in [(1,0),(0,1)]:
        tr=mul(mul(transpose(s),mass(ih,is_)),s);expected=zeros(5,5);expected[0][0]=ih;expected[1][1]=4*is_
        for i in range(3):
            for j in range(3):expected[i+2][j+2]=is_*gram[i][j]
        assert tr==expected
    cases=[(Q(1),Q(1),Q(1),Q(1,2),Q(1),Q(1)),(Q(0),Q(2),Q(3,2),Q(0),Q(2),Q(3)),(Q(3),Q(0),Q(1,3),Q(2,5),Q(4),Q(1,2)),(Q(2,3),Q(5,7),Q(3,4),Q(1,9),Q(7,3),Q(2,5))]
    for kh,ks,g,j,ih,is_ in cases:
        k=stiffness(kh,ks,g,j);m=mass(ih,is_)
        actual=det_poly([[[k[i][l],-m[i][l]] for l in range(5)] for i in range(5)])
        dc=padd(pmul([kh+4*g,-ih],[ks+g,-is_]),[-4*g*g]);diff=[ks+g+4*j,-is_]
        assert actual==pmul(dc,pmul(diff,pmul(diff,diff)))
        d0=(kh+4*g)*(ks+g)-4*g*g
        assert d0==kh*ks+kh*g+4*g*ks and d0>0
        assert 4*(ks+g)-16*g*g/(kh+4*g)==4*d0/(kh+4*g)
        # Full first-order Hamiltonian operator conserves kinetic+potential quadratic energy.
        a=zeros(10,10);h=zeros(10,10)
        for i in range(5):
            a[i][i+5]=1
            for l in range(5):a[i+5][l]=-k[i][l]/m[i][i];h[i][l]=k[i][l]
            h[i+5][i+5]=m[i][i]
        assert plus(mul(transpose(a),h),mul(h,a))==zeros(10,10)
    # Exact demonstrator: (Kh,Ks,Kc,Kt,Ih,Is)=(1,1,1,1/2,1,1).
    k=stiffness(Q(1),Q(1),Q(1),Q(1,2));ones=[Q(1)]*5;relative=[Q(4),Q(-1),Q(-1),Q(-1),Q(-1)]
    assert mv(k,ones)==ones and mv(k,relative)==[6*x for x in relative]
    for i in range(1,4):
        v=[Q(0)]*5;v[i]=1;v[4]=-1;assert mv(k,v)==[4*x for x in v]
    for p in permutations(range(1,5)):
        perm=(0,)+p;assert all(k[perm[i]][perm[j]]==k[i][j] for i in range(5) for j in range(5))
    # Heart-only initial strain a0=1/10 decomposes into two exact mode vectors.
    a0=Q(1,10);cminus=a0/5;cplus=a0/5
    initial=[cminus*x+cplus*y for x,y in zip(ones,relative)]
    assert initial==[a0,0,0,0,0]
    initial_energy=dot(initial,mv(k,initial))/2;assert initial_energy==Q(1,40)<Q(1,2)
    # Zero-coupling and unpinned counterexamples.
    decoupled=stiffness(1,1,0,1);assert mv(decoupled,[1,0,0,0,0])[1:]==[0]*4
    unpinned=stiffness(0,0,1,1);assert mv(unpinned,ones)==[0]*5
    # Exact radial geometry and nonlinear volume readout.
    outer=[tuple(map(Q,r)) for r in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]];v0=volume(outer);assert v0==Q(8,3)
    for strains in [(Q(0),)*4,(Q(1,10),)*4,(Q(1,10),Q(-1,10),Q(0),Q(0)),(Q(1,5),Q(-1,10),Q(1,20),Q(-1,30))]:
        radii=[1+x for x in strains];vertices=[tuple(s*x for x in r) for s,r in zip(radii,outer)]
        cells=[volume([(Q(0),)*3]+[r for l,r in enumerate(vertices) if l!=i]) for i in range(4)]
        products=[]
        for i in range(4):
            product=Q(1)
            for l in range(4):
                if l!=i:product*=radii[l]
            products.append(v0*product/4)
        assert cells==products and sum(cells)==volume(vertices)
        b=sum(strains)/4;ds=[x-b for x in strains]
        nonlinear=(1+b)**3-(1+b)*sum(x*x for x in ds)/4+sum(x**3 for x in ds)/12
        assert sum(cells)/v0==nonlinear
    # Coefficient-level check of linear volume Jacobian: 3b-d_i, and sum=12b.
    jac=[[Q(i!=j) for j in range(4)] for i in range(4)]
    assert mv(jac,[1]*4)==[3]*4
    for i in range(3):
        d=[0]*4;d[i]=1;d[3]=-1;assert mv(jac,d)==[-x for x in d]
    return {'status':'PASS','scope':'Declared scalar-heart/radial-shell model; exact algebra, no fit or native UD force-law claim.',
        'positive_energy':'Kh*a^2/2 + Ks*sum(q_i^2)/2 + Kc*sum((q_i-a)^2)/2 + Kt*sum_i<j((q_i-q_j)^2)/2',
        'stability_sufficient':'Ih,Is,Kc>0; Kh,Ks,Kt>=0; Kh+Ks>0',
        'collective_determinant_D0':'Kh*Ks+Kh*Kc+4*Kc*Ks',
        'collective_squared_frequencies':'(A+B +/- sqrt((A-B)^2+16*Kc^2/(Ih*Is)))/2; A=(Kh+4*Kc)/Ih,B=(Ks+Kc)/Is',
        'three_differential_squared_frequencies':'(Ks+Kc+4*Kt)/Is',
        'volume_readout':{'cell_opposite_i':'V0/4*product_{j!=i}(1+q_j)','total_over_V0':'(1+b)^3-(1+b)*sum(d_i^2)/4+sum(d_i^3)/12','uniform_cell':'V0/4*(1+b)^3','linear_cell_delta':'V0/4*(3*b-d_i)'},
        'heart_to_linear_volume_transfer':'3*V0*Kc/((Kh+4*Kc-Ih*w^2)*(Ks+Kc-Is*w^2)-4*Kc^2)',
        'coupling_pressure_uniform_shell':'4*Kc*(a-b)/(3*V0*(1+b)^2)',
        'example':{'parameters':{'Kh':'1','Ks':'1','Kc':'1','Kt':'1/2','Ih':'1','Is':'1'},'heart_initial_strain':str(a0),'other_initial_coordinates_and_velocities':'0','energy':str(initial_energy),'squared_frequencies':['1','6','4 (three copies)'],'a(u)':'a0*(cos(u)+4*cos(sqrt(6)*u))/5','b(u)':'a0*(cos(u)-cos(sqrt(6)*u))/5','each_cell_volume':'V0/4*(1+b(u))^3','uniform_shell_bound':'abs(b)<=2*abs(a0)/5=1/25'},
        'checks':{'parameter_coefficient_stiffness_blocks':4,'parameter_coefficient_mass_blocks':2,'rational_full_determinants_and_energy_skewness':len(cases),'example_S4_permutations':24,'rational_geometry_cases':4},
        'limitations':['Restricted radial ansatz excludes angular/shear modes.','Uniform sector invariant requires symmetric couplings and symmetric preparation/forcing.','Passive energy law supplies bounded exchange, not an autonomous pump.','Physical energy/clock units and native variable/parameter selection OPEN.']}

if __name__=='__main__':print(json.dumps(main(),indent=2))
