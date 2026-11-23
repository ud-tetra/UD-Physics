"""Replay three exact K4 controls and check the optional CLI exit contract."""

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / "scripts/check_basis_semantics.py"
FIXTURE = ROOT / "experiments/o14-lc-bundle/K4_NATIVE_BASIS_U_REFERENCE_v0.1.json"


def main():
    reference = json.loads(FIXTURE.read_text())
    harmonic = deepcopy(reference)
    reversed_pair = deepcopy(reference)
    for i, row in enumerate(harmonic["modal_to_full_chain_basis"]):
        row[0] = 0.5 if i < 4 else 0
    for row in reversed_pair["modal_to_full_chain_basis"]:
        row[1] = -row[1]
    bundle = {"native_basis": {
        "simplices": [{"ordered_vertices": [str(v) for v in s], "degree": len(s) - 1}
                      for s in reference["simplices"]],
        "modal_to_full_chain_basis": reference["modal_to_full_chain_basis"],
    }}
    wrong_order = deepcopy(bundle)
    labels = wrong_order["native_basis"]["simplices"]
    labels[0], labels[1] = labels[1], labels[0]
    cases = [
        ("reference", reference, 0, "PASS signed generator: 0"),
        ("bundle basis", bundle, 0, "PASS harmonic overlap: 0"),
        ("harmonic substitution", harmonic, 1, "FAIL harmonic overlap: 1"),
        ("quadrature reversal", reversed_pair, 1, "FAIL signed generator: 5.6568542"),
        ("wrong simplex order", wrong_order, 1, "Expected canonical ascending simplex row order"),
    ]
    with TemporaryDirectory() as directory:
        path = Path(directory) / "basis.json"
        for label, record, expected_exit, diagnostic in cases:
            path.write_text(json.dumps(record))
            result = subprocess.run([sys.executable, str(CHECKER), str(path)],
                                    text=True, capture_output=True)
            assert result.returncode == expected_exit, (label, result)
            assert diagnostic in result.stdout + result.stderr, (label, result)
            if label in ("harmonic substitution", "quadrature reversal"):
                assert "PASS Gram: 0" in result.stdout, (label, result)
            print(f"PASS {label}: CLI exit {expected_exit}, {diagnostic}")


if __name__ == "__main__":
    main()
