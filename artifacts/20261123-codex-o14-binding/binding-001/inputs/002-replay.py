"""Replay synthetic acceptance and rejection cases through the real CLI."""

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / "scripts/check_o14_bundle_binding.py"


def swap_first_two(records):
    records[0], records[1] = records[1], records[0]


def main():
    mock = json.loads(Path(sys.argv[1]).read_text())
    swapped_pairs = deepcopy(mock)
    swap_first_two(swapped_pairs["native_basis"]["modal_pairs"])
    orphan_output = deepcopy(mock)
    orphan_output["calibration"]["output_ids"][0] = "unmatched-output"
    swapped_selector = deepcopy(mock)
    swap_first_two(swapped_selector["native_basis"]["vertex_selector"])
    swapped_simplices = deepcopy(mock)
    swap_first_two(swapped_simplices["native_basis"]["simplices"])
    relabeled = deepcopy(mock)
    for pair, mode in zip(relabeled["native_basis"]["modal_pairs"], relabeled["calibration"]["modes"]):
        for field in ("mode_id", "u_id", "v_id"):
            pair[field] = "alias-" + pair[field]
        mode["mode_id"] = pair["mode_id"]
    relabeled["calibration"]["output_ids"] = [
        pair[field] for pair in relabeled["native_basis"]["modal_pairs"] for field in ("u_id", "v_id")
    ]
    cases = [
        ("canonical mock", mock, 0, "PASS:"),
        ("swapped modal pairs", swapped_pairs, 1, "match calibration.modes in order"),
        ("orphan output", orphan_output, 1, "match the ordered"),
        ("swapped selector rows", swapped_selector, 1, "select its simplex rows"),
        ("swapped simplex rows", swapped_simplices, 1, "lexicographic row order"),
        ("coordinated relabeling", relabeled, 0, "PASS:"),
    ]
    with TemporaryDirectory() as directory:
        path = Path(directory) / "binding.json"
        for name, record, exit_code, diagnostic in cases:
            path.write_text(json.dumps(record))
            result = subprocess.run([sys.executable, str(CHECKER), str(path)],
                                    capture_output=True, text=True)
            assert result.returncode == exit_code and diagnostic in result.stdout + result.stderr, (name, result)
            print(f"PASS {name}: expected exit {exit_code}")


if __name__ == "__main__":
    main()
