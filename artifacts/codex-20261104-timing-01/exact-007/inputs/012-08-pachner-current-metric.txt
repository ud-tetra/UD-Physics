# Local new-carrier current and transverse-mode gate v0.1

**2026-11-03 — development, no registry entry; physical promotion 0.** Integrated source base `5295ab317a1013e27296c20d44e8ee6a06784fba`. The supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165–Q173/Q177–Q179, is a read-only source. The supplied *CRL-2 subdivision governance proposal v1.0*, SHA-256 `8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4`, §§1–4, requires an independently reviewed bridge before higher status; this analysis makes no promotion. The prior [locality audit](../pachner-locality-port/README.md) supplies the exact snapped 2→3 transport and conditional memory metric.

## Typed setup and question

Let `K_old` be the two-tetrahedron bipyramid (chain dimensions `5,9,7,2`) and `K_new` the three-tetrahedron bipyramid (`5,10,9,3`), with ascending oriented simplices and rational coefficient spaces. The snapped map `M:C_*(K_old;Q)→C_*(K_new;Q)` has dimensions `27×23`, rank 21. Two kernel records form `L:Q^23→Q²`; their **assumed**, positive metric is `W=diag(2/5,1/2)`. The event embedding is `T=(M;L):Q^23→Q^27⊕Q²`, and `J=diag(I_27,W)`. Its induced old-coordinate metric `H=TᵀJT` is the prior `I+G`. These are dimensionless native amplitudes and stocks, not energy or physical time. The fixed-complex Q169 generator `A_new=B_new−B_newᵀ` acts on the 27 new simplices, with two static memory coordinates: `A=diag(A_new,0₂)`. Q166 currents connect only incident adjacent chain degrees. No event trigger, physical boundary port, or material coupling is sourced by Q169.

The question is whether exact local Q169 coefficients and support continuity select a new metric and an old-coordinate continuation that remains inside `T(Q^23)`.

## Metric selector and local current

**EXACT / CONDITIONAL.** For any positive diagonal metric `D=diag(d_i)` on the **new fixed complex**, conserving stock under the *unchanged numerical* Q169 incidence generator requires `(DA_new+A_newᵀD)_{ij}=A_ij(d_i−d_j)=0`. The new Hasse incidence graph is connected on all 27 simplices, so `D_new=d I_27`. Choosing the existing Q165 boundary-amplitude normalization `d=1` gives the native unit metric. This statement assumes a diagonal metric and unmodified incidence coefficients; non-diagonal metrics or changed couplings are other branches. The two isolated memory coordinates have unconstrained positive metric weights because Q169 contains no incidence edge to them.

For an incidence edge `i↔j`, Q166 gives the paired quadratic-stock flow from the signed coefficient `2 A_ij c_i c_j` (with opposite contributions to the two endpoints). Summing over a Hasse control volume yields Q170's cut-current balance. Q177–Q179 allocate existing simplex stock to incident cells; they do not add an event current between old and new complexes.

## Exact transverse obstruction and a born edge

The `J`-orthogonal projection onto the assumed event image is `Π=T H⁻¹TᵀJ`. If a post-event continuation `K` on the old 23-coordinate carrier is to reproduce the full local new dynamics, it needs `A T=T K`. The exact unavoidable transverse residual is

`R=(I−Π)A T`, with `TᵀJR=0` and `rank_Q(R)=6` (seven nonzero ambient rows). Thus **NO-GO / CONDITIONAL:** no `K:Q^23→Q^23` exactly intertwines the full `A` with this fixed `T`. The projected `K₀=H⁻¹TᵀJ A T` obeys `A T−T K₀=R` and is `H`-skew, but deletes six independent transverse derivative directions. Conservation alone does not make `R` vanish: `⟨Tc,Rc⟩_J=0`.

An independent local witness avoids relying on the rank computation. Prepare the old **vertex 3** amplitude `1`, all others zero, and apply `T`. The new internal edge `(3,4)` has zero event amplitude and **no row in the old map `M`**, while `A_new[(3,4),3]=+1` in the stated orientation. Its new-edge derivative is therefore `+1`; the edge stock starts as `τ²+O(τ³)` for formal parameter `τ`. In this witness `R e_3=e_(3,4)` and `||R e_3||_J²=1`. This is a native internal edge, not an electron carrier or physical charge. The local Q166 current is initially zero at the zero-amplitude edge and then transfers stock as it grows.

The natural full `A_new` evolution simply **leaves the event image** and grows the new edge mode; it needs no extra source after the postulated switch. If one instead imposes confinement to the old 23 coordinates, the instantaneous transverse correction must be `−Rc` up to a tangential term; that is an imposed constraint force, not a Q166 or Q173 derived actuator. Letting the new degree evolve resolves the kinematic inconsistency but still does not choose *when or why* the 2→3 move occurs, nor the map `M`, memory weights, or a physical readout.

## Disposition and next gate

AUTO_LOCK only the connected-diagonal-metric lemma, the exact `rank(R)=6` residual on this snapped embedding, and the born-edge witness, with the source and assumptions above. The cross-complex event trigger, memory normalization, new-mode initial condition and material port remain **CANDIDATE / OPEN_GATED**. An alternative transfer `T` or non-diagonal/changed metric is a new branch and must be checked independently. There is no physical time, joule, graphite friction, charge, or Standard Model identification here; nonconstructor review NOT_RUN and physical promotion 0.

Run `python3 experiments/pachner-current-metric/audit.py` for the [exact output](results.json), and see the [mathematical receipt](../../candidates/pachner-current-metric/mathematical_receipt.json) and immutable run capture. The next discriminant is an explicit **cross-complex event actuator and boundary preparation rule**, followed by a calibrated port and matched conventional null. The new-edge `τ²` stock onset is an internal diagnostic for that eventual bridge, not yet a measured prediction.
