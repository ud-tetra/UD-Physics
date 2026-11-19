# K4 cross-complex contact, time-rate and metric completion audit v2.0

**2026-11-05/06 | UD-Physics Discovery | EXACT under stated hypotheses / CANDIDATE changed-metric and changed-contact branches | Physical promotion 0.**

## Governance and decision status

Existing HELD task klein-tetra-face-flip-20261103, session ktff-20261103-01, claim ref refs/heads/claims/klein-tetra-face-flip-20261103 SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4. Existing isolated branch / draft PR #301. Original task base 0eef9a3f77198810b35bee8d3ef578ebc3af403a; current inspected main 7ef45805563b47cbe1e2f34bb9e6e97ce5f5c962. No mainline, source ledger, or site changes.

**Source-authoritative Q171 sign review issue #338 remains OPEN, with no review comments or accepted amendment** when checked. The proposal v0.39a is NOT canonical. The native sources used read-only are frozen coefficient ledger v0.39 Q165–Q171/Q173/Q177–Q179; QPB1 local generators v1.0 §§1–3; Pachner state transport v0.1 §1→4; Pachner current metric v0.1; Pachner event actuator v0.1 (different 2→3 toy overlay, not an admitted 1→4 physical mechanism); prior task Q170 current interface v1.9.

## Typed setup

Parent K0 has real graded simplicial chain dimension15 (4,6,4,1), signed differential D0 and source generator A0=D0−D0ᵀ under H0=I15. Centroid-refined K1 has chain dimension29 (5,10,10,4), D1 and A1=D1−D1ᵀ under H1=I29. F:R15→R29 is the original **integral** degree-one boundary-compatible 1→4 subdivision, D1 F=F D0. T=F[:,original14] is the isometric shell embedding. Let N=I29−TTᵀ, b=∂3 e_top/2 in R14, and C=N A1 T.

Original Q165 and Q170 are unit coefficient stocks and signed Hasse-cut currents on each fixed complex. No physical time, energy, length, Planck-scale data, metric change, or event selection is admitted.

## Theorem 1 — unchanged native interface and stronger local-contact no-go

Exact full matrices and the independent cone pairing show

    CᵀC = I14,       Lold=e_topᵀ A0 T=−2bᵀ,
    Loldᵀ Lold=4bbᵀ.

The necessary second-order shared-shell compatibility condition is CᵀC=4bbᵀ. In the actual source model the difference 4bbᵀ−I14 has eigenvalues 3 once and −1 thirteen times, rank14 and squared Frobenius norm **22**.

Every one-to-one cone-local contact assignment C_g=C diag(g_i) (arbitrary real g_i on the 14 distinct old-shell/new-cone incidence pairs) has diagonal Gram diag(g_i²). The old top Gram has twelve nonzero *ordered* off-diagonal entries among the four old outer face coordinates, each of magnitude1. Thus **best possible squared Frobenius mismatch ≥12** for any such real local weights; equality is attained at zero vertex/edge weights and face weights of magnitude1, but still does not intertwine dynamics.

Allowing an arbitrary positive definite newborn-coordinate metric H_born does not rescue that one-to-one pattern. Its Gram has rank equal to the number of active cone columns. To match rank1 of 4bbᵀ, at most one column may be active, whereas 4bbᵀ has nonzero support on *four* face coordinate directions. No positive definite newborn H with one-to-one masked cone pattern can meet the full equality under an unchanged shell metric.

The **conditional** face-contact interpretation of Q173 permits binary masks only on the four original outer-face→new-top links, leaving vertex/edge cone links unit. Exhausting all 16 assignments gives squared Frobenius mismatch at least22 (maximum26; unique optimum all-on). This does not authorize modifying the generator: actual Q173 masks a **current readout**, not the signed differential.

A scalar new formal-time rate λ(u) multiplying A1 cannot repair all-state shared-shell second-order matching. Universal first-derivative match enforces λ(0)=1 since shared A_shell is nonzero. Second-order discrepancy equals M+λ'(0) A_shell, where nonzero M=4bbᵀ−I14 is symmetric and A_shell is skew. A symmetric nonzero matrix cannot be canceled by a skew multiple. The original v1.9 no-go therefore survives arbitrary scalar time-reparameterization near the event under this stated first-jet condition.

## Theorem 2 — coherent rational, non-Hasse completion (CANDIDATE)

Set h=C b, a normalized collective new-top mode, and choose **new** shell/newborn coupling C★=−2h bᵀ. Let A★ retain old shared/shared and new born/born blocks of A1, replacing C and its skew transpose with C★ and −C★ᵀ. Then A★ is skew in the unit metric and C★ᵀC★=4bbᵀ. Define S★ as the identity embedding on the old original14 shell and S★ e_top=h. Exact source-bound matrices verify S★ᵀS★=I15 and A★ S★=S★ A0.

Taking the adjacent-grade upper blocks of A★ as a **changed rational boundary D★** gives D★²=0, D★S★=S★D0 and full 24 signed S4 covariance. However 12 face/top couplings connect non-incident original faces and child tetrahedra; the changed differential includes half-integer coefficients and the normalized top image S★ e_top is one-half (with orientation sign) of the original new fundamental chain. It does not preserve the **original** integral degree-one Pachner map F or the native D1. A★ differs on 26 unordered coordinate coupling pairs. Therefore this is a mathematically coherent, explicitly **non-native** counterexample to any overbroad impossibility claim, not a sourced physical contact law.

## Theorem 3 — positive non-diagonal metric completion with original D1 and integral F (CANDIDATE)

A separate exact construction preserves the **original** signed D1 and **original integral F**. Construct the rational barycentric chain retraction P:R29→R15 by mapping old vertices to themselves and the new centroid e4 to (e0+e1+e2+e3)/4, extending through exterior powers of oriented simplices. Then P F=I15 and P D1=D0 P, verified exactly and under all 24 signed S4 actions.

Let Q=I29−FP and define H=PᵀP+QᵀQ. The chain spaces im(F) and ker(P) are D1 invariant and H orthogonal; for x≠0, xᵀHx=||Px||²+||Qx||²>0. Thus H is positive definite and Fᵀ H F=I15.

Define a **changed Hodge adjoint**

    A_H=D1−H⁻¹D1ᵀH.

Exact matrices satisfy D1²=0, A_Hᵀ H+H A_H=0, and A_H F=F A0. The old-image stock and all old native trajectories are thus exactly preserved **relative to the new metric H**, including the original integral degree-one top chain map. All 24 S4 actions preserve P,F,H,A_H. Explicit H has 52 nonzero off-diagonal unordered entries, and A_H differs from numerical Q169 A1 on 50 directed entries, including 12 newly non-Hasse couplings. Characteristic polynomials:

    chi_A_H = lambda*(lambda²+4)^7*(lambda²+5)^7,
    chi_A1  = lambda*(lambda²+1)*(lambda²+5)^13.

This is an **inverse constructed** metric selecting an orthogonal split by an explicit chain retraction, not a native Q165 metric derivation. It changes the numerical generator/current coefficients and the refined chain squared-stock readout. Positive metrics on ker(P) are not uniquely selected by Q165/Q169. It does not provide a physical event trigger or finite-resolution floor. This changes the exact assumptions of v1.9 rather than invalidating its obstruction.

## Disposition

**EXACT / NO-GO scoped:** With original Q169, native unit metrics, and original local Hasse contacts, no scalar clock change or independent local cone weighting makes all shared-shell currents/accelerations agree beyond the switch. **EXACT/CONDITIONAL constructed:** Two altered models can restore dynamical intertwining, one by changing rational/non-Hasse differential and one by changing metric-adjoint while retaining integral topology. Neither is source-admitted; no automatic physical promotion.

**OPEN:** Q171 review issue #338, source-selected intercomplex metric/contact/event controller, the resulting complete Q165/Q170 physical current ledger, and an independent SI time/length action bridge. Physical promotion 0.

## Reproduction

Standalone exact package UD_K4_CROSS_COMPLEX_CONTACT_METRIC_v2.0.zip contains the previous complete v1.7–v1.9 input scripts, contact_metric_v20.py, metric_retraction_v20.py, independent_rank_contact_v20.py, 14 exact regression tests, complete proof, results and SHA-256 manifest. Local 14/14 tests PASS; source-authoritative and non-constructor review NOT_RUN. Separate GitHub concise replay and typed receipt/handoff are captured in this task's isolated branch. No Planck targets used.