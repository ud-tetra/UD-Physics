# Checkpoint: local reciprocal 3D network versus 4D apex

Session `icosa4dvol-20261022-gpt6-c7d2`; held claim `refs/heads/claims/icosahedral-4d-volume-20261022` at `23b04a0533df0bd6b26f0c7fc9f94a6864400cea`. Existing research branch prior SHA `1bc9f2d450bde6deb85f0b05dd31109795ef2b76`. New calculation `locality-001` is a separate additive artifact; no history rewritten, no mainline export.

STATUS: HANDOFF / CLAIM HELD. Findings EXACT/CONDITIONAL, NUMERICAL, and FAILED uniqueness.

The 3D all-pairwise spring countermodel has 24 nodes, 132 springs, full weighted distance constraint rank66, six rigid null modes; its 2D invariant uniform sector exactly matches K and M of 4D. Constructive cost 32 additional positive full-system modes compared with the entire 4D system. It differs at nonlinear order and in nonuniform readouts. Prior exact nonlinear equivalence using a guided 3D reduction remains unchanged.

Assumptions: target-exposed 4D K/M, gamma=1/5, b0=1/4, cross k=1/20, three tuned positive stiffnesses and fitted inner mass. Local Hookean springs, zero prestress, SO3-invariant energy, no material prototype or spacetime mapping. Mathematical receipt and code/outputs/manifest in run capture.

Executed: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 locality_audit.py` PASS with SymPy/NumPy/SciPy self checks. New repository validation and independent empirical check NOT_RUN until CI/reviewer; earlier PR CI does not certify new edits.

Next: constrain node counts/component budgets and frozen 3D model family, evaluate nonuniform/spectral or controlled interventions against actual physical data. Open PR39 remains draft until review. Preserve held claim until integration or abandonment.
