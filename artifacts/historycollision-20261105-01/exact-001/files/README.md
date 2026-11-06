# History-to-present collision gate v0.1

2026-11-05 · Discovery base `ud-tetra/UD-Physics@234f54471c32cc9ad4873cd8042103fa19795909` · physical promotion **0**.

## Source, objects and question

The recovered ledger v0.85 (SHA-256 `8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec`) P04 defines an eight-state opposite-pair register `Θ={0,1}³`. Its O09 distinguishes a lifted Hodge history from a projected phase; Q136 is a scalar accumulated obstruction, whose sufficiency for typed lifted history remains open. The prior [four-site source gate](../g0506-packet-hodge-sourcegate/README.md) §§1–2 gives a **candidate** `F:C⁴→E14` with a complex common-mode kernel and only rank-six image. The historical `ud-tetra/UD@a78193d`, `docs/UD_Master_Full.tex` §Foundational Axioms supplies packet site variables and spatial `U_ij` path transport, but no temporal event register update or universe-wide history ledger. This audit does not import a physical event law from those sources.

Question: given a complete present register state and a tick count, can one recover the ordered event labels? Define a *toy*, externally driven finite state `θ_n∈Θ`, alphabet `p_n∈{A,B,C}`, and update `θ_(n+1)=θ_n⊕e_(p_n)`, with initial `θ_0=000`. The three labeled opposite pairs and XOR are a declared **CANDIDATE** mechanism; no apparatus, energy, physical clock or stochastic event probabilities are assumed. The readout is either full `θ_N`, augmented pair counts `c_p`, or the preceding candidate Hodge projection `F` in a separate continuous model.

## Exact collision and bounded record theorem

**EXACT / conditional on the driven XOR rule:** `θ_N=θ_0⊕(⊕_n e_(p_n))`, so order is erased by the endpoint map. At `N=2`, `(A,B)` and `(B,A)` have the same endpoint `110`, same tick count and identical per-pair counts `(1,1,0)`. The distinct histories `(A,A)`, `(B,B)`, `(C,C)` all return to `000`. Thus even full present `θ_N` plus event counts does not recover ordered event history under this rule. This is a collision of *event histories*, not a claim that the full closed universe state is noninvertible: the external drive history was omitted from the state.

For length `N`, the domain has `3^N` words and the endpoint has at most eight values. By pigeonhole, some endpoint has at least `ceil(3^N/8)` histories; an independent register that distinguishes histories within every endpoint must have at least `ceil(log₂ max_θ |fiber_N(θ)|)` bits. Exact enumeration for `N=1,…,6` is in [results.json](results.json). This is a lower bound on an *additional* history readout in this toy model, not a universe-wide entropy bound, a claim that `N1=192` is physical storage capacity, or a statement about arbitrary coarse-grained probability entropy.

**EXACT / alternative closed model:** For a fixed known mask `m∈Θ`, autonomous `θ_(n+1)=θ_n⊕m` is bijective, with inverse also XOR `m`. Given the exact state, rule and tick count, its prior state trajectory is reconstructible. That does not create separate archived copies of events, and it says nothing about a driven law with unrecorded inputs. A larger globally reversible state could carry the drive, but UD must define that enlargement and a readout before asserting preservation.

**EXACT / separate candidate projection:** The prior `F(z)=P0 Re z+J P0 Im z` has `F(z+c1)=F(z)` for any complex `c` because `P0 1=0`. Distinct full site-amplitude histories differing by a time-dependent common mode can therefore share the entire projected Hodge trace even if each follows a chosen compatible evolution. For the imposed `z'=2iz`, choose `z_1(s)=e^{2is}v` and `z_2(s)=e^{2is}(v+c1)`; they are distinct for `c≠0` and `Fz_1(s)=Fz_2(s)` at every s. This is an observable-kernel collision, not a loss of the full packet state. The `z` identification and update are source-open.

## Disposition

**NO-GO / scoped:** The present three-bit register, even augmented by unordered event counts, is insufficient for ordered history reconstruction under the declared driven XOR law. The rank-six Hodge readout likewise does not recover its common packet mode under the candidate `F`. Neither proves that actual UD dynamics erase all traces, nor that nature retains a complete archive. A source temporal update, environment/boundary records, and a specified observation map are **OPEN**. Physical promotion remains 0.

[Exact replay](audit.py), [mathematical receipt](../../candidates/history-present-collision/mathematical_receipt.json), and [immutable capture](../../artifacts/historycollision-20261105-01/exact-001/manifest.json) document the bounded calculation. Constructor enumeration and analytical pigeonhole proof are not independent review. Next: determine whether a sourced packet/open-system event update preserves ordered receipts in an enlarged state or admits collisions under physically allowed forcing; test a declared record observable rather than infer an archive from conserved support alone.
