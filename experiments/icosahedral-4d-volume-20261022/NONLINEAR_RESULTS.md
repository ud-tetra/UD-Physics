# Nonlinear discrimination: 4D apex versus 3D mechanical analogues

**Session:** `icosa4dvol-20261022-gpt6-c7d2` | **Run:** `nonlinear-003` | **Branch-only:** EXACT / CONDITIONAL / NUMERICAL / FAILED discriminator.

**Verified source baseline:** `ud-tetra/UD-Physics@92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa`; prior 4D-to-volume experiment and exact equal-edge selection. Claim `23b04a0533df0bd6b26f0c7fc9f94a6864400cea` was checked held before continuation. This extension adds a new run; it does not modify previous captures.

## Question and assumptions

Does the extra Euclidean apex coordinate produce a nonlinear 3D shell-volume/force signature that a comparably flexible ordinary 3D passive mechanical system cannot replicate?

Coordinates `(s,z)` are a homothetic regular icosahedron shell and an apex fourth-axis displacement, normalized by edge length `a`. The shell remains in its fixed 3D hyperplane; the 4D bulk metric is positive Euclidean. Physical clock time is an independent Newtonian parameter. `rho²=(5+sqrt(5))/8`, `eta²=1-rho²`, `s*=1,z*=eta`. All springs have rest length `a`; 12 radial and 30 shell edges. `U/a²=6 kr (sqrt(rho²s²+z²)-1)²+15 ke(s-1)²`. Generalized mass `M=diag(12ms rho²,ma)`, with illustrative `a=kr=ke=ms=ma=1`, viscous `C=0.06M` for damped probes, and generalized force applied to z. Volume readout `V/V0=s³`. No physical data fitted; equal-edge geometry was an exposed target, while laws, spring calibration and forcing channel are imposed.

## Central result — exact non-identifiability within stated model class

The alternative *ordinary Euclidean 3D* guided-carriage positions `A=(rho*s,0,0)` and `B=(0,z,0)` have interpoint separation `sqrt(rho² s²+z²)`. Twelve copies of this spring together with shell-stiffness coupling realize exactly the **same scalar potential** for every `(s,z)`. Assumed ideal transmission/carriages and matching effective generalized masses, damping and force port give the identical full reduced nonlinear equations and volume readout, not merely matched linear transfer. This is a mathematical *existence* analogue with constrained 3D apparatus; it does not prove native locality, unconstrained icosahedral 3D mechanics, or equality of additional fields and observables.

At unit parameters, the quasistatic force-to-fractional-volume expansion (force conjugate to dimensionless z, in units `ka²`) is:

`deltaV/V0 = -0.2927050983124842 f + 1.154242419234321 f² - 10.423365879953792 f³ + O(f⁴)`.

These are exact symbolic derivatives evaluated numerically; the full symbolic coefficient expressions are in run_results.json. The matched 3D carriage has identical coefficients **to all orders** by exact equality of potential, effective masses and readout. A simpler quadratic 3D null matched only at the linear stiffness differs at higher orders and therefore does not discriminate dimensionality.

## Finite-force stability

The positive-height equilibrium branch has a negative-force saddle-node at `f=-0.0525875220599`, `s=1.00903853259`, `z=0.177004344668` (unit parameters). The full local Hessian determinant vanishes; a stable positive-height continuation at `f=-0.08` **FAILED**. No global non-existence theorem is claimed for other branches. The matching 3D carriages have the same fold.

## Dynamical checks

6 Gaussian pulses `A` in `[-.08,-.02,-.01,.01,.02,.08]`, time domain [0,70], DOP853 relative tolerance `3e-12`, absolute `3e-14`. Largest absolute state/readout 4D-versus-exact-3D trace mismatch across runs: `3.5978e-12`. Nonlinear volume responses differ from a simple *quadratic* two-coordinate 3D null by as much as `0.0912061` fractional volume (for the largest selected pulse, not a systematic model optimization).

Undamped full coupled nonlinear evolutions from mass-normalized lower-mode displacements: frequencies (amplitude: 4D / ordinary 3D planar):
- `0.005: 0.886552676 / 0.886552676`, fractional change versus linear `-0.0001940`.
- `0.020: 0.883887445 / 0.883887445`, fractional change versus linear `-0.0031997`.
- `0.040: 0.874975765 / 0.874975765`, fractional change versus linear `-0.0132498`.
- `0.060: 0.859275349 / 0.859275349`, fractional change versus linear `-0.0309559`.

Finite-time peak-interval estimator: this is **not** an exact full nonlinear normal-mode backbone. A separate analytic one-dimensional constrained modal slice yields a frequency-softening coefficient, but its slice is not invariant under full nonlinear coupled dynamics.

## Checks and alternatives

PASS: independent 3D/4D Euclidean distance formulas and potential identity; exact Hessian and implicit static derivatives through third order; finite-force derivative checks; independent 3D planar gradient implementation; Gaussian time-series agreement; undamped mode-frequency agreement across amplitudes. Reported checks are constructor/self-review, not independent replication. Local `python3 -m py_compile` and script execution completed. Repo `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` are **NOT_RUN** in this connector-only checkout, which is not a full Git repository; GitHub CI and external experimental verification are not claimed.

Negative results preserved: unconstrained physical 3D analogues are not ruled out (indeed an exactly matching guided 3D mechanism exists), the 3D linear null's failure is not a physical 4D signature, and the negative-force fold invalidates simple extrapolation outside its stable branch. 3D guided carriages have ideal constraints/transmission; the 4D interpretation likewise fixes shell w to zero, and has no native UD selection or GR/QFT readout. No independent target holdout or physical time/energy calibration.

**Next discriminant:** Compare constrained full 4D shell/apex normal modes with 3D *local, isotropic, reciprocal* networks of explicit complexity and equal access to internal scalar modes. State permitted linkages, materials, ports and readouts before searching for a dimensional discriminator. Priority 97/100. No mainline export.

## Versioned capture correction (integrity only)

First attempted capture `nonlinear-002` FAILED repository validation at GitHub Actions 39857539810 because its schema-2 input metadata omitted the required `source_path` field. This invalid attempt was withdrawn from the current branch tree, while its Git history is retained. The new `nonlinear-003` preserves unchanged code/results/pulse bytes and declares `source_location=repository` with the explicit script source path. Mathematical conclusions and target exposure are unchanged; subsequent CI status is assessed separately.
