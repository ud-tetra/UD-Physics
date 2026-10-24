# Native UD source and damping gate for the graphite bridge

**EXACT / CONDITIONAL obstruction; source identification and material law OPEN.** This is a narrow dependency audit for [graphite paper v2](../graphite-manuscript-v2/README.md). It uses the supplied *UD coefficient provenance ledger v0.39(2)* (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, rows Q22–Q26 and Q76–Q84) and the paper's proposed harmonic port. It does not equate a native phase overlap with friction or assert that all UD couplings vanish.

## Question and typed maps

The seven-cell carrier supplies a native, unit-edge incidence map `S(w)=Mᵀ diag(w) B₁ᵀ : R¹⁴→R²`. A proposed *material* identification is `C=S(w)R : R^h→R²`, where `R` maps physical internal coordinates into the 14 vertex-source coordinates and must carry the appropriate dimensions. At a stable registry, the assumed low-frequency passive material response is

`Γ_add=C K⁻¹ D_h K⁻¹ Cᵀ ⪰ 0`, with internal stiffness `K≻0` and Rayleigh loss `D_h⪰0`.

For dimensionless internal coordinates, `K` has energy per participating upper atom, `D_h` has energy × physical time per atom, `C` has energy/(atom × length), and `Γ_add` has energy × time/(atom × length²). Real force additionally needs contact participation and a readout protocol. The UD cellular unit metric and dimensionless phase kernels provide none of these material units by themselves.

## Two precise no-go statements

1. **Scalar-only current-source identification.** Ledger Q22 sets the *seam-sector pairing current source* `κ_{θ,pair}^{current}=0` within its stated internal scope. If the graphite coupling is **assumed** to be `C=κ_{θ,pair}^{current} C̃` for finite `C̃`, then `C=0` and `Γ_add=0`. Likewise, if the only weight contrast is `w_e=w₀+κ_{θ,pair}^{current} δ_e` with finite `δ_e`, all weights are uniform and `S(w)=w₀ MᵀB₁ᵀ=0`. These are exact consequences of those additional identifications, not a theorem that every other UD material source is zero. Q22 explicitly calls for a derivation of nonuniform edge stiffness before that lane activates.

2. **Phase kernel cannot set a dimensional loss or its load slope.** Q76–Q84 supply conditional dimensionless expressions such as `K_chain=cos(Δφ_chain)` and `Γ_chain=|cos(Δφ_chain)|`, with physical branch/context phase sourcing still open. They do not specify a map to `D_h(P)`, an energy scale or physical time. Even if `C` and `K` were independently fixed and `Γ_add(P₀)` calibrated, choose any baseline `D₀(P)⪰0` and any real `s`, and set `D_s(P)=exp[s(P−P₀)]D₀(P)`. At `P₀`, `D_s=D₀` and `Γ_s=Γ₀`, while

   `∂_P Γ_s|_{P₀}=∂_P Γ₀|_{P₀}+s Γ₀(P₀)`.

   Thus an arbitrary local load derivative remains compatible with the same phase-kernel statements and one-load response value whenever `Γ₀(P₀)≠0`. A constant positive rescaling `D_h→tD_h` likewise rescales `Γ_add→tΓ_add` without changing those ledger formulas. If `Γ₀=0`, a different nonzero coupling/source must first be established. This is an identifiability proof for the declared linear-response bridge, not a physical claim that damping is freely tunable in graphite.

## What the other ledger rows do and do not supply

Q23 gives a source-stratum conditional `a_ij^(src)=2η_O w_ij Ξ_ij`. Q24 gives a conditional symmetric candidate `(η_O/2)(w_ij Ξ_ij+w_ji Ξ_ji)`. Q25 records that `w_ij` has no single current canonical definition; Q26 leaves the route variable `Ξ_ij` and its state space, update, symmetry and normalization open. Hence these expressions define a **possible algebraic slot**, not independently sourced graphite weights, an N=7 selection law, or a material loss coefficient. Q77–Q84 concern coherence/phase and apparatus context; their cosine or logarithm should not be inserted as a viscosity or linewidth without a typed constitutive derivation.

The newest [Chen *et al.* PRL publisher page](https://doi.org/10.1103/ly48-b4l2), checked 24 October 2026, continues to expose the abstract while marking the article text and supplemental material subscription required. It reports detectable paired friction peaks and weak load dependence, but the public access path supplies no numerical force/load table, threshold or complex loss matrix. This audit therefore makes **no measured residual estimate**.

## Minimal constructive bridge programme

1. Define a *current* typed native edge law `w_e(state, registry, P)` and any route variable `Ξ_e` from independently specified primitives. Check positivity, C3 covariance, N=7/13/19 behavior, and the known uniform-source and local-stencil obstructions without choosing coefficients from the observed peaks.
2. Specify the map from native site/source coordinates through physical internal modes to `C(P)`, including energy, length, contact participation and atom-label registration. Apply the existing [two pure-source cross-Hessian relations](../graphite-source-constraints/README.md) to an independently subtracted additional coupling; the archived KC total coupling fails the pure-source test.
3. Derive or measure `K(P)` and the **complex** loss matrix, including cross-mode terms and linewidths, plus the physical-time map. Then propagate uncertainty into a finite-speed signed force estimator. A dimensionless phase overlap may constrain such a law only after its causal link is derived.
4. Freeze all of those inputs, ordinary two-dimensional PES/contact controls, and detector censoring before comparing held-out paired-angle and control force/load traces. The [directional passive null](../graphite-directional-shape/README.md) is one conventional control, not a UD selector.

**Outcome:** the present source/phase ledger does not supply a nonzero, dimensional, angle-selective graphite drag prediction. The conditional source-zero result and loss-scale/load-slope nonidentifiability are exact in their declared models. A future independently specified source and bath can reopen the bridge; physical promotion 0 and independent physics review NOT_RUN.

Replay the rational finite witness with `python3 experiments/graphite-native-source-gate/replay_source_gate.py`; the [mathematical receipt](../../candidates/graphite-native-source-gate/mathematical_receipt.json) records the general proof and the [immutable capture](../../artifacts/graphnative-20261024-01/exact-001/manifest.json) records the executed witness. Constructor algebra and repository integrity checks do not constitute independent physical review.
