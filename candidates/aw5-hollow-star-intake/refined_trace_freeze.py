"""Generate a synthetic AW5 packet and verify its pre-reveal freeze."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import secrets

import numpy as np
from scipy.linalg import expm

import intake_score
from intake_score import blind_score, digest

SCORER_BLOB = "29fa3c87e5b34b376558eb154f9fd38795452aed"
CERTIFICATE_REVISION = "c26feb7e1c93b3eb54d3d055df7a1fab3d6243cf"


def write(path, value, *, compact=False):
    options = dict(sort_keys=True, separators=(",", ":")) if compact else dict(indent=2)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, **options)+"\n")


def scorer_identity():
    import hashlib

    payload = Path(intake_score.__file__).read_bytes()
    git_blob = hashlib.sha1(f"blob {len(payload)}\0".encode()+payload).hexdigest()
    if git_blob != SCORER_BLOB:
        raise ValueError("Scorer differs from the frozen Git blob")
    return sha256(payload).hexdigest()


def trace(A, face_slice, faces, q, gamma, exterior, count):
    generator = np.asarray(A, dtype=float)
    for face in exterior:
        index = face_slice.start+faces.index(face)
        generator[index, index] -= float(gamma)
    source = np.asarray(q, dtype=float).ravel()
    source /= np.linalg.norm(source)
    times = [Fraction(2*k+1, 16) for k in range(count)]
    state = expm(generator/16)@source
    step = expm(generator/8)
    values = []
    for i, t in enumerate(times):
        if i in (0, count//2, count-1):
            direct = expm(float(t)*generator)@source
            if np.linalg.norm(state-direct) >= 1e-11:
                raise ValueError("Incremental propagation disagrees with direct exponential")
        values.append(str(Fraction(format(source@state, ".12f"))))
        state = step@state
    return {"times": list(map(str, times)), "values": values,
            "bounds": {"dissipative": True, "exterior_damping": str(gamma),
                       "drive_error": 0, "sensor_error": 0, "generator_error": 0,
                       "mean_bias": 0, "noise_proxy": 0}}


def seal(directory, private_reveal):
    from check_refined_window import (EXTERIOR, GAMMA, N, af, ar, basis, ff, filled_basis,
                                      fr, q_filled, q_null, q_ref)

    scorer_hash = scorer_identity()
    roles = ("aligned_hollow", "matched_filled", "orthogonal_hollow")
    # IDs are randomized independently of envelope values.
    ids = ["B8", "K3", "Z6"]
    secrets.SystemRandom().shuffle(ids)
    mapping = dict(zip(roles, ids))
    reveal = {"nonce": secrets.token_hex(32), "roles": mapping}
    traces = {
        mapping[roles[0]]: trace(ar, fr, basis[2], q_ref, GAMMA, EXTERIOR, N),
        mapping[roles[1]]: trace(af, ff, filled_basis[2], q_filled, GAMMA, EXTERIOR, N),
        mapping[roles[2]]: trace(ar, fr, basis[2], q_null, GAMMA, EXTERIOR, N),
    }
    packet = {"protocol": "AW5-ACQUISITION-v1", "evidence_mode": "SYNTHETIC",
              "role_commitment": digest(reveal), "centered_subgaussian": True,
              "independent_across_traces_and_samples": True, "traces": traces}
    packet_path = directory/"blind-packet.json"
    write(private_reveal, reveal)
    write(packet_path, packet, compact=True)
    freeze = {"certificate_revision": CERTIFICATE_REVISION, "scorer_git_blob": SCORER_BLOB,
              "scorer_sha256": scorer_hash, "packet_file_sha256": sha256(packet_path.read_bytes()).hexdigest(),
              "packet_canonical_sha256": digest(packet),
              "envelope_canonical_sha256": {key: digest(value) for key, value in sorted(traces.items())},
              "role_commitment": packet["role_commitment"]}
    write(directory/"freeze.json", freeze)
    scores = blind_score(packet)
    if scores.get("status") != "SCORED_BLIND":
        raise ValueError(f"Packet failed blind intake: {scores}")
    write(directory/"blind-scores.json", scores)
    verify(directory)


def verify(directory):
    """Verify published inputs and opaque scores without loading the reveal."""
    raw = (directory/"blind-packet.json").read_bytes()
    packet = json.loads(raw)
    freeze = json.loads((directory/"freeze.json").read_bytes())
    scores = json.loads((directory/"blind-scores.json").read_bytes())
    checks = {
        "frozen_scorer": freeze["scorer_git_blob"] == SCORER_BLOB and freeze["scorer_sha256"] == scorer_identity(),
        "certificate_revision": freeze["certificate_revision"] == CERTIFICATE_REVISION,
        "packet_bytes": freeze["packet_file_sha256"] == sha256(raw).hexdigest(),
        "packet_canonical": freeze["packet_canonical_sha256"] == digest(packet),
        "all_trace_envelopes": freeze["envelope_canonical_sha256"] == {
            key: digest(value) for key, value in packet["traces"].items()},
        "role_commitment": freeze["role_commitment"] == packet["role_commitment"],
        "blind_scores": scores.get("status") == "SCORED_BLIND" and scores == blind_score(packet),
    }
    if not all(checks.values()):
        raise ValueError(f"Freeze verification failed: {checks}")
    print(json.dumps({"status": "PASS_PRE_REVEAL", "checks": checks}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--seal", type=Path, metavar="PRIVATE_REVEAL")
    args = parser.parse_args()
    if args.seal:
        seal(args.directory, args.seal)
    else:
        verify(args.directory)


if __name__ == "__main__":
    main()
