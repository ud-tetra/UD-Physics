# Passive-port attribution limit for the graphite candidate

**Status: EXACT / CONDITIONAL mathematical no-go; physical source and material loss OPEN.** This note follows the [graphite hypothesis](../graphite-superlubricity/README.md). The observed paired angles and near-zero load response were known before construction. The conventional triangular coincidence already gives `cos(theta)=13/14` and the `60°−theta` partner. This calculation asks what remains predictable **after** that angle geometry and an ordinary honeycomb/moiré baseline are fixed.

## Typed model and theorem

Use the archived seven-orbit cellular torus with real unit-edge metric. Its oriented boundary `B₁: R²¹→R¹⁴` and harmonic map `M: R²→R²¹` define seven source matrices `Kᵢ=MᵀPᵢB₁ᵀ: R¹⁴→R²`. The orbit projectors `Pᵢ` select the seven three-edge rotation orbits. For weights `w∈R⁷`, set `S(w)=ΣᵢwᵢKᵢ`. This proposed identification of an abstract source with graphite is **HYPOTHESIS**, not a material law. The original two-coordinate basis has positive metric `G=[[1,1/2],[1/2,1]]`; Cartesian normalization is an invertible change of basis. No physical time, force, pressure, or native-to-laboratory unit conversion is asserted.

The archived exact source computation gives

`S(w)S(w)ᵀ = α(w)G`, `α(w)=wᵀQw`, `rank(Q)=6`, and `ker Q=span{(1,…,1)}`.

Here `4Q` is the connected weighted graph Laplacian listed in the [source verifier](../../artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures/2026-10-22T214428Z-codex-graphite-harmonic-source-49d5bb28-64263b7c-7b88-4f45-a8a9-e0cb34f52956/verify_harmonic_source.py). Thus a uniform `w` has `S=0`; every nonuniform `w` has `α>0` and `rank S=2`.

Assume a low-frequency passive added channel `Γ_add=S L Sᵀ`, where the internal loss/compliance matrix `L` is any symmetric positive-semidefinite `14×14` matrix. The common eliminated-bath form `L=K⁻¹D K⁻¹` with positive definite stiffness `K` and `D⪰0` is included (`K=I`, `D=L` realizes every allowed `L` in the abstract model). For any nonuniform `w` and any symmetric positive-semidefinite target `T∈R²ˣ²`, define

`R=Sᵀ(SSᵀ)⁻¹` and `L=RTRᵀ`.

Then `SR=I₂`, `L⪰0`, and **`SLSᵀ=T` exactly**. Therefore, with unrestricted passive internal response, this UD source ansatz has no additional pointwise tensor, magnitude, or nonnegative scalar restriction beyond ordinary passivity. The result also holds after Cartesian normalization. If a C₃-invariant physical tensor is required, take `T=γI` in Cartesian coordinates; every `γ≥0` remains attainable. A group-averaged internal `L` can realize the same invariant tensor when the source and internal representation intertwine. This is an existence result, not evidence that any graphite material has the constructed bath.

For an interior positive `γ(P₀)>0`, choose a locally nonnegative `γ(P)=a+b(P−P₀)`; **any real local load slope `b`** is permitted by pointwise passivity if bath pressure dependence is free. At a smooth exact zero sustained by nonnegative `γ` on both sides of `P₀`, its derivative must vanish; this boundary calculus fact does not identify UD. A measured signed residual after subtracting a conventional baseline need not itself be positive semidefinite, because it is a difference of two passive responses. This theorem concerns a static/low-frequency response at each pressure, not unrestricted frequency functions or causal kernels.

The zero target can arise either from uniform weights (`S=0`) or from a nonuniform source whose bath has no loss in the coupled subspace (`L=0` is one witness). Thus near-zero friction does not determine the source weights. Conversely, uniform weights force **this added channel** to zero, not the total conventional friction.

## Exact constructor check

Run `python3 experiments/graphite-port-attribution/verify_port_universality.py`. It imports the immutable archived carrier and source verifiers, chooses `w=(0,1,−1,0,0,0,0)`, obtains `α=5/2`, `rank S=2`, and `SSᵀ=(5/2)G`, then checks exact rational reconstructions for zero, isotropic, anisotropic, and rank-one PSD targets. The factorization `L=RTRᵀ` proves positivity for all 14-dimensional vectors; the finite examples check assembly and arithmetic. [Captured output](../../artifacts/graphite-port-20261023-8f5ca436/exact-001/files/graphite-port-result.json) is a constructor check, not independent replication or a physical friction measurement.

## Revised test contract

1. Measure an independent two-dimensional interfacial PES, pressure dependence, contact geometry, force estimator, and loss spectrum. Hold those inputs fixed before examining paired-angle residual force data. A first-shell ideal static ratio is not a kinetic-force or load-slope datum.
2. Independently infer the source cross-Hessian or displacement-force map and its uncertainties. The seven-orbit `S(w)` span has dimension six in the eight-dimensional C₃-equivariant map space, as the [prior projection audit](../../artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures/2026-10-22T224639Z-codex-graphite-material-projection-fcd6e90e-4531aa0e-8487-4d43-b0dd-cfe246d1b6b4/MATERIAL_SOURCE_PROJECTION_AUDIT.md) found. A statistically resolved component outside that span rejects the **pure** source mapping; agreement is necessary, not sufficient, for physical identification. Its KC example had a 0.155176 normalized projection residual and did not supply an independent measured force map.
3. Fix `w`, stiffness, damping, pressure map, and any remaining conventional nuisance parameters using calibration data disjoint from the force/load test. Only then compute a signed residual and uncertainty band at both complementary angles. If the frozen mechanism predicts no quantitative band, report nonidentifiability. A signed difference from a conventional baseline needs its own covariance and sign convention.

No new signed friction or load prediction follows from the current port alone. The earlier paired-angle geometry, harmonic carrier, material projection shortfall, and unresolved empirical question retain their original scopes. Mainline physical promotion remains zero.
