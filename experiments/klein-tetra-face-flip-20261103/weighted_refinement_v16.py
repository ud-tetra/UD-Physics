#!/usr/bin/env python3
"""Exact recursive K4 boundary response under CHOSEN generation edge weights."""
import itertools,json
import sympy as s

def levels(N):
 t=[(0,1,2,3)];edge_birth={};z=4
 yield 0,t.copy(),edge_birth.copy()
 for n in range(1,N+1):
  nxt=[]
  for T in t:
   c=z;z+=1
   for v in T: edge_birth[tuple(sorted((v,c)))]=n
   for k in range(4): nxt.append(tuple(sorted(T[:k]+T[k+1:]+(c,))))
  t=nxt
  yield n,t.copy(),edge_birth.copy()

def alpha(n,g):
 return s.Integer(1)+sum((s.Rational(11,4)**(k-1)*g(k)/4 for k in range(1,n+1)),s.Integer(0))

def response(t,birth,g):
 vertices=sorted({v for T in t for v in T})
 edges=sorted({e for T in t for e in itertools.combinations(T,2)})
 ids={v:i for i,v in enumerate(vertices)}
 L=s.zeros(len(vertices))
 for a,c in edges:
  j=birth.get((a,c),0);w=s.Integer(1) if j==0 else g(j)
  if not w>0:raise ValueError('Schur requires positive edge weights')
  i,k=ids[a],ids[c]
  L[i,i]+=w;L[k,k]+=w;L[i,k]-=w;L[k,i]-=w
 B=list(range(4));I=list(range(4,len(vertices)))
 return L.extract(B,B)-L.extract(B,I)*L.extract(I,I).inv()*L.extract(I,B) if I else L.extract(B,B)

def weighted_current_check(t,birth,g):
 vertices=sorted({v for T in t for v in T})
 edges=sorted({e for T in t for e in itertools.combinations(T,2)})
 ids={v:i for i,v in enumerate(vertices)}
 E=s.zeros(len(vertices),len(edges))
 for j,(a,c) in enumerate(edges):
  E[ids[a],j]=-1;E[ids[c],j]=1
 W=s.diag(*[s.Integer(1) if birth.get(e,0)==0 else g(birth[e]) for e in edges])
 n,m=E.shape;A=s.zeros(n+m)
 A[:n,n:]=-E*W
 A[n:,:n]=E.T
 H=s.diag(s.eye(n),W)
 assert A.T*H+H*A==s.zeros(n+m)
 return {'vertices':n,'edges':m,'H_skew':True}

def run():
 cases={}
 for name,g in [('unchanged_Q169_unit',lambda k:s.Integer(1)),
                ('CANDIDATE_quarter_geometric_proxy',lambda k:s.Rational(1,4)**(k-1))]:
  rows=[]
  for n,t,birth in levels(3):
   K=response(t,birth,g)
   assert K==alpha(n,g)*(4*s.eye(4)-s.ones(4))
   for pi in itertools.permutations(range(4)):
    P=s.zeros(4)
    for i,j in enumerate(pi):P[j,i]=1
    assert P.T*K*P==K
   rows.append({'n':n,'V':len({v for T in t for v in T}),
                'T':len(t),'alpha':str(alpha(n,g))})
   if n in (1,2):weighted_current_check(t,birth,g)
  cases[name]=rows
 assert [q['alpha'] for q in cases['unchanged_Q169_unit']]==['1','5/4','31/16','245/64']
 assert [q['alpha'] for q in cases['CANDIDATE_quarter_geometric_proxy']]==['1','5/4','91/64','1577/1024']
 q=s.Rational(11,16)
 assert all(s.simplify(alpha(n,lambda k:s.Rational(1,4)**(k-1))-(s.Rational(9,5)-s.Rational(4,5)*q**n))==0 for n in range(12))
 eps=s.Rational(1,100)
 assert s.Rational(1,4)*q**8>eps>=s.Rational(1,4)*q**9
 assert s.Rational(4,5)*q**11>eps>=s.Rational(4,5)*q**12
 return {'status':'PASS_EXACT_CONDITIONAL','all_depth_alpha':'1+1/4*sum_(k=1)^n (11/4)^(k-1)*g_k',
         'increment':'(11/4)^n*g_(n+1)/4','positive_weights_no_finite_plateau':True,
         'r_threshold':'4/11','quarter_proxy_limit':'9/5','adjacent_eps_1_100':9,
         'tail_eps_1_100':12,'cases':cases,'physical_promotion':0}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
