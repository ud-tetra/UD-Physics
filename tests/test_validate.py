import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from validate import LEGACY_EDGE_RUN, LEGACY_EDGE_TASK, LEGACY_RECORD_FIELDS, validate


class LegacyEdgeArchiveTests(unittest.TestCase):
    def test_scoped_compatibility_preserves_integrity_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in LEGACY_RECORD_FIELDS:
                path = Path(name)
                (root / path.parent).mkdir(parents=True, exist_ok=True)
                shutil.copyfile(REPO / path, root / path)
            run = Path(LEGACY_EDGE_RUN).parent
            for child in ("inputs", "files"):
                shutil.copytree(REPO / run / child, root / run / child)
            self.assertEqual(validate(root), (4, []))

            other = root / "tasks" / "unrelated.json"
            other.write_text((root / LEGACY_EDGE_TASK).read_text()
                             .replace("edge-preparation-homogeneity-20261116-6c91", "unrelated"))
            self.assertEqual(validate(root)[1], ["tasks/unrelated.json: Invalid task status"])

            output = next(f for f in (root / run / "files").rglob("*") if f.is_file())
            output.write_bytes(output.read_bytes() + b"tampered")
            self.assertTrue(any("SHA-256 mismatch" in error for error in validate(root)[1]))
