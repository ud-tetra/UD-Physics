from REF01_bipyramid_locality import *
from sub import boundary
B=boundary(b)
A=[[F(v) for v in row] for row in x['A_weighted']]
def add(a,b):return [[u+v for u,v in zip(r,s)] for r,s in zip(a,b)]
def neg(a):return [[-u for u in r] for r in a]
U=add(A,B)
assert mul(H,U)==mul(tr(B),H)
assert mul(R,S)==eye(23)
coarse=[tuple(s) for block in x['simplices']['old'] for s in block]
D=boundary(coarse); C=add(tr(D),neg(D))
assert mul(B,S)==mul(S,D) and mul(R,B)==mul(D,R)
assert mul(R,A)==mul(C,R)
def mat(v):
 K=[[F(0)]*n for _ in range(n)]
 for (i,j),a in zip(pairs,v):K[i][j]=K[j][i]=a
 return K
def flatten(a):return [v for r in a for v in r]
L=[row for k,row in enumerate(V) if ds[pairs[k][0]][pairs[k][1]]>2]
maps=[]
for v in tr(V):
 K=mat(v)
 maps.append(flatten(add(mul(K,U),neg(mul(tr(B),K)))))
print('local rank',len(piv(L)))
print('combined rank',len(piv(L+tr(maps))))
print('diagonal combined rank',len(piv(L+[v for (i,j),v in zip(pairs,V) if i==j])))
print('joint combined rank',len(piv(L+tr(maps)+[v for (i,j),v in zip(pairs,V) if i==j])))
# Common detail rescaling preserves the full generator while changing the hub norm.
K=[[u-v for u,v in zip(a,c)] for a,c in zip(H,H0)]
assert mul(K,U)==mul(tr(B),K)
assert spd(add(H,K))
j=b.index((5,))
print('hub norm squared under H and H+K:',H[j][j],H[j][j]+K[j][j])
assert all(K[i][j]==0 for i,j in pairs if ds[i][j]>2)
