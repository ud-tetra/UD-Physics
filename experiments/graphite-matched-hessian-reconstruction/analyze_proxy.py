#!/usr/bin/env python3
"""A declared bond-height-difference variance proxy on the exact N=7 carrier.

This does NOT identify a native packet edge with a graphite height difference.
The fitted scale against the conventional mixed Hessian is exposed-target fit.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import math
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
x=json.loads((HERE/"MATCHED_HESSIAN_RESULTS.json").read_text())
cov=np.array(x["covariance_per_Theta_bar"])
C=np.array(x["C"])

# Rebuild oriented honeycomb dual boundary from exact triangle incidence.
edges=list(combinations(range(7),2))
eidx={e:i for i,e in enumerate(edges)}
faces=[(k,(k+1)%7,(k+5)%7) for k in range(7)]
faces += [((k+1)%7,(k+6)%7,(k+5)%7) for k in range(7)]
P2=np.zeros((21,14),dtype=int)
for j,face in enumerate(faces):
    for a,b in zip(face,face[1:]+face[:1]):
        P2[eidx[tuple(sorted((a,b)))] ,j]+=1 if a<b else -1
sign=[-next(P2[e,j] for j in range(7) if P2[e,j]) for e in range(21)]
B1=(P2*np.array(sign)[:,None]).T # 14 vertices x 21 edges, A -> B
edge_labels={}
for e in range(21):
    i=next(j for j in range(7) if B1[j,e]==-1)
    k=next(j for j in range(7) if B1[7+j,e]==1)
    edge_labels[(i,k)]=e
assert len(edge_labels)==21
assert set(map(tuple,x["aligned_bond_edges"]))==set(edge_labels)

G=[[F(1),F(1,2)],[F(1,2),F(1)]]
d={0:[F(1,3),F(1,3)],1:[F(-2,3),F(1,3)],5:[F(1,3),F(-2,3)]}
M=[]
for e in range(21):
    i,k=next(key for key,val in edge_labels.items() if val==e)
    cls=(i-k)%7
    M.append([sum(d[cls][p]*G[p][j] for p in range(2)) for j in range(2)])
M=np.array(M,dtype=float)
assert np.array_equal(B1@M,np.zeros((14,2)))
assert np.allclose(M.T@M,3.5*np.array(G,dtype=float))

# h is a registered upper-atom height. q_e=h_B-h_A is a chosen physical proxy.
# Its stationary variance / Theta_bar is (B1^T K^-1 B1)_{ee}, A^2/meV.
w=np.diag(B1.T@cov@B1)
assert np.all(w>0)
S=M.T@(w[:,None]*B1.T)
assert np.linalg.matrix_rank(S)==2
orbits=[];seen=set()
for (i,k),e in edge_labels.items():
    if e in seen:continue
    orb=[]
    for _ in range(3):
        ee=edge_labels[(i,k)];orb.append(ee);seen.add(ee)
        i,k=(4*i)%7,(4*k-1)%7
    orbits.append(orb)
assert len(orbits)==7 and len(seen)==21

# Convert native two-coordinate covectors to the archived Cartesian x basis.
a=math.sqrt(3)*1.42
basis=np.array([[a,a/2],[0,a*math.sqrt(3)/2]])
R=np.array([[8,3],[-3,5]],dtype=float)/7
swap=np.array([[0,1],[1,0]])
Fcart=basis@R@swap
Sc=np.linalg.inv(Fcart).T@S
beta=float(np.sum(Sc*C)/np.sum(Sc*Sc))
residual=float(np.linalg.norm(C-beta*Sc)/np.linalg.norm(C))
pressure=[];pressure_alt=[]
for row in x["pressure_rows"]:
    kp=np.array(row["K"]);cp=np.array(row["C"])
    wp=np.diag(B1.T@np.linalg.inv(kp)@B1)
    sp=np.linalg.inv(Fcart).T@(M.T@(wp[:,None]*B1.T))
    gp=np.array(row["drag_per_unit_isotropic_d"])
    port_transfer=sp@np.linalg.solve(kp,np.linalg.solve(kp,sp.T))
    assert np.linalg.eigvalsh(port_transfer).min()>0
    pressure.append(dict(delta_pressure_MPa=row["delta_pressure_MPa"],
                         proxy_mean_weight_per_Theta_bar=float(wp.mean()),
                         proxy_weight_cv=float(wp.std()/wp.mean()),
                         proxy_cart_source_norm_per_Theta_bar=float(np.linalg.norm(sp)),
                         conditional_pure_port_transfer_per_beta2_d_Theta_bar2=float(np.trace(port_transfer)/2),
                         conventional_scalar_drag_per_unit_isotropic_d=float(np.trace(gp)/2),
                         base_scale_proxy_fit_residual_norm_fraction=float(np.linalg.norm(cp-beta*sp)/np.linalg.norm(cp))))
    ka=np.array(row["K_alt_step"]);ca=np.array(row["C_alt_step"])
    wa=np.diag(B1.T@np.linalg.inv(ka)@B1)
    sa=np.linalg.inv(Fcart).T@(M.T@(wa[:,None]*B1.T))
    pa=sa@np.linalg.solve(ka,np.linalg.solve(ka,sa.T))
    ga=ca@np.linalg.solve(ka,np.linalg.solve(ka,ca.T))
    pressure_alt.append(dict(proxy_cart_source_norm=float(np.linalg.norm(sa)),
                             pure_port_transfer=float(np.trace(pa)/2),
                             conventional_scalar_drag=float(np.trace(ga)/2)))
def slope(key):
    return (math.log(pressure[2][key])-math.log(pressure[0][key]))/5.0
def slope_alt(key):
    return (math.log(pressure_alt[2][key])-math.log(pressure_alt[0][key]))/5.0
out=dict(proxy="q_e=h_B-h_A, w_e=Var(q_e)/Theta_bar, with registered upper-layer bond incidence",
         evidence="NUMERICAL/CONDITIONAL material proxy; target-exposed one-scale conventional C fit; no UD force or loss calibration",
         units=dict(weights="Angstrom^2/meV of Theta_bar",S_native="Angstrom^2/meV of Theta_bar in native lateral basis",S_cart="Angstrom/meV of Theta_bar in Cartesian lateral basis",beta="meV^2/Angstrom^3, conditional on Theta_bar normalization"),
         thermal_normalization="w_e=Var(h_B-h_A)/Theta_bar, Theta_bar=k_B T/14; physical w_e at temperature T is Theta_bar times the reported coefficient.",
         aligned_bond_match=True,uniform_source_norm=float(np.linalg.norm(M.T@B1.T)),
         c3_edge_orbits=orbits,c3_orbit_weight_means=[float(np.mean(w[o])) for o in orbits],
         c3_orbit_max_range=float(max(np.ptp(w[o]) for o in orbits)),
         edge_weights_per_Theta_bar=w.tolist(),edge_weight_mean=float(w.mean()),edge_weight_cv=float(w.std()/w.mean()),
         edge_weight_minmax=[float(w.min()),float(w.max())],
         source_native=S.tolist(),source_cart=Sc.tolist(),source_cart_rank=int(np.linalg.matrix_rank(Sc)),
         source_native_norm_over_mean_weight=float(np.linalg.norm(S)/w.mean()),
         fitted_scalar_beta_to_conventional_C=beta,conventional_C_residual_norm_fraction=residual,
         conventional_C_explained_norm_squared_fraction=float(1-residual*residual),
         pressure_rows=pressure,
         conditional_log_slope_per_MPa=dict(proxy_cart_source_norm=slope("proxy_cart_source_norm_per_Theta_bar"),
                                             pure_port_transfer=slope("conditional_pure_port_transfer_per_beta2_d_Theta_bar2"),
                                             conventional_scalar_drag_per_unit_isotropic_d=slope("conventional_scalar_drag_per_unit_isotropic_d")),
         alternate_Hessian_step_log_slope_per_MPa=dict(proxy_cart_source_norm=slope_alt("proxy_cart_source_norm"),
                                                        pure_port_transfer=slope_alt("pure_port_transfer"),
                                                        conventional_scalar_drag_per_unit_isotropic_d=slope_alt("conventional_scalar_drag")),
         caveat="The signed native packet variable is not derived as a physical bond-height difference. The conventional mixed Hessian is not an observed or isolated UD coupling; its fitted projection supplies no held-out prediction.")
print(json.dumps(out,indent=2))
