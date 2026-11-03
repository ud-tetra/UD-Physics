# Pachner locality selector and boundary-port gate v0.1

**2026-11-03 — development, no registry entry; physical promotion 0.** Integrated base `d4b10ea6abeab50d5e1b74e8735fb98955c6e017`. This tests the [conditional first-entry and projected-flow candidate](../pachner-trigger-lift/README.md) against an explicit old-coordinate Hasse-locality criterion and prepares a *possible* six-channel measurement contract. The supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165/Q169/Q170/Q173/Q177–Q179, is read-only. Q169 defines the incidence generator on each fixed complex; Q173 gates an **existing** face/top incidence current. It supplies neither a cross-complex rule nor a physical port.

## Objects and selector questions

Use the exact rational 2→3 chain map `M:Q^23→Q^27`, old-coordinate kernel projector `P`, and positive event-image metric `H=MᵀM+P=I+G` from the prior notes. The source fixed-complex generators are `A_old=B_old−B_oldᵀ` and `A_new=B_new−B_newᵀ`. The candidate projected post-switch generator was `K₀=H⁻¹MᵀA_new M`; it is `H`-skew. The source old Hasse adjacency defines `B₂:C₂(K_old)→C₁(K_old)` and `B₃:C₃(K_old)→C₂(K_old)` in ascending oriented bases. The new memory carrier and `H`, old-coordinate continuation, formal evolution parameter and reserve are assumed; no seconds or joules map exists.

Ask two distinct questions:

1. **Unchanged incidence selector:** If the vertex↔edge coefficients inherited from the old complex must stay exactly Q169, does the earlier `K_λ=K₀+λH⁻¹A_old` family retain a free parameter?
2. **Strict old-coordinate locality:** If one additionally requires the pulled-back generator to preserve *both* oriented edge↔face coefficients and have zero face↔top entries whenever the old `B₃` incidence is zero, is this compatible with `H`-skew conservation and the projection? This is a **new criterion on pulled-back coordinates**, not an automatic reading of Q169 on `K_new`.

## Exact selector and obstructions

**DERIVED / scoped family:** `K₀` agrees with `A_old` on both vertex↔edge blocks and on the *upward* edge→face block. The `λH⁻¹A_old` perturbation changes the intact vertex→edge incidence coefficients by a factor `1+λ`; exact preservation therefore fixes `λ=0` **within that one-parameter family**. It does not establish global uniqueness.

**NO-GO / scoped to the inherited `H` and exact preservation of both old edge↔face blocks:** Write `H₂` for the old face-degree block of `H`; the old edge metric block is identity. If a candidate `H`-skew generator retained `K₁₂=B₂` and `K₂₁=−B₂ᵀ`, skewness would require `B₂(I−H₂)=0`. The exact matrix `B₂(H₂−I)` has **rank 1**, so those simultaneous demands are incompatible. The projected `K₀` accordingly differs from `A_old` in 21 reverse face→edge entries, including 12 entries absent from old incidence. A different memory metric or altered coupling is a distinct branch; it does not erase this conditional obstruction.

**NO-GO / scoped to the projected `K₀` and a Q173-style old face/top correction:** `K₀` has six nonzero old-coordinate face→top entries (`±1/2`) where the old `B₃` incidence is exactly zero. Let `C₂₃^old` be the full-open skew old face/top incidence block, and consider the equally conserving, all-12-automorphism-compatible family

`K_μ=H⁻¹(MᵀA_new M+μ C₂₃^old)`, `μ∈Q`.

The correction `H⁻¹C₂₃^old` is **zero on all six offending entries**. Hence no `μ` cancels them. This is a test of that declared correction family, not a universal impossibility of a different extended carrier. Q173 allows gate factors on its existing incidences; it does not select `μ` for an *additional* post-switch term.

## Readout nonuniqueness with an explicit prepared input

The two generators `K₀` and `K₁` for this `μ` family both preserve `H`, the 12 signed geometric automorphisms, and the intact vertex↔edge and upward edge→face blocks. Their difference has rank 4. For a locally inward budget crossing, prepare old amplitudes `x_(012)=1`, `c_(01)=1`, `c_(013)=1`, all others zero, with assumed reserve `R=G=8/5`. Then `Ġ=−4`; a sufficiently short earlier preparation interval has a unique local first entry. Let `L=Σ_(six outer-cap faces)c_f²` be a **native squared-amplitude readout**. The exact instantaneous receipts are:

| Model | `L` at event | `dL/dτ` | `d²L/dτ²` |
| --- | ---: | ---: | ---: |
| Old Q169, no move | `1` | `−2` | `−4` |
| New event with projected `K₀` | `7/2` | `−4` | `−38/3` |
| New event with `K₁` | `7/2` | `−4` | `−44/3` |

The native event jump is `5/2`. The `K₀`/`K₁` second-derivative difference is `2` per **formal parameter squared**; both share the same first derivative on this preparation. The witness was the **first** accepted member of a declared finite search of up to 136 single/two `±1` additions to the prior `x_(012)=c_(01)=1` state. One candidate was evaluated; the purpose was to expose algebraic nonidentifiability, not fit measured data. The earlier simpler witness has identical first and second derivatives under this `μ` family, so choice of preparation matters.

## Measurement contract before physical comparison

The table is an internal discriminator against a **fixed-old-complex no-move baseline**, not a conventional graphite or other material prediction. A possible **CANDIDATE emulator bridge** would expose six independently addressed cap-face amplitude channels with physical readings `V_f(t)=g_f c_f(τ(t))+b_f+ε_f(t)` in volts. Independently calibrate the gains `g_f` (volts/native amplitude), offsets `b_f`, noise covariance `Σ` (volt²), and `τ=κ_t(t−t₀)` with `κ_t` in formal-parameter units per second. For independently calibrated diagonal gains `D=diag(g_f)`, a noise-bias-corrected native estimator would be `L̂=||D⁻¹(V−b)||²−tr(D⁻¹ΣD⁻ᵀ)` under zero-mean additive noise. A physical stock or energy conversion is **not** supplied by this voltage readout.

The matched **conventional emulator null** would retain the old topology with the same source preparation, physical switching controls, sensor chain and drive; include a sham control to bound control-induced transients. Freeze the gains, timing map, state preparation, noise/uncertainty model, event window, `μ`, and readout statistic before examining event data. A proposed acceptance rule would require both (i) a detectable event-minus-sham step at the calibrated port and (ii) agreement of the registered second-derivative contrast with its propagated uncertainty while rejecting the matched no-move null. No apparatus, calibration record, uncertainty budget or such data are available here. Without them, the native `5/2` and `2` cannot be promoted to volts, joules, friction, or charge. A graphite honeycomb/moiré null would require a separate, explicitly mapped material interface.

**Disposition:** AUTO_LOCK the scoped rank-1 metric obstruction, six-entry correction-family no-go, rational readout receipts and bounded witness replay. Keep the first-entry rule, `H` memory metric, locality criterion and emulator bridge **CANDIDATE / OPEN_GATED**. The result blocks a claim that old Hasse locality uniquely selects the projected generator or that Q173 supplies a Pachner actuator. Nonconstructor review NOT_RUN; physical promotion 0. The next highest-value dependency is a local carrier/metric and support-current law on the **new** or common-refinement complex that defines event coupling without reusing incompatible old incidence coefficients, before a physical port can be preregistered.

Run `python3 experiments/pachner-locality-port/audit.py`; the [exact output](results.json), [calculation receipt](../../candidates/pachner-locality-port/mathematical_receipt.json) and immutable run capture provide the source revision, matrices, ranks, witnesses and limitations.
