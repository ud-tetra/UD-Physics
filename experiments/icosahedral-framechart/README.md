# Icosahedral proper-frame readout chart: exact nonlinear remainder bound

**RESULT — EXACT / CONDITIONAL:** On the twelve-shell-plus-hub primary positions of the source 3D icosahedral mechanical surrogate, an explicit proper SO(3) rotation and shell-centroid subtraction produce a smooth readout chart. For **any actual 13-primary displacement** with Frobenius norm at most 9/250 = 0.036, its deviation from the chart's first-order rigid-tangent-removing linearization is at most **5589/6160000 ≈ 0.0009073052** internal length units. This is a uniform mathematical result for the specified chart, NOT a certificate that the source's 560-state nonlinear trajectories remain inside that radius or satisfy the full volume/breathing threshold through u=100.

## Question, read-only sources and type firewall

We resume the integrated 3D passive-mechanics source at \`ud-tetra/UD-Physics@447ee4df3b9bc3e71bdfee3e29f7ee9379410df7\`, specifically [icosahedral pulsetube](../icosahedral-pulsetube/README.md), [pulse tube criterion](../icosahedral-pulsetube/TUBE_THEOREM.md), [results](../icosahedral-pulsetube/RESULTS.md), [joint damping/breathing window](../icosahedral-jointwindow/README.md) and [housing nonlinear energy domain](../icosahedral-nonlineartube/README.md). They remain unchanged. No 4D apex, quantum, charge/flux or graphite model is imported into this new mechanic calculation.

Source state: 280 configuration coordinates = scalar alpha + thirteen primary spatial points + 150 device coordinates + thirty housing spatial points, 560 mechanical phase variables and one heat accumulator. Current-axis strut damping and reciprocal device forces remain in the source Hamiltonian/dissipation law. The newly defined chart **only** postprocesses the 13 primary positions, in the same uncalibrated native length unit ell0. All 560 states, rigid momenta, housing energies, device variables, torque and reaction forces remain present in the mechanical ODE. The chart is not a moving-frame gauge elimination in the dynamics.

Source numerical exposure: limiting parameter set \`seed10422-0-boundary2\` at nu=.05, with housing phase energy \(E_h=E_p/40000\), reports a sampled all-phase **linear tangent** primary-position radius 0.03500972 and a Procrustes-aligned tangent shape radius 0.0002420865. The full nonlinear moving-pulse energy-ball u100 bound remains OPEN. The selected radius 0.036 was chosen *after seeing* the tangent radius; it is an explicit **FIT/development test radius**, not a source-enclosed nonlinear flow radius.

## Geometry, frame map, and exact first derivative

Let the regular 12-shell coordinate matrix \(X\in\mathbb R^{12\times3}\) have centered rows with shell edge length one, constructed from coordinates
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1)
\]
all divided by two, where \(\varphi=(1+\sqrt5)/2\). The reference hub is at the origin. Exact icosahedral geometry gives
\[
\sum_{i=1}^{12}X_i=0,\quad X^\top X=cI_3,\quad
 c=4R^2=(5+\sqrt5)/2.
\]
For a general primary position error \(E=(E_s,e_h)\in\mathbb R^{13\times3}\), write \(\mu=\frac1{12}\sum_i(E_s)_i\), \(\widetilde E_s=E_s-\mathbf1\mu^\top\), and \(\widetilde e_h=e_h-\mu\). Define
\[
\Omega(E)=\frac{\operatorname{skew}(X^\top\widetilde E_s)}{c}
\in\mathfrak{so}(3),\qquad
R(E)=\exp[-\Omega(E)]\in SO(3).
\]
The *aligned displacement* readout is
\[
\mathcal F(E)=
\binom{(X+\widetilde E_s)R(E)-X}{\widetilde e_h\,R(E)}.
\]
This is a globally defined analytic map of E with a proper (det +1) rotation, for all finite E; we require only the stated small radius for the uniform remainder. It subtracts shell-centroid translation from both shell and hub and rotates both, so it preserves every orientation-insensitive and proper-rotation-invariant cell-volume readout.

Its exact derivative at zero is
\[
D\mathcal F(0)E=
\binom{\widetilde E_s-X\Omega(E)}{\widetilde e_h}.
\]
For a pure global infinitesimal translation, this is zero. For a pure infinitesimal rigid rotation \((E_s,e_h)=(XK,0)\), K skew, we get \(\Omega=K\), so the derivative is also zero. The source ODE is not quotiented by these six directions; only a redundant *readout tangent* vanishes. Our shell-centroid gauge is NOT the same chart as the previous proper Procrustes alignment on all primary points. Its tangent and remainder radii cannot silently reuse that earlier Procrustes number.

## Exact uniform nonlinear chart error

Let \(r=\|E\|_F\le9/250\) and write \(\widetilde E=(\widetilde E_s,\widetilde e_h)\). Shell-centroid subtraction from all 13 positions has linear-operator norm \(\sqrt{13/12}\), hence
\[
\|\widetilde E\|_F\le\sqrt{13/12}\,r<\frac{21}{20}r.
\]
For \(c=(5+\sqrt5)/2\), exact rational bounds \(7/2<c<15/4\) give \(\|X\|_F=\sqrt{3c}<27/8\). Using \(\|X^\top\widetilde E_s\|_F\le\sqrt c\,r\), and the equality \(\|\Omega\|_2=\|\Omega\|_F/\sqrt2\) for 3×3 skew matrices,
\[
\|\Omega(E)\|_2\le \frac{r}{\sqrt{2c}}\le\frac{2r}{5}
\le t:=\frac9{625}<1.
\]

From \(R=\exp(-\Omega)\) and the full exponential series,
\[
\|R-I+\Omega\|_2\le e^t-1-t\le\frac{t^2}{2(1-t)},
\qquad
\|R-I\|_2\le e^t-1\le\frac{t}{1-t}.
\]
The chart difference is **exactly**
\[
\mathcal F(E)-D\mathcal F(0)E
=\binom{X(R-I+\Omega)+\widetilde E_s(R-I)}
{\widetilde e_h(R-I)}.
\]
Thus the triangle/submultiplicative matrix norm inequalities yield the rigorous uniform bound
\[
\begin{aligned}
\|\mathcal F(E)-D\mathcal F(0)E\|_F
&\le \frac{\|X\|_F t^2/2+\|\widetilde E\|_F t}{1-t}\\
&< \frac{(27/8)t^2/2+(21/20)(9/250)t}{1-t}\\
&=\boxed{\frac{5589}{6160000}}<\frac1{1000}.
\end{aligned}
\]
All rational bounds are checked by exact Python Fractions, and the algebra covers the **entire** 13-primary Euclidean displacement ball, not just the tested 120 numerical points. No assumption on the directions of the perturbation, velocities or alignment phase is used beyond the initial radius.

The strict inequalities are conservative. Numerical fixed-seed near-boundary examples had maximum actual chart/nonlinear linearization difference about 0.0001888063; these examples do NOT prove the universal result, which follows from the bound above.

## How this advances—and does not close—the u100 mechanics tube

The source [pulsetube criterion](../icosahedral-pulsetube/TUBE_THEOREM.md) needs an all-phase positive full-560-state norm, validated time-dependent full forced Green bounds \(U(t,s)\), uniform nonlinear Hessian/flow remainder, reference defect/error, continuous positive strut-length domain, and nonlinear mean-volume readout control. It currently has numerical \(U(t,0)B\) tangent data and finite adverse preparations, not those other enclosures. We **do not** replace them with the present chart theorem.

One missing *analytical readout subcomponent* is now available: should a later verified full-state tube prove a continuous actual primary radius \(\|E(t)\|_F\le0.036\), this explicit SO(3) chart has a guaranteed nonlinear readout coordinate correction below 0.001. This is of the same order as the earlier post-exposure design goal of a primary-shape flow remainder below 0.001, but the two error categories are different. The previously reported numerical Procrustes tangent radius 0.0002420865 **cannot** be added to or substituted for the derivative of this chart; the full 180-column tangent must be re-projected using the displayed \(D\mathcal F(0)\). Furthermore the oriented-volume determinant readout has its own nonlinear remainder and no validated bound is newly claimed.

The chart uses only proper SO(3) rotations and translations, never reflections; cell orientations and intrinsic volumes are preserved by the readout transformation. It is a conventional mechanics tool available on any centered isotropic 3D point cloud. It does not identify the icosahedral mechanical surrogate with UD spacetime, derive damping/constitutive coefficients, establish a physical clock, or beat an equivalently constrained classical local network.

## Reproduction, evidence and next discriminant

From repository root, with NumPy:
\`python3 experiments/icosahedral-framechart/audit.py --out /tmp/ico-framechart-result.json\`.

Actual local execution was \`python /mnt/data/ico_frame_20261024/audit.py --out /mnt/data/ico_frame_20261024/result.json\`; same exact source and output bytes are captured in [frame-001](../../artifacts/ico-framechart-20261024-gpt6-a1/frame-001/manifest.json). Source SHA256 \`4c9467ece8d7ee92e236eb71efe3abd18a028dcd6866d359ce116bd7921d0d6d\`, output SHA256 \`b72b139995f3f220b26b1de7e09bcb3d50bc50be7ed4244e2ba77c9ceb9da98e\`. The constructor checks exact rational constant inequalities, regular geometry identities, 120 deterministic numerical E samples including 0.03500972 and 0.036, proper rotation, first-order rigid tangent cancellation, and finite rotation/translation tests.

**Status:** EXACT / CONDITIONAL chart bound; NUMERICAL constructor tests; **OPEN** actual all-phase u100 primary radius, forced Green/Hessian/chart+determinant full remainder and physical engineering source. External mathematical review NOT_RUN; physical experiment NOT_EXECUTED; mainline promotion 0.

**NEXT (priority 99/100):** project the *same source 180-column tangent* with this explicit shell-centroid rotation derivative, and derive or validate a full-560-state **continuous-time primary-radius bound** from forced Green, nonlinear source defect and preserved housing/rigid blocks. Only then add the chart and determinant remainders in one named norm to see whether the exposed nonlinear all-phase breathing margin actually closes. Prefer a held-out mechanical property/dispersion test over additional coefficient fitting if this domain cannot be certified.
