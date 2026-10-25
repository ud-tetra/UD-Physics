#!/usr/bin/env python3
"""Rebuild a matched stationary conventional KC Hessian from retained coordinates.

Uses the archived grid-selected Cartesian reference, not the missing public grid
ZIP. The KC parameters are from Minkin et al., PRB 108 085411 (2023), SI Table S1.
No downloaded source code is executed. The fixed lower sheet, 14 mobile heights,
three-neighbor normals, pair cutoff and plate law match the archived v19/v20 model.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[2]
CAPTURES = ROOT / "artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures"
REF = next(CAPTURES.glob("*graphite-material-projection*/MATERIAL_PROJECTION_RESULTS.json"))
SPECTRUM = next(CAPTURES.glob("*graphite-finite-spectrum*/FINITE_HEIGHT_SPECTRUM_16A.json"))
ref = json.loads(REF.read_text())
archived = json.loads(SPECTRUM.read_text())

b = 1.42  # A, in the archived conventional model
a = math.sqrt(3) * b
basis = np.array([[a, a / 2], [0, a * math.sqrt(3) / 2]])
R = np.array([[8, 3], [-3, 5]], dtype=float) / 7
inv_supercell = np.linalg.inv(np.array([[2, -1], [1, 3]]))
cart = np.array(ref["reference_cart_translation_a"])
z = 3.46
n = 14
rc = 16.0
D_plate_ev = 1.44  # conservative elastic plate, NOT Rayleigh loss
A, z0, Cbase, C0, C2, C4, delta, lam = 10.238, 3.34, 3.030, 15.71, 12.29, 4.933, 0.578, 3.629

top, bottom, addr = [], [], []
for p in range(-18, 19):
    for q in range(-18, 19):
        u = np.array([p, q])
        inside = np.all(inv_supercell @ R @ u >= -1e-9) and np.all(inv_supercell @ R @ u < 1-1e-9)
        for site, atom in enumerate((np.zeros(2), np.array([1/3, 1/3]))):
            bottom.append(basis @ (u + atom))
            if inside:
                top.append(basis @ R @ (u + atom))
                addr.append((site, p, q))
top, bottom = np.array(top), np.array(bottom)
assert top.shape == (14, 2)
labels = [site*7+(q-2*p)%7 for site,p,q in addr]
assert labels == ref["atom_labels"]
lookup = {(site,(q-2*p)%7):j for j,(site,p,q) in enumerate(addr)}
neighbor_ids, neighbor_vecs = [], []
L = np.zeros((n,n))
for i,(site,p,q) in enumerate(addr):
    paths = [(1,p,q),(1,p-1,q),(1,p,q-1)] if site==0 else [(0,p,q),(0,p+1,q),(0,p,q+1)]
    ids, vecs = [], []
    for other,pp,qq in paths:
        j=lookup[(other,(qq-2*pp)%7)]
        v = np.array([pp-p,qq-q]) + (np.array([1/3,1/3]) if other==1 else 0) - (np.array([1/3,1/3]) if site==1 else 0)
        ids.append(j);vecs.append(basis@R@v)
        L[i,i]+=1;L[i,j]-=1
    neighbor_ids.append(ids);neighbor_vecs.append(vecs)
neighbor_ids=np.array(neighbor_ids);neighbor_vecs=np.array(neighbor_vecs)
assert np.allclose(L,L.T) and np.max(np.abs(L@np.ones(n)))<1e-12
Aatom = 3*math.sqrt(3)*b*b/4
Kplate = D_plate_ev*(1000*Aatom/n)*(4/(3*b*b))**2*(L@L)

s0 = top[:,None,:]+cart-bottom[None,:,:]
mask=np.sum(s0*s0,axis=-1)+z*z<rc*rc
ii,jj=np.where(mask);sv=s0[ii,jj]

def energy(q, load):
    x,h=q[:2],q[2:]
    t=np.concatenate([neighbor_vecs,(h[neighbor_ids]-h[:,None])[:,:,None]],axis=2)
    cr=np.cross(t,np.roll(t,-1,axis=1))
    cr/=np.linalg.norm(cr,axis=2)[:,:,None]
    normal=cr.sum(axis=1);normal/=np.linalg.norm(normal,axis=1)[:,None]
    s=sv+(x-cart)[None,:];zi=z+h[ii]
    r2=np.sum(s*s,axis=1)+zi*zi;r=np.sqrt(r2)
    rho_t=r2-(np.einsum("ij,ij->i",s,normal[ii,:2])+zi*normal[ii,2])**2
    rho_b=np.sum(s*s,axis=1)
    def f(rho):
        u=rho/delta**2
        return np.exp(-u)*(C0+C2*u+C4*u*u)
    pair=np.sum(-A*(z0/r)**6+np.exp(-lam*(r-z0))*(Cbase+f(rho_t)+f(rho_b)))/n
    return pair+h@Kplate@h/2+load*h.mean()

q0=np.r_[cart,np.zeros(n)]
def derivative(f,q,steps):
    g=np.zeros(len(q))
    for i,h in enumerate(steps):
        e=np.eye(len(q))[i]*h
        g[i]=(f(q+e)-f(q-e))/(2*h)
    return g
steps=np.r_[np.ones(2)*1e-5,np.ones(n)*1e-5]
load=-sum(derivative(lambda q:energy(q,0),q0,steps)[2:])
fn=lambda q:energy(q,load)
grad=lambda q:derivative(fn,q,steps)
res=minimize(fn,q0,jac=grad,method="L-BFGS-B",
             bounds=[(cart[0]-.03,cart[0]+.03),(cart[1]-.03,cart[1]+.03)]+[(-.015,.015)]*n,
             options={"ftol":1e-15,"gtol":1e-8,"maxiter":300})
assert res.success

def hessian(q,dx,dh):
    hs=np.r_[np.full(2,dx),np.full(n,dh)]
    H=np.zeros((n+2,n+2));f0=fn(q);eye=np.eye(n+2)
    for i,hi in enumerate(hs):
        a=eye[i]*hi;H[i,i]=(fn(q+a)-2*f0+fn(q-a))/hi**2
        for j in range(i):
            hj=hs[j];b=eye[j]*hj
            H[i,j]=(fn(q+a+b)-fn(q+a-b)-fn(q-a+b)+fn(q-a-b))/(4*hi*hj)
            H[j,i]=H[i,j]
    return H
H=hessian(res.x,1e-4,1e-3)
K,C=H[2:,2:],H[:2,2:]
eig=np.linalg.eigvalsh(K)
assert eig.min()>0
perm=np.argsort([site*7+(k+2)%7 for site,k in ((v//7,v%7) for v in labels)])
aligned_lookup={int(original):int(aligned) for aligned,original in enumerate(perm)}
bond_edges=sorted({(aligned_lookup[i],aligned_lookup[int(j)]-7) if aligned_lookup[i]<7
                   else (aligned_lookup[int(j)],aligned_lookup[i]-7)
                   for i in range(n) for j in neighbor_ids[i]})
K=K[np.ix_(perm,perm)];C=C[:,perm]
cov=np.linalg.inv(K) # Angstrom^2 per meV of Theta_bar=k_B*T/14; E_total=14*Ebar.
H2=hessian(res.x,3e-4,3e-3)
K2=H2[2:,2:][np.ix_(perm,perm)]
C2step=H2[:2,2:][:,perm]
cov2=np.linalg.inv(K2)
step_check=dict(max_relative_K_element_change=float(np.max(np.abs(K2-K))/np.max(np.abs(K))),
                max_relative_C_element_change=float(np.max(np.abs(C2step-C))/np.max(np.abs(C))),
                max_relative_site_variance_change=float(np.max(np.abs(np.diag(cov2)-np.diag(cov))/np.diag(cov))),
                max_relative_eigenvalue_change=float(np.max(np.abs(np.linalg.eigvalsh(K2)-eig)/eig)))
soft=C@np.linalg.solve(K,C.T)
drag=C@np.linalg.solve(K,np.linalg.solve(K,C.T)) # per unit isotropic Rayleigh d
old=np.array([row["height_stiffness_mev_per_a2_per_mean_atom"] for row in archived["mode_rows"]])
rel_spectrum=float(np.max(np.abs(eig-old)/old))
rel_soft=float(np.max(np.abs(soft-np.array(archived["static_softening_direct"])))/(np.max(np.abs(soft))))
rel_drag=float(np.max(np.abs(drag-np.array(archived["rayleigh_coefficient_matrix_per_unit_d"])))/(np.max(np.abs(drag))))
assert rel_spectrum<2e-5 and rel_soft<2e-5 and rel_drag<2e-5, (rel_spectrum,rel_soft,rel_drag)
assert np.linalg.norm(K-K.T)<1e-7 and np.linalg.norm(cov-cov.T)<1e-7
vp=[4*k%7 for k in range(7)]+[7+(4*k-1)%7 for k in range(7)]
P=np.zeros((14,14))
for v,pv in enumerate(vp):P[pv,v]=1
frame=basis@R@np.array([[0,1],[1,0]])
rot=frame@np.array([[-1,-1],[1,0]])@np.linalg.inv(frame)
rotC=np.zeros_like(C)
for v,pv in enumerate(vp):rotC[:,pv]=rot@C[:,v]
symmetry=dict(K_C3_relative_defect=float(np.linalg.norm(P@K@P.T-K)/np.linalg.norm(K)),
              C_C3_relative_defect=float(np.linalg.norm(rotC-C)/np.linalg.norm(C)))
assert symmetry["K_C3_relative_defect"]<1e-6 and symmetry["C_C3_relative_defect"]<1e-5

# Reuse the same stationary energy and fixed roster at two nearby model loads.
# This is not a measured load derivative or a dissipative material calibration.
base_load=load
pressure_unit=Aatom*1000/160217.6634 # model load (meV/A/atom) per MPa
pressure_rows=[]
old_pressure=next(CAPTURES.glob("*graphite-nonlinear-relax*/NONLINEAR_16A_RESULTS.json"))
old_pressure_rows={row["dp"]:row for row in json.loads(old_pressure.read_text())["pressure_rows"]}
for dp in (-2.5,0.0,2.5):
    load=base_load+dp*pressure_unit
    rr=minimize(fn,res.x,jac=grad,method="L-BFGS-B",
                bounds=[(cart[0]-.03,cart[0]+.03),(cart[1]-.03,cart[1]+.03)]+[(-.015,.015)]*n,
                options={"ftol":1e-15,"gtol":1e-8,"maxiter":300})
    assert rr.success
    HH=hessian(rr.x,1e-4,1e-3)
    HH_alt=hessian(rr.x,3e-4,3e-3)
    KK=HH[2:,2:][np.ix_(perm,perm)]
    CC=HH[:2,2:][:,perm]
    KK_alt=HH_alt[2:,2:][np.ix_(perm,perm)]
    CC_alt=HH_alt[:2,2:][:,perm]
    assert np.linalg.eigvalsh(KK).min()>0
    cv=np.linalg.inv(KK)
    sf=CC@np.linalg.solve(KK,CC.T)
    dg=CC@np.linalg.solve(KK,np.linalg.solve(KK,CC.T))
    soft_scalar=float(np.trace(sf)/2)
    archived_soft=old_pressure_rows[dp]["soften"]
    assert abs(soft_scalar-archived_soft)<1e-5
    pressure_rows.append(dict(delta_pressure_MPa=dp,model_load=load,stationary_heights_A=rr.x[2:].tolist(),
                              stationary_max_grad=float(np.max(np.abs(grad(rr.x)))),
                              mean_height_A=float(np.mean(rr.x[2:])),K=KK.tolist(),C=CC.tolist(),
                              K_alt_step=KK_alt.tolist(),C_alt_step=CC_alt.tolist(),
                              site_variances_per_Theta_bar=np.diag(cv).tolist(),
                              static_softening_scalar=soft_scalar,drag_per_unit_isotropic_d=dg.tolist(),
                              difference_from_archived_softening=soft_scalar-archived_soft))
load=base_load
out=dict(model="reconstructed v19/v20 stationary conventional KC plus plate from archived reference translation",
         sources=dict(reference=str(REF.relative_to(ROOT)),spectrum=str(SPECTRUM.relative_to(ROOT)),
                      SI="Minkin et al PRB 108 085411 (2023), arXiv:2308.06302 SI Table S1; arXiv source SHA256 adea7468f311c648a0d25abf4f5eecacd8eebe1b6fc7761ffcea7d073b2f460b"),
         caveat="The original Mendeley grid ZIP was not replayed; cart0 is read from its prior archived output. No experimental dissipation or physical native-edge map.",
         units=dict(K_C="meV/Angstrom^2 per mean upper atom",covariance_per_Theta_bar="Angstrom^2/meV of Theta_bar",load="meV/Angstrom per upper atom"),
         thermal_normalization="E_total=14 Ebar; Sigma_h=(k_B T/14) Kbar^-1. Theta_bar=k_B T/14, not k_B T.",
         settings=dict(cutoff_A=rc,height_A=z,D_plate_eV=D_plate_ev,normal="three nearest neighbors",pair_roster=len(ii),step_xy_A=1e-4,step_height_A=1e-3),
         reference_cart_A=cart.tolist(),stationary_lateral_A=res.x[:2].tolist(),stationary_heights_A=res.x[2:].tolist(),
         reference_load=load,stationary_max_grad=float(np.max(np.abs(grad(res.x)))),optimization_nit=int(res.nit),
         pair_roster_changes_at_stationary=int(np.sum((np.sum((top[:,None,:]+res.x[:2]-bottom[None,:,:])**2,axis=-1)+(z+res.x[2:,None])**2<rc*rc)!=mask)),
         finite_difference_step_check=step_check,C3_symmetry_check=symmetry,
         c3_aligned_physical_indices=perm.tolist(),aligned_bond_edges=bond_edges,eigenvalues=eig.tolist(),
         K=K.tolist(),C=C.tolist(),covariance_per_Theta_bar=cov.tolist(),
         site_variances_per_Theta_bar=np.diag(cov).tolist(),trace_covariance_per_Theta_bar=float(np.trace(cov)),
         softening=soft.tolist(),drag_per_unit_isotropic_d=drag.tolist(),
         pressure_rows=pressure_rows,
         archive_comparison=dict(max_relative_mode_error=rel_spectrum,max_relative_softening_element_error=rel_soft,
                                 max_relative_drag_element_error=rel_drag))
print(json.dumps(out,indent=2))
