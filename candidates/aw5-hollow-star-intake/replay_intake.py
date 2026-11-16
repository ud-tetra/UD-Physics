"""Synthetic pipeline fixtures. No measured data or simulated dynamics."""
from copy import deepcopy
from fractions import Fraction
from intake_score import LIMITS, N, adjudicate, blind_score, digest

reveal = {"nonce": "synthetic-replay-public-nonce-0001",
          "roles": {"aligned_hollow": "B7", "matched_filled": "K2", "orthogonal_hollow": "V4"}}
times = [str(Fraction(2*k+1, 16)) for k in range(N)]
bounds = {"dissipative": True, **{k: str(v) for k, v in LIMITS.items()}}
packet = {"protocol": "AW5-ACQUISITION-v1", "evidence_mode": "SYNTHETIC",
          "role_commitment": digest(reveal), "centered_subgaussian": True,
          "independent_across_traces_and_samples": True,
          "traces": {name: {"times": times.copy(), "values": [value]*N, "bounds": bounds.copy()}
                     for name, value in zip(("B7", "K2", "V4"), ("3/64", "0", "0"))}}

def check(label, result, expected):
    assert result["status"] == expected, result
    print(label, expected)

scores = blind_score(packet)
check("equality at both thresholds", adjudicate(packet, scores, reveal), "PASS")
low = deepcopy(packet)
low["traces"]["V4"]["values"][0] = "1/4096"
check("one contrast below threshold", adjudicate(low, blind_score(low), reveal), "FAIL")
for name, edit in {
    "correlation declared": lambda p: p.update(independent_across_traces_and_samples=False),
    "unverified timing": lambda p: p["traces"]["B7"]["times"].__setitem__(0, "0"),
    "operator error too large": lambda p: p["traces"]["K2"]["bounds"].update(generator_error="1/1024"),
    "offset too large": lambda p: p["traces"]["V4"]["bounds"].update(mean_bias="1/128"),
    "dissipativity absent": lambda p: p["traces"]["B7"]["bounds"].update(dissipative=False),
    "measured mode": lambda p: p.update(evidence_mode="MEASURED"),
}.items():
    changed = deepcopy(packet)
    edit(changed)
    check(name, blind_score(changed), "INADMISSIBLE")
check("tampered score", adjudicate(packet, dict(scores, means={}), reveal), "INADMISSIBLE")
check("swapped reveal", adjudicate(packet, scores, dict(reveal, nonce="changed")), "INADMISSIBLE")
