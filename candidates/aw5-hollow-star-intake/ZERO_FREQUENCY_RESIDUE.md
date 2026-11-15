# AW5 zero-frequency face readout

**EXACT / CONDITIONAL.** Native dimensionless flow parameter, signed simplex incidence, unit simplex metric, linear collocated source and sensor. Agile physical hypothesis. **Physical Promotion = 0.**

## Model and controls

For unit-norm face-only q use the driven linear model x' = Ax + q u, y = qᵀx and transfer H(s) = qᵀ(sI − A)⁻¹q. Here s is the complex Laplace variable. The 46-dimensional hollow model uses the native glued generator. Its degree-2 null vector is h = z − DDᵀz/4 with hᵀh = 3. The filled control has only a degree-zero null mode and uses the same face coordinates. No material, scale, SI mapping, or coupling constant is inferred. The qualitative flux proposal was exposed before replay and no fitting was used.

Because A is real skew, the zero eigenvalue is semisimple and the coefficient of 1/s is qᵀΠ₀q. For face-only q this is (qᵀh)²/3 in the hollow model and zero in the filled model.

| Unit-norm collocated readout | Filled | Hollow undamped | Hollow with exterior damping |
| --- | ---: | ---: | ---: |
| One exterior face | 0 | 1/48 | 0 |
| Exterior pattern aligned to h | 0 | 1/4 | 0 |
| Exterior pattern orthogonal to h | 0 | 0 | 0 |

The aligned choice q = P_ext h / ||P_ext h|| maximizes the residue over exterior unit vectors by Cauchy–Schwarz. It is a model-informed readout design. The three readouts provide distinct comparison and null controls.

For G = A − γP_ext with γ > 0, any Gx = 0 gives 0 = Re(x*Gx) = −γ||P_ext x||². Thus ker G = ker A ∩ ker P_ext. The same argument for Gᵀ gives the same kernel, so this kernel reduces G and the complementary block is invertible. The remaining vertex constant is invisible to face readout. The exact zero-frequency pole therefore disappears for every positive γ in the stated damping model. The replay checks γ = 1. Pole migration at nonzero damping remains open.

Replay with Python and SymPy 1.14 using `python3 candidates/aw5-hollow-star-intake/residue.py`. Constructor check. Independent review OPEN.

## Run footer

- **Mission** — Determine whether a face-only source and readout distinguish a hollow star from its filled control.
- **Done** — Derived the zero-frequency residue and replayed exact filled, hollow, orthogonal and damped controls.
- **Finding** — The matched exterior readout has hollow residue 1/4. The filled and orthogonal controls give zero, and positive exterior damping removes the pole at the origin.
- **Bridge value** — The result specifies a model-level discriminator. A calibrated face readout and physical mapping remain open.

## Next step

1. **Priority 90/100** — Derive the weak-damping pole location and residue, then obtain a finite observation-time contrast bound. This tests whether the exact undamped discriminator survives finite bandwidth and damping.
