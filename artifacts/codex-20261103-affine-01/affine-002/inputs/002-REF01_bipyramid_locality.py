# Run beside REF01_exact_verifier.py and BIPYRAMID_DATA.json from UD PR #120.
import sys
import json,itertools as it
from collections import deque
from fractions import Fraction as F
from REF01_exact_verifier import mul,tr,eye,spd
x=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'BIPYRAMID_DATA.json'))
S,R,H=[[[F(v) for v in row] for row in x[k]] for k in ('S','R','H')]
n=len(H)
Q=[[u-v for u,v in zip(a,b)] for a,b in zip(eye(n),mul(S,R))]
H0=mul(tr(R),R)
b=[tuple(s) for block in x['simplices']['fine'] for s in block]
lookup={s:i for i,s in enumerate(b)}
actions=[]
for p in it.permutations(range(3)):
 for a in [(3,4),(4,3)]:
  g=p+a+(5,)
  y=[tuple(g[j] for j in s) for s in b]
  actions.append([(lookup[tuple(sorted(s))],(-1)**sum(u>v for i,u in enumerate(s) for v in s[i+1:])) for s in y])
pairs=[(i,j) for i in range(n) for j in range(i,n) if len(b[i])==len(b[j])]
seen=set(); cols=[]
for i,j in pairs:
 if (i,j) in seen:continue
 terms=[]
 for t in actions:
  (a,u),(c,v)=t[i],t[j];seen.add(tuple(sorted((a,c))))
  terms.append((a,c,u*v))
  if a!=c:terms.append((c,a,u*v))
 cols.append([sum(s*Q[a][i]*Q[c][j] for a,c,s in terms) for i,j in pairs])
def piv(rows):
 basis={}
 for row in rows:
  a=list(map(F,row))
  for k in range(len(a)):
   v=a[k]
   if not v:continue
   if k in basis:a=[x-v*y for x,y in zip(a,basis[k])]
   else:
    basis[k]=[x/v for x in a];break
 return sorted(basis)
V=tr(cols);keep=piv(V);V=[[row[k] for k in keep] for row in V]
assert len(keep)==14 and mul(tr(S),H)==R and mul(R,S)==eye(23) and spd(H)
adj=[[j for j,t in enumerate(b) if abs(len(s)-len(t))==1 and (set(s)<=set(t) or set(t)<=set(s))] for s in b]
ds=[]
for i in range(n):
 d={i:0}; q=deque([i])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if v not in d:d[v]=d[u]+1;q.append(v)
 ds.append(d)
for mode,dist in [('hasse',lambda i,j:ds[i][j]),('disjoint',lambda i,j:int(not set(b[i])&set(b[j])))]:
 for r in sorted({dist(i,j) for i,j in pairs}):
  ix=[k for k,(i,j) in enumerate(pairs) if dist(i,j)>r]
  A=[V[k] for k in ix]; B=[-H0[i][j] for k in ix for i,j in [pairs[k]]]
  print(mode,r,len(ix),len(piv(A)),len(piv([a+[v] for a,v in zip(A,B)])),all(H[i][j]==0 for k in ix for i,j in [pairs[k]]))
for k,(i,j) in enumerate(pairs):
 if not set(b[i])&set(b[j]) and H0[i][j] and not any(V[k]):
  print('forced disjoint',b[i],b[j],H0[i][j]);break
for g in range(1,5):
 ix=[k for k,(i,j) in enumerate(pairs) if len(b[i])==g]
 print('grade',g-1,len(piv([V[k] for k in ix])),len(piv([V[k] for k in ix if ds[pairs[k][0]][pairs[k][1]]>2])))
