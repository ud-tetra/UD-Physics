# Registry modulation and the graphite harmonic port

**EXACT / CONDITIONAL.** This extends the [same-stencil locality limit](../graphite-locality-selection/README.md). The question is whether spatially variable edge weights alone produce a seven-cell response while respecting the rotational symmetry of a full periodic quotient. The answer for a uniform A/B vertex input is **no**. For a nonuniform input, the relevant quantity is the registry–source cross-correlation, so a physical angle-selection claim needs an independently specified source spectrum and material law.

## Typed quotient and local response

Let the connected periodic honeycomb have `N=m²+mn+n²` cells, cyclic representative `r∈Z/NZ` for the coprime examples `(m,n)=(2,1),(3,1),(3,2)`, and A-to-B edges `A_r→B_(r−s_t)` with `s=(0,m+n,n)`. Use unit Euclidean vertex/edge metric. The constant harmonic direction vectors are `h₁=(1,−1,0)` and `h₂=(1,1,−2)`. The harmonic output basis is `M_(r,t,a)=h_(t,a)/√N`; this fixed direction basis is orthogonal but not unit normalized. Divide the two columns by `√2` and `√6`, respectively, for an orthonormal output; all zero/nonzero and quotient-comparison statements survive that fixed change.

Let `W` be a local diagonal edge response `w_t(r)`, with no assigned force units, and let `x=(x_A(r),x_B(r))` be a vertex source. The proposed port is `F=Mᵀ W B₁ᵀx`, exactly

`F_a=N^(−1/2) Σ_(r,t) h_(t,a) w_t(r) [x_B(r−s_t)−x_A(r)]`.

This is a static linear projection, not a dissipation law or kinetic friction estimator. It preserves the previous A-to-B incidence sign convention. It does not establish that lateral sliding is represented by a vertex-gradient input.

## Mean-weight and symmetry theorem

For a normalized uniform input `x_A(r)=a/√N`, `x_B(r)=b/√N`, put `bar w_t=N^(−1)Σ_r w_t(r)`. Then

`F_a=(b−a) Σ_t h_(t,a) bar w_t`.

Thus all spatial variation disappears except the **three direction means**. If these means agree, the harmonic port is zero for **every** `N`, even with strong nonuniform registry weights. A global C3 action that cyclically permutes the three bond directions and preserves the complete edge set forces these means to agree. This strengthens the earlier statement that registry dependence can evade the same-stencil theorem: it can do so for the uniform input only if the direction means break the symmetry (or the full quotient, metric, preparation, or readout assumptions change). Local registry variation can still couple nonuniform sources.

For an A-site impulse `x_A(r)=δ_(r,r₀)` and `x_B=0`, `F_a=−N^(−1/2)Σ_t h_(t,a)w_t(r₀)`. A B-site impulse instead samples just the three incident edge weights: `F_a=N^(−1/2)Σ_t h_(t,a)w_t(r₀+s_t)`. There is no global seven-cell resonance in this purely local impulse formula. Different local registry values can change it, but that change must be supplied by a common material preparation law.

## Fourier sector selection

With `χ_k(r)=exp(2πikr/N)` and Fourier coefficients defined by `hat f(k)=N^(−1)Σ_r f(r)χ_(−k)(r)`, the exact finite-character identity is

`F_a=√N Σ_(t,k) h_(t,a) hat w_t(−k) [exp(−2πik s_t/N) hat x_B(k)−hat x_A(k)]`.

Only *matching opposite registry and source wavevectors* enter the harmonic output. This is a conditional kinematic selection mechanism; choosing `k` after seeing 21.8°/38.2° would be **FIT**, and the coefficient `hat w_t(−k)` is not supplied by UD here. Even a nonzero port is not evidence for a positive friction coefficient: dissipation, dynamics, load transfer and conventional subtraction are separate objects. The angle pair follows ordinary 60° honeycomb geometry; this calculation supplies no extra numerical angle or residual force prediction.

A deliberately engineered character example takes registry label `p=2` and source label `k=5`. Orthogonality permits their product to reach the zero sector when `N` divides `p+k=7`, so it matches at `N=7` and misses `N=13,19`. This is a **target-informed construction**, not a native selection rule: the characters `exp(2πikr/N)` have different physical wavelengths as `N` changes, and no common preparation or registry law has been identified that produces these labels in graphite.

## Exact replay and counterexamples

Run `python3 experiments/graphite-registry-convolution/replay_registry.py`. The script uses exact integer/Fraction arithmetic on N=7,13,19. Positive, spatially variable weights with equal direction means yield zero uniform B input in all three. A point A input gives the same `√N F=(-1,-1)` in all three; a signed zero-mean A input aligned with a local response perturbation yields `√N F=(-2,-2)`, whereas a disjoint translated input yields `(0,0)`. These are intentionally constructed counterexamples to the claim that registry variation *alone* picks N=7. They are not physical parameter fits. See the [immutable capture](../../artifacts/graphreg-20261024-7c09/exact-001/manifest.json) and [receipt](../../candidates/graphite-registry-convolution/mathematical_receipt.json).

## Material-source and measurement gate

The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` Q22 sets the seam-sector pairing current-source coefficient to zero and leaves nonuniform edge stiffness to be derived. Q77–Q84 are conditional phase kernels with physical context sourcing open. They do not specify `w_t(r;load,temperature)` or `x_A/B(r;sliding speed,load)`. The named packet-modulation/triangular-symbol/seam-transport attachments are placeholders. No native coefficient, physical clock, or force unit was imported.

The next useful construction must freeze one registry-to-edge response and one source-generation rule independently of the paired-angle data. Compute their cross-spectrum on `(2,1)`, `(3,1)` and a third control, then propagate it through a passive loss kernel and the same conventional two-dimensional PES/force estimator. Compare a held-out signed force and load slope with measured detection limits. Physical promotion 0; independent physics review NOT_RUN.
