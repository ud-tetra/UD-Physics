"""Replay same-path complex reference calibration and tangent-disk controls."""
import cmath
import json
import math
from pathlib import Path


def tangent(signal, error, sign):
    angle = sign * math.asin(error / abs(signal))
    return signal * math.cos(angle) * cmath.exp(1j * angle)


def replay(row):
    nominal = row["nominal_gap_rad"]
    offset_gap = row["minimum_offset_gap_rad"]
    half_gap = nominal / 2
    # Recover the weakest post-gain science magnitude from the zero-phase budget.
    science = (row["gain_trials"][0]["common_additive_budget_per_total_stock"]
               / math.sin((offset_gap - half_gap) / 2))
    reports = []
    for mismatch in (0, 1 / 400):
        for ratio in (1, 4, 10):
            reference = ratio * science
            half_spare = (offset_gap - half_gap - 2 * mismatch) / 2
            error = math.sin(half_spare) / math.sqrt(
                science**-2 + reference**-2
                + 2 * math.cos(half_spare) / (science * reference))
            assert abs(math.asin(error / science) + math.asin(error / reference)
                       - half_spare) < 1e-15
            raw, clean, noisy = [], [], []
            for phase, sign in ((0, 1), (offset_gap, -1)):
                gain_phase = sign / 160
                shared_phase = 0.73
                sample = science * cmath.exp(1j * (phase + gain_phase + sign * mismatch))
                pilot = reference * cmath.exp(1j * (shared_phase + gain_phase))
                raw.append(cmath.phase(sample))
                clean.append(cmath.phase(sample / pilot))
                noisy.append(cmath.phase(tangent(sample, error, sign)
                                         / tangent(pilot, error, -sign)))
            raw_gap = raw[1] - raw[0]
            calibrated_gap = clean[1] - clean[0]
            adversarial_gap = noisy[1] - noisy[0]
            assert abs(raw_gap - (offset_gap - 1 / 80 - 2 * mismatch)) < 1e-14
            assert abs(calibrated_gap - (offset_gap - 2 * mismatch)) < 1e-14
            assert abs(adversarial_gap - half_gap) < 1e-14
            reports.append({"reference_to_science_floor": ratio,
                            "residual_phase_cap_each_rad": mismatch,
                            "uncalibrated_gap_rad": raw_gap,
                            "calibrated_noiseless_gap_rad": calibrated_gap,
                            "adversarial_gap_rad": adversarial_gap,
                            "common_error_per_total_stock": error})
    return {"order": row["order"], "science_magnitude_floor": science, "controls": reports}


if __name__ == "__main__":
    prior = json.loads(Path(__file__).with_name("clock_alignment_results.json").read_text())
    print(json.dumps([replay(row) for row in prior], indent=2))
