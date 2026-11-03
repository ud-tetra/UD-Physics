import importlib.util, numpy as np, json
from scipy.optimize import minimize
from fractions import Fraction as F
from pathlib import Path
spec=importlib.util.spec_from_file_location('relax','/mnt/data/ud_barrier_continuation/relax_search.py'); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rng=np.random.default_rng(20261023)
d=4; X=np.zeros((12,4));X[:,:3]=m.VERT;X[:,3:]=rng.normal(0,.1,(12,1))
i,j,k=m.FACE;pq=np.linalg.lstsq(X[[i,j]].T,X[k],rcond=None)[0]
t=np.r_[X[[v for v in range(12) if v!=k]].ravel(),pq];r=minimize(lambda y:m.fg(y,d),t,method='L-BFGS-B',jac=True,options={'ftol':1e-14,'gtol':1e-10,'maxiter':2500,'maxls':80}); x,_=m.build(r.x,d);E,gr=m.fungrad(x)
s=np.linalg.norm(x,axis=1)/m.RAD-1;alpha=m.G*s.sum()/(1+12*m.G)
print('E=',E,'alpha=',alpha,'face=',m.FACE,'rank=',np.linalg.matrix_rank(x), 'grad norm=',np.linalg.norm(r.jac),'p,q=',r.x[-2:]);print(x)
N=10000
R=[[int(round(float(value)*N)) for value in xyz] for v,xyz in enumerate(x) if v!=k]
P,Q=[int(round(float(z)*N)) for z in r.x[-2:]]
A=int(round(float(alpha)*N))
raw={'source_revision':'1b214f66e00e8430fed0ce7c23506da7965bc977','provenance':'constructive rationalization of target-exposed four-dimensional Gram relaxation optimizer; not a 3D witness','full_dimension':4,'icosahedron_graph_order':'canonical sorted sign-phi points as in prior barrier_audit.py','face_indices':list(m.FACE),'dependent_face_vertex_index':k,'independent_vertex_numerators':R,'coordinate_denominator':N,'dependent_coefficients_numerators':[P,Q],'dependent_coefficients_denominator':N,'alpha_numerator':A,'alpha_denominator':N,'spoke_strength':'19/20','edge_strength':'19/50'}
path=Path('/mnt/data/ud_barrier_continuation/rational_witness.json');path.write_text(json.dumps(raw,indent=2)+'\n');print(path)
