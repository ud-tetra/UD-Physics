#!/usr/bin/env python3
"""Exact Fraction checks of checkpoint 026 scalar time-slab gates.

Reads frozen archive output JSON. This checker verifies only the rational
inequalities on the reported data; the full coefficient/defect reconstruction
is in the local checkpoint zip, and the original source ODE is NOT certified.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path


def check(uniform, slabs):
    u = json.loads(Path(uniform).read_text())
    assert u["status"] == "EXACT_UNIFORM_SPLINE_TAYLOR_TAIL_IEEE754_OUTWARD_ROUNDING"
    assert u["intervals"] == 4000 and u["taylor_degree"] == 20
    assert u["cauchy_radius"] == 8
    M, Q = F(u["M_max_rational"]), F(u["complex_exponent_Qmax_rational"])
    assert M < F(401, 1000) and Q < F(321, 100)
    tail = (1 - Q / F(64)) ** (-64) / F(8 ** 20 * 7)
    assert tail == F(u["global_degree20_Taylor_tail_bound_rational"])
    assert tail < F(4, 10 ** 18)
    selected = []
    for source in slabs:
        one = json.loads(Path(source).read_text())
        assert one["status"] == "EXACT_CERTIFIED_FLOAT_SPLINE_SURROGATE_ONLY"
        assert one["dimension"] == 36 and one["taylor_degree"] == 20
        assert F(one["M_rational"]) < 1
        err = F(one["local_transfer_error_inf_rational"])
        assert err < F(3, 10 ** 21)
        selected.append({"left": one["left"],
                         "right": one["right"], "bound": str(err)})
    return {"status": "EXACT_CONDITIONAL_GATE_PASS",
            "uniform_taylor_tail": str(tail), "selected_slabs": selected,
            "scope": "Only exact scalar checks on archived derived values; "
                     "not a verified original-source Jacobian or u100 theorem."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uniform", type=Path, required=True)
    parser.add_argument("--slabs", type=Path, nargs="+", required=True)
    a = parser.parse_args()
    print(json.dumps(check(a.uniform, a.slabs), indent=2))
