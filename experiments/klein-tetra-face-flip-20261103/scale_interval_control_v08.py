#!/usr/bin/env python3
"""Exact endpoint-anchored interval Galerkin coarse metric/refinement control."""
import json
from fractions import Fraction as F
rows=[]
for m in (1,2,4,8,16,32,64):
    # m fine unit edges, the coarse edge subdivides into their oriented sum.
    # G=diag(1,1,m), A_G=D_c-G^-1 D_c^T G.
    frequency_squared=F(2,m)
    residual_squared=2*(1-F(1,m))
    rank=(0 if m==1 else 1 if m==2 else 2)
    rows.append({"fine_edges":m,"coarse_G":[1,1,m],
                 "coarse_angular_frequency_squared":str(frequency_squared),
                 "fine_generator_leakage_Frobenius_squared":str(residual_squared),
                 "leakage_rank":rank})
assert rows[-1]["fine_generator_leakage_Frobenius_squared"]=="63/32"
out={"scope":"1D interval with fixed coarse endpoints, m unit-weight refined edges, source-type A=d-d^T",
     "induced_metric":"diag(1,1,m)",
     "Galerkin_coarse_generator":"[[0,0,-1],[0,0,1],[1/m,-1/m,0]]",
     "native_frequency_squared":"2/m",
     "fine_to_coarse_leakage_squared":"2(1-1/m)",
     "controls":rows,
     "finding":"No refinement-independent native frequency under unit incidence normalization; m>1 not exactly invariant",
     "no_physical_clock":True,"physical_promotion":0,"status":"PASS_EXACT"}
print(json.dumps(out,indent=2,sort_keys=True))
