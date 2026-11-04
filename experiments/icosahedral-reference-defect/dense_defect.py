#!/usr/bin/env python3
"""Actual frozen DOP853 dense-polynomial defect and exact CM block comparison.

NUMERICAL defect *samples* are not a rigorous interval maximum. Formula for
Gronwall/log norm is exact conditional. Mainline mechanics read-only.
"""
import argparse
import json
import math
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"experiments/icosahedral-pulsetube"))
from jacobian import model
from variational import SOURCE

def poly_and_derivative(piece,x):
    y=np.zeros_like(piece.y_old)
    dy=np.zeros_like(y)
    for i,f in enumerate(reversed(piece.F)):
        y=y+f
        if i%2==0:
            dy=dy*x+y
            y=y*x
        else:
            dy=dy*(1-x)-y
            y=y*(1-x)
    return piece.y_old+y,dy/piece.h

def mass_center(y,m):
    q=np.concatenate((y[1:40],y[190:280]))
    v=np.concatenate((y[281:320],y[470:560]))
    mass=np.r_[m.mass[1:40],np.repeat(m.hm,3)]
    total=mass.sum()/3
    return np.array([sum(mass[i::3]*q[i::3])/total for i in range(3)]),np.array(
      [sum(mass[i::3]*v[i::3])/total for i in range(3)])

def run(case_id):
    c=next(x for x in json.loads((SOURCE/"cases.json").read_text()) if x["id"]==case_id)
    m=model(c,.05);y0=m.initial_augmented(.1)
    sol=solve_ivp(m.ode,(0,100),y0,method="DOP853",rtol=5e-12,
                  atol=5e-15,dense_output=True)
    assert sol.success and sol.t[0]==0 and abs(sol.t[-1]-100)<1e-10
    GL=(.1127016653792583,.5,.8872983346207417)
    max_residual=0.;max_primary_residual=0.
    sampled_residual_integral=0.;max_poly_endpoint_error=0.
    intervals=len(sol.sol.interpolants)
    for pc in sol.sol.interpolants:
        local=0.
        for x in GL:
            yp,dp=poly_and_derivative(pc,x)
            t=pc.t_old+pc.h*x
            ref=pc._call_impl(np.array(t))
            discrepancy=float(np.linalg.norm(yp-ref))
            max_poly_endpoint_error=max(max_poly_endpoint_error,discrepancy)
            r=dp-m.ode(t,yp)
            size=float(np.linalg.norm(r[:560]))
            max_residual=max(max_residual,size)
            max_primary_residual=max(max_primary_residual,float(np.linalg.norm(r[1:40])))
            local=max(local,size)
        sampled_residual_integral+=local*(pc.t-pc.t_old)
    x=np.linspace(0,100,2001)
    y=sol.sol(x).T
    c0,v0=mass_center(y0,m)
    cm_errors=[]
    for t,point in zip(x,y):
        cm,_=mass_center(point,m)
        cm_errors.append(float(np.linalg.norm(cm-c0-t*v0)))
    source_pos=np.linalg.norm(y[:,1:40]-y0[1:40],axis=1)
    # Since the Euclidean full-state log norm MUST be >=1/2 due to the
    # invariant unanchored translation shear [[0,I],[0,0]], a constant
    # scalar Gronwall with mu>=1/2 requires a raw residual <=budget/(2(e^50-1)).
    target=.010310941027943417
    log10_threshold=math.log10(target*.5)-math.log10(math.expm1(50))
    amplification=math.expm1(50)/.5
    assert max_poly_endpoint_error<1e-8
    return {
      "case":case_id,"status":"NUMERICAL_RESIDUAL_PROBES_NOT_RIGOROUS",
      "strict_reference_solver":{"method":"DOP853","rtol":5e-12,"atol":5e-15,
        "nfev":sol.nfev,"interpolants":intervals},
      "defect_probe_nodes_per_step":3,
      "max_sampled_full_mechanical_defect_L2":max_residual,
      "max_sampled_primary_position_derivative_defect_L2":max_primary_residual,
      "sampled_interval_quadrature_upper_SURROGATE_not_certified":sampled_residual_integral,
      "dense_polynomial_vs_scipy_evaluation_max":max_poly_endpoint_error,
      "max_sampled_primary_reference_shift":float(max(source_pos)),
      "max_sampled_analytic_CM_position_error":max(cm_errors),
      "raw_equal_weights_euclidean_log_norm_lower_bound_exact":.5,
      "raw_gronwall_at_u100_amplification_floor_exact_expression":"2*(exp(50)-1)",
      "raw_gronwall_at_u100_amplification_floor_numeric":amplification,
      "sufficient_uniform_full_defect_target_for_delta_primary0p01031_if_mu_equals_half":10**log10_threshold,
      "required_log10_uniform_defect_upper_bound_if_mu_equals_half":log10_threshold,
      "conclusion":"Even idealized raw full-state mu=1/2 constant-exponential Gronwall is severely overconservative; actual mu>=1/2 and no certified supremum defect/Lipschitz tube provided; need CM-block removal + projected shape/full stability and validated local residual bounds.",
      "no_certification":"Probed residual is not uniform over each step; derivative computed analytically for DOP853 dense polynomial but f evaluations and position are Float64, not interval; CM position checks only numerical against an EXACT Galilean law."}
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--out",type=Path,required=True);a=ap.parse_args()
    result={"evidence":["EXACT","CONDITIONAL","NUMERICAL","FAILED","OPEN"],
            "source_scope":"original two frozen 560+heat mechanical reference cases, no material law/parameter change",
            "method":"analytical derivative of original SciPy DOP853 dense polynomial, 3 interior probe nodes per accepted step, exact CM trajectory check",
            "cases":{name:run(name) for name in ("seed10422-0-boundary2","uniform-b0.05-cf0.0")}}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("ICO_DEFECT_RESULTS:"+json.dumps(result,sort_keys=True),flush=True)
