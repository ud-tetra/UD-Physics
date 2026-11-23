# UD-Physics Discovery handoff — Recursive K4 operational resolution v1.5

**2026-11-05 | EXACT / CONDITIONAL / NO-GO only for declared native observer | PHYSICAL PROMOTION 0**

**Ownership:** Same existing HELD task \`klein-tetra-face-flip-20261103\`, session \`ktff-20261103-01\`, claim ref \`refs/heads/claims/klein-tetra-face-flip-20261103\` at \`667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4\`. Isolated branch \`discovery/klein-tetra-face-flip-20261103/ktff-20261103-01\`, draft PR #301. Current main checked \`738b9d205fd9f9735a05d4976de70f1519474bff\`, original task base \`0eef9a3f77198810b35bee8d3ef578ebc3af403a\`. No merge, claim release, mainline/site/registry change or physics promotion.

## Source-bound definitions

- \`experiments/four-cell-tetrahedron/README.md\` v1.0: actual recursive 1→4 centroid tetrahedra, outer fixed shell (4,6,4), f-vector \`((4^n+11)/3,(4^(n+1)+14)/3,2·4^n+2,4^n)\`.
- \`experiments/pachner-boundary-observability/README.md\` v0.1: **developmental candidate** unit-edge graph Laplacian boundary hold/readout and static Dirichlet-to-Neumann \`Lambda=L_bb-L_bi L_ii^-1 L_ib\`, initial K4 response \`4I-J\`, after first split \`(5/4)(4I-J)\`; this is an exact mathematical observer but **not** an admitted physically measured device.
- Frozen coefficient ledger v0.39 P01–P06: N1=24×8=192 **local address count**, not global top-cell bound or distance. Q171: top-cell native core support \`S_tau^core=c_(3,tau)^2\`. Q177–Q179 recursive ownership/dissipation remains source-gated.
- \`experiments/qpb1-native-events/EVENT_CONTRACT.md\` v1.0: observer/event rule added; no physical event clock or global full-observable set. Earlier K4 multilevel v0.9 nonintertwining means static response does not establish dynamics.

## Exact all-depth theorem and independent checks

For **each distinct edge of the full refined 1-skeleton with unit conductance**, freeze the original four boundary vertices, minimize \`E=1/2 Σ_(ij)(x_i-x_j)^2\` over interior vertices. The exact response is

\`\`\`
Lambda_n = alpha_n(4I−J),   alpha_n=[6+(11/4)^n]/7,
alpha_(n+1)−alpha_n=(11/4)^n/4 > 0 for every integer n>=0.
\`\`\`

Proof: define the effective inner-added-edge clique conductance \`w_n\` of a tetrahedron with original six edges omitted, w0=0. Four child copies of the w_n network contribute \`2w_n\` to each original edge and \`3w_n\` to each radial edge. Newly inserted center adds one unit per radial edge. Eliminating that center by exact Kron reduction adds \`(1+3w_n)/4\` to every original edge, giving \`w_(n+1)=(11w_n+1)/4\` and closed form \`w_n=((11/4)^n−1)/7\`. Restore unit original K4 edges once: alpha=1+w.

**Direct exact independent graph calculation** at n0,n1,n2,n3 gives f-vectors (4,6,4,1),(5,10,10,4),(9,26,34,16),(25,90,130,64) and alpha 1,5/4,31/16,245/64 respectively; all 24 S4 boundary relabelings pass each level. A separately coded symbolic five-node Kron reduction verifies recurrence identically. For phi=(1,−1,0,0), native minimized energy is \`4alpha_n\`, strictly increasing. There is **no finite positive floor** at which this *declared* exact boundary-response port ceases to distinguish further 1→4 depth. Under these unit weights the response actually diverges; this is not evidence of physical energy divergence.

## Algebraic local support counterexample for all n

For any parent cell at level n−1 with children tau0..tau3, take pure-top-degree real chain states \`x=e_tau0\` and \`y=(Σ e_tau_i)/2\` at n>=1. Both have total squared norm1 and zero original outer-shell chain amplitudes. But Q171 top-cell core stocks are \`(1,0,0,0)\` versus \`(1/4,1/4,1/4,1/4)\`, not related by any simplex permutation. This is an instantaneous native amplitude distinction at every finite n, not proof of physical preparation, lifetime, measurement, or growth. Outer-shell **combinatorics alone** is exactly blind at every level from n=0, not a positive Planck-scale cutoff.

## What fails and what remains OPEN

The original local 192 count and expanding global top-cell count \`4^n\` are differently typed; by n4 top cells 256, with no contradiction of 192 addresses *per packet*. If UD later specifies that all new states are gauge-equivalent or physically inadmissible, that changes the premises and may produce an operational floor. No *complete* physically admitted observation algebra, resolution threshold, metric/clock, or recursive terminal admission rule was recovered. Thus **NO-GO is scoped to these named exact mathematical readouts**, and a physical minimum-length assertion remains OPEN, promotion0.

## Artifacts and replay

- \`experiments/klein-tetra-face-flip-20261103/OPERATIONAL_RESOLUTION_FLOOR_v1.5.md\` (full theorem and source typing).
- \`experiments/klein-tetra-face-flip-20261103/operational_resolution_v15.py\` (direct exact n0..3 full graphs and all-depth proof).
- \`experiments/klein-tetra-face-flip-20261103/independent_kron_v15.py\` (separate symbolic five-node recurrence).
- \`experiments/klein-tetra-face-flip-20261103/test_operational_resolution_v15.py\` (eight exact regression tests).
- \`experiments/klein-tetra-face-flip-20261103/operational_resolution_results_v15.json\`; \`candidates/klein-tetra-face-flip-20261103/mathematical_receipt_resolution_v1.5.json\`; current session record/journal and this handoff.
- Standalone locally executed \`UD_K4_OPERATIONAL_RESOLUTION_FLOOR_v1.5.zip\` includes full Python source, detailed report, two exact outputs, 8/8 passing tests and SHA-256 manifest; verified archive SHA256 \`67623c6beedfb8068c345eca0634f6c99dc16b930180e35235261bb541387114\`. Local source files are equivalent but not necessarily byte-identical with separately authored GitHub variants. No external non-constructor mathematics review; repository integrity CI is not physical verification.

## Next discriminant / stop rule

**Recommended:** freeze an explicit physically admitted measurement algebra and scale-aware observation threshold on the K4 chain carrier. Test whether any source-selected action, weighted edge response or event-admission rule makes refinement observations saturate while keeping conserved currents. Do not inject Planck constants/meters or a target scale; test native resolution first. Preserve current exact scoped no-go against a floor from 192 alone. Physical promotion remains 0.
