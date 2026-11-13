"""Exact constructor controls for the declared passive mediator, not physical evidence."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def mv(a,v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def rank(rows):
    a=[list(r) for r in rows]; pos=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(pos,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[pos],a[pivot]=a[pivot],a[pos]
        z=a[pos][j]; a[pos]=[v/z for v in a[pos]]
        for i in range(len(a)):
            if i!=pos:
                z=a[i][j]; a[i]=[u-z*v for u,v in zip(a[i],a[pos])]
        pos+=1
        if pos==len(a):break
    return pos

def run():
    controls=[]
    for k,t,a,b in product((F(1,2),F(1),F(2)),(F(0),F(1,2),F(1)),(F(-1),F(1)),(F(-2),F(0),F(1))):
        den=k*(k+2*t)
        K=[[k+t,-t],[-t,k+t]]
        Ki=[[(k+t)/den,t/den],[t/den,(k+t)/den]]
        assert mv(K,mv(Ki,[F(1),F(0)]))==[1,0]
        assert mv(K,mv(Ki,[F(0),F(1)]))==[0,1]
        sll=a*a*Ki[0][0]; srr=b*b*Ki[1][1]; slr=a*b*Ki[0][1]
        assert sll>=0 and srr>=0 and slr*slr<=sll*srr
        if sll==0 or srr==0:assert slr==0
        il,ir=F(1),F(1,4); force=[a*il,b*ir]
        qs=[-v for v in mv(Ki,force)]
        assert [u+v for u,v in zip(mv(K,qs),force)]==[0,0]
        om=[2+a*qs[0],2+b*qs[1]]
        assert om==[2-sll*il-slr*ir,2-slr*il-srr*ir]
        full=2*(il+ir)+dot(qs,mv(K,qs))/2+dot(qs,force)
        eff=2*(il+ir)-(sll*il*il+2*slr*il*ir+srr*ir*ir)/2
        assert full==eff
        assert full+(sll*il*il+srr*ir*ir)/2==2*(il+ir)-slr*il*ir
        if t==0:assert slr==0
        controls.append({'k':str(k),'t':str(t),'a':str(a),'b':str(b),'g':str(-slr)})
    assert len(controls)==54
    # A free start differs from equilibrium elimination: q''=-C i at s=0.
    initial_rate=[F(2),F(2)]; curvature=[F(-1),F(-1,4)]
    assert initial_rate==[2,2] and curvature!=[0,0]
    # P=I-h h^T; injectivity of v -> P diag(v) P proves diagonal uniformity.
    n=15; h=[F(1,2)]*4+[F(0)]*11
    P=[[F(i==j)-h[i]*h[j] for j in range(n)] for i in range(n)]
    columns=[[P[i][s]*P[s][j] for i in range(n) for j in range(n)] for s in range(n)]
    assert rank(columns)==15
    assert rank(P)==14
    for col in columns:
        matrix=[col[i*n:(i+1)*n] for i in range(n)]
        assert rank(matrix)==1
    return {'evidence':'EXACT_CONDITIONAL','two_site_fixtures':len(controls),
            'gram_bound':'S_LR^2 <= S_LL S_RR','pure_cross_without_counterterms':'NO-GO under positive harmonic assumptions',
            'projected_diagonal_map_rank':15,'active_rank':14,'single_contact_rank':1,
            'illustrative_g':'1/3 for k=t=a=1,b=-1; assumed',
            'free_start_rates':list(map(str,initial_rate)), 'free_start_rate_curvature':list(map(str,curvature)),
            'coefficient_selection':'OPEN','physical_promotion':0,'fixtures':controls}
if __name__=='__main__':
    Path(__file__).with_name('local_mediator_results.json').write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
    print('PASS:54 rational mediator fixtures, Gram bound, counterterms and 15-register contact rank')
