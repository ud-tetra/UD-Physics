# Checkpoint027 — exact symmetric source trajectory

**EXACT / CONDITIONAL:** Source-matched original 3D uniform pulse on 187 slabs through u=187/40=4.675. The exact piecewise rational Taylor defect is <3.3e-30 and a source state error energy norm bound is <3e-28, conditional on the imported original 3D mechanical equations. All 187 polynomial energy/Bernstein checks, safe-domain checks, and C0 joins executed successfully.

Provenance: held claim `claims/icosahedral-phasewindow-20261022`, owner session `phasewindow-20261022-gpt6-7c41`, read-only integrated main `3b9f6dee5e8c69cf9b4d11787966bda05f99137d`; mechanical source blobs verified unchanged. The detailed proof is `experiments/icosahedral-phasewindow-20261022/SOURCE_PEAK_027.md`.

Independent checks: reconstructed all 120 moving-axis damping paths from original 3D geometry, maximum force residual 2.54e-16; independent DOP853 endpoint difference to exact Taylor polynomial center 6.98e-14. These are NUMERICAL constructor checks, not the source of the exact bound.

Local immutable reproduction: `UD_3D_Exact_Source_Peak_027_20261102.zip`, SHA256 `0eb7227b5e51ac918e3f6cf871aec10c7d3e47feade66734ba18f2ae48a8edd7`. Five inputs, fifteen outputs, schema2 SHA256 metadata, eight staged execution results. Full executable ZIP local, not claimed uploaded into repository.

**OPEN:** Frozen checkpoint026 21MB binary64 sector4 spline is not available in current runtime; no source-to-spline eta<=1e-8 proof. No validated 4000-slab composition or unrestricted u100 nonlinear phase-ball theorem. PR44 remains separate held ownership; PR45 is draft and no mainline export.

**NEXT priority 99/100:** Recover the exact frozen sector4 spline and use the certified source baseline on [4.65,4.675] to enclose source Jacobian minus spline in directed interval arithmetic. Prove or refute eta<=1e-8; preserve original source, no retuning.
