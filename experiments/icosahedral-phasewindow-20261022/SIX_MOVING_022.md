# Symmetric moving-pulse six-channel adjoint through u=100 — checkpoint 022

**RESULT — EXACT / CONDITIONAL group reduction; NUMERICAL / DEVELOPMENT time propagation; full nonlinear u100 OPEN.**

## Question

Can the exact A5 six-seed representation of checkpoint 021 be propagated through the original uniform-property moving heart pulse, and reproduce the worst first-order response over every allowed initial housing phase up to u=100?

## Mathematical objects and assumptions

- Space: 560 mechanical phase coordinates (280 configuration plus 280 velocities) and a separate heat ledger, with 150 auxiliary transmissions, 30 housings, 120 moving-axis viscous paths. Physical Euclidean spatial metric (+++); internal u is uncalibrated Newtonian model time.
- Exact symmetric moving reference from checkpoint 019: positions X_i=b(u)v_i, housings H_e=c(u)(v_i+v_j)/2, alpha(u) evolving; auxiliary coordinates remain zero. Initial alpha=.1, b=c=1, all other initial velocities zero. Model has beta=.005, nu=.05, cf=0, uniform unit reciprocal gains and uniform masses/couplings.
- 180 housing phase directions are energy normalized by a 560-by-180 injection B. Housing energy E_h <= 51/20000000, so initial perturbation is sqrt(2 E_h) B a with ||a||_2<=1.
- Output Z=(I-P0-PV) delta Y in rank24, represented by six compatible seeds from checkpoint 021. The exact A5 identity implies that the squared gain equals the largest eigenvalue of two 1x1 and two 2x2 sector Gram blocks built from six 180-dimensional adjoint rows.
- At each t*: propagate Lambda'=-J(y_ref(u))^T Lambda **backwards** to u=0, with terminal values the six output seeds; evaluate G=L(0)^T B, the six-by-180 response. Reconstruct all 24 output eigenvalues from 3,3',4,5 sectors; multiply the operator gain by sqrt(2E_h). The 560x560 Jacobian uses the unchanged full derivative formula, not a six-degree physical truncation.

## Executed results

Eleven selected times: 1, 2, 4, 6, 10, 20, 40, 70, 80, 90, 100. Peak of tested points at u=4: 6.60027513675e-05 reference-edge-length units, about 0.2640% of the previously exposed 1/40 orientation threshold. At u100 two completed numerical runs give 4.26093655299e-06 (rtol2e-6) and 4.24427605794e-06 (rtol3e-6); relative spread about 0.3918%. These are NOT error enclosures.

A separate full-24-output adjoint at u4 gives the same top gain to relative difference 4.838e-08. A 2-direction forward tangent-versus-six-adjoint transpose comparison at u4 yields relative difference 3.080e-07. The u100 forward comparison exceeded runtime; no completed u100 independent transpose check is claimed.

The symmetric reference has Z=0 by exact A5 symmetry. The previous exact primary/housing symmetric clearance remains applicable only to the baseline, **not all housing phases**.

## Failed attempts and limitations

- Combined multi-target integration exceeded the compute window; separate targets completed. More stringent u100 adaptive tolerances also exceeded the window. Numerical solver sensitivity remains unresolved.
- Time points are post-selected/developmental, not a validated supremum over [0,100]. No continuous-time quadrature or strict integration-error enclosure.
- The six-seed map is a *linearized* response: nonlinear coupling among all 180 phases, the mixed nullspace, and all-time housing-strut safety are not bounded by it. A5 symmetry of the reference is not a physical identification and does not extend to source-frozen scattered coefficients.
- Coercivity under equilibrium linearization is a separate theorem (checkpoint012); it must not be applied without proof to this moving reference.

## Next discriminant

Priority 99/100: produce a stable, independently cross-checked u100 projected propagator and certified continuous-time operator envelope (ideally with interval or a posteriori ODE defect control). In parallel, obtain a joint nonlinear bootstrap controlling moving housing-to-anchor displacements and shell non-affine deformation for all initial phases. PR44 owns its forced Green recovery; do not write to that owner.