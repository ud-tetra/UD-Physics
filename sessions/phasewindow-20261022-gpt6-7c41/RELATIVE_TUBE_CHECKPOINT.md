# Checkpoint — improved original-pulse relative tube (relative-tube-005)

**STATUS — EXACT / CONDITIONAL / HANDOFF** (2026-10-22). User-authorized 3D Discovery only. No mainline export.

**Repository:** ud-tetra/UD-Physics. Verified main read-only revision `2b133c7889cde7aae9127d0c0fa2036c278884a9`; original MountLoss, Hardware, Free3D source files remain byte-identical with the prior integrated mechanical baseline. Research branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`; owning session `phasewindow-20261022-gpt6-7c41`; live held ref `claims/icosahedral-phasewindow-20261022` remains held under this session. Draft PR #45 pending review.

**Question:** Does the original `alpha(0)=1/10` nonlinear 3D MountLoss pulse preserve positive housing-strut lengths, primary members and all 20 oriented cell-volume signs beyond `u=2/5` for *every* initial housing phase with `Eh<=51/20000000`, throughout qualified continuous material parameter ranges?

**EXACT / CONDITIONAL FINDING:** Yes through `u=9/10`. Every one of 120 struts is strictly >`11/1250` reference edge lengths and every oriented cell volume ratio lies strictly between `27/1000000` and `7645373/1000000`, for every `u in[0,9/10]`. The ODE solution exists through that interval. No rigid modes or housing phase directions were suppressed. This is an 18x horizon extension relative to integrated `u=1/20` and 2.25x relative to prior shorttube corrected `u=2/5`.

**Method:** Improved endpoint-relative Duhamel identity, operator norm of instantaneous primary point velocity coefficients using the total positive kinetic energy (avoids counting common translation twice), exact all-interval `integral_0^x |sin t| dt<=3x/4` proof, and star-incidence operator norm2 for cell orientation. Exact Fraction inequalities; an additional same-runtime SymPy/star-spectrum check and sampled sine diagnostic were executed. Same-law passivity and domain continuation used. Horizon 9/10 is a chosen sufficient rational threshold (development/FIT), not an observed collapse transition.

**Reproduction:** `python3 experiments/icosahedral-phasewindow-20261022/relative_tube.py --out /tmp/relative-tube.json`; `python3 experiments/icosahedral-phasewindow-20261022/relative_tube_check.py`. Both underlying exact code and independent same-runtime check ran locally; byte-identical copies and full derivation were committed. Immutable `artifacts/phasewindow-20261022-gpt6-7c41/relative-tube-005/manifest.json` includes 5 source-code inputs and 2 output files with SHA-256 and sizes. Local archive `UD_3D_relative_pulse_tube_20261022_checkpoint.zip` also generated.

**Validation:** `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` NOT_RUN in local container without complete repo checkout. Check PR CI at exact head and record separately. Mathematical proof has no independent nonconstructor review; no physical tests.

**FAILED/OPEN:** Original energy-only u100 certificate remains obstructed by accessible singular housing configuration in total-energy sublevel (not a demonstrated trajectory). Full u100 nonlinear all-phase breathing>=80%, hub mismatch<=5%, housing ringdown<=50% remain OPEN. Prior nu=.02 low-beta and out-of-budget challenge failures unchanged. Hardware realization, native selection, physical clock/energy/length calibration UNSCORED.

**Next discriminant:** Coordinate nonoverlapping PR #44 recovery/forced Green bound; apply a positive full-state/frame-aware nonlinear tube starting from the newly established u=.9 safety domain, without claiming completion of the u100 target. Do not touch PR44 owned paths; leave this claim held pending review/integration.
