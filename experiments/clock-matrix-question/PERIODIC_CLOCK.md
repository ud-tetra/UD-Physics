# Direct periodic embedding of the prepared clock v0.1

**EXACT / CONDITIONAL.** The zero-extended single-cell clock plane is not invariant under the existing periodic incidence generator. The vertex-contrast launch spreads while its stock centroid stays fixed. A dressed or directional preparation is a separate test.

## Source and definitions

Discovery parent `6145840b9ffce6b17f8ffee32e61c126ff07a360`; integrated base `234f54471c32cc9ad4873cd8042103fa19795909`. Use [Prepared plane v0.1](PREPARED_PLANE.md) §§1–3 and the [UD cubic macrocell audit](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/Docs/UD%20cubic%20macrocell%20metric%20and%20propagation%20audit.md), Carrier construction and Periodic scalar propagation. The [BCC observation audit](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/Docs/UD%20BCC%20observation%20clock%20and%20causality%20audit.md), Vertex observation, supplies the scalar lane.

On the infinite periodic six-tetrahedron complex use real square-summable chains and the unit chain metric, increasing vertex order and the closed autonomous flow x'=Ax, with A=d−dᵀ to match the clock branch. This reverses the sign convention in the macrocell audit and leaves the squared-stock diagnostics invariant. No added nonlinear terms, boundary, drive or physical clock. Test the zero-extended clock in the linear limit λ=0. The tetrahedron is (000,100,110,111). Put v=e100−e110 and h=A_local v/2, with both squared norms 2. The launch is x(0)=v. Read q=<v,x>/2, p=<h,x>/2, with lifted phase atan2(p,q) where defined. Translation addresses are independent of these readouts.

## Leakage and phase

For the vertex launch, A v has edge components only, and the ensuing orbit stays in the vertex and gradient-edge lane by boundary nilpotency. The two vertices each meet 14 edges and share one. The common edge amplitude derivative has magnitude 2. Each of the other 26 incident edges has magnitude 1. In the original tetrahedron the derivative is 2h and has squared norm 8. Outside that tetrahedron the derivative has squared norm 22. Thus the normalized outside stock is 11s²+O(s⁴). Odd powers vanish by grade parity under reversal of s. The restriction of A to the proposed plane does not close, even at arbitrarily small positive s.

The readout has p'(0)=2 and q''(0)=−15. The isolated clock at λ=0 instead has q''(0)=−4. Its initial phase slope alone would therefore miss the failure. Replacing h by a quadrature proportional to the full A v still fails to close a two-dimensional invariant plane: ||A²v+15v||²=14. This test is against an exact carried clock plane, not a bound on the lifetime of a different dressed clock.

## Independent spatial readout

Place vertex stock at its lattice address and edge stock at its midpoint, weighted by the squared coordinate divided by conserved total stock 2. Measure squared radius with the conditional propagation metric G=I/2−11ᵀ/8 from the BCC observation audit, in lattice units, not meters. Reflection r↦(100+110)−r preserves the periodic carrier and swaps the two launch vertices. Its signed chain action commutes with A, and v has eigenvalue −1. Hence squared stock is reflection symmetric and its centroid stays exactly at (1,1/2,0). The initial mean squared radius is 3/32 and becomes 3/32+(45/32)s²+O(s⁴). The coefficient follows by assigning 2v_i(A²v)_i to the second derivative of vertex stock and 2(Av)_e² to that of edge stock. Finite incidence range and bounded degree give factorial spatial tails at finite s, so these moments exist. The observed spreading supplies no moving-clock rate comparison for this launch.

Reproduce with `python3 experiments/clock-matrix-question/periodic_clock.py`. The next discriminant is a directional preparation in the repository's scalar lane, with a tracked envelope, a co-moving phase port and fixed admissible leakage. The exact tests here use the exposed clock geometry and no fits or empirical inputs. Independent review NOT_RUN. Physical promotion 0.
