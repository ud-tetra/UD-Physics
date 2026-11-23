# G05 path observables within an all-pass epoch

Physical Promotion = 0. Base `54c76f50f00f831409819d2ba11b55139261968a`. Follow-up to the fixed-clock control in [draft PR #463](https://github.com/ud-tetra/UD-Physics/pull/463). Its reviewed head is kept pinned.

## Conditional witness on a fixed filled tetrahedron

Use real simplicial chains, ascending orientations and the Euclidean coefficient metric. Write `D` for the graded boundary, `A=D-D^T`, `e` for the unit 3-cell and `f=D3 e/2` for its oriented unit boundary. The chain identity and the unit basis give `Ae=2f` and `Af=-2e`. With native time `s` and stock `a>0`, set
`x(s)=sqrt(a)[cos(2s)e+sin(2s)f]` on `[0,πn]`, where n is a positive integer. For this test, the receipt mask is held at 11111, signed currents are ungated, and the complex is fixed until the observation window ends. These are preparation assumptions. Matching endpoints alone cannot certify the C06 transport or first-entry guards.

The [existing Hodge one-form](../g0506-hodge-port-calibration/README.md) is
`ϑ_x(v)=⟨Ax,v⟩/4`. Along the witness, `ϑ_x(x′)=||Ax||²/4=a` and the integral is `πan`. It is additive over oriented path segments and changes sign under reversal of the parametrized curve. The reverse curve is a kinematic test and requires the reverse generator to be an evolution on the same fixed carrier. The integral and the mode stock use native, dimensionless conventions.

With v0.39a's flow-incidence alias, each face-to-cell current is
`2(-D3[f,e]) x_f x_e` with all gates open. Their sum equals `d(x_e²)/ds=-4a sin(2s)cos(2s)`. Each face contributes one quarter of the total on this plane. Over the closed witness, each net current integral is zero. Integrating the magnitude of the total gives `4an`, the total variation of `x_e²` over the interval. That integral changes with the path but is invariant under kinematic reversal. It is measured here in coefficient stock, with the absolute value taken after summing the currents. No identification with signed O09 action is inferred. [Flow convention amendment](https://github.com/ud-tetra/UD-Physics/pull/462)

At fixed a, one and two turns return to the same state and have the same receipt mask while their Hodge integrals differ. Their elapsed times differ. At matched elapsed time, two different supports also give different integrals, with different initial preparations. Neither comparison supplies a matched, source-admitted Pachner relay.

## Q136 transport gate

The [historical transport equation](../g0506-transport-energy/README.md) implies
`Q136 = -log ∏_k (T_k/T0)` conditional on the same obstruction triple and unit step weights. A candidate directed weight is `T_k/T0=exp(-λ ∫_{γ_k}ϑ)`. It reproduces `λ∫ϑ` as a sum by construction. The source still needs to supply the directed transport ratio, its path measure, and the coefficient λ. The three historical terms remain unidentifiable from the single ratio. A bidirectional attenuation law with both ratios bounded by one and reciprocal weights forces both to one, so the signed exponential cannot implement nonzero bidirectional attenuation under that contract.

The discriminating next step is to obtain independently source-defined directed ratios for complete admitted segments. The paired test compares the independently computed ratios against the oriented integral on multiple support preparations under a fixed receipt mask, checks composition and reversal where both directions are admitted, and treats the zero net conservative flux as a control. Across interfaces, record any phase or jump contribution separately. Do not infer source admission from a synthetic mask, choose λ to force agreement with O09, or substitute published receipt timestamps for the authoritative event time.

## Replay

`python3 experiments/g05-all-pass-path/audit.py` (SymPy). The exact replay checks the boundary-generated rotation plane, the current identity, and symbolic integrals for one and two turns at two exact supports. G05 remains OPEN_CONSTITUTIVE_SOURCE. No O14 calibration or physical mapping is introduced.
