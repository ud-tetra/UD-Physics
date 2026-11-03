# Directional contact and six-cycle topology audit v0.1

**2026-11-03 — EXACT finite-quotient calculations; CANDIDATE contact activation; graphite bridge OPEN.** This audit continues [contact-pulse harmonic charge v0.1](../graphite-contact-pulse-casimir/README.md) at integrated base `b7d3205d59256335bbd78a91dbd596ed485573fc`. The [equivariant endogenous-gate obstruction](../graphite-endogenous-gate/README.md) applies to the symmetric seed without an external direction. The [UD coefficient provenance ledger v0.39(2)](../../artifacts/action-normalization-20261022-a1/exact-001/inputs/011-20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md), SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q166/Q167 and Q22–Q26, supplies incidence/conditional contact algebra but no graphite edge-selecting law. The [PRL publisher abstract](https://journals.aps.org/prl/abstract/10.1103/ly48-b4l2), published 2026-10-14, is already exposed: it reports **sharp friction peaks**, with negligible load dependence, at 21.8° and 38.2° for the `(2,1)` pattern, with other patterns below its detection level. No force, pulse duration, or load value is fitted here. The [designated UD site](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/) reports Papers I–III 1.1.1 / IV 0.1 and physical promotion 0 at retrieval on 2026-11-03.

## Objects, domain, conventions

For `(m,n)=(2,1),(3,1),(3,2)`, take `N=m²+mn+n²` and the finite periodic honeycomb chain complex over `Z` (cycle counts) or `Q` (harmonic pairing). Vertex set is `A_r,B_r`, `r∈Z/NZ`; edge class `t=0,1,2` is oriented `A_r→B_(r-s_t)` with `s=(0,m+n,n)`. Faces, their signed boundary `B₂:Z^N→Z^(3N)`, and the unnormalized harmonic embedding `U:Q²→Q^(3N)` with edge-class covectors `u₀=(1,1),u₁=(-1,1),u₂=(0,-2)` are the declared prior carrier. Its metric is unit chain metric; `G=UᵀU=N diag(2,6)`. The root `A₀` is a prepared contact location, not a preferred vertex of an unprepared uniform sheet. The input direction `d∈Q²` below is a *registered native harmonic-coordinate direction*; its map from physical sliding direction is OPEN. No physical length, time, force or load units attach to these counts.

Let `C₆(v)` be the set of unoriented simple six-cycles containing vertex `v`. A face cycle is identified by its exact six signed edge IDs from `B₂`. The surplus `X₆(v)=|C₆(v)|−3` is a scalar graph observable, not a contact gate or a friction observable. A six-cycle with `Uᵀ c≠0` cannot be a face boundary, because `B₂ᵀU=0`.

## Exact graph result and locality bound

| Quotient `(m,n)` | `N` | Rooted distance layers from `A₀` | All six-cycles | Face cycles | Extra six-cycles | `|C₆(A₀)|` |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| `(2,1)` | 7 | `1,3,6,4` | 28 | 7 | 21 | 12 |
| `(3,1)` | 13 | `1,3,6,9,6,1` | 13 | 13 | 0 | 3 |
| `(3,2)` | 19 | `1,3,6,9,12,7` | 19 | 19 | 0 | 3 |

**EXACT / finite carrier.** Every vertex has the same `C₆` count by translation and A/B exchange. All 21 nonface cycles in `N=7` have nonzero `Uᵀc` in the code's chosen orientation; hence they are nonboundaries in this chain complex. The six-cycle double count `6·#cycles=(2N)·|C₆(v)|` gives `168=14·12`, `78=26·3`, `114=38·3`. An independent count uses the 12 nonbacktracking three-step paths from `A₀`: their endpoint multiplicities are `4×3` for `N=7`, and `6×1+3×2` for each of `N=13,19`. With no four-cycles in these three graphs, pairs of paths to the same endpoint enumerate six-cycles once, giving `4·binom(3,2)=12` and `3·binom(2,2)=3`.

**NO-GO / rooted radius at most 2.** The induced rooted radius-two neighborhoods, including local edge-class pattern, are isomorphic trees with layers `1,3,6` for the three primary quotients. Any deterministic selector using only such a neighborhood, the same local packet data and the same registered direction cannot decide `N=7` versus `N=13,19` without a global label or other input. Radius three can read the distinction, but reading a toroidal quotient wrap is a nonlocal/coherent modeling assumption for an extended graphite interface.

**Counterexamples to a naive surplus gate.** The scaled `(4,2)` quotient has `N=28`, 56 six-cycles, 28 faces, 28 extras and 6 through a vertex. `(2,2)` has `N=12`, 16 cycles, 12 faces, 4 extras and additional four-cycle identifications; the independent three-step formula requiring girth six is not applied there. Thus `X₆>0` is not exclusive to the primitive `N=7` carrier. An exact scan of coprime `2≤m≤8, 1≤n≤m` found a surplus only for `(2,1)` within **that finite search**, not a theorem for all quotients or a physical selection principle. `(4,2)` is a scaled description of the same angle family, so its surplus is not an independent-angle friction counterexample.

## Directional edge choice, and the remaining gate

For the supplied root and a generic nonzero registered `d=(d₁,d₂)`, define `t*(d)=argmax_t u_t d`, i.e. maximize `d₁+d₂`, `−d₁+d₂`, `−2d₂`. Exclude the three maximum-tie rays (or supply an independently defined tie law). Let

`R=[[-1/2,-3/2],[1/2,-1/2]]`.

Then `R³=I`, `Rᵀ diag(2,6) R=diag(2,6)`, `u_t R=u_(t−1 mod 3)`, so `t*(Rd)=t*(d)+1 mod 3`. **DERIVED / equivariant under joint action:** a registered direction picks one incident edge without an arbitrary class label; it works in *all* three quotients. The native direction metric and rotation are specified, but the physical registration `d=T u_slide` and the contact-site/pulse clock are not sourced. The rule ceases to be single valued on tie rays. A spatially uniform `d` alone does not localize a single-edge pulse to `A₀`; a contact envelope is still required.

A *target-informed* exploratory gate could activate this choice when `|C₆(A₀)|=12`, close edge `(t*(d),0)` for externally supplied `0<s<ε≤1/100`, and reopen. Conditional on that **imposed** activation, the prior exact pulse theorem gives `a'(0)=G⁻¹u_(t*)` on `N=7` and zero pulse transfer on `N=13,19`. This is **CANDIDATE/FIT**, since the threshold 12 and use of quotient topology were selected after knowing the `(2,1)` target. It is not a derivation of why a graphite contact samples a periodic six-loop, and it supplies no dimensional damping or signed friction. The simpler `X₆>0` gate has the scaled and degenerate counterexamples above. Do not promote either gate as a physical law or freeze a graphite forecast.

## Verification and disposition

Run `python3 experiments/graphite-contact-selector-topology/audit.py`. It independently enumerates vertex-simple cycles and three-step path pairs (where girth permits), matches face edge sets, checks `Uᵀc` for every nonface cycle, verifies rooted uniformity/double counting, and tests the rational `C₃` direction action and previous pulse derivative. [`results.json`](results.json) records all listed quotients. See the candidate receipt and immutable capture for exact source/replay hashes.

**AUTO_LOCK** the finite graph counts, nonboundary witness, radius-two locality obstruction under the stated local-data premise, and directional equivariance under joint `R`. **AUTO_FREEZE** the proposed surplus/12 activation as a graphite selector: no source binds toroidal loop sensing to contact gating, and physical damping/force remains open. Reopen with an independently defined spatial coherence/contact law, registered sliding-direction map, physical pulse clock and measured material response; compare with conventional moiré barriers and held-out signed force/load data. Independent physics review NOT_RUN; physical promotion 0.
