"""Generate AW5 model impulse packets and replay the unchanged v1 scorer."""
from fractions import Fraction

import numpy as np
from scipy.linalg import expm

from intake_score import N, adjudicate, blind_score, digest
from residue import af, ah, ff, hf, p, matched, orthogonal, embed


def trace(A, faces, face_vector, gamma):
    operator = np.asarray(A, dtype=float)
    operator[faces, faces] -= float(gamma)*np.asarray(p, dtype=float)
    source = np.asarray(embed(face_vector, A, faces), dtype=float).ravel()
    source /= np.linalg.norm(source)
    times = [Fraction(2*k+1, 16) for k in range(N)]
    state = expm(operator/16)@source
    step = expm(operator/8)
    values = []
    for k, time in enumerate(times):
        if k in (0, N//2, N-1):
            direct = expm(float(time)*operator)@source
            assert np.linalg.norm(state-direct) < 1e-11
        values.append(str(Fraction(format(source@state, ".12f"))))
        state = step@state
    return {"times": list(map(str, times)), "values": values,
            "bounds": dict(dissipative=True, exterior_damping=str(gamma),
                           drive_error=0, sensor_error=0, generator_error=0,
                           mean_bias=0, noise_proxy=0)}


def replay(gamma):
    reveal = {"nonce": "public-model-replay-fixture-nonce",
              "roles": {"aligned_hollow": "Q4", "matched_filled": "B8",
                        "orthogonal_hollow": "M2"}}
    packet = {"protocol": "AW5-ACQUISITION-v1", "evidence_mode": "SYNTHETIC",
              "role_commitment": digest(reveal), "centered_subgaussian": True,
              "independent_across_traces_and_samples": True,
              "traces": {"Q4": trace(ah, hf, matched, gamma),
                         "B8": trace(af, ff, matched, gamma),
                         "M2": trace(ah, hf, orthogonal, gamma)}}
    scores = blind_score(packet)
    assert scores["status"] == "SCORED_BLIND"
    result = adjudicate(packet, scores, reveal)
    assert result["status"] == "PASS"
    print(f"gamma={gamma} {result['status']} packet_sha256={scores['packet_sha256']}")
    for role, gap in result["gaps"].items():
        print(f"  {role}: {float(Fraction(gap)):.9f}")


if __name__ == "__main__":
    for damping in (Fraction(0), Fraction(1, 512)):
        replay(damping)
