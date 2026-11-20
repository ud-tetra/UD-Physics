# Session journal — March native modes
BOOT: ud-tetra/UD-Physics@2ab32f5f28d0461dc4d35a389e814e8415cb58e8, connector write + local Python compute, claim refs/heads/claims/march-native-mode-publication-20261115-2ce90b held at 0c0757cf0f2d9878a23f37c04f47ea4efb983a7a.
Sources: recovered user March files; current UD mainline/source v0.85 takes precedence over historical v0.39 where conflicting. Linked mainline capture: https://github.com/ud-tetra/UD/commit/dfa3d08de54205ad13bc29b8aa100a75024d7b46.
Calculation: raw iid binary b_v ∈ Z2, edge characters (-1)^(b_i+b_j), unsigned face-edge incidence H, covariance C=HHᵀ/16.
Conditional null generator: one uniformly selected vertex flip per event tick; q_N=1-4/N. Fully admissible K4 face-gate readout has zero variance; isolated vertex changes event rate but not face covariance. Neither event law nor physical k mapping is sourced.
Target exposure: observed cosmological tilt/running were known from historical March model; face covariance itself did not fit them. No held-out physical comparison executed.
2026-11-15 local verification: historical March script, Gap2 script and independent face-mode replay each exited 0. Exact artifact byte hashes preserved from local source when uploaded as UTF-8 with trailing newline.
Review status: constructor/local replay only; non-constructor reviewer pending. GitHub validation suite NOT_RUN in this connector-only runtime.
Next: source-selected local seam/phase/burden/closure transition law and matched null; then nonconstructor review. Physical promotion 0.
