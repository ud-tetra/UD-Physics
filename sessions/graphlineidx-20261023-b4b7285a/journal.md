# Graphite linewidth integration pointer

- Verified main `9f5c49a1d6cea34499f22ac8470bf6b3c98ab82d` includes linewidth research PR #88 and closure PR #89. Held integration claim `ac6831bbf6585cc79b6ec17770dac0ec3d766357` acquired before editing shared paths.
- Linked the conditional material-width transfer from the original graphite entry and current state, preserving the absence of measured dissipative widths and UD-specific source calibration. No revision of the versioned PDF.
- Next: acquire mode-resolved pressure-dependent dissipative widths and off-diagonal self-energy, then source-specific coupling and held-out signed force data.
- Checks: `python3 scripts/validate.py` PASS (169 records); `python3 -m unittest discover -s tests -q` PASS (16 tests). Repository integrity only.
- Closure: PR #90 merged as `848358a1c642af177ab813d7fcf95aa9caf18123`, CI run 40048700565 succeeded, and exact-SHA release marker `5905d547529207f016dd0ec9eff2a482c41cc000` was verified.
