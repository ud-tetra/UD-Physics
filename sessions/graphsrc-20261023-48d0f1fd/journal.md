# Graphite source constraints

- Boot: clean `79fd6d6cc8f2d40d516df0074e728e3f9428f60b`; atomic held claim `41a13dcc31129026f6743a4587cf5a69b8e1c943`. Source archives are earlier integrated development; paired angles and weak load response already exposed.
- Exact construction: representative A1,A3,B0,B1 columns give eight real coordinates. The seven weight columns have rank six and uniform kernel; their left nullspace is two-dimensional with rows `(0,1,0,0,0,0,1,0)` and `(1,0,-1,0,1,-1,0,1)`. Checked full 14-site C3 covariance, two fixed-site zeros, and eight independent allowed basis maps. No fit to friction.
- Numerical replay: archived KC cross Hessians with prior C3 offset 2 and prior physical basis. Five cutoff/step variants violate both exact pure-source constraints. Their spread is parameter sensitivity, not experimental or model uncertainty. The conventional KC map may supply a baseline; this does not reject an *added* source component.
- Constructor correction: one initial assertion summed each source row across eight site coordinates rather than summing the seven source matrices at each coordinate to test the uniform-weight null. It failed as expected for that mistaken test; the code now checks the correctly typed column sum and was recaptured after correction.
- Checks: exact verifier PASS; `python3 scripts/validate.py` PASS (157 records); `python3 -m unittest discover -s tests -v` PASS (16 tests). These are constructor and integrity checks, not independent physical review.
- Next discriminant: infer site-resolved measured-minus-conventional coupling with baseline and registration uncertainty, then test both constraints; separately constrain bath stiffness/loss before a signed paired-angle force prediction.
- Closure: PR #83 merged as `e9dc0e074af561a8e9e309f72f2b6b365a7553c8` after updated-head CI success (run 40047683252); exact-SHA claim release marker `e3bb4941e4ebf3ebb483d8bb08155326d632abfe` verified. Independent physics review NOT_RUN.

## 2026-10-24T00:57:48.447697+00:00

Captured artifacts/graphsrc-20261023-48d0f1fd/exact-001 (EXACT): Two exact C3 source null constraints and five archived KC replays
