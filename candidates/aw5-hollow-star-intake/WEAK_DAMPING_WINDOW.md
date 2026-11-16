# AW5 weak damping and finite observation window

**DERIVED / EXACT CONDITIONAL.** Native unit simplex metric, undamped skew generator A, uniform exterior-face damping Gγ = A − γP, and collocated unit-norm face impulse/readout q. Physical mapping OPEN. **Physical Promotion = 0.** The qualitative cavity target was exposed before analysis. No parameters were fitted. The damping and readout are declared model choices.

## Pole migration

Remove the degree-zero constant vertex mode by taking its orthogonal complement. This restriction is invariant under A and P and contains the face readouts. On it the hollow A has a simple zero eigenvalue with normalized eigenvector u = h/√3. For sufficiently small real γ, the isolated eigenvalue λ(γ) and spectral projector E(γ) are analytic. Differentiating the eigenvalue equation at zero gives λ′(0) = −uᵀPu = −1/4. Reality and simplicity make the continued eigenvalue real. The identity Gγᵀ = −G₋γ gives λ(−γ) = −λ(γ) and E(−γ) = E(γ)ᵀ. Hence the pole and its collocated residue satisfy

$$\lambda(\gamma)=-\gamma/4+O(\gamma^3),\qquad q^TE(\gamma)q=1/4+O(\gamma^2)$$

for q = Pu/||Pu||. The orthogonal exterior control has zero residue at γ = 0 and at most O(γ²) residue from this pole near zero. These are local asymptotic statements. The window result below uses a separate nonasymptotic estimate.

## Guaranteed time-average contrast

Define the signed time average Mγ(T) = (1/T) ∫₀ᵀ qᵀexp(t Gγ)q dt. In the undamped model the collocated response is a stationary term plus real cosines with nonnegative weights summing to at most one. The exact characteristic polynomials give every positive frequency greater than one for both carriers. Integrating the cosines bounds the error from the stationary term by 1/T.

Both damped and undamped propagators are contractions for γ ≥ 0. Duhamel's identity gives ||exp(t Gγ) − exp(t A)|| ≤ γt, so |Mγ(T) − M₀(T)| ≤ γT/2. Apply the bounds to the aligned hollow response and to either control, namely the same spatial pattern on the filled star or an orthogonal unit exterior pattern on the hollow star. For each control one obtains

$$M_{\rm hollow,aligned}(T)-M_{\rm control}(T)\ge 1/4-2/T-\gamma T.$$

The estimate also holds if the two damping strengths differ and γ is an upper bound on both. Choosing T = 32 and 0 ≤ γ ≤ 1/512 yields contrast at least 1/8 in native units. This is a sufficient window under the declared model. It neither assumes asymptotic pole dominance at T = 32 nor specifies a calibrated physical time or noise floor.

## Run footer

- **Mission** — Determine whether the hollow-star impulse signature remains distinguishable over a finite window under exterior damping.
- **Done** — Derived the pole displacement and residue order, and bounded the signed time-average against each control.
- **Finding** — The pole moves initially at slope −1/4 with respect to damping. The controlled contrast is at least 1/8 for T = 32 and γ ≤ 1/512.
- **Bridge value** — The result supplies a finite-duration mathematical test with explicit nuisance bounds. Instrument response and calibrated mapping remain open.

## Next step

1. **Priority 90/100** — Derive a contrast guarantee with discrete sampling, independent readout noise, and bounded channel mismatch. This converts the continuous-time prediction into a testable acquisition specification.
