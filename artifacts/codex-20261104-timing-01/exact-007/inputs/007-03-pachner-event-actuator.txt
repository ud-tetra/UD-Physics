# Pachner event actuator and overlay gate v0.1

**2026-11-04 — development, no registry entry; physical promotion 0.** Remote integrated base `ecd0949a6f03eb30680e432409b7dc8c1742a76f`; local computation checkout `20efe0f7784aedc24130f2f0883324fea6eb9d04` because Git fetch returned 503. The only intervening main change was the closure-only PR #304 to prior session records, verified against the remote branch; the mathematical dependencies were unchanged. Read-only supplied sources: *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165/Q166/Q169/Q170/Q173/Q177–Q179; *CRL-2 subdivision governance proposal v1.0*, SHA-256 `8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4`, §§1–4. The [prior new-carrier note](../pachner-current-metric/README.md) established the postulated instantaneous switch's internal edge onset.

## Carrier and proposed actuator

Let `K_old` be the two-tetrahedron bipyramid with tetrahedra `0123,0124` and `K_new` the three-tetrahedron bipyramid `0134,0234,1234`. Both use ascending oriented simplices over `Q`, with the same outer boundary. Their **abstract union** `U=K_old∪K_new` has all five four-vertex subsets of `{0,1,2,3,4}` and `f(U)=(5,10,10,5)`, Euler characteristic zero. It is the combinatorial boundary of a 4-simplex. Because the old and new tetrahedral fillings occupy overlapping interiors in the same geometric bipyramid, this abstract overlay is **not a geometric common refinement** of that bipyramid.

The native overlay carrier is `C_*(U;Q)≅Q^30` with unit Q165 quadratic stock. Embed the two fixed-complex Q169 incidence generators `A_o` and `A_n` by zeros on simplices missing from each triangulation. The deliberately **CANDIDATE** gate is

`A_g(τ)=(1−g(τ))A_o+g(τ)A_n`, `0≤g(τ)≤1`; `dc/dτ=A_g(τ)c`.

Both generators are skew and Hasse-supported on the overlay. Thus `d||c||²/dτ=0` for **every** prescribed gate history, including a state-dependent `g(c,τ)`. Q166's paired incidence currents and Q170's control-volume cut-current balance hold for the currently weighted edges; the weights are not Q169 coefficients of an intermediate simplicial complex. No source row supplies an equation for `g`, a physical clock, or a move trigger. This is a conservative interface construction, not a derived UD actuator.

## Gate-sensitive born-edge preparation

Set the common vertex-3 amplitude to one and all other overlay amplitudes to zero. The born new edge `(3,4)` is absent in the old complex and has `A_n[(3,4),3]=+1`. For a post-event gate `g(τ)=τ^p` on `0≤τ≤1`, `p=0,1,2`, exact rational Taylor recurrence gives:

| Assumed gate | Born-edge amplitude leading term | Born-edge stock leading term |
| --- | --- | --- |
| Immediate new generator, `p=0` | `τ` | `τ²` |
| Linear ramp, `p=1` | `τ²/2` | `τ⁴/4` |
| Quadratic ramp, `p=2` | `τ³/3` | `τ⁶/9` |
| No switch, `g=0` | `0` | `0` |

**EXACT / CONDITIONAL:** more generally if `g(τ)=aτ^p+O(τ^(p+1))` with nonzero `a` and integer `p≥0`, the prepared edge amplitude starts `aτ^(p+1)/(p+1)`, and stock starts `a²τ^(2p+2)/(p+1)²`, subject to the same initial state and the declared overlay equation. This leading coefficient follows by integrating the local vertex→edge incidence; no measured target was used. The previous `τ²` stock law therefore belongs specifically to its **instantaneous full-new** branch, not to all conservative 2→3 switches. The exact program verifies the first three cases and native norm preservation through eighth-order coefficients.

## Frozen records and selector obstruction

Three simplices are old-only: interior face `012` and top cells `0123,0124`. Seven are new-only: edge `34`, faces `034,134,234`, and top cells `0134,0234,1234`. At an immediate switch to the zero-extended `A_n`, all three old-only coordinates are exactly frozen. In particular, prepare unit amplitude on old interior face `012`. It retains unit overlay stock indefinitely while the readout restricted to the new complex is zero. This is an explicit hidden-state counterexample for a **bare incidence-gate overlay**. Q165 conservation alone cannot erase or reassign its stock. Resetting those amplitudes requires a specified isometric transfer into the new carrier or an accounted source/sink record; neither is provided by Q166/Q173/Q177–Q179.

**NO-GO / scoped to this overlay:** local skew incidence and stock conservation do not select an event time, gate ramp, or old-only reset. The distinct histories above satisfy those same constraints and yield different born-edge onset orders. This is not a no-go against an added constitutive trigger, a different carrier, or a measured actuator. The bare overlay as a **complete** actuator is AUTO_FREEZE; its conservation lemma, exact onset family, and frozen-mode witness are retained. A candidate cross-complex switch requires (i) an endogenous gate variable with source/update and initial condition, (ii) a conservative or explicitly open reset/transfer for all three old-only coordinates, and (iii) a physical port and matched null before correspondence. Independent nonconstructor review NOT_RUN; physical promotion 0.

Run `python3 experiments/pachner-event-actuator/audit.py` to reproduce the [exact output](results.json); the [receipt](../../candidates/pachner-event-actuator/mathematical_receipt.json) and immutable capture record the inputs and checks.
