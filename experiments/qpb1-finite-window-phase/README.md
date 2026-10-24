# Fixed-window open-path phase under independent gain errors

**RESULT — EXACT / CONDITIONAL.** The previously integrated simplex-local three-gain family supports a nonzero-visibility endpoint-corrected phase on an explicit entire uncertainty box, **without imposing g1=g2**. This contrasts with the earlier exact-return holonomy sensitivity, which changes the observation time and hence compares different endpoints.

## Source and question

Pinned integrated base: `41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb`. Inputs: [local-generator classification](../qpb1-local-generators/README.md), [continuous phase construction](../qpb1-continuous-phase/README.md). Their original evidence scopes are retained. Goal: quantify fixed-time endpoint-corrected phase/visibility under independent gain errors. No new physical source data. The reference g0=(1,1,3/2), support weights r=(1/4,1/4,1/2), and intended nominal -1 were already exposed before this run. The epsilon 1/100 and 99%/0.01-radian screens are declared engineering choices, not measured tolerances.

## Model and gauge-corrected readout

Use the original signed oriented filled-tetrahedron carrier C=R^15, Euclidean H=I, active J=A/2 with J^2=-I on rank14, and three orthogonal active sectors Pk of ranks (6,6,2). The local skew-adjoint generator is G=sum_k gk Kk (Kk=Dk-Dk^T); evolution x'=Gx conserves every sector norm. For normalized nonzero active x, let rk=||Pk x||^2 with rk>=0 and sum rk=1. Declare J as complex multiplication by +i and native s dimensionless. The proposed endpoint overlap and open-path phase are

```text
Z(T) = sum_k rk * exp(i*2*gk*T)
V(T) = |Z(T)|
Hol_open(T) = (Z(T)/|Z(T)|) * exp(-i*2*T*sum_k rk*gk), when V>0.
```

The corrected formula includes the phase of the non-orthogonal endpoint overlap and subtracts integral alpha, where alpha=<Jx,dx>/||x||^2. It is invariant under time-dependent common J-fiber gauge rotations (the endpoint overlap phase and integral alpha change equally). It is a declared Pancharatnam model readout, not an established UD detector or measured gauge coupling.

## Exact all-box certificate

At T=2pi, choose g0=(1,1,3/2) and any fixed sector-weight distribution r. Each baseline sector returns with endpoint phase +1; the reference weights give integral alpha=5pi and Hol0=-1. Let independent |delta_gk|<=1/100, xk=4pi delta_gk, mu=sum rk xk, yk=xk-mu. The corrected phase change relative to this state's own baseline is

```text
delta_phi = Arg(sum_k rk exp(i*yk)), sum_k rk*yk = 0.
```

Since |yk|<=8pi/100 < B=44/175, by pi<22/7, Re sum rk e^(iyk) >= 1-B^2/2>0 and |Im sum rk e^(iyk)| <= B^3/6, using |sin y-y|<=|y|^3/6. Therefore the phase has a unique continuous principal branch and

```text
|delta_phi| <= B^3/[6*(1-B^2/2)]
            = 42592/15569925 < 1/100 radians.
```

The xk have range <=8pi/100; rotating by the midpoint gives all angles within +/-4pi/100. Thus V>=cos(4pi/100)>=1-(22/175)^2/2=30383/30625>99/100. These bounds hold for every independent gain triple in the entire box and even any nonnegative normalized r. Only the nominal -1 value depends on choosing the exposed r=(1/4,1/4,1/2). They are exact rational enclosures in the conditional model, not an interval numerical scan.

For small errors, subtracting mu kills the linear term in the imaginary part; the phase drift is -sum rk*yk^3/6+O(epsilon^5), whereas the uncorrected dynamical phase shifts at first order. In the single second-gain perturbation, delta_phi=Arg(3/4+exp(i theta)/4)-theta/4 with theta=4pi delta_g2, giving -theta^3/64+O(theta^5)=-pi^3 delta_g2^3+O(delta_g2^5). This is a fixed-window geometric robustness mechanism within the assumed readout, not attraction or robustness of moving exact recurrence.

## Constructor checks and failure modes

Run from repository root with standard-library Python:

```bash
python3 experiments/qpb1-finite-window-phase/audit.py --out /tmp/ud-finwindow-summary.json
```

The executed staged command used `artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-001/files/summary.json` as output. Its 125 deterministic three-gain grid fixtures pass the analytic bounds. The worst grid visibility is about 0.9921147013, worst absolute phase drift about 0.0002490323 radians. For odd N=(101,1001,10001) with delta_g2=1/N, the *moving* exact-return phase is +1 at T=2N*pi (old reference -1 at 2pi), yet the fixed-window corrected phase stays close to -1; this is not a same-time discontinuity.

Baseline comparison: exact-return-only readout fails stability under independent gains; dynamic-phase-only phase has linear drift; the declared open-path correction has cubic local phase drift near an exact baseline ray closure. An overlap can in general vanish, so V>0 must be certified (done for this box). With an apparatus, visibility and phase measurement noise could overwhelm these mathematical margins. No empirical calibration, reference clock, physical source-selection rule, independent mathematical reviewer, or mainline export is claimed.

See [session record](../../sessions/qpb1-finwindow-20261023-gpt6-b6f2/record.json), [mathematical receipt](../../sessions/qpb1-finwindow-20261023-gpt6-b6f2/mathematical_receipt.json), [candidate](../../candidates/qpb1-finite-window-phase/candidate.json), and [immutable run](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-001/manifest.json). Complete-repository validation and unit tests: **NOT_RUN** (GitHub connector available, authenticated clone/network unavailable); standalone script: **PASS**.

**Next discriminant:** a specified interference/noise model with preparation and time-window uncertainty and a non-constructor mathematical audit, then held-out physical comparison if calibrations become available. Physical status **UNSCORED**, promotion **0**.


## Follow-up operational receiver (phase-002)

[Separate analytic receiver and joint uncertainty contract](OPERATIONAL_RECEIVER.md) gives a conditional four-fringe readout, a distinct dynamical-phase calibration dependency, and a combined error certificate. Previous phase-001 results and review status remain unchanged.


## Phase-003 short-time calibration (follow-up)

[Richardson-based dynamical correction and worst-case metrology budget](CALIBRATION_REVIEW.md) specifies a conditional way to test the previous 0.001-radian calibration assumption without selecting native gains. This phase-003 result assumes substantially more precise short-time fringe probes and shared reference metrology; it is neither a physical experiment nor outside review.


## Phase-004 shot noise and reference-frame feasibility

[Statistical probe-count and measurement-frame audit](SHOT_NOISE_AND_FRAME.md) challenges the unmeasured detector and same-frame assumptions of phase-003. Prior exact conditional algebra is preserved; no physical phase success is inferred.


## Phase-005 independently monitored reference/null experiment

[Three-channel protocol, synthetic injection tests and conventional-tone exact null comparison](REFERENCE_NULL_PROTOCOL.md) show what an independently monitored reference can cancel, and where unmatched signal-path drift remains indistinguishable. The newly captured phase-005 result is not a physical experiment or uniquely UD response.


## Phase-006 multiport signature and classical matched null

[Exact tetrahedral four-face signs, all-time transfer zeros, one-bond defect and classical 15-port equivalence](MULTIPORT_DISCRIMINANT.md). The new `phase-006` exact constructor is an interpretable controlled-port candidate, but the unrestricted classical incidence-matched null eliminates unique physical attribution.


## Phase-007 source-closed constitutive audit

[Native analytic closure, minimal local quartic nonlinear alternative, J-fiber obstruction and matched conventional Hamiltonian null](CONSTITUTIVE_SOURCE_AUDIT.md). A preparation-scaling signature exists only after a new unselected quartic coefficient is postulated; the old phase theorems do not transfer and unique physical attribution fails.
