#!/usr/bin/env python3
"""Exact rational global error check for an executed 187-slab polynomial source replay.
Check all 187 Bernstein/domain/continuity assertions separately by re-running
the complete local validated_peak.py from checkpoint 027 ZIP.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

def check(record):
    assert record["status"] == "EXACT_RATIONAL_TAYLOR_DEFECT"
    assert record["steps"] == 187 and record["degree"] == 20
    assert F(record["interval_width"]) == F(1,40)
    D=10**75
    q=F(int(record["sqrt5_floor_grid"]),D)
    assert q*q < 5 < (q+F(1,D))**2
    r=(5+q)/8; m=(3+q)/8
    mc=F(3,50)*m/r
    eta=F(1,10000)/r
    assert F(9,10)<r<F(19,20) and F(13,20)<m<F(25,36)
    assert F(43,1000)<mc<F(44,1000) and eta<F(1,9000)
    assert F(13,324)<F(21,100)**2
    assert F(13,324)+F(1)/(100*mc)<F(53,100)**2
    assert F(21,100)+F(5,6)*F(53,100)<F(2,3)
    assert r/F(12)+m/mc<16
    assert F(7,100)*F(13,162)<F(3,40)**2
    assert F(14,100)<F(3,8)**2
    dmu=F(1,2)*2*F(1,9000)*120*16*F(2,3)/F(37,80)*F(3,8)
    assert dmu == F(64,555) and dmu<F(1,8)
    Kabssum=13+24+(36+100*mc)+200*mc+100*mc
    assert Kabssum+13+mc<121
    residual=F(record["max_residual_infinity_per_model_time"])
    assert residual < F(33,10**31)
    assert F(187,320)<F(3,5)
    # e^(3/5) <= 1+3/5 + ((3/5)^2/2)/(1-(3/5)/3) < 2.
    expupper=1+F(3,5)+(F(3,5)**2/2)/(1-F(1,5))
    assert expupper<2
    # True-source sqrt5 parameter error <10^-73 by analytic derivative gate.
    error=88*(residual+F(1,10**73))
    assert error<F(3,10**28)
    assert 5*error<F(3,2*10**27)
    return {"status":"EXACT_CONDITIONAL_SOURCE_ERROR_GATE_PASS",
            "max_residual":str(residual),
            "energy_norm_error_upper":str(error),
            "energy_norm_error_display":float(error),
            "scope":"uniform six-state original model u<=187/40; source 187-polynomial and sqrt5 derivative premises require their separately captured replay",
            "source_to_sector4_spline_eta_1e-8":"OPEN"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--source",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    result=check(json.loads(a.source.read_text()))
    a.out.write_text(json.dumps(result,indent=2)+"\n")
    print(result["status"],result["energy_norm_error_display"])
