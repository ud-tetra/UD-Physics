# K4 action and positive intercomplex metric selection gate v2.1

**2026-11-06 / Discovery / EXACT-CONDITIONAL / SOURCE_BLOCKED / physical promotion 0.** Existing HELD task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, claim SHA `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated branch and draft PR #301, original base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`. Main checked `322ea849bfb949e4136a898e05d9d7fa0ec7604f`. No mainline, frozen source, registry or site edits. Q171 issue #338 remains OPEN with zero reviewer comments and no accepted amendment.

## Source audit and selection status

| Source / version / section | Exact stated role | Source-selected 1→4 H? |
|---|---|---|
| Frozen coefficient provenance ledger v0.39, Q165–Q171/Q173/Q177–179 | Q165 fixed-carrier **unit** quadratic support; Q169 native signed skew A=D−Dᵀ; Q170 Hasse currents; Q173 measured-current mask; Q177 existing-cell stock allocation | **NO** P, H, or event rule |
| QPB1 Local Generators v1.0 §§1–3 | Single filled K4 C15, H=I, signed S4, A=d−dᵀ | **NO**, fixed carrier |
| Action Normalization Audit v1.0 §§1–3, O09–O15 / IDENTIFIABILITY_THEOREM v0.1 | Native loop action I=a Δφ/2; action unit A0=B0 a0²/τ0; physical η_A=A0/ℏ numerically OPEN | **NO**, action units not an intercomplex metric |
| Pachner State Transport v0.1 §1→4 | Integral degree-one F, chain-compatibility, native unit norm1→4 obstruction | **NO** |
| Pachner Current Metric v0.1 | Connected Hasse graph and unchanged numerical skew require scalar diagonal H | **NO** |
| Pachner Trigger Lift/Event Actuator v0.1 | **Candidate** 2→3 event/memory/overlay with unsourced gate | **NO**, distinct carrier |
| Main UD `UD_BARYCENTRIC_RENEWAL_CANDIDATE_v0.1.md` (2026-10-13) §§1–4 | Candidate full barycentric **1→24** refinement and external renewal index | **NO**, neither 1→4 nor sourced trigger |
| Main UD `UD_PACHNER_CANONICAL_EVENT_SECTOR_SELECTOR_v0.1.md` (2026-09-18) §§1–11 | Conditional rank6 sector selection on ∂Δ4/2→3 event | **NO**, different carrier; dynamical identity OPEN |
| Main UD `Docs/UD cubic macrocell metric and propagation audit.md` v0.1 | Macrocell metric not unique under geometry/volume; conditional isotropic propagation selects shape after *adding* criterion | **NO**, different carrier |
| Uploaded `Unified Dynamics (Distinction Theory) v2.2: Master Manuscript.pdf`, Part II X.4/X.10, Parts III/V/X | Formation-floor and Update Engine *concepts*, generic Qobs=Q0(1+zQ), symbolic gravity Hamiltonian | **NO** typed 1→4 event map or positive 29D metric |
| Uploaded `master_action.md` and `packet_field_equation.md` | Reconstructed-source placeholders | **NO** |
| Designated UD portal, checked 2026-11-06 | Current public paper edition and physical promotion0; review pending | No selection exposed in fetched public landing page |

Historical/conditional source entries are *not* promoted to an accepted constitutive law by this audit.

## Theorem A — exact source metric obstruction

Let C0=R15, C1=R29, D0/D1 the original signed oriented simplicial boundaries, A0=D0−D0ᵀ, A1=D1−D1ᵀ, and F:C0→C1 the original degree-one integral 1→4 chain map. It satisfies
```
D1 F=F D0, Fᵀ F=diag(I14,4).
```
Thus native Q165 unit stock is not conserved on old occupied top. Even a scalar new metric c I29 would require c=1 on old 14 lower-grade coordinates and 4c=1 on the old top: impossible. Grade-dependent positive diagonal metrics fail unchanged Q169 H-skew unless scalar across connected Hasse incidence. **NO-GO, under source unit metrics and original integral F.**

## Theorem B — continuum of exact but **unselected** positive metrics

Previous v2.0 deliberately constructs a rational barycentric chain retraction P:R29→R15 with PF=I15 and PD1=D0P. Define Q=I29−FP. Because D1 F=F D0, Q commutes with D1; imF and kerP are D1-invariant. For every real t>0 define
```
H_t=PᵀP+t QᵀQ.
```
For every nonzero x, x=F(Px)+Qx and xᵀH_t x=||Px||²+t||Qx||²>0, so H_t is positive. Also FᵀH_tF=I15. The changed metric-adjoint skew
```
A_t=D1−H_t⁻¹D1ᵀH_t
```
obeys A_tᵀH_t+H_tA_t=0 and A_tF=FA0, with signed S4 covariance. **The same A_t is obtained for every t>0.** Proof: in the direct-sum coordinates (x,y)↦Fx+y, y∈kerP, D1 is block diagonal and H_t=diag(I15,tI14), so the scalar t cancels from the adjoint on kerP. Thus chain compatibility, symmetry, isometry and exact generator intertwining do **not** select any one H_t.

Exact 29D SymPy checks for t=1/4,1,2 PASS, including all 24 signed S4 actions. Distinct H_t give identical full A_t but different newborn stock values. For the centroid-complement y=Q e4,
```
||y||²_native=5/4, ||y||²_Ht=(5/4)t,
t=1/4→5/16, t=1→5/4, t=2→5/2.
```
Even requiring selected newborn basis vectors to have H_t norm1 yields incompatible t: centroid e4 requires t=3/5, edge e04 requires t=13/19. All H_t change source Q165's refined unit-coefficient norm and the numerical Q169 adjoint.

If the O09 action I=a Δφ/2 is **additionally** extended with a=||x||²_Ht for newborn modes, it inherits t-dependence; that extension is not supplied by the action source. Native action unit A0, a physical ℏ map, or the generic historical dressing rule do not resolve t.

## Theorem C — exact non-selection decision

**EXACT:** There is a continuum of distinct, positive, S4-invariant metrics all satisfying exact F chain/isometry and A_t-F intertwining, and all producing the *same changed new generator*. No checked source provides a newborn-kernel normalization that singles out t=1, nor any independent reason to choose P and the associated Q orthogonal splitting as the UD material action. All-v2.0 mathematical identities remain valid as conditional constructions.

**NO-GO / SOURCE_BLOCKED (narrow):** Under accepted Q165/Q169 unit metrics, F is not globally isometric. Invoking isometry/current continuity or native action dimensions alone cannot select a nonunit intercomplex metric. No source-selected 1→4 contact, admission predicate, physical time/length or physical refinement floor has been established. The 2→3 event candidates and 1→24 barycentric-renewal candidate cannot be imported into the 1→4 K4 branch as accepted rules.

## Verification, source release and reopening

Full local executable `UD_K4_ACTION_METRIC_SELECTION_AUDIT_v2.1.zip` contains: versioned source matrix and detailed audit; complete same-source v2.0 K4 reconstruction; exact 29D family replay; independent 4D direct-sum theorem control; machine results; 10/10 passing exact tests; SHA-256 per-file manifest. This work remains constructor mathematical verification, independent non-constructor review NOT_RUN; GitHub CI integrity is not source approval.

**Disposition:** `PARK_SOURCE_BLOCKED` for a **physical/native** intercomplex metric, contact or refinement-floor claim. Preserve earlier scoped no-go and new exact positive-family theorem, not a claim of universal impossibility of an additional law. Reopen only when an independently established action/metric term on the 14 newborn modes (or a new typed event law) specifies its state space, dynamics, readout, current, units/normalization and independent validation. Issue #338 still awaits source-authoritative Q171 direction review. Physical promotion=0.
