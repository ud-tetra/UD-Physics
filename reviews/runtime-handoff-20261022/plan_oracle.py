#!/usr/bin/env python3
"""Plan-derived exact oracle; not an observation of writer output."""
import json
from fractions import Fraction


def main():
    train = [(Fraction(n), Fraction(y)) for n, y in [(0, 1), (1, 3), (2, 5)]]
    evaluation = [(Fraction(n), Fraction(y)) for n, y in [(3, 7), (4, 9)]]
    mean_n = sum(n for n, y in train) / len(train)
    mean_y = sum(y for n, y in train) / len(train)
    scale = sum((n-mean_n)*(y-mean_y) for n,y in train) / sum((n-mean_n)**2 for n,y in train)
    offset = mean_y - scale*mean_n
    affine_residuals = [offset+scale*n-y for n,y in train+evaluation]
    baseline_residuals = [mean_y-y for n,y in train+evaluation]
    # Training remains identical if the already exposed evaluation labels change.
    perturbed = [(Fraction(3), Fraction(8)), (Fraction(4), Fraction(9))]
    result = {"scope": "Exact oracle derived from HANDOFF_TRIAL_v1.0 synthetic plan; writer output not yet observed", "residual_convention": "predicted minus label", "offset_ns": str(offset), "scale_ns_per_tick": str(scale), "constant_baseline_ns": str(mean_y), "affine_residuals_ns": list(map(str, affine_residuals)), "baseline_residuals_ns": list(map(str, baseline_residuals)), "baseline_training_sse_ns2": str(sum(x*x for x in baseline_residuals[:3])), "baseline_evaluation_sse_ns2": str(sum(x*x for x in baseline_residuals[3:])), "perturbed_evaluation_residuals_ns": [str(offset+scale*n-y) for n,y in perturbed], "interpretation": "All targets exposed; exact fitted arithmetic does not establish native UD dynamics or independent physical prediction."}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
