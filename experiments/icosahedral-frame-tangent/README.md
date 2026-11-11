# Archived 180-column icosahedral frame projection and moving-reference repair

**RESULT — NUMERICAL final-time counterexample to the prior equilibrium-radius antecedent; EXACT / CONDITIONAL moving-reference chart theorem.** The source 3D 560-phase mechanical ODE, 180-dimensional housing-phase energy ball, damping/material family, and previous accepted results are **unchanged**. A full time-uniform nonlinear u=100 robustness certificate remains **OPEN**.

## Source, question, model scope and chronology

Read-only integrated 3D source: \`ud-tetra/UD-Physics@447ee4df3b9bc3e71bdfee3e29f7ee9379410df7\`, [moving-pulse tangent analysis](../icosahedral-pulsetube/README.md), [tube theorem](../icosahedral-pulsetube/TUBE_THEOREM.md), [exposed numerical results](../icosahedral-pulsetube/RESULTS.md), [archived immutable checkpoints](../../artifacts/icosahedral-pulsetube-20261022-a1/pulsetube-001/files/compact_checkpoints.npz). The newer [frame-001 draft PR #187](https://github.com/ud-tetra/UD-Physics/pull/187) at \`f1294cd0b7a6887ff9722fb5f8cb6dfc2b065b03\` is an unmerged *read-only research reference*, NOT an integrated task dependency.

The source mechanical model has 280 configuration / 560 mechanical phase variables plus a heat accumulator, consisting of one alpha, thirteen unconstrained spatial primary points, 150 auxiliary device coordinates and thirty moving housing points. Positive current-axis strut damping, geometric response, spatial rigid momentum, heating and all material parameters remain exactly as in the original source. This study changes ONLY geometric postprocessing of the 13 primary positions, and tests how the already archived 180 initial-housing directions appear under that postprocessing.

The frozen source parameter cases at strength nu=0.05 are the previously exposed \`seed10422-0-boundary2\` worst limiting case and \`uniform-b0.05-cf0.0\` nominal case. Initial housing energy E_h=E_p/40000 is unchanged. Length/time/energy units ell0,t0,E* have no physical SI calibration. No material/damping parameter was refitted; previously exposed target raw radius 0.03500972 and Procrustes shape radius 0.0002420865 influenced choice of chart/radius and are FIT/development exposure, not independent prediction.

## 1. Exact archival data and reproducible endpoint re-projection

The integrated 2.67 MB \`compact_checkpoints.npz\` archive holds, for the limiting normal/fine and nominal normal cases, the **final** tangent W(100) of shape 560×180, 561-entry initial and final reference states, the 560×180 initial injection and selected volume Grams/cross terms. It does **not** hold U(t,0)B at every time or the full forced Green U(t,s); the original large intermediate NPZ time histories were explicitly left uncaptured by the source and require rerunning its unmodified variational ODE.

The new executable [repository test](../../tests/test_icosahedral_frame_tangent_20261025.py) uses only Python 3 standard-library \`zipfile\`, \`array\`, \`struct\` and a 39×39 symmetric Jacobi eigensolver. CI executes it in a repository checkout directly against those archived binary bytes; no assumption is made that a container can independently download or edit the binary. The source checkpoint's \`reference_initial[1:40]\` and \`reference_final[1:40]\` contain the hub first and twelve shell points next. The tangent's corresponding physical q rows are \`W[1:40,:]\`. Scale them by \(\epsilon=\sqrt{2E_h}\), so the operator norm is the radius for all unit-norm 180 initial housing directions at the *endpoint*.

For an isotropic equilibrium shell \(X\), subtract the mean shell-position error from all 13 points. The first derivative of the explicit proper SO3 chart previously introduced is \(E\mapsto E_{\rm centered}-X\Omega\) on shell, with the hub's reference position zero. For a **moving reference shell**, the correct infinitesimal proper rotation instead solves
\[
G\Omega+\Omega G=2\operatorname{skew}(X_{\rm ref}^\top E_{\rm shell,centered}),
\quad G=X_{\rm ref}^\top X_{\rm ref},
\]
and the **hub** derivative is \(E_{h,\rm centered}-h_{\rm ref}\Omega\). The new archive test includes this hub term and uses a 3×3 positive-definite Sylvester solver. This is a local proper-frame tangent, not a transformation applied to any dynamical state/momentum.

**NUMERICAL final-time results from [CI test run 40213880131](https://github.com/ud-tetra/UD-Physics/actions/runs/40213880131):**

| case at u100 | Raw eps*||Wprimary||2 | Equilibrium-frame eps*||DFrame Wprimary||2 | Moving-reference eps*||DFrame_t Wprimary||2 | ||Yref(100)-Yeq||F |
|---|---:|---:|---:|---:|
| limiting fine | 0.03500971996661 | 0.00009867394738 | 0.00009867394310 | 0.01052593951521 |
| limiting normal | 0.03500971996662 | 0.00009867394256 | 0.00009867393828 | 0.01052593951174 |
| nominal normal | 0.03520937943793 | 0.00016894760813 | 0.00016894760813 | 0.00935149933936 |

The largest limiting raw/final shape operator ratio is roughly 355. These are full 180-direction endpoint *linear operators*, not 180 random preparations, but the CI Jacobi eigensolver remains floating-point numerical verification rather than a certified interval singular-value bound. The moving limiting shell has Gram anisotropy \(\max|G-\operatorname{tr}(G)I/3|\approx9.9286\times10^{-5}\) and hub offset from shell centroid \(\approx1.9520\times10^{-5}\). The nominal reference stays isotropic to numerical precision.

## 2. Explicit linearized counterphases defeat the old raw-radius antecedent

The old [frame-001](https://github.com/ud-tetra/UD-Physics/pull/187) uniform analytic chart remainder required that the **total actual primary error from the static equilibrium** obey \(\|E\|_F\le0.036\). The earlier source number 0.03500972 was only the size of a housing **tangent perturbation** and did not include displacement of the reference breathing pulse.

At final time construct admissible unit-norm housing phase directions \(a\in\mathbb R^{180}\). The test uses a deterministic matched-to-reference direction \((W_{\rm primary}^\top b)/\|W_{\rm primary}^\top b\|\), and/or deterministic 500-step leading raw tangent power-iteration directions, plus both signs, where \(b=Y_{\rm ref}(100)-Y_{\rm eq}\). Each candidate is exactly specified by executable source; no outside parameter or dataset is used. The corresponding linearized full error \(b+\epsilon W_{\rm primary}a\) yields:

| case | Constructed feasible lower bound on maximum linearized total error |
|---|---:|
| limiting fine | **0.03661309786733** |
| limiting normal | **0.03661309786648** |
| nominal | **0.03643008290268** |

All exceed 0.036. Consequently the \`frame-001\` radius is **insufficient as an all-initial-phase endpoint bound even for the *linearized* model**. This is not a counterexample to the exact conditional chart theorem (its antecedent is false for these linearized preparations). Neither is it an actual nonlinear trajectory counterexample: the finite-amplitude mechanical flow has unverified second-order error and the full nonlinear maximum may differ. These numerical phase witnesses are development/target-exposed, not a blind test.

## 3. New EXACT/CONDITIONAL moving-reference chart repair

Define \(Y_0\) as the 13-point equilibrium configuration, including the centered regular icosahedron shell and the hub. At an arbitrary but fixed time, suppose the **actual reference** \(Y_{\rm ref}\) satisfies
\[
\|Y_{\rm ref}-Y_0\|_F\le d:=11/1000
\]
and the **actual perturbed** 13-point state satisfies
\[
\|Y_{\rm actual}-Y_{\rm ref}\|_F\le r:=9/250.
\]
The first inequality is **only numerically checked at the final endpoint** for the two source cases, not continuously in time or rigorously with validated ODE integration. The second inequality is NOT verified for the nonlinear mechanical flow.

At each time, center the moving shell \(X_{\rm ref}\) and moving hub \(h_{\rm ref}\) by the reference shell centroid, let \(G=X_{\rm ref}^\top X_{\rm ref}\), and solve
\[
G\Omega+\Omega G=2\operatorname{skew}(X_{\rm ref}^\top \widetilde E_s).
\]
Here \(\widetilde E\) is the error after subtracting its shell centroid from both shell and hub, and \(\Omega\) is skew; then \(R=\exp(-\Omega)\in SO(3)\). The aligned error chart is
\[
\mathcal F_{\rm ref}(E)=
\begin{pmatrix}
(X_{\rm ref}+\widetilde E_s)R-X_{\rm ref}\\
(h_{\rm ref}+\widetilde e_h)R-h_{\rm ref}
\end{pmatrix}.
\]
Its derivative at zero is \((\widetilde E_s-X_{\rm ref}\Omega,\;\widetilde e_h-h_{\rm ref}\Omega)\), exactly the operator used in the source final-tangent CI test. It removes infinitesimal translations and rigid rotations without deleting rigid mechanical momentum or internal energy.

For the golden-ratio reference \(X_0^\top X_0=c_0I_3\), \(c_0=(5+\sqrt5)/2\), exact rational upper/lower constants are
\[
c_0>7/2,\quad\|X_0\|_{\rm op}<39/20,\quad
\|Y_0\|_F<27/8,\quad\sqrt{13/12}<21/20.
\]
Because the centered reference shell differs from equilibrium by no more than \(d\),
\[
\lambda_{\min}(G)\ge c_0-2(39/20)d-d^2
>\frac{3456979}{1000000}.
\]
The skew Sylvester operator \(G\Omega+\Omega G\) has minimum singular value at least twice this eigenvalue on 3D skew coordinates. Using \(1/\sqrt2<3/4\) and the above limits, for every \(\|E\|_F\le r\),
\[
\|\Omega\|_{\rm op}\le
t_*:=\frac{52947}{3456979}\approx0.01531597<1.
\]
The full centered reference norm is bounded by \(27/8+(21/20)d\). The exponential remainder and product terms then yield the EXACT rational bound
\[
\boxed{
\|\mathcal F_{\rm ref}(E)-D\mathcal F_{\rm ref}(0)E\|_F
\le\frac{93325499434647}{94141337114624000}
\approx0.000991333906<0.001.}
\]
This proof and exact Fraction checks are reproducible in [moving_frame_bound.py](moving_frame_bound.py). The bound is uniform across **all 13-point relative error directions** satisfying both radius hypotheses and works for the moving, mildly anisotropic reference. It does NOT prove either hypothesis for actual nonlinear dynamics. The quantity bounded is a geometric SO3 chart error, **not** the full nonlinear flow remainder or the oriented-volume determinant remainder.

## 4. Discriminating evidence, remaining conditions, baseline

The source [a posteriori pulse tube](../icosahedral-pulsetube/TUBE_THEOREM.md) still requires validated full forced Green \(U(t,s)\) on 560 dynamical variables, positive time-dependent full-state norm (rigid momenta retained), uniform flow Hessian/remainder on the tube, numerical reference defect plus reference-error enclosure, continuous \(\|Y_{\rm ref}(t)-Y_0\|\) and \(\|Y_{\rm actual}(t)-Y_{\rm ref}(t)\|\) bounds, and continuously positive mount lengths/cell orientations. A meaningful all-housing-phase \(u=100\) 80% breathing certificate must add the nonlinear aligned volume derivative/determinant remainder to the flow and frame errors in the SAME norm. None is newly claimed solved by endpoint tangent spectra.

The numerical result does identify the right next projection: **frame-aware endpoint shape response can be much smaller than raw displacement**, but a static equilibrium-radius assumption that ignores reference breathing is structurally inadequate. A moving-reference chart can repair the readout subproblem under explicit radius conditions. Generic SO3 alignment of a 3D spring/dashpot network has the same result; this is a conventional 3D mechanics null. It does not select native UD constitutive constants, physical scales, or an independent stress/dispersion prediction.

## Reproduction and checkpoint

1. From a complete repository checkout, run \`python3 -m unittest discover -s tests -v\`, which includes [test_icosahedral_frame_tangent_20261025.py](../../tests/test_icosahedral_frame_tangent_20261025.py). The test reads the pinned archived NPZ with pure standard-library zip/NPY parsing; no download from restricted web/API or dependency on NumPy in CI.
2. Run \`python3 experiments/icosahedral-frame-tangent/moving_frame_bound.py --out /tmp/moving_bound.json\` for the exact rational moving-chart bound.
3. [Immutable tangent-001 run](../../artifacts/ico-frametangent-20261025-gpt6-a1/tangent-001/manifest.json) captures the exact CI-executed test script (SHA-256 \`202e07f8ea5fafceb72cdcc9ca0970307c3a87111ae63bb2ceb9f384a4ed7dfd\`), full endpoint result (SHA-256 \`c4a7bf9973c09781682dddcda2ebcdc2a3ae0c37c74641e7508abc83b31dc40c\`), exact standalone theorem (SHA-256 \`3a6ea505a8b36e2aa7fc2cd7a3432a62d24ea86ec25b531e372f5deac73dddbf\`) and its exact output (SHA-256 \`9fc65751d193d6e575308af336184bd504cb194268f67b21b98978c193ea0fb8\`). The endpoint computations ran in GitHub Actions CI #40213880131; the theorem ran locally in standard-library Python, each with actual distinct execution provenance.
4. Input source revisions and target exposure are recorded in the session and mathematical receipt. No original prior artifact, frozen physical coefficient, 4D model, QPB or mainline shared state was altered.

**Status: NUMERICAL endpoint counterphases, EXACT / CONDITIONAL moving SO3 bound, full nonlinear u100 certificate OPEN.** Independent non-constructor mathematical review NOT_RUN, material implementation and physical validation NOT_EXECUTED.

**NEXT (priority 99/100):** reproduce time-dependent 560×180 tangent \(U(t,0)B\) from the retained source runner and project it into this SAME moving reference, then produce **verified** reference and relative full-state bounds plus forced Green \(U(t,s)\), nonlinear and alignment/volume remainders. Park a global all-phase guarantee if those quantities cannot be enclosed; do not replace them with endpoint or sample checks.
