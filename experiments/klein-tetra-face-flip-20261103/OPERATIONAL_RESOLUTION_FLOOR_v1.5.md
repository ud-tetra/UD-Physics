# K4 recursive operational distinguishability and resolution-floor audit v1.5

**2026-11-05 — Discovery / EXACT-CONDITIONAL all-depth boundary-response theorem / scoped NO-GO / physical promotion 0.**

**Ownership:** Existing task \`klein-tetra-face-flip-20261103\`, session \`ktff-20261103-01\`, HELD claim at \`667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4\`, same isolated branch and draft PR #301. Source main checked \`738b9d205fd9f9735a05d4976de70f1519474bff\`, original task base \`0eef9a3f77198810b35bee8d3ef578ebc3af403a\`. No mainline export, claim release, physical promotion or site changes.

## Exact source strata and observable types

- \`experiments/four-cell-tetrahedron/README.md\` v1.0 §§Definition and scope; Exact sharing, geometry and recursive counts: 1→4 centroid splits preserve the outer four triangular faces and give recursive \`T_n=4^n\`, \`V_n=(4^n+11)/3\`, \`E_n=(4^(n+1)+14)/3\`, \`F_n=2·4^n+2\`. Source unit metric is a mathematical choice, not a measured physical metric.
- \`experiments/pachner-boundary-observability/README.md\` v0.1 §§Question and typed construction; Exact snapped moves and response: the **candidate** boundary probe uses the unit-edge vertex graph Laplacian \`L=B1 B1^T\`, holds four original boundary vertex potentials \`phi\`, eliminates interior vertices, and reads \`Lambda=L_bb-L_bi L_ii^-1 L_ib\`. Its proven first-level values are \`Lambda0=4I-J\`, \`Lambda1=(5/4)(4I-J)\`. This development observer is **not a physically calibrated measurement**.
- Frozen imported coefficient ledger \`sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md\` P01–P06 gives **local** label capacity N1=24×8=192. Q170–Q171 give Hasse-stock continuity and exact top-cell core stock \`S_tau^core=c_(3,tau)^2\`; Q177–Q179 give equal-top-star cell ownership and current. Their physical open-system and recursive admissibility rules remain OPEN.
- \`experiments/qpb1-native-events/EVENT_CONTRACT.md\` v1.0: event threshold readouts are an **added** observer on the single 15D K4 carrier. No source-accepted all-depth measurement algebra or SI clock exists.
- \`experiments/klein-tetra-face-flip-20261103/K4_MULTILEVEL_METRIC_CLOCK_v0.9.md\` gives exact native skew generator nonintertwining at two levels; do not infer dynamical persistence from a static response.

**Types of operational equality:** (a) \`O_shell=(V,E,F)_outer=(4,6,4)\` is exactly constant for all n and is blind to internal refinements; (b) \`O_DN(K_n)=Lambda_n\` is an explicitly selected boundary port; (c) \`O_core(x)=(c_(3,tau)^2)\` is local mathematical support stock. An all-physical-observables equivalence relation is OPEN because the physical readout set and finite sensitivity are not sourced.

## Theorem A — exact all-depth boundary response

For \`K_n\` the n-fold 1→4 centroid subdivision of the original filled tetrahedron, include each graph edge exactly once with **unit** conductance. Fix the original four boundary vertex potentials \`phi\`, minimize \`E_n=1/2 Σ_(edges ij)(x_i-x_j)^2\` over all new interior vertex values, and obtain the exact quadratic boundary-response matrix \`Lambda_n\`. Then

\`\`\`
       Lambda_n = alpha_n (4 I_4 - 1_4 1_4^T),
       alpha_n = [6 + (11/4)^n]/7,
       alpha_(n+1) - alpha_n = (11/4)^n/4 > 0.
\`\`\`

**Proof by weighted graph gluing and Kron elimination (all n):** Exclude the six original edges of one tetrahedron and let \`w_n\` denote the uniform edge conductance of the effective four-port clique formed by the edges added recursively *inside* that tetrahedron. \`w_0=0\`. After inserting centroid \`z\`, there are four new radial edges of unit conductance. Each of the four child tetrahedra carries its own depth-n added-edge port \`w_n\`. An old-old edge lies in **two** children and therefore has induced conductance \`2w_n\`; a center-old radial edge lies in **three** children and has conductance \`1+3w_n\`. The newly added interior edges of different children are disjoint except for their port vertices, so no edge is double-counted. Eliminating \`z\` gives a clique of conductance \`(1+3w_n)/4\` on the four original vertices. Consequently

\`\`\`
     w_(n+1) = 2w_n + (1+3w_n)/4 = (11w_n+1)/4,
     w_n = [(11/4)^n-1]/7,       alpha_n=1+w_n.
\`\`\`

The last equality restores the six original unit edges once. The graph is S4-covariant, so \`Lambda_n\` is scalar on the three-dimensional nonconstant boundary-vertex representation. For any nonconstant \`phi\`, the quadratic energy \`1/2 phi^T Lambda_n phi\` changes **strictly at every finite n** and grows without bound under this unweighted observer. This is an all-depth exact result for the stated graph, NOT a physical divergence theorem.

**Independent direct check:** Enumerate exact simplex edge graphs at n=0,1,2,3; compute the rational 4×4 Schur complements independently of the above recurrence; verify all 24 S4 boundary relabelings at each level.

| n | (V,E,F,T) | alpha_n | nonconstant eigenvalue 4 alpha_n | E_n for phi=(1,-1,0,0) |
|---:|---|---:|---:|---:|
| 0 | (4,6,4,1) | 1 | 4 | 4 |
| 1 | (5,10,10,4) | 5/4 | 5 | 5 |
| 2 | (9,26,34,16) | 31/16 | 31/4 | 31/4 |
| 3 | (25,90,130,64) | 245/64 | 245/16 | 245/16 |

A separately authored five-vertex symbolic Kron script independently verifies \`w_(n+1)=(11w_n+1)/4\` without enumerating the entire refined tetrahedron.

**NO-GO under named assumptions:** There is no finite N such that the exact candidate boundary readout \`Lambda_n\` becomes the same for every n≥N. A finite physical sensor resolution, scale-dependent conductance weighting, alternative metric or physical admission rule is an entirely different branch.

## Theorem B — original shell blindness and all-depth core-stock distinction

The original boundary remains four vertices, six edges and four triangular faces at every depth. Hence shell geometry alone cannot distinguish the refinements, and that blindness starts **immediately**, not at a positive physical minimum interval.

On any one of the \`4^(n-1)\` parent top tetrahedra at depth n−1, take its four child top cells \`tau0..tau3\`. Define two real pure-top-grade chain states at level n:

\`\`\`
       x = e_tau0,
       y = (e_tau0 + e_tau1 + e_tau2 + e_tau3)/2.
\`\`\`

Both have total native squared norm exactly one and have **zero original-shell chain coefficients**. Q171's top-cell core readout \`S_tau^core=c_(3,tau)^2\` gives \`(1,0,0,0)\` versus \`(1/4,1/4,1/4,1/4)\`. These distinguish the states even modulo simplex permutations, and the construction works for **every finite n≥1** on the declared graded chain carrier. The Q177–Q179 equal-top-star readout would also see top-cell differences if its summation includes maximal simplices; that extension is not needed for this proof.

This is an **instantaneous algebraic support** distinction, not a theorem that physical observers can instrument each cell, that states persist under evolution, or that matter grows preferentially.

## Finite 192 local labels do not yield a global cutoff

The local address capacity \`N1=24×8=192\` and the *number of distinct tetrahedral 3-cells* \`4^n\` are differently typed. At depth n=4 there are already 256 top cells, without contradicting a 192-state alphabet per cell. Neither finite local labels nor exact shell combinatorics imposes a termination depth, physical minimum edge length, frequency, or SI metric. If physical admissibility later caps recursion or gauges away new modes, that requires an independent constitutive rule and a fresh test.

**Disposition:** AUTO_LOCK only this scoped mathematical all-depth boundary-response and Q171-local-support counterexample, subject to exact verified hypotheses. AUTO_FREEZE a universal operational or Planck-scale floor from 192 alone; **physical promotion 0**. Any physical claim must freeze a complete admitted observable algebra, physical metric/sensitivity and clock, and test whether refinements remain distinguishable under those fixed readouts.

## Replay and verification

Exact local scripts, separate symbolic Kron script, machine JSON results, eight passing tests, full source report and SHA256 manifest in \`UD_K4_OPERATIONAL_RESOLUTION_FLOOR_v1.5.zip\`. Local archive SHA256 \`67623c6beedfb8068c345eca0634f6c99dc16b930180e35235261bb541387114\`. GitHub proof/source/result/receipt/handoff are archived in the existing isolated claim branch. Constructor exact proof and checks PASS; non-constructor peer review NOT_RUN; repository CI is integrity-only. No Planck constants, meters or fitted lengths used.

**Next discriminant:** derive a truly admitted physical/burden measurement algebra and an event/refinement stopping rule, or audit scale-dependent weights for a controlled **native** continuum response. Do not impose an SI-scale Planck numerical match.