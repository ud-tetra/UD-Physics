# Recursive AW5 boundary resolvent and depth 4–6 window

**EXACT** Schur identity and recursive gluing. **NUMERICAL / CONDITIONAL** midpoint bounds with analytical tail, damping and arithmetic allowances. **Physical Promotion = 0.** No fit or measured parameters were used. This extends the [prior depth certificate](REFINEMENT_SWEEP_WINDOW_CERTIFICATE.md) on the same unit simplex metric, signed ascending bases, probes and 256 midpoint grid.

## Grade-aware boundary recursion

Use s in the open right half-plane and K_d(s)=sI−A_d. Let H_d be its Schur complement onto the original tetrahedral boundary ∂, consisting of four vertices, six edges and four faces. Retaining shared lower-degree coordinates makes the recursion composable. Eliminating them separately inside each four-face leaf would remove coordinates that are shared at the next gluing.

Write K_∂(s)=sI−A_∂ for the bare boundary block. For depth zero,

    H_0(s) = K_∂(s) + w wᵀ/s,

where w is the signed top boundary column, padded with zero vertex and edge entries. The four children have a shared 25-coordinate skeleton S. Let E_i restrict skeleton coordinates to child i in its inherited ascending orientation. Then

    M_d(s) = sI_S − A_S + Σ_i E_iᵀ [H_d(s)−K_∂(s)] E_i
    H_(d+1)(s) = Schur_∂ M_d(s).

The subtraction removes the child boundary block before scattering. Each shared incidence and each s term therefore occurs exactly once. Child interior elimination is independent across children and Schur elimination is associative. With a different orientation convention, include the appropriate diagonal signs in E_i. Every eliminated block is invertible for Re(s)>0 by accretivity of sI−A, and the identity also extends as a rational transfer where defined.

For hollow AW5, glue four H_d blocks the same way on the 42-coordinate shared boundary skeleton. Eliminate its vertices and edges once, leaving the requested 16-face block S_F(s). With exterior face mask P and exterior damping γ, the scalar collocated transfer is

    F_q(s;γ) = qᵀ [S_F(s)+γP]⁻¹ q / (qᵀq).

The final solve is 16 by 16, after the 42-coordinate AW5 assembly. Each recursive leaf assembly uses 25 coordinates and returns 14. The main depth 4–6 replay builds no full refined chain complex. Full matrices are built for the original filled reference and to cross-check the shallow reduction at depths 0–2.

## Finite-window enclosure

Let g(t) be the normalized signed response from G=A−γP. Probes have exterior support. Subtract 1−γt from g(t). Its Laplace transform is R(s)=F_q(s)−1/s+γ/s². Its weighted causal periodic copy with period L=256 and weight exp(−t/16) has Fourier coefficients R(α+iω_k)/L, where α=1/16 and ω_k=2πk/L. Fourier inversion on the original time grid uses indices |k|≤8192. The elementary geometric midpoint weights are computed by an order-40 exponential recurrence. Add back the exact mean 1−16γ.

**Tail.** For a unit q, the resolvent expansion gives R(s)=qᵀ G(sI−G)⁻¹Gq/s². On the fixed probes both ||Gq|| and ||Gᵀq|| are at most 9/4. Indeed, the exterior face-to-edge part is fixed, and at depths ≥1 each exterior face meets a distinct top cell, so the top part has unchanged norm. The shallow exact derivative bounds apply. For d≤6 the vertex incidence count is bounded by 6+2(3^d−1), the edge-to-face count by 6+4(2^d−1), and at most two tetrahedra meet a face. Under a stellar split an existing vertex’s tetrahedron multiplicity triples and an existing edge’s doubles. At each step one new edge or face is incident per enclosing old tetrahedron. Interior births have vertex degree and top-cell multiplicity 4, or edge-to-face degree and top-cell multiplicity 3, which fit those bounds. Since B²=0, ||A|| equals the maximum norm of the graded boundaries, giving ||G||<56. For |k|>K=8192, use

    |R(s_k)| ≤ (81/16)/[|ω_k|²(|ω_k|−56)].

Bounding the sum of k⁻³ by 1/(2K²) gives an omitted weighted tail at most exp(2)(81/16)L² / [(2π)³ K²(1−56L/(2πK))].

**Alias and scalar arithmetic.** Contractivity gives |g(t)−1+γt|≤2+γt. For aliases t+jL, the sum is bounded by the geometric sums with ratio exp(−16)<1/8000000. The replay bounds Machin’s formula for π, the above tail and the alias sum by rationals. It reserves 1/100000 per arm for scalar weighting and summation, included in the common radius 1/4000. For the scalar weight calculation the reduced Taylor arguments have modulus <4, and the order-40 truncation is bounded by 4⁴¹/[41!(1−4/42)]. With unit roundoff u=2⁻⁵³, the elementary complex multiply, division by a real integer and addition recurrence has a conservative γ₅₀₀=500u/(1−500u) envelope times exp(4)<55. Including the phase argument error gives <4×10⁻¹² per exponential. The geometric denominator has modulus ≥1/128, giving <3×10⁻⁹ per undoubled weight. Since |R(s)|≤33, the resulting sum error plus ordinary scalar arithmetic is below the reserved 1/100000.

**Local backward error.** This item is additional to the common radius. For a local Schur calculation with blocks (A,B;C,D), use the computed solve Z and Schur S. Its exact corrections are δC=DZ−C and δA=S−(A−BZ). Both live on the retained skeleton of that assembly and make its approximate Schur value exact for the perturbed matrix. Bound these corrections from the computed residual and dot-product rounding. The script uses 128(n+1)u times the summed absolute-product envelope at block width n, and multiplies by the skeleton dimension to bound the induced norm. This covers the real operations in complex dot products, subtraction, absolute-value evaluation and their rounding under IEEE binary64 in the finite normal range. Child corrections lift without norm growth. For repeated children their bounds add with multiplicity four. The code also charges the rounded boundary increment, scatter additions and the represented frequency. This produces a full-operator perturbation bound δ at each frequency even though the full operator is never stored. Check δ<α. Perturbing a dissipative resolvent costs at most δ/[α(α−δ)]. The final solve residual has support only on the face ports and costs its normalized norm divided by α−δ. No accuracy assumption about the linear solver is needed beyond the checked residual and the stated arithmetic model.

**Damping and acquisition.** For each arm independently use the minimum or maximum of its enclosed γ=0 and γ=1/512 endpoint means. The linear interpolation allowance across a contrast is 1/3072 by the previous t² second-derivative bound. Subtract 9/2048 for jitter, 49169/2097152 for operator/channel mismatch and mean bias, and 1/32 for adverse independent sub-Gaussian noise. The last term gives joint failure probability ≤2 exp(−16) for both comparisons in a selected carrier run, under the declared noise assumptions.

## Results

| Uniform depth | Lower bound vs. filled | Lower bound vs. fixed reference | Headroom above 3/64 |
| ---: | ---: | ---: | ---: |
| 4 | 0.052667 | 0.055295 | 0.005792 |
| 5 | 0.177999 | 0.109238 | 0.062363 |
| 6 | 0.173116 | 0.047115 | 0.000240 |

Lower bounds are rounded downward at six decimal places. The window result is conditional on carrier, readout, tolerances, binary64 arithmetic assumptions and declared noise. At depth six the *stationary* residue 32/793 is below 3/64, while the *sampled finite-window* contrast still clears it under this enclosure. The depth-six worst control is the fixed two-face readout, and its certified margin is narrow. The undamped harmonic mode has exterior overlap under these unit weights. For uniform depth d, the first derivative of its observable zero pole under exterior damping is −R_d; treating that mode as exactly undamped would change the model.

Run `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 recursive_dtn.py` with NumPy and SymPy. The constructor replay checks agreement with the full shallow matrices at four frequencies and both damping endpoints. This completes the declared fixed-window computation through depth six. An independent check and the measured bench gate remain open.
