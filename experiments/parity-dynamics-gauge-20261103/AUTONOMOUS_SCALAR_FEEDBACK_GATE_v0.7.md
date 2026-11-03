# Autonomous scalar feedback on the QPB1 matched source port — v0.7

**2026-11-03, UD-Physics Discovery. EXACT / CONDITIONAL / NO-GO / OPEN. Physical promotion 0.**

## Source, carrier and conventions

Source-bound starting point: `experiments/qpb1-source-reservoir/README.md` v1.1 §§1–5 (source port; matched two-component real modes; reciprocal joint generator; gate envelope *not selected*). The port has target plane `r=E_topᵀx∈R²` and matched reservoir `y∈R²`. This `E_top` is NOT the edge extractor from prior studies. Unaddressed 13 real packet coordinates are spectators; the presented equations use the co-rotating frame of the joint native `2j` rotation and unit Euclidean modal metric. The native evolution coordinate `u` is dimensionless. Retained modal stock `||r||²` is NOT physical mass.

For any scalar nonnegative coupling `g=g(r,y)`, the matching free rotations cancel in the co-rotating frame, leaving

```
dr/du = g(r,y) y,       dy/du = -g(r,y) r.
```

The source proves this for a prescribed scalar envelope. Substituting state-dependent g is an **additional autonomous constitutive hypothesis**, not a consequence of signed incidence, S4 or source-selected action. We now test whether it helps and identify its invariants.

## Theorem 1 — exact invariants for every scalar feedback (EXACT / CONDITIONAL)

Define `N=||r||²+||y||²≥0` and `D=det(r,y)=r1*y2-r2*y1`. Differentiate:

```
N' = 2g(r·y) - 2g(y·r)=0,
D' = det(g y,y)+det(r,-g r)=0.
```

These identities hold for arbitrary scalar `g(r,y)` wherever the ODE is defined. In the original rotating frame `D` remains invariant because the common modal rotation has determinant +1. They are not physical clock/energy measurements.

Consequently, by planar Cauchy–Schwarz,

```
|D| ≤ ||r|| ||y|| ≤ sqrt(N) ||y||,
||y||² ≥ D²/N       (N>0).
```

**NO-GO, precisely scoped:** If `D≠0`, *no scalar feedback* of this reciprocal-port form can remove the reservoir stock completely. Full transfer requires `D=0` at preparation. The stronger exact geometric minimum under unrestricted reciprocal rotation is `(N-sqrt(N²-4D²))/2` (when `D≠0` it is positive). Therefore a robust claim of unit complete capture over all relative phases is false for this family. No statement is made about a nonscalar coupling, extra channels, nonreciprocal dissipative system or an independently derived controller.

## Candidate feedback and explicit exact trajectory

Choose (not derive)

```
g(r,y)= ||y||²/N       for N>0,       g(0,0)=0.
```

This is dimensionless and lies in `[0,1]`, respecting the source paper's `0≤g<2` positive-energy branch. The special unit coefficient is a **constitutive normalization choice**, not a parameter-free physical law. Since `N` is invariant, `g` is a smooth rational state function away from the origin, zero at an empty reservoir.

Under the specially prepared aligned branch `r(0)=0`, `||y(0)||²=N>0`, let `r=√N sinθ e`, `y=√N cosθ e` for a fixed unit vector e. Then `θ'=cos²θ`, hence with `θ(0)=0`,

```
tan θ(u)=u,
||r(u)||²=N u²/(1+u²),
||y(u)||²=N/(1+u²).
```

The target stock increases monotonically and approaches `N`, while the source stock decreases to zero **only asymptotically**. At no finite `u` is the source completely empty, and no separate controller is required to obtain this asymptotic aligned branch. This is an **EXACT/CANDIDATE** dynamical existence result conditional on both the chosen feedback and the aligned/empty preparation.

For unit initial source, exact fixtures give target stock `0,1/2,4/5,9/10,100/101,10000/10001` at `u=0,1,2,3,10,100` respectively. This is native model time, not seconds.

## Phase sensitivity and comparison controls

For `D≠0`, the universal bound `||y||²≥D²/N` implies `g≥D²/N²>0`, so the reciprocal mixing angle continues changing. The stored modal pair remains on its compact rotation orbit, rather than latching at zero reservoir stock. Thus the proposed feedback **fails generic-phase retention**; the successful aligned branch has `D=0`, a nongeneric codimension-one condition in the nondegenerate modal-pair space.

Concrete exact controls:
- **Null** `g=0`: no transfer, source remains charged.
- **Constant reciprocal** `g=1`: reversible periodic exchange; no attraction.
- **Autonomous stock feedback** `g=||y||²/N`: asymptotic transfer for empty target/aligned input; nonzero D prevents complete transfer for arbitrary phases.
- **Externally switched perfect swap** from v0.6: can latch, but switching time and controller energy/record remain imposed.

Take `r=(1,0),y=(0,1)`, so `N=2,D=1`; source stock never falls below `1/2` by the universal bound (the exact orbit minimum is 1). Take `r=(1,1),y=(2,-1)`, giving `N=7,D=-3`; source stock is at least `9/7`. These counterexamples are exact rational preparation fixtures.

## S4 and support-current provenance

In the QPB1 source, both modal vectors transform in the sign representation of S4. Therefore `N,D`, and the proposed scalar `g=||y||²/N`, are S4-invariant, so the feedback is equivariant **conditional on that source representation hypothesis**. S4 covariance does not select g: for example `g=0`, `g=1`, and `g=||y||²/N` all obey it while producing distinct dynamics.

The Q170–Q179 support ledger describes a separate **29D 1→4 carrier** with equal-share ownership and signed currents. No isomorphism or dynamically compatible transfer between the QPB1 17D packet-plus-reservoir and 29D support carrier is established. Claiming that this feedback creates retained cell matter would conflate different carriers and stocks. Physical action weighting G05 and environment/gate renewal remain OPEN.

## Verification / disposition

Run `python3 experiments/parity-dynamics-gauge-20261103/autonomous_gate_v07.py`, with stdlib exact Fractions; expected `autonomous_gate_v07.results.json`. A separate four-test constructor audit `test_autonomous_gate_v07.py` checks both conserved quantities, the aligned exact solution, a phase lower bound and zero gate. Exact tests locally PASS. The mathematical results are independent of any experimental target values; the feedback formula was freely proposed **after** the native-port question was exposed, so it is Discovery CANDIDATE, not source-derived selection. Non-constructor review NOT_RUN.

**Disposition:** Conditioned scalar-port invariants and nongeneric aligned asymptotic capture are EXACT for their declared model. AUTO_FREEZE any statement that this is a unique native selection law, robust physical matter persistence, a physical clock, or a universal particle mechanism. Reopen with a separately sourced non-scalar coupling or an admitted dissipation/reservoir-controller constitutive law with exact signed support receipts, then test generic relative phases and independent observables.
