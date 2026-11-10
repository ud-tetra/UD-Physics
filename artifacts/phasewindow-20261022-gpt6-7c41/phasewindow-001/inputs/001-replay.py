#!/usr/bin/env python3
"""Recompute phase-energy enlargement from immutable integrated UD records.

Requires only Python 3 stdlib and an existing repository checkout. No
nonlinear integration. Frozen nine strength nodes and 50 exposed coefficient
cases are DEVELOPMENT data, not held-out confirmation.
"""
import argparse, csv, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

BASE="ce89a9cd15439463d9a64d983d91c22ea4368726"
SRC=Path("artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files")
HASHES={
 "linear.csv":"971a8dc46bc42fc9b246ef7c20b13b9f3651d29d4704e111fa402f9e2edaf3e5",
 "full_housing_refined.json":"d3fc9c63f21811b65e3d0bed04063d8f4725eaab01970602e560876ccc569427"
}
E=F(51,20000000);sig=F(1,400);e=F(1,250);h=F(1,180)
assert sig**2>2*E
assert e**2>2*E/F(19,50)
assert h**2>2*E/F(9,50)
anchor=(1-e)/2-h
opposite=(1-e)**2-(1+e)**2/4
assert opposite>F(1,4) and anchor>0
G=3*(2*sig+sig**2)+F(49,40)*(2*e+e**2)
assert F(49,40)**2>F(3,2) and G<F(1,40)
assert anchor==F(554,1125)

def run(repo):
    folder=repo/SRC
    for name,digest in HASHES.items():
        actual=hashlib.sha256((folder/name).read_bytes()).hexdigest()
        assert actual==digest,(name,actual)
    rows=list(csv.DictReader((folder/"linear.csv").open(newline="")))
    nus=sorted({float(r["nu"]) for r in rows})
    assert len(rows)==450 and len(nus)==9 and len({r["id"] for r in rows})==50
    saved=json.loads((folder/"full_housing_refined.json").read_text())
    assert saved["status"]=="FULL_HOUSING_WINDOW_PASS"
    assert saved["initial_phase_dimension"]==180 and saved["parameter_sets"]==50
    nodes=[]
    for nu in nus:
        candidates=[]
        for r in rows:
            if float(r["nu"])!=nu:continue
            rp=float(r["linear_pulse_rms"])
            ro=float(r["original_linear_rms"])
            delta=float(r["all_phase_readout_rms_bound"])
            lip=float(r["breathing_rms_lipschitz_bound"])
            radius=(rp-math.sqrt(1.5)*delta-0.8*ro)/lip
            candidates.append((radius,r["id"]))
        assert len(candidates)==50
        radius,limiter=min(candidates)
        nodes.append(dict(nu=nu,radius=radius,limiter=limiter))
    overlaps=[nodes[i]["radius"]+nodes[i+1]["radius"]-
              (nodes[i+1]["nu"]-nodes[i]["nu"]) for i in range(8)]
    assert min(overlaps)>0.0003
    assert nodes[0]["nu"]==.04 and nodes[-1]["nu"]==.05
    energy=saved["maximum_full_housing_energy_upper"]["continuous_strength_full_housing_energy_upper"]
    assert energy<.5
    return dict(status="NUMERICAL_FINITE_CASE_LINEAR_EXTENSION",
                initial_energy_over_reference_pulse="3/80000",
                source_revision=BASE,input_rows=len(rows),parameter_sets=50,
                initial_housing_phase_coordinates=180,nu_interval=[.04,.05],
                full_housing_energy_max_upper=energy,
                minimum_neighborhood_overlap=min(overlaps),nodes=nodes,
                exact_conditional_housing_only=dict(Eh_max=str(E),all_struts_gt=str(anchor),
                     normalized_gram_perturbation_lt="1/20",
                     volume_ratio_lower="(19/20)^(3/2)",
                     volume_ratio_upper="(21/20)^(3/2)"),
                limitations="No full nonlinear pulse T=100 bound or continuous property-box guarantee")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--repo-root",type=Path,default=Path("."))
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    answer=run(a.repo_root)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(answer,indent=2)+"\n")
    print("PASS",answer["status"],"margin",answer["minimum_neighborhood_overlap"])
