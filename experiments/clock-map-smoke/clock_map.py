#!/usr/bin/env python3
"""Exact synthetic affine FIT; all evaluation targets were exposed in advance."""
import argparse
from fractions import Fraction
import json
from pathlib import Path


def evaluate(points, offset, slope):
    rows = []
    for n, label in points:
        prediction = offset + slope * n
        rows.append({"n": str(n), "label_ns": str(label),
                     "prediction_ns": str(prediction),
                     "residual_ns": str(prediction - label)})
    return {"points": rows,
            "sse_ns2": str(sum((offset + slope * n - label) ** 2
                               for n, label in points))}


def run(fixture):
    if fixture["index_unit"] != "tick" or fixture["label_unit"] != "ns":
        raise ValueError("This declared mapping requires tick indices and ns labels")
    training = [(Fraction(n), Fraction(y)) for n, y in fixture["training"]]
    evaluation = [(Fraction(n), Fraction(y)) for n, y in fixture["evaluation_exposed"]]
    count = len(training)
    if count < 2 or not evaluation:
        raise ValueError("At least two training points and one evaluation point required")
    mean_n = sum(n for n, _ in training) / count
    mean_y = sum(y for _, y in training) / count
    variance = sum((n - mean_n) ** 2 for n, _ in training)
    if not variance:
        raise ValueError("Affine slope is unidentifiable with constant training indices")
    slope = sum((n - mean_n) * (y - mean_y) for n, y in training) / variance
    offset = mean_y - slope * mean_n
    return {
        "evidence": ["FIT", "EXACT"],
        "data_kind": "synthetic labels, no measured physical clock",
        "target_exposure": "All training and evaluation labels exposed before fitting",
        "evaluation_role": "development evaluation, not blinded prediction",
        "mapping": "t_label_ns = offset_ns + scale_ns_per_tick * n",
        "residual_convention": "prediction minus label",
        "fit_objective": "unweighted training sum of squared residuals",
        "arithmetic": "fractions.Fraction; rational values serialized as strings",
        "affine": {
            "offset_ns": str(offset), "scale_ns_per_tick": str(slope),
            "free_parameters": 2,
            "training": evaluate(training, offset, slope),
            "evaluation_exposed": evaluate(evaluation, offset, slope)},
        "constant_baseline": {
            "level_ns": str(mean_y), "free_parameters": 1,
            "training": evaluate(training, mean_y, Fraction(0)),
            "evaluation_exposed": evaluate(evaluation, mean_y, Fraction(0))}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path,
                        default=Path(__file__).with_name("fixture.json"))
    args = parser.parse_args()
    print(json.dumps(run(json.loads(args.fixture.read_text(encoding="utf-8"))),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
