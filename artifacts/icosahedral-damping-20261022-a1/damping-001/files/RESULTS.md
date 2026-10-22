# Passive damping results — v1.0

**RESULT — Ordinary passive dashpots reduce absolute deformation, but consume collective breathing.** Exact model identities explain the tradeoff. The chosen80% retained mean-volume RMS /50% soft-envelope screen passed at0 of363 sampled coefficient points. This is a finite design result, not a universal impossibility theorem.

## Exact/conditional findings

- Nontrivial homothetic breathing is exactly undamped under independent nonnegative radial/edge dashpots only when both loss coefficients vanish.
- The soft five-dimensional equilibrium eigenspace has frequency square (5+sqrt5)/20 and no first-order radial strain. Radial dashpots do not directly suppress it; ordinary edge dashpots do.
- Its underdamped modal exponential envelope at u100 is exp(-50 c_e R²), R²=(5+sqrt5)/8. Halving this envelope requires c_e>=0.0153264935 within the underdamped regime.
- For weak edge loss, the low collective amplitude-decay coefficient is (5/8)(1+5/sqrt37), larger than the soft coefficient (5+sqrt5)/16. The high collective mode decays more slowly. These are linear-equilibrium, small-loss statements.
- The energy certificate |A0|<sqrt(19/680)≈0.167156 prevents radial and edge length collapse for all time, for every positive mass and every g_i,k_ij in the specified ±5% ranges and any nonnegative losses. It does not certify oriented cell volumes or coherent breathing.

## Symmetric design scan, u0..100

Mean-volume RMS is computed from (1+b)^3-1 at A0=1/10 and normalized to zero loss. The soft column is a linear modal pole envelope at u100, a different observable with a different time convention.

| c_s | c_e | Mean-volume RMS retained | Soft modal envelope remaining |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 100% | 100% |
| 0 | 0.005 | 87.74% | 79.76% |
| 0 | 0.010 | 80.16% | 63.62% |
| 0 | 0.016 | 74.24% | 48.50% |
| 0 | 0.020 | 71.34% | 40.47% |
| 0 | 0.080 | 50.87% | 2.68% |

Among the sampled points halving the soft envelope, the largest breathing retention is74.24%, at(c_s,c_e)=(0,0.016). Among points retaining at least80%, the smallest soft envelope is63.62%, at(0,0.010). Added radial loss leaves the soft pole unchanged and worsened retention throughout this scan. No monotonicity or optimality theorem over all coefficients is claimed.

## Full free3D finite-amplitude probes

Three ±5% property realizations and three amplitudes {0.025,0.1,0.2} give nine preparations per loss setting. Each ratio compares a damped preparation with its own matched undamped preparation over u0..100. The reused exposed sample7 reproduces the previous A0=.1 undamped mismatch0.1861787707. No statistical confidence or continuous tolerance-box claim follows from these points.

| (c_s,c_e) | Minimum mean-volume RMS retained | Absolute shell-shape RMS remaining, range | Maximum hub-offset RMS remaining | Maximum normalized hub-relative volume mismatch |
| --- | ---: | ---: | ---: | ---: |
| (0,0) | 100% | 100% | 100% | 18.95% |
| (0,0.005) | 87.89% | 84.28–88.13% | 96.45% | 20.34% |
| (0,0.02) | 71.59% | 61.09–68.09% | 86.76% | 21.88% |
| (0.02,0.02) | 66.99% | 45.01–50.40% | 65.76% | 17.53% |

The normalized mismatch is sqrt(integral ||P20 y||² / integral ||y||²), y_k=V_k/V_k0-1. A larger ratio need not mean larger absolute deformation: edge damping can remove common signal faster than hub-relative volume differences. Moving-hub volume partition, shell-centroid volume partition and rigid/scale-fit shell shape are distinct. The full tables preserve each.

All sampled cell volumes remained positive: minimum0.887008 of reference volume. Supporting-halfspace checks, sampled every tenth output, had only floating-point residuals. These finite checks do not extend the all-time length certificate into a cell-orientation or convexity theorem. A0=.2 lies outside that certificate.

## Verification and limits

- Exact Q(sqrt5) ranks35/35 certify the soft eigenspace and its radial/alpha constraints; the exact mass-normalized stiffness crosscheck agrees within3e-14.
- A separate strain-Jacobian force assembly agrees within4.34e-19; its power balance within1.09e-19. Full3D force reduction agrees with the collective equations within1.56e-15.
- Twelve full3D symmetric integrations agree with the analytic matrix-exponential subsystem within1.63e-9.
- Maximum relative E+D balance residual8.67e-9; linear/angular momentum drifts3.17e-15 /5.91e-13 in internal units.
- Refining the largest observed damped mismatch from2001 to4001 samples and tightening tolerances changed it by3.62e-7; refined energy-balance residual9.57e-11.
- The soft-envelope proxy does not bound a nonautonomous finite-amplitude propagator. No damped analogue of the previous all-phase stiffness certificate is inferred from it.
- Constructor calculations and alternative implementations are checks, not independent physical replication. All thresholds and design choices are exposed. There is no native UD, physical-time, material or spacetime identification.

![Damping tradeoff and finite mismatch probes](../../artifacts/icosahedral-damping-20261022-a1/damping-001/files/damping-summary.png)

## Next discriminant

Construct a passive multiport loss acting on differences of measured edge strains, optionally supplemented by radial-strain differences, with zero common-strain loss. Include its auxiliary coordinates, forces and reactions; test whether it damps the soft tangential family. Merely projecting the damping matrix or reusing the earlier scalar difference law would not establish a spatial realization. A differential channel may protect breathing yet fail to see first-order tangential motion, so both requirements need an explicit mechanism.
