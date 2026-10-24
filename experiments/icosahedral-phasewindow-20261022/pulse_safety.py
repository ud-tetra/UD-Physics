#!/usr/bin/env python3
"""Exact fraction certificate for full 3D MountLoss pulses at reduced amplitude.

Source: ud-tetra/UD-Physics main ce89a9cd15439463d9a64d983d91c22ea4368726.
No physical time/length calibration, simulation or measured evidence.
"""
from fractions import Fraction as Q
import argparse, json
from pathlib import Path

K=Q(19,50)   # minimum edge stiffness
KH=Q(9,50)   # STRICT lower housing mount stiffness, R²<1
EH=Q(3,2)*Q(17,250)/40000  # amplified initial housing energy
assert EH==Q(51,20000000)

def check(alpha,sigma,epsilon,delta,orientation=False):
    E=Q(34,5)*alpha*alpha+EH
    assert 2*E<sigma*sigma
    assert 2*E/K<epsilon*epsilon
    assert 2*E/KH<delta*delta
    endpoint=(1-epsilon)/2-delta
    median2=(1-epsilon)**2-(1+epsilon)**2/4
    assert endpoint>0 and median2>(endpoint+delta)**2
    result={"alpha_max":str(alpha),"energy_upper":str(E),
            "radial_strain_upper":str(sigma),"edge_strain_upper":str(epsilon),
            "housing_lag_upper":str(delta),"all_struts_strict_lower":str(endpoint),
            "median_squared_lower":str(median2),
            "global_existence":True,"all_member_lengths_positive":True}
    if orientation:
        gram2=2*E*(3*(2+sigma)**2+(2+epsilon)**2/(2*K))
        assert gram2==Q(206656471,855000000)
        assert gram2<Q(123,250)**2<Q(1,2)**2
        result.update(gram_frobenius_squared_upper=str(gram2),
                      gram_relative_spectral_upper="123/125",
                      oriented_cell_volume_lower="(2/125)^(3/2)",
                      oriented_cell_volume_upper="(248/125)^(3/2)",
                      oriented_cell_sign_preserved=True)
    return result

def calculate():
    safe4=check(Q(1,25),Q(3,20),Q(1,4),Q(7,20))
    assert safe4["all_struts_strict_lower"]=="1/40"
    safe3=check(Q(3,100),Q(1,9),Q(1,5),Q(4,15),True)
    assert safe3["all_struts_strict_lower"]=="2/15"
    # Amplitudes above selected bounds fail these sufficient inequalities;
    # no inference that they dynamically collapse.
    assert 2*(Q(34,5)*Q(41,1000)**2+EH)/KH >= Q(7,20)**2
    assert 2*(Q(34,5)*Q(31,1000)**2+EH)>=Q(1,9)**2
    assert Q(1,36)<Q(13,200) # old alpha=.1 energy witness
    return {"status":"EXACT_CONDITIONAL","source_revision":"ce89a9cd15439463d9a64d983d91c22ea4368726",
            "housing_energy_max":str(EH),
            "initial_preparation":"heart pulse alpha, reference primary/device positions and zero velocities, arbitrary housing phase of energy<=EH",
            "nonlinear_all_time_struts":safe4,
            "nonlinear_all_time_cell_orientation":safe3,
            "limitations":["No original amplitude .1 all-time certificate",
                           "No ringdown-by-u100 or breathing-coherence bound",
                           "No empirical data or physical calibration",
                           "Chosen rational amplitude thresholds are development selections"]}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    result=calculate()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("PASS EXACT/CONDITIONAL",result["housing_energy_max"],result["nonlinear_all_time_struts"]["all_struts_strict_lower"])
