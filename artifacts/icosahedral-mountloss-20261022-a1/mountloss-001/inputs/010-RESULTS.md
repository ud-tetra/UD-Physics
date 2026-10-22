# Passive housing loss — results v1.0

**RESULT — CONDITIONAL local decay and NUMERICAL finite-budget success; uniform ringdown target remains OPEN.** Model/source definitions and proof are in [README](README.md). [Protocol](PROTOCOL.md) records the pre-scan choices and post-selection scope amendment. Immutable run: [mountloss-001](../../artifacts/icosahedral-mountloss-20261022-a1/mountloss-001/manifest.json).

## Exact findings

- 30 housings, four central viscous struts each: 120 additional loss paths, no extra state/storage. All reactions retained; total primary-plus-housing momenta conserved and E' is minus the sum of nonnegative loss powers.
- Each reference housing direction Gram has determinant8/9 and eigenvalues2,(3±sqrt5)/3. It detects all90 housing velocities with primary velocities fixed, including all54 old reaction-cancelling modes.
- Under the stated positive parameters/gains and nu>0, all274 nonrigid equilibrium configuration modes decay in the linearization, even c_f=0. The free assembly retains six rigid directions. This is not global nonlinear attraction or a uniform rate bound.
- Added reference b,c loss is eta[[35,10],[10,5]]; common homothety dissipates60 eta b_dot². Breathing is not exactly protected by these ordinary struts.

## Declared development selection

Nominal beta=.05, Omega=10, c_f=.001; original symmetric undamped/nohousing breathing baseline. Worst housing energy means the maximum over all108 displacement/velocity phases of the old54-dimensional housing sector, propagated in the full equilibrium linear system to u=100.

| nu | Worst housing energy remaining | Nonlinear breathing RMS retained | Both selection gates |
| ---: | ---: | ---: | :--- |
| 0 | 100.000% | 92.970% | Fail |
| .005 | 81.349% | 92.389% | Fail |
| .01 | 66.216% | 91.822% | Fail |
| **.02** | **43.966%** | **90.726%** | **Selected** |
| .05 | 13.190% | 87.719% | Pass |
| .1 | 2.003% | 83.503% | Pass |
| .2 | .082979% | 77.232% | Fail breathing |
| .5 | .0000734% | 66.792% | Fail breathing |
| 1 | 1.04e-9% | 57.806% | Fail breathing |

The frozen rule selected the smallest scanned nu meeting <=50% housing energy and >=80% breathing. There were nine strengths, no added scan points or subsequent retuning. At nu=.02, nominal eta=.0004422291236. These choices remain target-informed engineering FIT, not independent predictions.

## Frozen joint pulse budget

The 24 cases and11 baselines are byte-identical to the previous hardware study. With nu=.02, **20/20 in-budget cases pass** the inherited80% breathing /5% hub-volume mismatch /50% residual-shape screen at alpha0=.1,u0..100.

| Readout | Result |
| --- | ---: |
| Minimum breathing RMS / original undamped | .901533505 (fine .901533291) |
| Maximum hub-relative volume mismatch | .007461607 (fine .007461624) |
| Maximum shell-centroid volume mismatch | .006680925 |
| Residual absolute shell-shape RMS / original | .0438075–.0991508 |
| Added retention cost vs matching previous loaded case | 1.209–2.227 percentage points |
| Maximum housing lag / ell0 | .00223397 |

The prior minimum retention was92.311%; the new minimum is90.153%. Both compare with original undamped/nohousing baselines; nominal scan values use the symmetric baseline and are different observations.

| Out-of-budget challenge | Breathing retained | Screen |
| --- | ---: | --- |
| 3% ratio errors | 86.114% | Pass this case |
| 20% housing mass | 77.138% | **Fail breathing** |
| c_f=.02 | 68.997% | **Fail breathing** |
| Mount Omega=4 | 80.320% | Pass this case |

The20% mass challenge passed the previous conservative-mount pulse screen; the added loss makes it fail. Do not discard this design cost. None of the passing individual challenges expands a certified tolerance range.

## Nonzero housing preparations and checks

At nominal properties, the saved original four-cycle housing displacement (amplitude1e-4,alpha0=0) retains .9999999993 mechanical energy without added loss and **.1126988143** with added loss at u=100. The nonlinear run initialized with the worst108-phase linear direction retains **.4396602268**, differing from .4396602278 by1.005e-9. These are small-amplitude preparations, not a global-amplitude statement.

Adding that housing phase at scale1e-4 to the worst-mismatch joint pulse also passes:91.128% breathing, .746160% volume mismatch and6.123% residual shape. It is a separate development challenge, not another original in-budget point.

Three additional **post-selection** zero-input-friction matrix checks support the local-decay scope. Nominal beta=.05 retains43.966% old-sector energy; the scattered beta=.05 case retains44.370%. Nominal beta=.005 retains **50.735%**, narrowly **failing the half-energy-at100 target** despite positive local decay. Thus the nominal housing ringdown target is not certified across the proposed broader parameter budget. The slowest nonrigid amplitude decay rates for these three cases are9.737e-5,1.992e-4 and1.057e-5 per unit u; these slow poles are not the worst-sector energy fraction.

Force/torque/power checks pass; odd finite-difference ODE vs analytic full linear matrices differs by5.98e-9. Full nonlinear vs three-coordinate reduced motion differs by less than1e-9. The maximum pulse E+heat relative residual is4.153e-9; maximum full P/L drifts are1.20e-15/6.95e-15. Sampled strut length stays>=.49219 ell0 and oriented cell-volume ratio>=.95320. These sampled length/orientation observations are not all-time bounds.

Two tighter, sample-doubled reruns cover the worst mismatch and retention cases: mismatch changes<=1.74e-8 and retention<=2.14e-7. NumPy2.3.5/SciPy1.17.0, float64 DOP853; declared tolerances are in the protocol. The all-phase worst calculation uses matrix exponentials/eigenvalues and remains NUMERICAL. Constructor checks and a second calculation method are not empirical replication or separate-context review.

![Tradeoff, independent housing preparations and joint pulse budget](../../artifacts/icosahedral-mountloss-20261022-a1/mountloss-001/files/mountloss-summary.png)

## Status and next discriminant

The old54-mode failure is repaired by a defined passive extension; the original failure remains valid for its old model. A narrower, successful finite pulse budget now includes explicit housing loss. The nominal housing energy gate and local all-mode decay do not imply a uniform finite-time tolerance-box guarantee. The120 extra ideal struts add substantial implementation complexity; routing, fixture/strut inertia and compliance are not modeled. The [mount test plan](MOUNT_TEST.md) is UNSCORED/NOT_EXECUTED; no physical/native UD identification or mainline promotion follows.

Next: derive and test a damping-strength range that meets both the housing ringdown and breathing gates across the joint parameter budget, including nonzero housing phases and c_f=0. Preserve the beta=.005 counterexample and the failed mass/friction challenges; do not silently promote the nominal choice into a box bound.
