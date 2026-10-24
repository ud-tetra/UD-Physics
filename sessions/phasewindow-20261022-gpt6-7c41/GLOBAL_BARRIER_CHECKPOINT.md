# Checkpoint — global icosahedral cell-collapse energy barrier

2026-10-23 UTC; source main `467e2208fba9da086535bd5b8a6a07f6d6f8e08b`, phasewindow session `phasewindow-20261022-gpt6-7c41`, held task claim and isolated phasewindow branch.

**EXACT/CONDITIONAL completed:** Explicit rational shell coordinates provide a genuinely coplanar centre-to-face cell, all retained lengths nonzero, and a rationally verified total conservative energy **strictly below 1/8** at allowed minimum g/k. This is an upper-barrier witness only. A different exact local-only face arrangement costs **strictly below the original pulse energy** when 27 other edge springs and 9 other radial contributions are ignored. Thus the full global shell geometry is indispensable for an energy-only all-time orientation certificate.

**NUMERICAL development:** 72 constrained full-shell minimizations with analytical gradients, all converged; 59 reached the best observed 0.12442609484; separate coplanarity parametrization found same result. This number is not a proven global minimum or minimum barrier. Original reference energy is 0.06800255. No physical data were fit or held out.

**FAILED/OPEN:** Neither local six-member energy inequalities nor numerical optimizer convergence certify global minimum energy above the original pulse. Therefore the nonlinear original pulse **u100 safety, breathing and ringdown remain OPEN**. The previous exact u49/50 time safety is unchanged and preserved. PR44's forced Green recovery is owned by a different active task and not modified.

Code: `barrier_audit.py`, `verify_witness.py`, `independent_check.py`. Data: `barrier_results.json`, `flat_witness.json`, `witness_result.json`, `candidate_flat_vertices.csv`. Independent same-runtime reconstruction and derivative finite differences executed; global rigor and independent external review NOT_RUN.

Repository integrity should run on any published branch head. User-directed work remains Discovery only; no mainline export. Next: globally certified lower bound or explicit below-energy collapse counterexample; then return to u100 forced response once PR44 source recovery is verified.