# Checkpoint: rank-unrestricted icosahedral Gram relaxation fails

STATUS — EXACT / CONDITIONAL / FAILED CERTIFICATE FAMILY.
Task `icosahedral-phasewindow-20261022`; session `phasewindow-20261022-gpt6-7c41`; held task claim. Branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Verified current main `1b214f66e00e8430fed0ce7c23506da7965bc977`; integrated mechanics are read-only. PR45 draft/unmerged; PR44 recovery held by another session.

Question: can a convex rank-free Gram relaxation certify E_min(flat)>original pulse E0=1360051/20000000?

Finding: **NO.** EXACT rational rank-four Gram witness, selected exterior face Gram det=0, total Gram rank=4, original reference graph exactly 12 vertices/30 edges, strictly positive member lengths, primary model with g=19/20 and k=19/50, energy certified **strictly below 1/20**, itself less than E0. This is **not** a 3D counterexample; 3D global lower bound remains OPEN.

NUMERICAL source: 17 relaxed-dimension minimizations at d=3,4,5,8,12, exposing dimension/starting-lift freedom. d4 energy about .047842; d5+ about .047458. 3D numeric minimum from prior campaign .124426 remained unproved. Rational 4D coordinates were obtained by rounding a fitted optimizer solution, then independently validated by exact arithmetic. No physical target or new constitutive law.

Proof: `experiments/icosahedral-phasewindow-20261022/GRAM_RANK_RELAXATION.md`; exact verifier `gram_rank_witness.py`; independent same-runtime SymPy `gram_rank_sympy.py`; frozen candidate `gram_rank_witness.json`; exploratory `gram_rank_relax_search.py`; source graph exact Q(sqrt5). Immutable run `artifacts/phasewindow-20261022-gpt6-7c41/gram-rank-008/` retains code, candidate, result, numerical scan, manifest with SHA256.

Checks: exact `fractions.Fraction` inequality PASS; exact symbolic face Gram det/ranks/reference edges PASS; numerical scan PASSED but is exploratory; repository CI NOT_RUN unless subsequently verified; independent physical test NOT_EXECUTED. This is a constructor adversarial check, not empirical evidence.

Failures preserved: rank-free PSD/Gram/SOS lower-bound path cannot certify original pulse barrier. Earlier finite time u=49/50 theorem unchanged. No rank-three global optimization, no u100 nonlinear result, no mainline export.

Next: rank≤3 constrained Gram polynomial SOS / validated interval branch-and-bound; maintain counterexample as a guard. Prepare independent mathematical review; do not merge until source replay and CI verify final head; keep existing claim until review/integration or explicit abandonment.
