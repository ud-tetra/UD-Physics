"""Exact heart/shell mode and volume audit; no numerical eigensolver."""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import importlib.util
import json

source = Path(__file__).resolve().parents[1] / 'k5-four-cell' / 'analyze.py'
spec = importlib.util.spec_from_file_location('k5_exact', source)
k5 = importlib.util.module_from_spec(spec); spec.loader.exec_module(k5)


def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(a,x): return [dot(r,x) for r in a]
def plus(x,y,c=1): return [a+c*b for a,b in zip(x,y)]
def scale(c,x): return [c*a for a in x]
def gram(vs): return [[dot(x,y) for y in vs] for x in vs]
def columns(vs): return list(map(list, zip(*vs)))
def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def volume(points):
    return abs(Q(det3([[points[i][j]-points[0][j] for j in range(3)] for i in (1,2,3)]),6))


def main():
    tops=[(0,1,2,3),(0,1,2,4),(0,1,3,4),(0,2,3,4)]
    cells,bs,a,_=k5.inspect(tops); flat=[s for g in cells for s in g]; ix={s:i for i,s in enumerate(flat)}
    def unit(s):
        v=[0]*29;v[ix[s]]=1;return v
    def lin(terms):
        out=[0]*29
        for c,s in terms:out=plus(out,unit(s),c)
        return out
    heart=unit((0,)); s=lin([(1,(i,)) for i in range(5)])
    contrast=lin([(4,(0,))]+[(-1,(i,)) for i in range(1,5)])
    spoke=lin([(1,(0,i)) for i in range(1,5)])
    assert mv(a,s)==[0]*29
    assert mv(a,heart)==spoke and mv(a,contrast)==scale(5,spoke) and mv(a,spoke)==scale(-1,contrast)
    assert plus(s,contrast)==scale(5,heart)
    assert gram([s,contrast,spoke])==[[5,0,0],[0,20,0],[0,0,4]]
    # All powers of A applied to the heart stay in this three-dimensional space.
    krylov=[];w=heart
    for _ in range(30):krylov.append(w);w=mv(a,w)
    heart_rank=k5.rank(columns(krylov));assert heart_rank==3
    assert all(w[ix[t]]==0 for w in krylov for t in cells[2]+cells[3])
    # Shell vertex contrasts span a three-dimensional heart-dark family.
    shell_contrasts=[plus(unit((i,)),unit((4,)),-1) for i in (1,2,3)]
    for w in shell_contrasts:
        aw=mv(a,w);assert mv(a,aw)==scale(-5,w)
        assert dot(heart,w)==0 and dot(heart,aw)==0
    # Coherent top-cell orientation signs are minus the four corresponding boundary-of-4-simplex signs.
    coherent=[-(-1)**next(v for v in range(5) if v not in t) for t in cells[3]]
    top_basis=[scale(sign,unit(t)) for t,sign in zip(cells[3],coherent)]
    top_sum=[sum(row) for row in zip(*top_basis)]; shell_cycle=mv(a,top_sum)
    assert dot(top_sum,top_sum)==4 and dot(shell_cycle,shell_cycle)==4
    assert mv(a,shell_cycle)==scale(-1,top_sum)
    assert all(shell_cycle[ix[t]]==0 for t in cells[2] if 0 in t)
    top_gram=gram([mv(a,w) for w in top_basis])
    assert top_gram==[[5*int(i==j)-1 for j in range(4)] for i in range(4)]
    cell_contrasts=[plus(top_basis[i],top_basis[3],-1) for i in range(3)]
    for w in cell_contrasts:
        aw=mv(a,w);assert mv(a,aw)==scale(-5,w)
        assert all(v[ix[t]]==0 for v in (w,aw) for t in cells[0]+cells[1])
    assert all(dot(v,w)==0 for v in (s,contrast,spoke) for w in [top_sum,shell_cycle]+cell_contrasts)
    # Under S4, the coherent top-cell sum has the orientation character; the heart is a scalar.
    for p in permutations(range(1,5)):
        perm=(0,)+p; sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        acted=[0]*29
        for t in cells[3]:
            word=tuple(perm[v] for v in t)
            orientation=(-1)**sum(word[i]>word[j] for i in range(4) for j in range(i+1,4))
            acted[ix[tuple(sorted(word))]]+=orientation*top_sum[ix[t]]
        assert acted==scale(sign,top_sum)
    # Exact barycentric geometry: outer vertices fixed, interior point moves.
    outer=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    total=volume(outer);assert total==Q(8,3)
    gradients=[scale(Q(total,4),v) for v in outer]
    assert k5.rank(gradients)==3 and all(sum(row[j] for row in gradients)==0 for j in range(3))
    for h in [(0,0,0),(Q(1,10),Q(1,20),Q(-1,30)),(Q(-1,5),Q(1,10),Q(1,15))]:
        fractions=[Q(1+dot(v,h),4) for v in outer]
        assert min(fractions)>0 and sum(fractions)==1
        measured=[volume([h]+[v for j,v in enumerate(outer) if j!=i]) for i in range(4)]
        assert measured==[total*x for x in fractions] and sum(measured)==total
    for eps in [Q(-1,10),Q(0),Q(1,5)]:
        grown=[scale(1+eps,v) for v in outer]
        assert volume(grown)==(1+eps)**3*total
        assert all(volume([(0,0,0)]+[v for j,v in enumerate(grown) if j!=i])==(1+eps)**3*total/4 for i in range(4))
    # Candidate scalar port model L=alpha*Ls+beta*Lo: check coefficient matrices separately,
    # proving the mode identities for arbitrary alpha,beta without parameter sampling.
    def lap(edges):
        l=k5.zeros(5,5)
        for i,j in edges:l[i][i]+=1;l[j][j]+=1;l[i][j]-=1;l[j][i]-=1
        return l
    ls=lap([(0,i) for i in range(1,5)]);lo=lap(list(combinations(range(1,5),2)))
    u=[1]*5;q=[4,-1,-1,-1,-1]
    assert mv(ls,u)==mv(lo,u)==[0]*5
    assert mv(ls,q)==scale(5,q) and mv(lo,q)==[0]*5
    for i in range(1,4):
        d=[0]*5;d[i]=1;d[4]=-1
        assert mv(ls,d)==d and mv(lo,d)==scale(4,d)
    return {'status':'PASS','scope':'Exact for declared real H=I chain model, fixed-shell Euclidean geometry, and separately assumed scalar port potential.',
        'heart_krylov_dimension':heart_rank,'heart_basis_gram':gram([s,contrast,spoke]),
        'heart_seed_flow':{'heart':'(1+4*cos(sqrt(5)*u))/5','each_outer_vertex':'(1-cos(sqrt(5)*u))/5','each_outward_spoke':'sin(sqrt(5)*u)/sqrt(5)','faces_and_cells':'identically zero'},
        'mode_families':[{'name':'heart-shell collective','oscillator_copies':1,'frequency':'sqrt(5)','heart_visible':True}, {'name':'shell vertex differences','oscillator_copies':3,'frequency':'sqrt(5)','heart_visible':False}, {'name':'coherent cell/shell-cycle pair','oscillator_copies':1,'frequency':'1','heart_visible':False}, {'name':'cell differences','oscillator_copies':3,'frequency':'sqrt(5)','heart_visible':False}],
        'cell_gram_coherent':top_gram,'S4_top_collective_character':'sign; heart vertex trivial',
        'geometry':{'parent_volume':str(total),'cell_fraction':'lambda_i(h)=(1+r_i dot h)/4','heart_displacement_volume_jacobian':[[str(x) for x in row] for row in gradients],'jacobian_rank':3,'total_volume_change_heart_only':'0 exactly while inside fixed shell','uniform_shell_scale_volume':'V_i(eps)=(1+eps)^3*V/4'},
        'candidate_scalar_port_model':{'potential':'alpha/2 sum_i(q_i-q_0)^2 + beta/2 sum_i<j(q_i-q_j)^2','assumptions':'unit model inertia; alpha>0,beta>=0; q_0 internal scalar, not centre position','relative_collective_omega_squared':'5*alpha','three_differential_omega_squared':'alpha+4*beta','common_mode':'free (Q_ddot=0); fixed zero velocity is an additional initial condition','geometric_readout':'OPEN','damping_and_active_pump':'absent'}}

if __name__=='__main__':print(json.dumps(main(),indent=2))
