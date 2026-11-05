#!/usr/bin/env python3
"""Exact 12D scale-aware Klein coarse generator. Run on repository branch with SymPy.
The G weights are verified separately from v0.6 348D integer subdivision.
"""
import contextlib,io,runpy,json
from pathlib import Path
import sympy as S
root=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    x=runpy.run_path(str(root/"bulk_bridge_v04.py"))
blocks=x["dS"]
dims=(2,5,4,1)
off=[0]
for n in dims:off.append(off[-1]+n)
D=S.zeros(12)
for k,mat in enumerate(blocks,1):
    D[off[k-1]:off[k],off[k]:off[k+1]]=mat
g=(1,1,2,2,2,2,2,8,8,12,12,72)
G=S.diag(*g)
A=D-G.inv()*D.T*G
assert A.T*G+G*A==S.zeros(12)
assert (D*D)==S.zeros(12)
assert A!=D-D.T
pairs=[]
for i in range(12):
    for j in range(i+1,12):
        if A[i,j]:
            assert D[i,j] or D[j,i]
            assert G[i,i]*A[i,j]==-G[j,j]*A[j,i]
            pairs.append([i,j,str(G[i,i]*A[i,j])])
assert len(pairs)==11
assert (A-(D-D.T)).rank()==5
assert sum(x*x for x in A-(D-D.T))==S.Rational(151,18)
out={
"source":"prior v0.6 subdivision S metric G=S^T S; independently replay with 348D input package",
"coarse_metric_diagonal":list(g),
"generator":"A_G=D_c-G^-1 D_c^T G",
"conserved_quadratic_stock":"y^T G y",
"metric_skew":True,"incidence_local":True,
"incidence_pairs":len(pairs),"flux_coefficients_2GiAij_signless":[*pairs],
"naive_unit_metric_generator":"A_0=D_c-D_c^T",
"difference_rank":5,"difference_Frobenius_squared":"151/18",
"formal_parameter":"native u, no physical clock or SI unit",
"physical_promotion":0,
"status":"PASS_EXACT_CONDITIONAL"}
print(json.dumps(out,indent=2,sort_keys=True))
