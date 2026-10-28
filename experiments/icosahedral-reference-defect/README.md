# Frozen 3D reference DOP853 residual and raw Gronwall obstruction

**RESULT — EXACT / CONDITIONAL:** The original full 560-mechanical-state, unanchored 43-spatial-point source has an exact rigid translation position/velocity shear. In the ordinary equally weighted position–velocity Euclidean coordinates its Jacobian logarithmic norm mu2(J) is at least 1/2 at every time, by a normalized rigid translation Rayleigh quotient. Thus a full-state raw scalar exponential Gronwall residual certificate over u=100 would require an extremely small uniform residual, even if the actual reference integration were accurate.

**NUMERICAL / SAMPLED:** Isolated [GitHub Actions run 40713694075](https://github.com/ud-tetra/UD-Physics/actions/runs/40713694075) executed the unchanged original limiting and nominal full-state reference ODE, strict DOP853 rtol=5e-12/atol=5e-15, with SciPy dense output. The [executable audit](dense_defect.py) analytically differentiates each DOP853 interpolating polynomial and probes the residual p'(u)-f(p(u)) at three interior Gauss nodes per accepted step. This gives finite-point probes, NOT interval upper bounds or an independently certified numerical error.

## Exact obstruction

Let q be unit global spatial position translation of all 43 point masses, with auxiliary device coordinates and alpha unchanged; let v be the corresponding unit global velocity translation. Internal central springs and dashpots use only relative positions and velocities, so Jq=0 and Jv=q. Therefore the normalized vector (q+v)/sqrt(2) has symmetric Jacobian quadratic form 1/2 and mu2(J)>=1/2. This is exact for the specified source and equally weighted Euclidean norm; a different block/energy norm need not retain the numerical floor 1/2.

For a true trajectory y and differentiable approximate p with the same initial condition, define defect rho=p'-f(p). With independently validated uniform log-norm upper bound L on an error tube and uniform defect bound ||rho||<=R, the standard scalar estimate is ||y(100)-p(100)|| <= R*(exp(100L)-1)/L. Since L>=1/2, this amplification is at least 2*(exp(50)-1)=approximately 1.0369411057e22. To prove the pre-existing nominal sampled primary-position error target 0.0103109410 by this raw full-state method, even at the optimistically smallest L=1/2, a sufficient uniform full-state defect bound smaller than 9.9436129700e-25 would be required. This is a NO-GO for the simple raw scalar certificate at the executed numerical defect scale, not proof the actual global solver error is large.

## Executed defect and exact center-of-mass comparisons

| Diagnostic | Limiting frozen reference | Nominal frozen reference |
| --- | ---: | ---: |
| Accepted DOP853 dense intervals | 3479 | 3481 |
| Function evaluations | 53927 | 57785 |
| Max sampled full mechanical defect L2 | 1.3877613e-9 | 2.7534220e-9 |
| Max sampled primary derivative defect L2 | 8.1322060e-12 | 2.0001292e-11 |
| Width times sampled-max defect sum (NOT certified) | 4.3620109e-8 | 4.6412359e-8 |
| Max dense-polynomial reconstruction discrepancy | 1.11158e-14 | 1.13990e-14 |
| Max sampled analytic center-of-mass position difference | 1.04196e-15 | 2.23113e-15 |

The exact global center-of-mass trajectory satisfies M*Rcm''=0, as previously established on the same source. It can be handled by a linear Green shear rather than an exponential comparison. The numerical CM agreement is a consistency check on source integration, NOT a certified floating-point/interval error on all remaining internal positions.

The residual probes are at only three points per accepted step and use ordinary Float64. Their maximum is NOT the supremum over an integration step or a validated global residual. Likewise the surrogate summed defect is NOT a rigorous integral. The true trajectory and numerical approximant must still be enclosed inside a Jacobian tube before any error estimate can close. No interval arithmetic or whole-time Jacobian/Green stability enclosure was performed.

## Provenance, limitations, next gate

Source [integrated baseline](https://github.com/ud-tetra/UD-Physics/tree/cba74cc20ba323599339f88830bd0cc97fc9a6da/experiments/icosahedral-pulsetube) and original MountLoss mechanics are read-only. Source cases seed10422-0-boundary2 and uniform-b0.05-cf0.0, alpha0=.1, nu=.05, original 280 configuration/560 mechanical phase variables, house masses and all dampers unchanged. [Prior reference interpolation PR #220](https://github.com/ud-tetra/UD-Physics/pull/220) is unmerged read-only. No mainline changes or 4D/quantum cross-contamination.

Immutable [defect-001](../../artifacts/ico-refdefect-20261028-gpt6-a1/defect-001/manifest.json) captures actual executed script 5431 bytes SHA256 f775e3f1b0815e1503a69acb33737c6bdda704cfe3235d1c683f9a72ffe0f0ff and full output 3934 bytes SHA256 e60baeaf53b815cd875c5713304126c0634df821410cc0275071f22b0ae95d8f. The complete time-step probe summary is also in a GitHub Actions 30-day retained artifact. Exact data and source bytes verified.

**FAILED / PARKED:** raw full-state scalar Gronwall with equal position and velocity coordinate weighting as a useful certification route. **OPEN:** actual verified sampled numerical reference error delta_num<0.01031; genuine internal relative-coordinate Green and stepwise interval dense residual; full 180-phase nonlinear relative radius r=.036, forced U(t,s), Hessian, housing strut and cell-volume all-phase u100 80% target. Ordinary unanchored reciprocal 3D mechanics has identical rigid shear and numerical proof limitation. No independent reviewer, actual material system or physical spacetime identification.

**NEXT priority 99/100:** Work in a positive full-state block norm retaining the EXACT center-of-mass and rigid kinetic energy, but bound a force-range-projected internal mechanical Green separately; replace three-node residual probes with verified per-step enclosures and an a posteriori bootstrap. Only after a validated delta_num<0.01031 can reference d=.07 be certified. The all180 nonlinear phase ball remains a distinct later gate.
