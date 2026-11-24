import sympy as S
from itertools import combinations,product
from math import factorial
import json
R=S.Rational
A=[S.Matrix(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
B=[-v for v in A]
Q=S.Matrix([[-61,-22,58],[62,-19,58],[-2,82,29]])/87
assert Q.T*Q==S.eye(3) and Q.det()==1
# Exact convex intersection: tetrahedron A has inequalities a.x >= -1.
def overlap(q):
    normals=A+[-q*a for a in A]
    verts=set()
    for ix in combinations(range(8),3):
        m=S.Matrix.vstack(*(normals[i].T for i in ix))
        if m.det():
            v=m.inv()*S.Matrix([-1]*3)
            if all(n.dot(v)>=-1 for n in normals): verts.add(tuple(v))
    verts=sorted(verts); v=[S.Matrix(x) for x in verts]; vol=0; edges=set(); faces=[]
    for n in normals:
        f=[i for i,p in enumerate(v) if n.dot(p)==-1]
        if len(f)<3:continue
        if tuple(f) in faces:continue
        faces.append(tuple(f)); center=sum((v[i] for i in f),S.zeros(3,1))/len(f)
        # Facet edges are pairs that share another active nonparallel plane.
        for i,j in combinations(f,2):
            if any(n.cross(m)!=S.zeros(3,1) and m.dot(v[i])==m.dot(v[j])==-1 for m in normals):
                edges.add((i,j)); vol+=abs(S.det(S.Matrix.hstack(center,v[i],v[j])))/6
    return (len(v),len(edges),len(faces)),vol,sorted(map(len,faces))
V=R(8,3)
results={}
for label,q in [('canonical',S.eye(3)),('rotated',Q)]:
    f,o,sizes=overlap(q); cross=-o/V**2
    defect=S.Matrix([[0,cross],[cross,0]])
    results[label]={'f':f,'facet_sizes':sizes,'overlap_volume':str(o),'top_whitney_pre':str(1/V),'top_whitney_post_pullback':str(S.eye(2)/V+defect),'defect_eigenvalues':list(map(str,defect.eigenvals().keys()))}
    assert o>0 and o<V
assert results['canonical']['f']==(6,12,8) and results['rotated']['f']==(12,18,8)
assert results['canonical']['overlap_volume']=='4/3'
# Fan top chain map counts eight shared cells of volume 1/6 and four private of volume 1/3 per packet.
chain_gram=S.Matrix([[8*6+4*3,-8*6],[-8*6,8*6+4*3]])
assert chain_gram==S.Matrix([[60,-48],[-48,60]])
results['chain_top_pullback']=str(chain_gram)
# Same-domain cochain transfer is volume-fraction weighted, unlike subdivision chain map.
assert 8*(R(1,6)/V)**2*6+4*(R(1,3)/V)**2*3==1/V
assert -8*(R(1,6)/V)**2*6==-R(3,16)
# A cochain map does not force its metric adjoint to intertwine: interval [0,1] split in halves.
# nodal Whitney mass and oriented edge mass for original and refined intervals.
M0=S.Matrix([[2,1],[1,2]])/6; M1=S.Matrix([[1]])
N0=S.Matrix([[2,1,0],[1,4,1],[0,1,2]])/12; N1=2*S.eye(2)
P0=S.Matrix([[1,0],[R(1,2),R(1,2)],[0,1]]); P1=S.Matrix([[R(1,2)],[R(1,2)]])
d=S.Matrix([[-1,1]]); e=S.Matrix([[-1,1,0],[0,-1,1]])
assert P0.T*N0*P0==M0 and P1.T*N1*P1==M1 and e*P0==P1*d
# For this symmetric interval the adjoint happens to commute; use unequal subdivision instead.
h=R(1,3); N0=S.Matrix([[2*h,h,0],[h,2,1-h],[0,1-h,2*(1-h)]])/6; N1=S.diag(1/h,1/(1-h)); P0=S.Matrix([[1,0],[1-h,h],[0,1]]); P1=S.Matrix([h,1-h]);
assert P0.T*N0*P0==M0 and P1.T*N1*P1==M1 and e*P0==P1*d
adj=N0.inv()*e.T*N1*P1-P0*M0.inv()*d.T*M1
assert adj!=S.zeros(3,1)
results['adjoint_intertwining_counterexample']=str(adj)
print(json.dumps(results,indent=2))
