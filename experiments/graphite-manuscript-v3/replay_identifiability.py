#!/usr/bin/env python3
"""Exact mode-summary counterexample and conditional archived spectral bound."""
from fractions import Fraction as Q
import json

K1 = (Q(1), Q(4))
K2 = tuple(reversed(K1))
def summary(k):
    return {"eigenvalues": sorted(str(x) for x in k),
            "static_softening": str(sum((1/x for x in k), Q(0))),
            "isotropic_loss_drag": str(sum((1/x**2 for x in k), Q(0))),
            "site_one_variance_over_Theta": str(1/k[0])}
a, b = summary(K1), summary(K2)
assert a["static_softening"] == b["static_softening"] == "5/4"
assert a["isotropic_loss_drag"] == b["isotropic_loss_drag"] == "17/16"
assert a["site_one_variance_over_Theta"] == "1"
assert b["site_one_variance_over_Theta"] == "1/4"
print(json.dumps({"K1": a, "K2": b,
                  "conclusion": "mode scalars do not identify registered site covariance"}, indent=2))
