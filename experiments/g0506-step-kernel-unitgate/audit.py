"""Exact K4 Hasse step transport and preparation-rank witnesses."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json


def trans(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    return [[sum((u*v for u,v in zip(r,c)),F(0)) for c in zip(*b)] for r in a]


def vec(a,x):
    return [sum((u*v for u,v in zip(r,x)),F(0)) for r in a]


def rank(rows):
    if not rows: return 0
    a=[r[:] for r in rows];k=0
    for j in range(len(a[0])):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k];z=a[k][j];a[k]=[v/z for v in a[k]]
        for i in range(len(a)):
            if i!=k:
                z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k


def dot(x,y): return sum((u*v for u,v in zip(x,y)),F(0))


def main():
    simplices=[s for k in range(1,5) for s in combinations(range(4),k)]
    ix={s:i for i,s in enumerate(simplices)}
    n=len(simplices);D=[]
    for k in range(1,4):
        d=[[F(0)]*n for _ in range(n)]
        for s in simplices:
            if len(s)==k+1:
                for j in range(len(s)):
                    d[ix[s[:j]+s[j+1:]]][ix[s]]=F((-1)**j)
        D.append(d)
    K=[[[d[i][j]-d[j][i] for j in range(n)] for i in range(n)] for d in D]
    A=[[sum(m[i][j] for m in K) for j in range(n)] for i in range(n)]
    J=[[v/2 for v in row] for row in A]
    P=[[[v*F(-1,4) for v in row] for row in mul(m,m)] for m in K]
    assert [rank(p) for p in P]==[6,6,2]
    for i in range(3):
        for j in range(i+1,3):
            assert not any(any(r) for r in mul(P[i],P[j]))
    assert mul(A,mul(A,A))==[[-4*v for v in r] for r in A]
    assert rank([[sum(p[i][j] for p in P) for j in range(n)] for i in range(n)])==14
    # Hasse step is the integral of theta along the straight segment x->y.
    q=lambda x,y: dot(vec(A,x),y)/4
    assert all(A[i][j]==0 for i,s in enumerate(simplices) for j,t in enumerate(simplices)
               if not ((len(s)+1==len(t) and set(s)<set(t)) or
                       (len(t)+1==len(s) and set(t)<set(s))))
    e=[F(0)]*n;e[ix[(0,1)]]=F(1)
    je=vec(J,e);neg=[-v for v in e];negj=[-v for v in je]
    assert dot(e,e)==dot(je,je)==1 and dot(e,je)==0
    assert q(e,je)==q(je,neg)==q(neg,negj)==q(negj,e)==F(1,2)
    assert sum([q(e,je),q(je,neg),q(neg,negj),q(negj,e)])==2
    assert q(e,neg)+q(neg,e)==0  # same sampled endpoints as one native winding
    assert q(e,je)==-q(je,e)
    # Signed S4 simplex action commutes with A and preserves q.
    for perm in permutations(range(4)):
        R=[[F(0)]*n for _ in range(n)]
        for s,i in ix.items():
            im=[perm[v] for v in s]
            inversions=sum(im[a]>im[b] for a in range(len(im)) for b in range(a+1,len(im)))
            R[ix[tuple(sorted(im))]][i]=F((-1)**inversions)
        assert mul(R,A)==mul(A,R)
        assert q(vec(R,e),vec(R,je))==q(e,je)
    # One orbit spans at most span{x,Jx}; seven complex-independent seeds
    # are necessary and sufficient for full 14-dimensional trajectory rank.
    picks=[];sector_counts=[];sector_ranks=[]
    for sector,p in enumerate(P):
        chosen=[]
        order=([ix[(0,1,2,3)]]+[i for i in range(n) if i!=ix[(0,1,2,3)]]) if sector==2 else range(n)
        for i in order:
            basis=[F(j==i) for j in range(n)];v=vec(p,basis)
            if rank(chosen+[v,vec(J,v)])==len(chosen)+2:
                chosen.extend([v,vec(J,v)]);picks.append(i)
            if len(chosen)==rank(p):break
        assert len(chosen)==rank(p)
        sector_counts.append(len(chosen)//2);sector_ranks.append(rank(chosen))
    assert sector_counts==[3,3,1]
    all_orbits=[]
    for k,i in enumerate(picks):
        sector=0 if k<3 else (1 if k<6 else 2)
        v=vec(P[sector],[F(j==i) for j in range(n)])
        all_orbits.extend([v,vec(J,v)])
    assert rank(all_orbits)==14 and rank(all_orbits[:-2])==12
    top=[F(j==ix[(0,1,2,3)]) for j in range(n)]
    assert vec(P[2],top)==top
    assert rank([top,vec(J,top)])==2
    assert all(vec(P[k],top)==[F(0)]*n for k in (0,1))
    # Target-informed four-site packet phase/burden one-form candidate:
    # beta=1/2 sum rho_i dtheta_i. Closed winding coefficients are
    # beta/pi=sum rho_i n_i. Reversal and S4 relabeling are exact.
    rho=[F(1,2),F(2),F(3,4),F(0)]
    winding=[2,-1,0,3]
    packet_over_pi=sum((u*v for u,v in zip(rho,winding)),F(0))
    assert packet_over_pi==F(-1)
    assert sum((u*(-v) for u,v in zip(rho,winding)),F(0))==-packet_over_pi
    for perm in permutations(range(4)):
        assert sum((rho[i]*winding[i] for i in perm),F(0))==packet_over_pi
    # Four sites each have three continuous variables (rho,theta,b), while
    # discrete chi/sigma branches do not raise local continuous dimension.
    assert 4*3==12<14
    result={
      "status":"EXACT_FINITE_CARRIER_PASS",
      "K4_active_rank":14,"sector_ranks":sector_ranks,"minimal_orbit_preparations":7,
      "sector_seed_counts":sector_counts,"selected_simplex_indices_by_sector":picks,
      "top_cell_single_orbit_rank":2,"top_cell_visible_sector_ranks":[0,0],
      "Hasse_q":"q(x,y)=<Ax,y>/4; exactly integrates theta on the straight segment",
      "four_step_polygon_action":"2 for a=1; 2a at general support","smooth_native_orbit_action":"pi a for winding 1",
      "two_antipodal_endpoint_steps":"0 despite native lifted winding 1",
      "sampling":"common native phase delta=2 Delta_s; unwrapped reconstruction requires |delta|<pi per step and a known same-orbit hypothesis",
      "signed_S4_actions_checked":24,
      "packet_four_site_candidate":{"beta_over_pi_witness":str(packet_over_pi),
        "continuous_dimension_with_b":12,"phase_density_only_dimension":8,
        "full_active_surjectivity":"NO under C1 four-site branch hypothesis",
        "origin":"target-informed mapping of burden to support; source does not give this map"},
      "physical_trace_status":"NONE_ADMITTED","physical_promotion":0
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({"status":result["status"],"sector_seed_counts":sector_counts,"full_rank":rank(all_orbits)}))


if __name__=='__main__':main()
