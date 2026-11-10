# UD Discovery — Full 12-vertex rank-three non-affine exclusion certificate

**RESULT: EXACT / CONDITIONAL.** A physical three-dimensional icosahedral shell in the original passive mechanical surrogate **cannot flatten any of its 20 centre-to-face cells under the original pulse-energy ceiling unless its residual from the full 3D reference-affine subspace has Frobenius norm strictly greater than `1/40` reference exterior edge length.**

This is a new **necessary condition** on a full-12-vertex collapsed configuration. It is **not** a global primary-energy barrier, a closed nonlinear `u=100` theorem, or an empirical UD/physical identification.

## Source, geometry, coordinates and units

The mechanical source was rechecked against `ud-tetra/UD-Physics` main at commit `0a058176d9dd079b6aad8fa530cd8093f1fcf43c`. Relevant source objects are the already integrated `experiments/icosahedral-free3d/model.py`, `experiments/icosahedral-multiport/network.py`, `experiments/icosahedral-tolerances/hardware.py`, and `experiments/icosahedral-mountloss/mountloss.py`. The current continuation owns only `sessions/phasewindow-20261022-gpt6-7c41/`, `experiments/icosahedral-phasewindow-20261022/`, `candidates/icosahedral-phasewindow-20261022/`, and `artifacts/phasewindow-20261022-gpt6-7c41/`, with the live claim still held. The Green-response draft PR #44 is held by a different session and is not edited.

Reference shell `V ∈ R^(12×3)` contains the twelve regular-icosahedron vectors centred at the free original hub, with exterior edge length `ell0=1` and squared circumradius

\[
R^2=(5+\sqrt5)/8 \in \mathbb Q(\sqrt5).
\]

For arbitrary *physical* shell points `Y_i=X_i-C ∈ R^3` measured from the moving hub, define shell translation and affine projection `Y=V B^T+1 t^T+Z`, where

\[
P_0=\frac{11^T}{12},\quad P_V=V(V^TV)^{-1}V^T,\quad
Z=(I-P_0-P_V)Y,\quad V^TV=4R^2 I_3.
\]

Here `B` is a real `3×3` linear map, `t` a real vector, and `Z` the genuinely **non-affine** shape residual. These are structural decompositions of actual coordinates, **not imposed dynamical constraints**. The metric for `||Z||_F` is the ambient Euclidean matrix norm, measured in reference exterior-edge lengths. The clock is the inherited continuous nondimensional Newtonian `u`; it is not relevant to this static exclusion theorem.

The unchanged positive primary elastic energy, with spoke strains `s_i=|Y_i|/R-1`, edge strains `e_ij=|Y_i-Y_j|-1`, scalar heart coordinate `alpha`, and qualified material lower endpoints, is

\[
U=\frac12\left[\alpha^2+\sum_i s_i^2+\sum_i g_i(s_i-\alpha)^2+\sum_{(i,j)\in E}k_{ij}e_{ij}^2\right],
\qquad g_i\ge\frac{19}{20},\quad k_{ij}\ge\frac{19}{50}.
\]

All port, housing and kinetic storage terms are nonnegative. Thus the full passive system starting in the original `alpha0=1/10` preparation, with enlarged housing energy allowance, satisfies `U(u)≤E_pulse` on the model's regular positive-length domain, where

\[
E_{\rm pulse}=\frac{1\,360\,051}{20\,000\,000}=0.06800255.
\]

The proof makes no assumption that `Y` stays affine.

## The exact 30-edge, fourth-moment identity

For each of the thirty unoriented unit reference exterior-edge vectors `d_e=V_i-V_j`, the icosahedral edge frame obeys, for **all** symmetric real `3×3` matrices `H,J`,

\[
\sum_{e=1}^{30}(d_e^T H d_e)(d_e^T J d_e)
=2\big[(\operatorname{tr}H)(\operatorname{tr}J)+2\operatorname{tr}(HJ)\big].
\]

A full six-element basis for the symmetric matrix space yields 36 exact bilinear checks over `Q(sqrt5)`, hence the identity follows for arbitrary real `H,J` by polarization. Consequently

\[
\sum_e(d_e^T H d_e)^2\ge4\|H\|_F^2.
\]

The original adjacency spectrum has eigenvalues `5, sqrt5, -1, -sqrt5`, with multiplicities `1,3,5,3`; its graph Laplacian has largest eigenvalue `5+sqrt5`. This controls edge differences of the non-affine residual by

\[
\Big(\sum_e|Z_i-Z_j|^2\Big)^{1/2}
\le\sqrt{5+\sqrt5}\,\|Z\|_F<\frac{27}{10}\|Z\|_F.
\]

## Energy allocation across antipodal radial modes

The 12 reference shell points form six antipodal pairs. Resolve the actual spoke strain vector into an odd and even part under antipodal exchange: `s=s_odd+s_even`. Set

\[
a=\|e\|_2,\quad o=\|s_{\rm odd}\|_2,\quad b=\|s_{\rm even}\|_2.
\]

Since the heart scalar `alpha` is even, and every `g_i≥19/20`, the original energy satisfies the **joint** lower bound

\[
2U\ge\frac{19}{50}a^2+\frac{39}{20}o^2+b^2.
\]

Under `U≤E_pulse` it follows that `a<3/5`. For `a` in each of the three disjoint bins below, subtract the minimum edge energy already consumed and apply the same inequality to obtain rational strict upper bounds:

| Edge-strain bin | Upper bound on `o` | Upper bound on `b` |
|---|---:|---:|
| `0≤a≤1/2` | `53/200` | `37/100` |
| `1/2<a≤11/20` | `3/20` | `21/100` |
| `11/20<a<3/5` | `21/200` | `3/20` |

The actual energy remainder in each bin is checked as an exact fraction, not estimated from a numerical solution.

## Why low-energy flattening must be non-affine

Assume by contradiction that some face is flattened and `||Z||_F≤δ=1/40`. Its three physical face vectors have a common perpendicular unit vector `w`. Denote `C=B^TB` and the reference face-plane unit normal by `n`. The regular-face centroid is `h n`, where

\[
h^2=\frac{7+3\sqrt5}{24},\qquad
\frac{h}{R}>\frac{79}{100}.
\]

The exterior-edge strain norm of the **affine projection** is at most `a+sqrt(5+sqrt5)δ`; bound it using `a+27δ/10`. The fourth-moment identity applied to `C-I` gives

\[
\lambda_{\min}(C)>\lambda_0
:=1-\left(a_{\max}+\frac{27}{10}\delta\right)
-\frac12\left(a_{\max}+\frac{27}{10}\delta\right)^2>0.
\]

Here `a_max` is the upper endpoint of the relevant bin. Thus **B is invertible**; this is derived rather than assumed. Let `q=B^{-1}t` and `v=B^Tw`. Because the face-centred reference frame satisfies

\[
\sum_{i\in F}(V_i-hn)(V_i-hn)^T=\tfrac12(I-nn^T),
\]

and `w` annihilates each actual `Y_i`, the three face residuals yield

\[
\|v_{\perp n}\|\le\sqrt2\,\delta,\qquad
|h(v\cdot n)+v\cdot q|\le\delta/\sqrt3.
\]

Using `||v||≥sqrt(λ_0)`, `R²>9/10`, `3R²λ_0>1/4` (all bins), and `sqrt(1-x)≥1-x`, one obtains

\[
\frac{|q|}{R}>
\frac{79}{100}\left(1-\frac{2\delta^2}{\lambda_0}\right)-2\delta.
\]

Now form the six differences between **squared radii** of antipodal shell vertices. For the affine component they are exactly `4 V_i^T C q`; by the icosahedral antipodal isotropy their Euclidean norm is `4sqrt(2) R ||Cq||`. For the actual shell these same six differences are bounded in terms of `o,b` by `2sqrt(2) R² o(1+b/sqrt2)`. Their discrepancy is bounded by `sqrt2 (2L+δ)δ` from the residual, where `L=137/100` is an exact pointwise upper bound on the actual shell radii under `U≤E_pulse`.

Dividing through by `2sqrt2 R²` and using `R²>9/10` yields the **necessary inequality for a flattened physical cell**

\[
\frac{79}{50}(\lambda_0-2\delta^2)-4\lambda_0\delta
< o\left(1+\frac b{\sqrt2}\right)
+\frac59(2L+\delta)\delta.
\]

But the rational energy bounds force the right side to be **strictly less** than the left side in **every** possible edge-strain bin. The final two columns are exactly checked rational numbers:

| Bin | Necessary left exceeds | Necessary right is below | Strict contradiction margin |
|---|---:|---:|---:|
| `a≤1/2` | `3198427/8000000` | `188213/504000` | `13287901/504000000` |
| `1/2<a≤11/20` | `2255667/8000000` | `3037/14400` | `5116003/72000000` |
| `11/20<a<3/5` | `1283307/8000000` | `2227/14400` | `414763/72000000` |

Each contradiction margin is **positive**; the smallest is `414763/72000000≈0.0057606`. Therefore a flattened face with `U≤E_pulse` is impossible whenever `||Z||_F≤1/40`, completing the proof.

## Exact rank-three and graph-stress corollaries

The proof uses *actual* shell positions in `R^3` and all 30 exterior edges. It does not relax to rank-four or discard outer vertices. The previous exact rank-four low-energy flattened witness is outside its physical domain; the previous nine-vertex partial-network witness is outside its **full-12-vertex energy** domain. Both remain important adversarial checks on any attempted stronger theorem.

Using the previous exact PSD icosahedral stress operator

\[
\Omega=\sqrt5 I-A+(5-\sqrt5)P_0,
\qquad\Omega\succeq(1+\sqrt5)(I-P_0-P_V),
\]

any physically admissible **flattened** shell with `U≤E_pulse` must also satisfy the scalar necessary bound

\[
\operatorname{tr}(Y^T\Omega Y)>
\boxed{\frac{1+\sqrt5}{1600}}.
\]

This is a structural requirement, not a proof that no such shell exists.

A mirror-reflected full shell can still have `U=0` but opposite oriented cell signs. It is in another connected component; a continuous path between the reference and its mirror must flatten a cell, and the theorem obstructs such a crossing **inside** the low-energy subset with `||Z||≤1/40`. No claim is made that energy alone excludes all reflected configurations.

## Reproducibility, evidence boundary and next test

- **EXACT / CONDITIONAL:** `affine_barrier.py` checks all 36 reference edge-frame polarization cases and proves the affine-only limit; `whole_shell_nonaffine.py` proves the three rational contradiction bins and the `1/40` residual threshold. Both executed successfully in local Python 3.13/SymPy 1.14.
- **NUMERICAL constructor cross-check:** `independent_check.py` independently reconstructs the graph and projectors, checks graph-stress eigenvalues and random-frame/affine residual examples. This is a self-check, not independent experimental replication.
- **Target exposure:** Original energy budget, selected barrier threshold, previous failures and numerical 3D optimum are exposed. The three rational bins and `1/40` threshold were chosen during this discovery calculation; no held-out physical data were used.
- **FAILED / OPEN:** This proof does *not* bound `||Z(u)||` from above along the full nonlinear `u≤100` heart pulse. It does not prove global 3D cell-collapse energy exceeds `E_pulse`, does not prevent housing-strut collapse, and does not certify the 80%/5%/50% dynamic screens.
- **NEXT discriminant:** Derive a uniform dynamic upper bound `||Z(u)||_F≤1/40` for the complete original pulse, with the chosen damping interval, all housing phases and property tolerances; or prove the graph stress controls `Z` at the full-energy-sublevel level. The forced-response PR #44 owns complementary Green-data recovery and remains untouched. 

Physical time, length, material scales, native UD selection and hardware realization remain uncalibrated or UNSCORED. No mainline export or promotion follows from this mathematical result.
