# Native refinement admission and weighted observability gate v1.6

**2026-11-05 | UD-Physics Discovery | EXACT / CONDITIONAL / SCOPED NO-GO / SOURCE SELECTION OPEN | Physical promotion 0.**

**Claim:** Existing task klein-tetra-face-flip-20261103, session ktff-20261103-01; coordination ref refs/heads/claims/klein-tetra-face-flip-20261103 HELD SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4, isolated discovery/klein-tetra-face-flip-20261103/ktff-20261103-01, draft PR #301. Main/source checked 738b9d205fd9f9735a05d4976de70f1519474bff; original task base 0eef9a3f77198810b35bee8d3ef578ebc3af403a. No mainline promotion, integration, status override or physical unit map.

## Source and object types

- Frozen ledger v0.39 P01–P06: N1=24·8=192 local frame×parity address capacity, not a total cell cap.
- Frozen Q165/Q166/Q169/Q170: native unit-metric squared simplex-chain support, signed adjacent-degree Hasse currents, fixed-complex A_K=B_K−B_Kᵀ, and exact cut-current conservation. No cross-complex event trigger or source-selected recursive weights.
- Q171: top-simplex core stock c_(3,tau)². Q173: masked face–cell current 2 h_f B3_(f,tau) c2_f c3_tau (128 mask checks), **not an event admission/edge-conductance rule**. Q177–Q179: per-incident-cell allocation w_(sigma,tau)=1/n3(sigma), not physical edge conductance or a move probability. For one 1→4 split an old edge is incident on two child tetrahedra and a radial edge on three, so this allocation is respectively 1/2 or 1/3 per incident cell, not the 1/4 trial used below.
- Experiments/four-cell-tetrahedron/README.md v1.0: the geometric 1→4 centroid split, child volume Vparent/4, not a length-conductance scaling.
- Experiments/pachner-boundary-observability/README.md v0.1: *developmental candidate* static unit-edge Dirichlet-to-Neumann (DN) port, not a physical measurement. The previously established recursive unit-weight response is in this task's OPERATIONAL_RESOLUTION_FLOOR_v1.5.md: Lambda_n=alpha_n(4I−11ᵀ), alpha_n=[6+(11/4)^n]/7.
- Experiments/pachner-state-transport/README.md v0.1 and pachner-current-metric/README.md v0.1: 1→4 integral top chain map changes unit top stock1→4; connected incidence graph enforces a scalar positive diagonal metric under unmodified Q169 A. No physical switch, reservoir, source selection or cross-complex normalization.

## Theorem A — Exact all-depth weighted boundary response

On K_n, keep each original outer-tetrahedron edge at conductance1. For every edge born at generation k>=1, choose a strictly positive **hypothetical** rational weight g_k; give the identical weight to all such edges for full S4 symmetry. The outer boundary vertex potentials are fixed and all inner vertex potentials minimize graph energy 1/2 sum_(edges) w_e(x_i−x_j)². Define Lambda_n as the Schur complement (Dirichlet-to-Neumann response). Then

    Lambda_n = alpha_n(4I4−11ᵀ)
    alpha_n = 1 + (1/4) sum_(k=1)^n (11/4)^(k−1) g_k
    alpha_(n+1)−alpha_n = (1/4)(11/4)^n g_(n+1).

**Proof:** Define w_(k,n) as the effective added-edge clique conductance inside a tetrahedron beginning at generation k, excluding its original six edges. Four depth-tail child tetrahedra contribute 2w_(k+1,n) on each old-to-old edge and 3w_(k+1,n) on each radial edge. The new central radial edge carries g_k. Five-node Kron elimination gives

    w_(k,n) = (11/4) w_(k+1,n) + g_k/4,
    w_(n+1,n)=0.

Iterating from k=1 to n gives the stated sum. This is **EXACT** over any positive rational/real generation weights. Under g_k>=0, exact finite saturation after N is equivalent to g_k=0 for all k>N, assuming zero-weight new inner vertices are handled by deleting disconnected zero-weight edges or using the energy-minimization limiting convention. It is not an autonomous physical refinement-stop rule. When all g_k>0 no finite N has identical Lambda responses for all later depths, regardless of possible limit.

Direct exact rational graph responses at n=0..3, plus separate symbolic five-node Kron elimination, verify the formula. All 24 S4 outer-vertex relabelings pass each level.

## Theorem B — Summability threshold for geometric weighting

For g_k=g1*r^(k−1), g1>0 and r>=0, put rho=(11/4)r. Then

    alpha_n = 1 + (g1/4) sum_(j=0)^(n−1) rho^j.

If r<4/11, alpha_n→1+g1/(4−11r). If r=4/11, alpha_n=1+n g1/4. If r>4/11, alpha_n diverges. None of these behaviors is selected by the finite-state count N1=192 or by Q165–Q179.

**Explicit candidate:** use g_k=4^(−(k−1)) as a *proxy* prompted by geometric child volume1/4. Volume ratio is not graph-edge conductance, so this is CANDIDATE, not an inference from Q177. Exact:

    alpha_n=9/5−(4/5)(11/16)^n, alpha_infinity=9/5,
    alpha_(n+1)−alpha_n=(11/16)^n/4.

At n0..3 alpha=(1,5/4,91/64,1577/1024), checked by direct rational Schur. The response remains strictly distinguishable at **every finite n**, while its residual to infinity tends to zero.

**Chosen measurement threshold, not physically sourced:** epsilon=1/100 yields first n=9 after which a *single adjacent-level change* does not exceed epsilon; a stronger test measuring the full remaining tail has first n=12. These are different observer contracts, and neither implies physical minimum length, time or termination. Q171 can still distinguish cell-owned top-stock configurations at every n under recursive admission, even when boundary response is below tolerance.

## Theorem C — Conservation versus native generator selection

Let B1:C1→C0 be the signed vertex-edge boundary, W=diag(w_e)>0 from the chosen graph weights, x=(v,e) with v in C0 and e in C1. A deliberately changed, incidence-local vertex–edge generator and metric are

    A_W = [[0,−B1 W],[B1ᵀ,0]],
    H_W=diag(I_C0,W).

Then A_Wᵀ H_W+H_W A_W=0. Thus xᵀH_W x is conserved *within a fixed K_n*. The paired stock/current on incident vertex i and edge j is 2v_i(−B1_ij w_j)e_j and its negative edge entry; every control-volume flux obeys exact cut balance. This is a mathematically consistent alternative, **not unchanged Q169/Q166**, and the raw edge coordinates have a changed coefficient metric.

**Uniqueness/no-go for unchanged Q169:** For any positive diagonal H on the full graded K_n chain and *unchanged* unit-coefficient Q169 skew A_K, the equation A_KᵀH+H A_K=0 implies H_ii=H_jj along every Hasse incidence edge. The full simplicial Hasse graph is connected, therefore H=c I. A generation-dependent diagonal metric cannot be inserted into Q169 without modifying A or its interpretation. This agrees with the source pachner-current-metric connected-Hasse lemma.

**Independent cross-complex stock obstacle:** The degree-one integral 1→4 top-cell chain map sends a unit parent tetrahedron to four signed unit child tetrahedra. Its Q165 squared norm changes 1→4. The vertex–edge weighted model does not change that top-cell map or supply a reservoir/current across complexes. Therefore even when the weighted fixed-complex generator conserves its own quadratic stock, it does not establish a physically admissible, stock-conserving recursive event.

## Decision

**EXACT conditional:** all-depth weighted DN formula, positive-weight no finite exact plateau, summability threshold r<4/11, separate metric-skew weighted vertex–edge conservation, and connected-Hasse unit-metric restriction for original Q169.

**NO-GO (scoped):** No source-selected finite recursion cutoff or physical floor follows from 192 local addresses, Q173 masks, Q177 ownership or 1/4 child-volume geometry. A positive geometric-weighted response limit is not a finite stopping depth or proof of global operational indistinguishability.

**OPEN:** physical/native selection of g_k, event admission/termination or tolerance, metric/source action across moves, recursive Q171 observability, frame and clock. No Planck constants or SI units. Physical promotion 0.

## Verification

Full locally executed v1.6 weighted_refinement_v16.py, independent_weighted_kron_v16.py, test_weighted_refinement_v16.py (8 exact tests PASS); source report, rational results and SHA-256 manifest packaged as UD_K4_WEIGHTED_ADMISSION_GATE_v1.6.zip. Local exact source may differ in bytes from corresponding GitHub replay; record hashes in handoff. Non-constructor mathematical review NOT_RUN. GitHub CI integrity does not certify the mathematics.

Next highest-value gate: source or preregister a genuine refinement event/admissibility predicate and an explicit measurement algebra and test stock-conserving continuity across the added 3-cells. Do not treat the volume ratio as an accepted edge conductance or insert a tolerance selected to produce an anticipated floor.
