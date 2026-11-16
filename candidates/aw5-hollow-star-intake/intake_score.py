"""AW5 v1 blind intake. Inputs use exact rational strings or JSON integers."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

N = 256
MARGIN = Fraction(3, 64)
ROLES = ("aligned_hollow", "matched_filled", "orthogonal_hollow")
LIMITS = {
    "exterior_damping": Fraction(1, 512),
    "drive_error": Fraction(1, 512),
    "sensor_error": Fraction(1, 512),
    "generator_error": Fraction(1, 4096),
    "mean_bias": Fraction(1, 256),
    "noise_proxy": Fraction(1, 16),
}


def digest(payload):
    return sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def rational(value):
    if type(value) not in (str, int):
        raise ValueError("Expected a rational string or integer")
    return Fraction(value)


def blind_score(packet):
    result = {"packet_sha256": digest(packet), "status": "INADMISSIBLE"}
    try:
        if packet["protocol"] != "AW5-ACQUISITION-v1" or packet["evidence_mode"] != "SYNTHETIC":
            raise ValueError("This version admits synthetic inputs only")
        commitment = packet["role_commitment"]
        if len(commitment) != 64 or any(c not in "0123456789abcdef" for c in commitment):
            raise ValueError("Expected a SHA-256 role commitment")
        if packet["centered_subgaussian"] is not True or packet["independent_across_traces_and_samples"] is not True:
            raise ValueError("Centered sub-Gaussian and independence declarations required")
        traces = packet["traces"]
        if len(traces) != 3:
            raise ValueError("Exactly three blind traces required")
        means = {}
        for blind_id, trace in sorted(traces.items()):
            cert = trace["bounds"]
            if cert["dissipative"] is not True:
                raise ValueError(f"{blind_id}: dissipativity gate failed")
            for key, limit in LIMITS.items():
                if not 0 <= rational(cert[key]) <= limit:
                    raise ValueError(f"{blind_id}: {key} gate failed")
            times, values = trace["times"], trace["values"]
            if len(times) != N or len(values) != N:
                raise ValueError(f"{blind_id}: sample count gate failed")
            for k, t in enumerate(times):
                if abs(rational(t)-Fraction(2*k+1, 16)) > Fraction(1, 1024):
                    raise ValueError(f"{blind_id}: timing gate failed at sample {k}")
            means[blind_id] = str(sum(map(rational, values))/N)
        return dict(result, status="SCORED_BLIND", means=means)
    except (KeyError, TypeError, ValueError, AttributeError, ZeroDivisionError) as exc:
        return dict(result, reason=str(exc))


def adjudicate(packet, scores, reveal):
    if scores != blind_score(packet) or scores.get("status") != "SCORED_BLIND":
        return {"status": "INADMISSIBLE", "reason": "Blind scores missing, inadmissible or altered"}
    if not isinstance(reveal, dict) or digest(reveal) != packet["role_commitment"]:
        return {"status": "INADMISSIBLE", "reason": "Role commitment mismatch"}
    mapping, nonce = reveal.get("roles"), reveal.get("nonce")
    if (not isinstance(nonce, str) or len(nonce) < 32 or not isinstance(mapping, dict)
            or set(mapping) != set(ROLES) or any(not isinstance(v, str) for v in mapping.values())
            or set(mapping.values()) != set(scores["means"])):
        return {"status": "INADMISSIBLE", "reason": "Expected a nonce and a bijective role map"}
    means = {role: rational(scores["means"][blind_id]) for role, blind_id in mapping.items()}
    gaps = {role: means[ROLES[0]]-means[role] for role in ROLES[1:]}
    return {"status": "PASS" if min(gaps.values()) >= MARGIN else "FAIL",
            "threshold": str(MARGIN), "gaps": {role: str(gap) for role, gap in gaps.items()},
            "packet_sha256": scores["packet_sha256"], "evidence_mode": "SYNTHETIC"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("--scores", type=Path)
    parser.add_argument("--reveal", type=Path)
    args = parser.parse_args()
    if bool(args.scores) != bool(args.reveal):
        parser.error("--scores and --reveal must be supplied together")
    packet = json.loads(args.packet.read_text())
    result = (adjudicate(packet, json.loads(args.scores.read_text()), json.loads(args.reveal.read_text()))
              if args.reveal else blind_score(packet))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
