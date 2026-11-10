#!/usr/bin/env python3
"""Conditional continuous-time reference displacement enclosure for frozen 3D source.

Exact analytic lemma: if mechanical E<=E0 and all potentials>=0, primary
Frobenius speed <=sqrt(2 E0/m_min). For samples at spacing Δ, continuous
reference position radius <= max_sample + Δ*speed_bound/2 + ε_global,
where ε_global is an externally established global primary numerical error
at the sampled timestamps. Convergence difference is NOT ε_global.
"""
import argparse,json,math,sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"experiments/icosahedral-pulsetube"))
from jacobian import model
from variational import SOURCE
CASES=["seed10422-0-boundary2","uniform-b0.05-cf0.0"]
def run(case_id,step):
    c=next(c for c in json.loads((SOURCE/"cases.json").read_text()) if c["id"]==case_id)
    m=model(c,.05);init=m.initial_augmented(.1)
    E0=float(m.energy(init))
    Eformula=float((1+m.g.sum())*.01/2)
    assert abs(E0-Eformula)<1e-11
    mmin=float(min(m.mass[1:40]))
    v_bound=math.sqrt(2*E0/mmin)
    t=np.linspace(0.,100.,round(100./step)+1)
    assert abs(t[1]-t[0]-step)<1e-11
    sols=[]
    for tol in [(2e-11,2e-14),(5e-12,5e-15)]:
        x=solve_ivp(m.ode,(0.,100.),init,method="DOP853",t_eval=t,rtol=tol[0],atol=tol[1])
        assert x.success
        y=x.y.T
        primary=y[:,1:40]
        disp=np.linalg.norm(primary-init[1:40],axis=1)
        energy=np.array([m.energy(a) for a in y])
        assert max(energy)<=E0+1e-8
        vel=np.linalg.norm(y[:,281:320],axis=1)
        assert max(vel)<v_bound+1e-6
        sols.append({"time":t,"position":primary,"displacement":disp,"vel":vel,
                     "nfev":x.nfev,"energy_peak":float(max(energy)),
                     "tolerance":tol})
    a,b=sols
    peak_idx=int(np.argmax(b["displacement"]))
    maxsample=float(b["displacement"][peak_idx])
    allowance=step*v_bound/2
    cross_delta=float(np.max(np.linalg.norm(a["position"]-b["position"],axis=1)))
    # A posteriori *necessary* global error allowance to close d=.07.
    epsilon_budget=float(.07-maxsample-allowance)
    return {"case":case_id,"status":"NUMERICAL_SAMPLES_PLUS_EXACT_CONDITIONAL_INTERSAMPLE_LEMMA",
        "n_samples":len(t),"grid_step":step,"source_nu":.05,"source_A0":.1,
        "source_initial_energy":E0,"source_min_primary_mass":mmin,
        "exact_analytic_speed_cap_from_energy":v_bound,
        "max_sampled_primary_reference_displacement":maxsample,
        "time_at_sampled_max":float(t[peak_idx]),
        "all_time_bound_IF_SAMPLED_STATES_EXACT":maxsample+allowance,
        "global_numeric_sample_error_budget_to_certify_d0p07":epsilon_budget,
        "strict_minus_nominal_sampled_numeric_difference":cross_delta,
        "strict_dop853_nfev":b["nfev"],"nominal_dop853_nfev":a["nfev"],
        "strict_max_sampled_primary_speed":float(max(b["vel"])),
        "reference_energy_peak_strict":b["energy_peak"],
        "passes_conditional_budget":epsilon_budget>0,
        "continuous_time_status":"NOT_CERTIFIED unless independent validated sample-global error epsilon_global < positive budget",
        "missing_after_this":"full180 housing phase nonlinear relative radius and forced Green/Hessian/strut-volume enclosure"}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--step",type=float,default=.05);p.add_argument("--out",type=Path,required=True)
    args=p.parse_args(); assert 0<args.step<=.25
    out={"status":"CONDITIONAL_INTERSAMPLE_BUDGET_WITH_UNVALIDATED_NUMERICAL_ERROR",
         "lemma":"sup_time ||Yprimary(t)-Y0||F <= max_grid ||Ytrue_primary(tj)-Y0||F + (Δ/2) sqrt(2E0/m_min); if numeric sample error≤δ, add δ",
         "assumptions":"source positive mechanical energy components, nonnegative heat production, no external source, E0=Ep, m_min>0",
         "cases":{case:run(case,args.step) for case in CASES},
         "evidence":["EXACT","CONDITIONAL","NUMERICAL","OPEN"]}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print("ICO_REF_ENVELOPE_JSON:"+json.dumps(out,sort_keys=True),flush=True)
