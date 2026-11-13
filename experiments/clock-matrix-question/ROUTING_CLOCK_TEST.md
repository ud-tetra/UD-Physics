# Routing-budget clock test v0.1

**RESULT — EXACT / CONDITIONAL.** Neither proposed clock rule follows from the prepared tetrahedral clock. On its invariant plane the edge-stock fraction can sweep from zero to one while the signed clock rate stays constant. The model has no translational speed or independent frame map.

## 1. Source and scope

Discovery base `234f54471c32cc9ad4873cd8042103fa19795909`, branch parent `84c59f35f58405c06820d5697c74674305aeedbc`. [Prepared-plane v0.1](PREPARED_PLANE.md) §§1–3 and [positive stabilization](LOCAL_STABILIZATION.md) supply the source calculation. Use the filled tetrahedron with ascending orientations and Euclidean chain metric, no drive or boundary flux, and dimensionless continuous parameter s. The prepared plane has x=qv+ph, where v is pure vertex, h pure edge, and both have squared norm 2. The stabilizing terms leave the on-plane law unchanged. The initial phase is arbitrary and I=q²+p²>0. The rate uses the lifted signed phase atan2(p,q). This is a target-exposed comparison, with no fitted parameters or SI calibration.

## 2. Source-derived observables

The closed equations are q'=−Ωp, p'=Ωq, Ω=2+μI, μ≥0. Thus I'=0 and θ'=(qp'−pq')/I=Ω. Define normalized edge stock f=p²/I and vertex stock 1−f=q²/I. The flow gives f'=2Ωpq/I and f=sin²(θ). These are stock fractions, with signed exchange, on the same carrier. They have no sourced identity with physical velocity or a capacity spent per tick.

**NO-GO / scoped substitution.** If f is proposed as the overhead and a fixed positive reference Ω_ref is used, the square-root rule would require (Ω/Ω_ref)²=1−f. With the same I and coefficients, choose (q,p)=(√I,0) and (0,√I), visited a quarter native period apart. The left side is the same positive constant, whereas the right side changes from 1 to 0. Even on any open phase interval the right side is nonconstant. Using the phase-average edge stock gives exactly 1/2 at every I and μ, so it cannot provide a variable overhead. Reading routing as a signed instantaneous flux also fails to provide a nonnegative budget share without a new readout.

**NO-GO / affine loading.** For μ>0 and a fixed positive reference, increasing action strictly increases the phase rate. If one adds an affine overhead in I, its square-root rate cannot agree on any open action interval: (2+μI)²/Ω_ref² has a nonzero I² coefficient. A map inferred by solving β²=1−(Ω/Ω_ref)² is an inverse assignment. It supplies no independent translation law. At μ=0 the rate remains constant across all I>0, and cannot track varying overhead.

## 3. Evidence and reopening

The native balance is exact. The velocity-squared cost remains OPEN because the isolated carrier has no sourced displacement, translation generator or independently defined reference speed. The square-root response fails for the explicit stock readout and affine loading above. Other dynamics, couplings and independently selected readouts remain separate branches. A useful reopening test would define inter-packet propagation and a speed observable independently of clock phase, then compare a moving and reference clock under a fixed coupling. Physical promotion 0. Non-constructor review NOT_RUN.

Exact constructor check: `python3 experiments/clock-matrix-question/routing_clock_test.py`.
