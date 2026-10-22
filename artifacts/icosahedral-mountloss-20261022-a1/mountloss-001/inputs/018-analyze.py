"""Exact coordinate/incidence/operator audit; no external symbolic dependency.

Geometry: Q(sqrt(5)), edge length a=1. Chains: Z matrices, ascending simplices.
Spectral certificates: square-free annihilating polynomial plus exact moments.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import argparse
import json
import math
import numpy as np


@dataclass(frozen=True)
class Q5:
    p:F=F(0)
    q:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'p',F(self.p));object.__setattr__(self,'q',F(self.q))
    @staticmethod
    def of(x):return x if isinstance(x,Q5) else Q5(x)
    def __add__(self,x):
        x=self.of(x);return Q5(self.p+x.p,self.q+x.q)
    __radd__=__add__
    def __neg__(self):return Q5(-self.p,-self.q)
    def __sub__(self,x):return self+-self.of(x)
    def __rsub__(self,x):return self.of(x)+-self
    def __mul__(self,x):
        x=self.of(x);return Q5(self.p*x.p+5*self.q*x.q,self.p*x.q+self.q*x.p)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.of(x);norm=x.p*x.p-5*x.q*x.q
        if not norm:raise ZeroDivisionError
        return self*Q5(x.p/norm,-x.q/norm)
    def __pow__(self,n):
        assert n>=0;r=Q5(1)
        for _ in range(n):r=r*self
        return r
    def sign(self):
        if not self.q:return (self.p>0)-(self.p<0)
        if not self.p:return (self.q>0)-(self.q<0)
        if self.p*self.q>0:return 1 if self.p>0 else -1
        difference=self.p*self.p-5*self.q*self.q
        return ((difference>0)-(difference<0))*(1 if self.p>0 else -1)
    def __float__(self):return float(self.p)+float(self.q)*math.sqrt(5)
    def __str__(self):return str(self.p) if not self.q else f'({self.p})+({self.q})*sqrt(5)'


def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a,b,c):return dot(a,cross(b,c))


def construction():
    phi=Q5(F(1,2),F(1,2));vertices=[[Q5(0)]*3]
    for s,t in product((-1,1),repeat=2):vertices.append([Q5(0),Q5(F(s,2)),phi*F(t,2)])
    for s,t in product((-1,1),repeat=2):vertices.append([Q5(F(s,2)),phi*F(t,2),Q5(0)])
    for s,t in product((-1,1),repeat=2):vertices.append([phi*F(s,2),Q5(0),Q5(F(t,2))])
    edges=[e for e in combinations(range(1,13),2) if dot(sub(vertices[e[0]],vertices[e[1]]),sub(vertices[e[0]],vertices[e[1]]))==Q5(1)]
    edge_set=set(edges)
    faces=[f for f in combinations(range(1,13),3) if all(e in edge_set for e in combinations(f,2))]
    assert len(edges)==30 and len(faces)==20
    # Every candidate triangle is a genuine supporting face, checked exactly.
    for f in faces:
        a,b,c=[vertices[i] for i in f];n=cross(sub(b,a),sub(c,a));orient=dot(n,a).sign();assert orient
        assert all((dot(n,sub(v,a))*orient).sign()<=0 for v in vertices)
    cells=[(0,)+f for f in faces]
    simplices=[sorted(set(s for c in cells for s in combinations(c,k+1))) for k in range(4)]
    B=[]
    for k in range(1,4):
        lower={s:i for i,s in enumerate(simplices[k-1])};matrix=np.zeros((len(lower),len(simplices[k])),dtype=np.int64)
        for j,s in enumerate(simplices[k]):
            for i in range(k+1):matrix[lower[s[:i]+s[i+1:]],j]=(-1)**i
        B.append(matrix)
    return vertices,edges,faces,cells,simplices,B


def spectral_certificate(matrix,roots):
    """roots: [(Q5 eigenvalue, multiplicity)]; distinct real eigenvalues assumed.

    Exact annihilation proves all eigenvalues belong to roots. Exact moments
    through degree r-1 give unique multiplicities by invertible Vandermonde.
    """
    n=len(matrix);assert sum(m for _,m in roots)==n
    assert len(set(x for x,_ in roots))==len(roots)
    poly=[Q5(1)]
    for root,_ in roots:
        nxt=[Q5(0)]*(len(poly)+1)
        for i,c in enumerate(poly):nxt[i]+=c;nxt[i+1]-=c*root
        poly=nxt
    assert all(c.q==0 and c.p.denominator==1 for c in poly)
    M=matrix.astype(object);I=np.eye(n,dtype=object);value=np.zeros((n,n),dtype=object)
    for c in poly:value=value@M+int(c.p)*I
    assert not np.any(value)
    power=I
    for k in range(len(roots)):
        target=sum((x**k)*m for x,m in roots)
        assert target==Q5(int(np.trace(power)))
        power=power@M
    expected=np.sort(np.concatenate([np.full(m,float(x)) for x,m in roots]))
    residual=float(max(abs(np.linalg.eigvalsh(matrix)-expected)));assert residual<2e-11
    return {'status':'PASS','distinct_eigenvalues':len(roots),'annihilating_polynomial_coefficients':[int(c.p) for c in poly],
            'exact_moments_checked':len(roots),'numeric_spectral_error':residual,
            'eigenvalues':[{'value':str(x),'multiplicity':m} for x,m in sorted(roots,key=lambda z:float(z[0]))]}


def main(out):
    out.mkdir(parents=True,exist_ok=True)
    vertices,edges,faces,cells,simplices,B=construction();f=list(map(len,simplices));assert f==[13,42,50,20]
    assert not np.any(B[0]@B[1]) and not np.any(B[1]@B[2])
    radial_inc=[sum({0,i}<=set(c) for c in cells) for i in range(1,13)]
    edge_inc=[sum(set(e)<=set(c) for c in cells) for e in edges]
    assert set(radial_inc)=={5} and set(edge_inc)=={2}
    D=np.zeros((20,20),dtype=np.int64)
    for i,j in combinations(range(20),2):
        if len(set(cells[i])&set(cells[j]))==3:D[i,j]=D[j,i]=1
    assert np.all(D.sum(axis=1)==3)
    # Radial links give twelve explicit pentagons in the dual.
    for i in range(1,13):
        containing=[j for j,c in enumerate(cells) if i in c]
        assert len(containing)==5 and np.all(D[np.ix_(containing,containing)].sum(axis=1)==2)
    Aico=np.zeros((12,12),dtype=np.int64)
    for i,j in edges:Aico[i-1,j-1]=Aico[j-1,i-1]=1
    sqrt5=Q5(0,1)
    d_roots=[(Q5(0),1),(Q5(3)-sqrt5,3),(Q5(2),5),(Q5(3),4),(Q5(5),4),(Q5(3)+sqrt5,3)]
    ico_roots=[(Q5(0),1),(Q5(5)-sqrt5,3),(Q5(6),5),(Q5(5)+sqrt5,3)]
    dualcert=spectral_certificate(3*np.eye(20,dtype=np.int64)-D,d_roots)
    icocert=spectral_certificate(5*np.eye(12,dtype=np.int64)-Aico,ico_roots)
    offsets=np.cumsum([0]+f);n=sum(f);boundary=np.zeros((n,n),dtype=np.int64)
    for k,b in enumerate(B,1):boundary[offsets[k-1]:offsets[k],offsets[k]:offsets[k+1]]=b
    lap=boundary@boundary.T+boundary.T@boundary
    # Exact cone contraction, including projection to the central point in degree0.
    h=np.zeros_like(boundary)
    for k in range(3):
        higher={s:i for i,s in enumerate(simplices[k+1])}
        for i,s in enumerate(simplices[k]):
            if 0 not in s:h[offsets[k+1]+higher[(0,)+s],offsets[k]+i]=1
    projection=np.zeros_like(h);projection[0,:f[0]]=1
    assert np.array_equal(boundary@h+h@boundary,np.eye(n,dtype=np.int64)-projection)
    roots=[(Q5(0),1),(Q5(1),2),(Q5(13),2),(Q5(3),20),(Q5(4),16),(Q5(6),16),(Q5(7),20),
           (Q5(4)-sqrt5,12),(Q5(4)+sqrt5,12),(Q5(6)-sqrt5,12),(Q5(6)+sqrt5,12)]
    fullcert=spectral_certificate(lap,roots)
    relative_indices=[offsets[k]+i for k in range(4) for i,s in enumerate(simplices[k]) if 0 in s]
    rel=boundary[np.ix_(relative_indices,relative_indices)];rellap=rel@rel.T+rel.T@rel
    relroots=[(Q5(0),1),(Q5(12),2),(Q5(6),10),(Q5(2),10),(Q5(3),8),(Q5(5),8),
              (Q5(5)-sqrt5,6),(Q5(5)+sqrt5,6),(Q5(3)-sqrt5,6),(Q5(3)+sqrt5,6)]
    relcert=spectral_certificate(rellap,relroots)
    cell_sign=np.array([det(*[vertices[i] for i in c[1:]]).sign() for c in cells],dtype=np.int64)
    oriented_cell_lap=cell_sign[:,None]*(B[2].T@B[2])*cell_sign[None,:]
    assert np.array_equal(oriented_cell_lap,4*np.eye(20,dtype=np.int64)-D)
    global_cell=np.zeros(n,dtype=np.int64);global_cell[offsets[3]:]=cell_sign
    surface=boundary@global_cell
    assert np.count_nonzero(surface)==20 and surface@surface==20
    assert np.array_equal(lap@global_cell,global_cell) and not np.any(boundary@surface)
    skew=boundary.T-boundary;heart=np.zeros(n,dtype=np.int64);heart[0]=1
    assert np.array_equal(skew@skew@skew@heart,-13*(skew@heart))
    heart_space=np.column_stack([heart,skew@heart,skew@skew@heart]);assert not np.any(heart_space[offsets[2]:])
    assert not np.any(heart_space.T@global_cell) and not np.any(heart_space.T@surface)
    # Exact metric checks, a=1. Derive every cell volume, Gram determinant and face area squared.
    R2=Q5(F(5,8),F(1,8));h2=Q5(F(7,24),F(1,8));mid2=Q5(F(3,8),F(1,8))
    volume=Q5(F(1,16),F(1,48));internal_area2=Q5(F(3,32),F(1,32))
    for c in cells:
        rays=[vertices[i] for i in c[1:]];vdet=det(*rays)
        assert vdet* vdet==36*volume*volume
        assert all(dot(v,v)==R2 for v in rays)
        assert all(dot(rays[i],rays[j])==Q5(F(1,8),F(1,8)) for i,j in combinations(range(3),2))
        for i,j in combinations(range(3),2):assert dot(cross(rays[i],rays[j]),cross(rays[i],rays[j]))/4==internal_area2
        normal=cross(sub(rays[1],rays[0]),sub(rays[2],rays[0]))
        assert dot(normal,normal)/4==Q5(F(3,16))
        assert dot(normal,rays[0])**2/dot(normal,normal)==h2
        assert dot([x/2 for x in [rays[0][j]+rays[1][j] for j in range(3)]],[x/2 for x in [rays[0][j]+rays[1][j] for j in range(3)]])==mid2
        # Interior lateral-lateral dihedral cosine from signed normal products.
        n1=cross(rays[0],rays[1]);n2=cross(rays[0],rays[2]);cos2=dot(n1,n2)**2/(dot(n1,n1)*dot(n2,n2))
        assert cos2==(Q5(F(-1,4),F(1,4)))**2
        assert dot(normal,n1)**2/(dot(normal,normal)*dot(n1,n1))==Q5(F(1,2),F(-1,6))
    metrics={'R_squared':str(R2),'h_squared':str(h2),'midradius_squared':str(mid2),'cell_volume':str(volume),
        'total_volume':str(20*volume),'internal_area_squared':str(internal_area2),
        'R':math.sqrt(float(R2)),'h':math.sqrt(float(h2)),'midradius':math.sqrt(float(mid2)),
        'apex_angle_degrees':math.degrees(math.acos(1/math.sqrt(5))),
        'base_lateral_degrees':math.degrees(math.atan((3+math.sqrt(5))/2)),
        'lateral_lateral_degrees':72,'central_solid_angle':'pi/5',
        'Gram_matrix':'a^2/8 * [diagonal 5+sqrt(5), off-diagonal 1+sqrt(5)]'}
    result={'status':'PASS','coefficient_domains':['Z boundary/operator identities','Q(sqrt(5)) geometry/moments','float64 spectral cross-check'],
        'f_vector':f,'boundary_f_vector':[12,30,20],'relative_f_vector':[1,12,30,20],
        'chain_dimensions':{'full':125,'boundary':62,'relative':63},
        'chain_ranks':[12,30,20],'betti_Q':[1,0,0,0],
        'incidence':{'radial_edge_cells':5,'boundary_edge_cells':2,'cell_neighbours':3,'radial_link_cycle_length':5},
        'metric':metrics,'dual_laplacian':dualcert,'icosahedral_vertex_laplacian':icocert,
        'full_unit_metric_hodge_laplacian':fullcert,'relative_unit_metric_hodge_laplacian':relcert,
        'heart_seed':{'cyclic_dimension':3,'minimal_polynomial':'z*(z^2+13)','active_degrees':[0,1],'inactive_degrees':[2,3]},
        'oriented_cell_collective':{'cyclic_dimension':2,'minimal_polynomial':'z^2+1','cell_to_boundary_face_cycle':'20 oriented cells map to20 exterior oriented faces; internal faces cancel','orthogonal_to_heart_cyclic_space':True},
        'limitations':['Unit chain metric H=I is a declared combinatorial convention, not the Euclidean Gram metric or a physical constitutive law.','No specified graph diffusion or mechanical evolution is inferred from static adjacency.','A five-cycle link is not a five-tick temporal clock; counts13,63,125 do not establish modular, qubit or physical interpretations.']}
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    data={'vertices_a1':[[str(x) for x in v] for v in vertices],'boundary_edges':edges,'boundary_faces':faces,'cells':cells,'simplices_by_degree':simplices,'boundary_matrices':[b.tolist() for b in B],'dual_adjacency':D.tolist(),'cell_orientation_signs':cell_sign.tolist()}
    (out/'complex.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
