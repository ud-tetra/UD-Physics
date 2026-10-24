# Locality test for a UD graphite angle-selection source

**Status: EXACT / CONDITIONAL incidence-source limitation; N-dependent material law OPEN.** The [quotient-family audit](../graphite-quotient-contrast/README.md) established that the two-dimensional harmonic edge carrier and uniform-source cancellation occur at seven, thirteen and nineteen moiré cells. This calculation asks whether a *single local, translation-covariant* weighted-incidence law distinguishes seven cells. It does not constrain a different UD operator, a registry-modulated material law, or boundary/contact dynamics.

## Typed setup

For a periodic honeycomb torus with `N` cells, let the vertex and oriented edge spaces be `V_N=R^N⊗R²` (A/B sublattices) and `E_N=R^N⊗R³` (three A-to-B bond directions). Use the unit Euclidean cell/edge metric. The normalized translation-zero vertex basis has one constant A and one constant B column, each `1/√N` per site. A normalized harmonic edge basis has columns `1/√N` times constant direction vectors in the plane `t₀+t₁+t₂=0`; an unnormalized basis for that plane is `h₁=(1,−1,0)`, `h₂=(1,1,−2)`. The fixed normalization of these two columns changes neither rank nor `N` dependence.

Define the proposed source `S_N=M_Nᵀ K_N B₁,Nᵀ`. `B₁,N` maps A-to-B edges to vertex divergence, `M_N` maps the harmonic edge subspace to a two-component readout, and `K_N:E_N→E_N` is a linear edge response. This is a **conditional candidate**, with no inferred graphite force units, native physical clock or material value for `K_N`.

## Same-stencil theorem

Assume `K_N` is assembled from the *same finite-range translation-covariant local stencil* for each quotient: `K_N=Σ_d T_d⊗K_d`, with local `3×3` matrices `K_d` that do not depend on `N`. The normalized zero-mode block is `K(0)=Σ_d K_d`, independent of quotient size. The zero-mode incidence block is also fixed: `B₁(0)ᵀ` sends the A/B uniform input to the three direction vector `(-a+b)(1,1,1)`. Hence

`S_N^(0)=Hᵀ K(0) (1,1,1) [-1,1]`,

where the columns of `H` span `t₀+t₁+t₂=0`, with an `N`-independent normalization. This matrix has rank at most one and is **independent of N**. Translation covariance also prevents nonzero Fourier sectors of a vertex input from mixing into the harmonic zero sector. In this source class, the same local stencil cannot activate an intrinsic seven-cell channel while cancelling the thirteen-cell channel.

If the stencil is C3-equivariant, the image `K(0)(1,1,1)` is itself a multiple of `(1,1,1)`, so `HᵀK(0)(1,1,1)=0`: **the port cancels for every N**. This includes equal bond weights. If bond directions have fixed unequal weights `W=diag(w₀,w₁,w₂)` the port may be nonzero, but it is the same rank-one zero-sector map at N=7, 13 and 19. With the illustrative, unfitted weights `(1,2,3)` and the displayed integer harmonic basis, it is exactly `[[1,−1],[3,−3]]` at each quotient. A single-site vertex force has a harmonic amplitude proportional to `N^(−1/2)` for the same weights; the seven/thirteen amplitude ratio is `√(13/7)≈1.36`, with neither response selected to vanish. This ratio is purely a unit-metric normalization, not a friction ratio.

**Scope of the theorem:** The fixed `K_d`, translation covariance, incidence-gradient input and the unit metric are essential. A registry-dependent `K_N(r)`, a contact edge, a symmetry-breaking preparation, a non-incidence lateral input, or an N-dependent constitutive law can evade the conclusion. Those changes need their own source law and a physical readout; naming a seven-cell phase after seeing the experimental angle would be a fit.

## Native-source check and next gate

The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` records `Q22`, the seam-sector pairing current-source coefficient, as zero and explicitly leaves nonuniform edge stiffness to be derived from current primitives. Its `Q77–Q84` phase kernels are conditional and leave branch-to-chain phase and apparatus context sourcing open. These are distinct typed objects; none supplies the graphite-specific edge stencil or a physical friction law. The supplied `packet_modulation_layer.md`, `triangular_transport_symbol_alphabet.md` and `seam_phase_transport.md` contain only placeholder text, so they provide no additional local rule. The latest inspected `ud-tetra/UD` default revision was `f22659b9fa9e9f3ab5ca34d7215ea53ebf2adc71`; the named packet-modulation capture there is likewise a placeholder. This is a bounded source check, not a declaration about every unpublished UD proposal.

The minimal constructive route is to define **one** local registry-to-edge response `K(registry,load,temperature)` from a source independent of the paired-angle force target, transport it over each moiré quotient with the same rule, and compute `S_N` at `(2,1)`, `(3,1)` and a third control. A predictive UD paper needs a common calibration, a conventional two-dimensional PES and force estimator, measured detection limits, and a held-out signed force/load contrast. A separately fitted `K_N` at each angle has no incremental angle-selection content. Physical promotion 0; independent physics review NOT_RUN.

Run `python3 experiments/graphite-locality-selection/replay_locality.py` for exact rational zero-mode projections on N=7/13/19. See the [immutable capture](../../artifacts/graphlocal-20261023-f8d5ab37/exact-001/manifest.json) and [mathematical receipt](../../candidates/graphite-locality-selection/mathematical_receipt.json).
