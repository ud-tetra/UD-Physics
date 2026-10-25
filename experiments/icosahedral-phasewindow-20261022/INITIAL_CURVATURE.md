# UD Discovery — initial all-phase nonlinear acceleration and energy-only Hessian obstruction

**RESULT — EXACT / CONDITIONAL (two theorems); NUMERICAL / DEVELOPMENT (238 direction constructor checks).**

Task `icosahedral-phasewindow-20261022`, session `phasewindow-20261022-gpt6-7c41`, held claim and separate isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Import mechanical sources read-only from main `4aaf0a39d24328e27bc425e333e3612baea888a5`, verified unchanged model blobs. Separate held integration/Green PR #44 is not modified. This is checkpoint **initial-curvature-017** and does not supersede the previous nonlinear nullspace observations 016.

## Question and typed model

Can the full 180-dimensional initial housing-phase ball admit an *exact* finite-amplitude bound on the nonlinear moving-axis viscous contribution to the **initial non-affine shell acceleration**? Can the same bound be extended through the original time horizon `u=100` from passivity/energy alone?

Use the unchanged passive 280-configuration/560-phase 3D surrogate. Original primary points are the regular unit-edge icosahedron with centre `C`, 12 shell vertices, 30 moving midpoint housings, four current-axis viscous struts per housing, 150 auxiliary coordinates, scalar heart `alpha0=1/10`; initial primary/device velocities vanish. Let `D_e` and `V_e` be the freely specified *initial* displacement and velocity of housing `e` only. The housing energy constraint is

\[
\frac12\sum_e m_e\big(|V_e|^2+100|D_e|^2\big)\le E_h\le\frac{51}{20\,000\,000}.
\]

Here `m_e=(2/5) beta w_e/R²`, `R²=(5+sqrt(5))/8`, `beta in [1/200,1/20]`, `w_e in [9/10,11/10]` (mean one), and `nu in [1/25,1/20]`. Mount stiffness `k_h,e=100 m_e`; current-axis coefficient `eta=(2/5)nu beta/R²=nu m_e/w_e`. Primary shell mass is `m_i/R²` with `m_i>=19/20`. The time `u`, length unit and physical energy are not calibrated to nature.

Define `P=I_12 - 11^T/12 - VV^T/(4R²)` with the 12x3 reference-coordinate matrix `V`, and `Z=P Y in R^(12x3)`. `P` is an orthogonal projector with norm one; the non-affine sector has rank 24. Let `Z''(0;D,V)` be the shell non-affine acceleration computed from the full nonlinear equation. The quantity bounded here is the **finite initial nonlinear remainder**

\[
 \mathcal R_0(D,V):=Z''(0;D,V)-Z''(0;0,0)-D Z''(0;0,0)[D,V].
\]

The derivative in the final term is with respect to initial housing phase, not physical time. All other initial coordinates are fixed. No claim about `Z(u)` is implicit.

## Theorem A: uniform initial-time all-180-phase remainder

For any initial phase satisfying the displayed energy constraint, every allowed parameter realization, and all 120 struts in their initial domain,

\[
\boxed{\|\mathcal R_0(D,V)\|_F <\frac{267699}{3022662500000}
 <\frac9{100\,000\,000}=9\times10^{-8}.}
\]

For normalized energy radius `0<=r<=1`, `\|\mathcal R_0(rD,rV)\|<r²(267699/3022662500000)`. This bound includes *every* mixture of the 90 housing displacement and 90 housing velocity coordinates, including the 24 mixed-cancellation modes from 016. It uses no sampled trajectory or choice of phase direction.

**Exact proof.** Since `11/5<sqrt(5)<56/25`, `9/10<R²<181/200`; consequently every `m_e>9/5000` and `100m_e>9/50`. The energy bound gives `|D_e|<1/180` for each housing. At reference, each housing-to-anchor strut has length `1/2` for two edge endpoints and `sqrt(3)/2>4/5` for two opposite face vertices. Perturbed lengths therefore exceed `89/180` (two) and `143/180` (two).

For a reference strut displacement `d0`, displaced separation `d=d0+D_e`, and unit axes `n0=d0/|d0|`, `n=d/|d|`, write `P_n=nn^T`. The **exact** initial viscous-force remainder after subtraction of its first derivative is

\[
\mathcal F_{ea}=\eta(P_n-P_{n0})V_e,
\qquad
\|P_n-P_{n0}\|_2=\sin\angle(n,n_0)
\le\frac{|D_e|}{|d_0|-|D_e|}.
\]

The mechanical mount force is linear in `D_e`; all other initial forces are independent of housing phase or linear in housing velocity. Therefore only this four-anchor viscous remainder contributes to `\mathcal R_0`. For each housing, Young's inequality implies

\[
20m_e|D_e||V_e|\le m_e(|V_e|²+100|D_e|²).
\]

Sum over all houses and their two endpoint/two opposite paths, use `eta/m_e=nu/w_e`, the phase-energy bound, `w_e>=9/10`, `nu<=1/20`, the primary shell inverse mass `<181/190`, and projector contraction. The resulting upper bound is the exact rational number

\[
 \frac{181}{190}\,
 \frac{(1/20)(51/20\,000\,000)}{10(9/10)}
 \left(\frac{360}{89}+\frac{360}{143}\right)
 =\frac{267699}{3022662500000}.
\]

Strictness comes from the strict circumradius/mass and path-length bounds. This is a conservative uniform bound; it is not asserted optimal.

## Theorem B: no energy-only global flow-Hessian majorant

**EXACT / FAILED generalization.** Choose admissible `beta=1/200`, one housing weight `w=9/10`, and `nu=1/20`. Keep all primary points, other housings and auxiliary elements at reference with zero velocities and set heart `alpha=0`. For one original edge `(i,j)`, choose its unit axis `e`, an orthogonal unit vector `p`, and move its housing to `H_tau=X_i+tau p`, with relative housing velocity `V_e=e`, `0<tau<=1/10`. All mechanical struts are strictly positive for `tau>0`. Since `R²>9/10`, the selected housing mass `m_e<1/500` and stiffness `k_e<1/5`, so the **entire** mechanical energy obeys

\[
 E(\tau)<\tfrac12(\tfrac15)(\tfrac14+\tfrac1{100})
   +\tfrac12(\tfrac1{500})=\frac{27}{1000}
 <\frac{1\,360\,051}{20\,000\,000}.
\]

The one housing-to-vertex-i strut has `d(s)=s e+tau p` and the corresponding viscous force is

\[
 f(s)=\eta\,\frac{d(s)[d(s)\cdot e]}{|d(s)|²},\qquad
 \left.\frac{d²}{ds²}f(s)\right|_{s=0}=\frac{2\eta}{\tau²}e.
\]

The other three struts from that housing have lengths `>=1-tau>=9/10`; their force Hessians remain bounded as `tau->0`. The non-affine projector of one shell-vertex force is nonzero (`P_ii=2/3`), so the **projected primary acceleration Hessian** diverges in norm as `tau^-2` even on the energy sublevel below the original pulse budget. The force Hessian of the full ODE also diverges.

These deliberately constructed states are **not** shown dynamically reachable from the designated `alpha0=1/10` pulse. This result disproves only a proposed *energy-only*, all-sublevel Hessian bound; it does not disprove trajectory-restricted control or the physical surrogate itself.

## Numerical verification and scope

- `exact_initial_bound.py`: Python standard-library `Fraction` assertions of all parameter, length and energy inequalities and final rational bound — PASS.
- `singular_energy_obstruction.py`: the energy-only singular witness inequality is verified exactly; source-matched floating source checks for `tau={1/10,1/20,1/40,1/80,1/160}` confirm `tau² ||projected Hessian||` converges to the nonzero predicted coefficient — PASS.
- `independent_assembly.py`: 238 fixed, energy-normalized initial phase vectors: 160 seeded random, 24 mixed-cancellation basis, 24 random mixed-cancellation vectors, 30 single-housing cross directions. The worst observed remainder is about `3.2879e-8` and 13 full-assembly four-corner checks agree with the analytical projector remainder to maximum error `9.06e-17`. These are same-runtime constructor checks, not independent experimental confirmation.
- Frozen development coefficient ID `edge-p1-b0.005-cf0.0` and SHA256 `8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd`; `gain_t4p0.npz` imported as previous development data only to select mixed-cancellation diagnostics. No new fitting or broad trajectory search.

**Limitations.** Theorem A bounds `Z''` at **u=0**, not `Z(u)` or its Hessian at `u=4` or `u=100`. At later times, the baseline has moving velocities and the displaced housing phases feed back into primary positions and velocities. A valid Duhamel remainder would require an invariant positive-length domain, a full-state propagator/Green bound, and a uniform nonlinear forcing estimate along *every* admissible trajectory. Theorem B proves why one cannot drop the domain requirement and use total energy only. No continuous property-box nonlinear `u100` result, breathing/ringdown readout, physical time scale or mainline promotion.

**Next discriminant — priority 99/100:** obtain a trajectory-restricted strict strut-length tube and compute a continuous-time block/adjoint propagator bound for the projected nonlinear forcing. Retain the mixed-cancellation phases as adversarial tests, and let separate PR #44 retain ownership of its forced-Green recovery files.