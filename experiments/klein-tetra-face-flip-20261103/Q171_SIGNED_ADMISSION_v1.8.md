# Q169/Q171 signed-current and first-crossing admission gate v1.8

**UD-Physics Discovery — 2026-11-05. EXACT / CONDITIONAL / CANDIDATE first-crossing switch / NO-GO scoped. Physical promotion = 0.**

## Source control, claim and typed objects

Continue the same held task klein-tetra-face-flip-20261103, session ktff-20261103-01 and coordination claim refs/heads/claims/klein-tetra-face-flip-20261103 at SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4. Isolated draft PR #301, original task base 0eef9a3f77198810b35bee8d3ef578ebc3af403a, source main examined at 74fe8f61856792fda717f2fffe8d3ed9a6564da2. No shared state, frozen ledger, mainline or website modification.

Read-only source ledger sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md: Q165 unit chain squared support, Q166 adjacent-degree signed incidence current, Q169 A=D−Dᵀ, Q170 cut balance, Q171 core stock and its printed **positive-B3 top derivative**, Q173 masked current readout, Q177–Q179 cell stock ownership. Primary exact single K4 generator: experiments/qpb1-local-generators/README.md v1.0 §§1–3. Explicit 1→4 boundary-identity map and unit stock1→4: experiments/pachner-state-transport/README.md v0.1 §1→4. Previous task v1.7: CROSS_COMPLEX_NATIVE_TRANSFER_v1.7.md with rank-one Q165 norm defect and exact postevent oscillator. QPB1 native events EVENT_CONTRACT.md v1.0 is an **added edge-quadrature event observer**, not a source-selected top-cell crossing or physical clock.

Types: C0 = C_*(single filled K4;R), graded (4,6,4,1), dimension15; C1=C_*(1→4 centroid refinement;R), graded (5,10,10,4), dimension29. The signed ascending oriented boundary matrices are D0,D1; native generators A0=D0−D0ᵀ,A1=D1−D1ᵀ under distinct unit Euclidean chain metrics. Parameter u is formal dimensionless evolution. Let e be original normalized top 3-cell and b=(B3_old e)/2 normalized signed face boundary; e and b are orthogonal and transform by the S4 orientation sign.

## 1. Algebraic current direction — exact and source convention gate

For face f and top tetrahedron tau, with the **same ascending B3 convention**,

    A_(f,tau)=B3(f,tau),        A_(tau,f)=−B3(f,tau).
    J_(f←tau)=+2 B3(f,tau)c_f c_tau,
    J_(tau←f)=−2 B3(f,tau)c_f c_tau=−J_(f←tau).
    dot(c_tau²)=Σ_f J_(tau←f)=−2Σ_f B3(f,tau)c_f c_tau.

This is exactly Q169's native top-stock derivative and Q166/Q170 antisymmetric pair-current accounting. Example f=012, tau=0124 has B3(f,tau)=−1, c_f=c_tau=1: face gain J_(f←tau)=−2 and top gain/stock derivative J_(tau←f)=+2. The **literal** frozen Q171 row prints +2Σ B3(f,tau)c_f c_tau as the *top-core stock derivative*, producing −2 for that example. Therefore both equalities cannot hold with the same B3 and flow convention. A consistent **CANDIDATE direction-alias amendment** would label +2B3 as the oriented face gain/outward tetrahedron current and write dot S_tau=−Σ J_out, or define an inward top current −2B3 and dot S_tau=+Σ J_in. This proposes an explicit sign/direction reconciliation without editing the frozen Q171 row. Until source stewardship accepts a typed amendment or demonstrates a different B3 convention, the archival source wording conflict remains OPEN_GATED. No physical energy/length is inferred.

## 2. Exact instantaneous Q165 admission criterion

The signed grade-preserving subdivision F:C0→C1 has FᵀF−I15=3eeᵀ exactly. For any old chain state x, with a=⟨e,x⟩,

    ||Fx||²−||x||²=3a².

Hence F is Q165-stock conserving on a state iff a=0. This makes the hyperplane ker(eᵀ), dimension14, the **exact instantaneous isometric-admissibility set for this F**, not a source-selected event rule.

Native old generator on span{e,b} satisfies A0e=2b, A0b=−2e. With initial a, beta=⟨b,x⟩, the exact top amplitude at formal time u is

    a(u)=a cos(2u)−beta sin(2u).

Whenever (a,beta)≠(0,0), its zeros are isolated, with spacing π/2 and slope magnitude 2sqrt(a²+beta²) at each root. The top stock S=a(u)² obeys S=dot S=0 and ddot S=8(a²+beta²)>0 at an isolated root. The **CANDIDATE** local/S4-invariant gate "first isolated top-stock zero", equivalently S=0 and ddot S>0 under continuous observation, would permit a support-conserving switch if an external event controller selects K1. At (a,beta)=(0,0) top stock is identically zero but ddot S=0, so no isolated crossing is detected; a current-only guard dot S=0 cannot distinguish root from null or turning point.

Equal top-pair norm²=2 examples (a,beta)=(1,1) and (1,−1) have first positive roots u=π/8 and u=3π/8, respectively. No universal clock tick or preparation-independent event period is obtained. For initially occupied top (a,beta)=(1,0), first root is u=π/4, at which old state equals b. The map F b is isometric and the new native A1 thereafter gives the previously proved reservoir-free shell/new-top exchange. However the old derivative mapped through F differs from new derivative:

    ||A1 F b−F A0 b||²=9.

Thus the potential event preserves **state support** (a C0 identification) but does NOT identify differentiable dynamics (C1 generator matching), energy or physical time. Choosing when/why to switch is a new constitutive premise.

## 3. Source-native rank13 dynamical tradeoff

Let Q_top=eeᵀ+bbᵀ and P13=I15−Q_top. Rank(P13)=13, [P13,A0]=0. This is the **maximal old A0-invariant linear subspace** contained in the instantaneous isometric hyperplane ker(eᵀ): for any invariant W in ker eᵀ, eᵀ A0 x=−2bᵀx=0 forces W⊂ker bᵀ, hence W⊂im P13. Conversely im P13 is invariant.

The independent earlier native first-refinement theorem (NATIVE_EIGHT_PROJECTOR_LEAKAGE_v1.1.md) gives for the orthogonal projection Π=F(FᵀF)⁻¹Fᵀ and transverse residual R=(I29−Π)A1F:

    RᵀR=P13.

Therefore for all x∈im(P13), ||R x||²=||x||². The 13-dimensional old-flow-invariant no-stock-jump sector is **maximally transverse to the new generator** under the declared normalization. For E=A1F−F A0 and x∈im P13, (I−Π)E x=R x, so

    ||E x||² ≥ ||x||².

**NO-GO:** No nonzero state in this old-dynamically-invariant, Q165-isometric 13D sector exactly intertwines full old/new native derivatives under F. Example normalized y=(e_012+e_013)/sqrt(2) lies in im P13, has zero old top amplitude *and* old top derivative for all times, but under A1 on the refined carrier it has nonzero new top derivative of squared norm1. This counterexample is distinct from the special shell b state that oscillates and hits simple top zero crossings.

## 4. Decision and scope

**EXACT / DERIVED:** Native oriented current directions, strong all-state admission condition, isolated crossing formula, 13D invariant no-defect subspace, first-refinement transverse leakage identity, lower bound on generator mismatch, and two phase-preparation controls.

**CANDIDATE:** the S4-invariant first *simple* top-zero-crossing event predicate; source Q169/Q171 specifies its algebraic inputs but DOES NOT select it as a jump instruction. It needs continuous phase history, event choice, state preparation and a cross-complex current/action account.

**OPEN:** frozen Q171 signed-current direction alias awaits versioned acceptance; no autonomous event trigger, no differentiable cross-complex evolution, no physical SI clock/metric/resolution floor, no Planck correspondence. Physical promotion=0.

## Reproducibility

Local full executable artifact UD_K4_SIGN_ADMISSION_GATE_v1.8.zip includes the earlier complete v1.7 matrix replay as source input, new full exact sign/admission SymPy script, an independent 2×2 modal/sign proof, 13 passing regression tests, both JSON outputs, detailed report and SHA256 file manifest. ZIP SHA256 5a660a3b739e09e4c4707e0b56ec80901ec777ea60d677a720c0a384f6885119. GitHub concise source replay sign_admission_v18.py and regression controls are independently authored equivalents (not claimed byte-identical). Constructor math PASS, independent non-constructor review NOT_RUN; GitHub CI integrity is not a mathematical proof.

**Next discriminator:** resolve Q171's direction alias by source-authoritative typed amendment, then test whether a *source-selected* top-mode/history-based event rule can consistently supply Q165/Q170 cross-complex current and control across generic occupied-top preparations, retaining the exact native 13D mismatch obstruction. If no selector is accepted, freeze an autonomous refinement-floor claim and preserve the narrower exact conservative transfer results.
