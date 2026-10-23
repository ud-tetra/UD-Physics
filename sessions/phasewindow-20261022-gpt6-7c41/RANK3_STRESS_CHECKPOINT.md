# Rank-three spectral-stress handoff (2026-10-22/23)

Session `phasewindow-20261022-gpt6-7c41`, task claim held at `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`; research branch isolated, imported main `bbf7b9ec09a86378f6503c16460771a033e48593` read-only.

**EXACT / CONDITIONAL:** 12-vertex adjacency characteristic polynomial gives PSD Omega with eigenvalues 0x4, (1+sqrt5)x5, (2sqrt5)x3. For any shell Y, tr(Y^T Omega Y)>=(1+sqrt5)||Z||². For 3D flat face, the necessary singular-value inequality is in RANK3_STRESS.md.

**EXACT / FAILED patch strategy:** frozen rational 3D nine-vertex induced patch has rank-three coordinate span, selected face rank2, and positive spring potential U9<1/20<1360051/20000000. Omitted positive terms mean NO complete twelve-vertex underbudget collapse is established.

**NUMERICAL:** 84/36/9 subset surveys plus selected increased multi-start checks; apparent shallow nine-vertex barriers failed. Numerical 11-vertex candidate minima above target are NOT rigorous.

Original full12 barrier, all-time orientation, u100 breathing/ringdown, native UD selection and physical calibration OPEN. Rank4 Gram witness remains preserved; no overlap with held PR44.

Verification: previously locally executed full exact script and separate high precision implementation PASS. Branch compact source and repo test suite require execution/check under PR CI. Local ZIP captures complete script, witness, exact output and numerical survey. Task claim remains held, PR45 draft, no mainline export.

Next priority 98/100: full rank3/12-vertex certified optimization or exact inequality combining stress and affine deformation; adversarially test partial patch and rank4 witnesses.
