from REF01_bipyramid_detail_visibility import *
rows=L+tr(maps)
def kernel(rows):
 a=[r[:] for r in rows]; k=0; p=[]
 for j in range(14):
  i=next((i for i in range(k,len(a)) if a[i][j]),None)
  if i is None:continue
  a[k],a[i]=a[i],a[k]; a[k]=[v/a[k][j] for v in a[k]]
  for i in range(len(a)):
   if i!=k and a[i][j]:a[i]=[v-a[i][j]*w for v,w in zip(a[i],a[k])]
  p.append(j);k+=1
 free=[j for j in range(14) if j not in p]
 return [[(-a[p.index(i)][j] if i in p else F(i==j)) for i in range(14)] for j in free]
N=kernel(rows); assert len(N)==4
selected=[]
for i,s in enumerate(b):
 row=V[pairs.index((i,i))]
 v=[sum(a*c for a,c in zip(row,u)) for u in N]
 if len(piv([r for _,r in selected]+[v]))>len(selected):selected.append((s,v));print(s,list(map(str,v)),H[i][i])
assert len(selected)==4
