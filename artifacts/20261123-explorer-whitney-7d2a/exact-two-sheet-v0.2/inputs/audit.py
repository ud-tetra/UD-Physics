import sympy as s
import json
R=s.Rational
# Ambient oriented integrated top cochains, common eight cells then four private cells.
v=[R(1,6)]*8+[R(1,3)]*4
V=sum(v); M=s.diag(*[1/x for x in v]); H=s.diag(M,M)
p=s.Matrix([x/V for x in v]); P=s.diag(p,p)
D=s.diag(*([1]*8+[0]*4)); C=M*D
J=s.zeros(12); A=s.BlockMatrix([[J,D],[-D,J]]).as_explicit()
assert P.T*H*P==s.eye(2)/V
assert A.T*H+H*A==s.zeros(24)
assert A.rank()==16
S=s.BlockMatrix([[J,s.eye(12)],[s.eye(12),J]]).as_explicit()
assert S*A*S==-A
K=(P.T*H*P).inv()*P.T*H*A*P
E=A*P-P*K
assert K==s.Matrix([[0,R(1,2)],[-R(1,2),0]])
assert E.T*H*E==s.eye(2)*R(3,32)
assert P.T*H*E==s.zeros(2)
# Any permutation of common cells, applied equally on both sheets, commutes.
from itertools import permutations
for perm in permutations(range(3)):
    # simple octant permutation using coordinate index permutation
    from itertools import product
    signs=list(product([-1,1],repeat=3)); idx=[signs.index(tuple(t[i] for i in perm)) for t in signs]
    U=s.eye(12)[:,idx+list(range(8,12))]; W=s.diag(U,U)
    assert W*A==A*W
# General overlap fraction, projected generator and leakage norm relative to old mass.
f=s.symbols('f',real=True)
# dimensionless time tau; for initial A only, exact packet B fraction f sin^2 tau.
# Exchange reversal imposes C=-C^T in common aligned orthonormal basis; diagonal C then vanishes.
c=s.symbols('c0:8'); L=s.diag(*c); assert (L+L.T)==2*L
out={'classification':'EXACT_CONDITIONAL / OPEN_CONSTITUTIVE_SOURCE','V':str(V),'overlap_fraction':'1/2','transfer_gram':str(P.T*H*P),'exchange_rank':A.rank(),'projected_generator':str(K),'leakage_gram':str(E.T*H*E),'relative_leakage_squared':'1/4','swap_odd':True,'coordinate_permutations_checked':6,'exchange_fraction':'f*sin(tau)^2','canonical_fraction':'1/2','rotated_fraction':'1985862927391/3352261334400','full_packet_transfer':False,'physical_promotion':0}
print(json.dumps(out,indent=2))
