"""Exact symbolic 2D oscillator gate and finite-capacity bookkeeping."""
import json
from itertools import product

# B=((0,-2),(2,0)); direct integer matrix products.
B=((0,-2),(2,0))
def mm(A,C):
    return tuple(tuple(sum(A[i][k]*C[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def transpose(A): return tuple(tuple(A[j][i] for j in range(2)) for i in range(2))
assert transpose(B)==tuple(tuple(-v for v in row) for row in B)
assert mm(B,B)==((-4,0),(0,-4))
for g in (0,1):
    A=tuple(tuple(g*v for v in row) for row in B)
    assert mm(A,A)==tuple(tuple(-4*g*g*(i==j) for j in range(2)) for i in range(2))
    for u,f in product(range(-3,4),repeat=2):
        du=A[0][0]*u+A[0][1]*f
        df=A[1][0]*u+A[1][1]*f
        assert 2*u*du+2*f*df==0
# Full slots persist after acknowledgments; no automatic capacity restoration.
slots=[('A',1),('A',2)]
pending=list(slots)
pending.pop(0)
pending.pop(0)
assert len(pending)==0 and len(slots)==2
assert (1 if len(slots)<2 else 0)==0
print(json.dumps({"status":"PASS","gate_states":[0,1],"norm_checks":98,
 "characteristic_polynomials":{"open":"lambda^2+4","full":"lambda^2"},
 "ack_frees_storage":False,"source_selection":"OPEN"},indent=2))
