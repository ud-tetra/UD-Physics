# Fixed local transport–clock coupling v0.1

**EXACT / CONDITIONAL.** An even Laplacian coupling shifts the internal phase relative to the decoupled clock, but gives identical global clock readings for the moving packet and its matched stationary-centroid reference. Tracking both lobes restores usable signal in the ideal replay.

## Source and model

Discovery parent 079f716f21e7a7f6cf411586f20252c34a2f5fa9. Retain the unit-metric periodic scalar lane and product clock of [Internal phase null v0.1](INTERNAL_PHASE_NULL.md) §§1–2. Historical ledger v0.39(2), Q169–Q170, supplies the skew incidence and its native stock context. It does not select a transport–clock interaction. Add the single fixed comparison generator

    K = A_scalar ⊗ Id + (2 Id + λ L) ⊗ J,
    L = −A_scalar²,  λ = 1/128.

Here L is symmetric positive semidefinite with incidence range two, and commutes with A_scalar. J is the internal real rotation on two coordinates. Thus K is skew on the product metric and preserves total stock. The added coupling, including its rational coefficient, is an explicit development choice with no fit or sourced physical value. Use native time and the same periodic boundary conditions. On the retained propagation eigenmode at k, L has eigenvalue ω(k)², so the circular channels evolve at carrier frequencies ω±(2+λω²). The phase shifts are deterministic spectral detuning in this candidate.

## Exact discrimination

For a moving spectrum f and its reflected spectrum f(−k), use the coherent equal-weight sum as the reference. The supports are disjoint for the admitted preparation. Since ω² is even, the normalized global two-channel contrast after removing the baseline exp(4is) is

    Σ_k |f(k)|² exp(2iλ ω(k)² s) / Σ_k |f(k)|²

for both the moving and reference states. Parseval gives this expression, and disjoint support removes the interference terms in the global sum. Equality holds even when the contrast loses magnitude. The phase is available wherever the contrast is nonzero. Its initial internal detuning is λ times the stock-weighted mean of ω², positive on this support. The equality extends to any even spectral shift on this same matched preparation. Corresponding reflected windows for the separately propagated lobes also give identical contrast by spatial reflection.

The standing reference has zero stock centroid but its constituent lobes propagate. This result separates net centroid motion from spectral detuning for the stated comparison. It cannot distinguish a shift that depends on the speed of each lobe from a shift that depends on its spectrum. That test needs a rest or different-speed comparator with the relevant local loading independently controlled.

## Numerical replay

On 97³ with launch width 9/50, sample s=0,4,8,12 for λ=0 and λ=1/128. Compute stock centroids separately for the two lobe launches, and apply the average of their Gaussian windows (width 6) to the coherent reference. This two-window spatial readout still admits interference. The global and reflected-lobe equalities pass the numerical checks at 10⁻¹² tolerance.

At s=12 the coupled global phase residual is approximately 0.38676 rad for both launches, with contrast 0.98023. The moving-window residual is 0.39222 rad and differs from the coherent reference's two-window residual by about 3.50×10⁻⁹ rad at that checkpoint. Window differences are preparation-dependent. The two-window reference collects about 26.85% of vertex stock versus 0.164% in the single centroid window. This is an ideal finite-grid readout, not a noise certificate.

Reproduce with NumPy and `python3 experiments/clock-matrix-question/laplacian_clock.py`. Non-constructor review NOT_RUN. Physical promotion 0.
