# AW5 finite-window certificate for all 16 first-level refinements

**EXACT / CONDITIONAL** finite-model bound with rational enclosures, and **PROBABILISTIC / CONDITIONAL** noise allowances. **Physical Promotion = 0.**

## Carriers and fixed probes

Start with the four-leaf hollow AW5 and replace each selected original leaf by its four stellar children, once, at vertex 8+i for leaf i. This gives 16 labeled subsets, grouped by 0 to 4 replacements. The real graded chain space uses ascending simplex orientations, unit simplex weights and signed A=Bᵀ−B. All twelve exterior probe faces are preserved. The reference carrier is the original filled AW5.

Use the original sign pattern q and fixed reference p=(e₀₁₆+e₀₁₇)/√2 from the [one-leaf certificate](REFINED_WINDOW_CERTIFICATE.md). Each contrast subtracts either the filled mean using q, or the same hollow carrier’s mean using p, from the hollow average using q. These probes and T=32, N=256 and gate 3/64 were known before this analysis. There is no fitted parameter or measured target.

The hollow q residue is (20−m)/80 for m refined leaves. When exactly one of leaves 0136 and 0127 is refined, the fixed reference p loses exact orthogonality. Its residue is 1/[120(20−m)] in that case and zero otherwise. The two signed harmonic face coefficients then have magnitudes 1/4 and 1/5, with opposite signs, and the shell-normalized harmonic norm squared is 3(20−m)/20. Exact signed incidence checks recover both formulas and the graded nullity of two in all 16 carriers. The largest fixed-reference leakage is 1/2040. The finite-window calculation includes the actual reference for every subset.

## Rigorous midpoint mean enclosure

Compute the undamped signed mean of qᵀ exp(tA)q/||q||² on t=(2k+1)/16, k=0,…,255. Use nonnormalized integer representatives of q and p and divide by their squared norms. The replay uses scale S=2⁸⁰ and a degree-24 Taylor polynomial for one half-step 1/16 and 255 full steps 1/8. Within each polynomial form term k by multiplying the preceding term by A and dividing by the step denominator times k, with componentwise floor on the 1/S grid. Accumulate the signed means with integers.

For either step size, a=||A||₂Δ≤3/2, by the exact row/column norm bound 12. Dimension ≤102 gives per-term rounding error at most 11/S in Euclidean norm. A floor error introduced in term k contributes to later term j with multiplier at most a^(j−k) k!/j!, which is bounded by a^(j−k)/(j−k)!. All of its contributions to the summed polynomial therefore cost at most e^a·11/S < 55/S. The exponential tail in operator norm is at most a²⁵/[25!·(1−a/26)] at a=3/2. The exact undamped state norm is less than 4, and enclosing it within one unit bounds the recurrence input norm by 5. Each update then costs at most five times the tail plus 24·55/S. Contraction of the exact skew flow and the rational test of 256 times this bound prove an error below 1/10¹² per arm. Since each integer probe norm is at least one, this also encloses the normalized signed mean. This is an integer calculation with a proven truncation and rounding allowance. Decimal results below are display values.

## Conditional measured contrast

Apply the same tolerances as the one-leaf certificate. The pairwise deductions from the enclosed undamped sample means are:

- Exterior damping ≤1/512 costs at most 1/16 by Duhamel on the midpoint grid.
- Timing jitter ≤1/1024 costs at most 9/2048. Replay verifies each ideal damped probe derivative bound ≤9/4 from its exact Aq norm squared and the orthogonal face damping term.
- Dissipative realized operators with norm error ≤1/4096, drive and sensor errors ≤1/512 each, and mean bias ≤1/256 per trace cost at most 49169/2097152 per comparison, including jittered times.
- Independent centered sub-Gaussian sample errors with proxy σ≤1/16 authorize an adverse allowance 1/32 at joint failure probability ≤2 exp(−16) for both comparisons in a selected carrier run.

| Refined leaves | Labeled subsets | Minimum gap vs. filled | Minimum gap vs. fixed reference |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 0.1228598499 | 0.1305335946 |
| 1 | 4 | 0.1110037855 | 0.1228849923 |
| 2 | 6 | 0.0991477211 | 0.1111364517 |
| 3 | 4 | 0.0872916566 | 0.0979944538 |
| 4 | 1 | 0.0754355922 | 0.0837986590 |

The uniform rational lower bound is 4274814147512619692820270848855671/56668397794435742564352000000000000. An outward-rounded statement is **contrast ≥7/100** against both controls. The worst certified headroom above 3/64 is about 0.02856. The old negative four-leaf bound used a generic oscillation allowance. Evaluating the signed means on the actual grid removes that loss. 

### Correlated-noise sensitivity

As a theoretical variant, assume the concatenated noise vector has a centered joint sub-Gaussian moment-generating bound with proxy matrix Σ satisfying Σ ⪯ (361/100)(1/16)² I. For each difference of means the weight vector's squared norm is 2/256, so the scalar variance proxy is at most (361/100) times the independent bound. Increasing the adverse allowance from 1/32 to 19/320 retains exponent 16. The uniform contrast floor then remains about 0.0473105922, still above 3/64. This uses a bound on the joint moment-generating function. A sample covariance estimate supplies different information. The existing scorer's independent-noise declaration is still the protocol for scoring.

## Deeper uniform refinements

The same rational-enclosure method, using degree 48 and the row-sum bound of each generator, also certifies the undamped midpoint means for uniform depths two and three. The exact probe derivative check remains valid. The budgeted minimum subtracts the same allowances.

| Uniform depth | Graded coordinates | Undamped gap vs. filled | Undamped gap vs. fixed reference | Budgeted minimum |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 326 | 0.1778983989 | 0.1772682427 | 0.0556781053 |
| 3 | 1222 | 0.1143683970 | 0.1187691267 | −0.0072217405 |

Depth two clears 3/64 with the generic damping deduction. At depth three that deduction supplies no pass guarantee, so we enclose the damped flow more directly. See [the static depth law](RECURSIVE_LEAF_RESIDUE.md) for the separate stationary result.

### Direct damped enclosure at uniform depth three

Use the same fixed-point series to enclose each arm’s mean at γ=0 and γ=1/512. At the second endpoint we use the integer numerator 512A−P and a factor of 512 in the step denominator. The induced norm is bounded by the maximum undamped row sum plus γ. Contractivity follows from the symmetric part −γP, and the same rational truncation and rounding argument applies.

For a unit probe q, the second derivative of qᵀexp(t(A−γP))q with respect to γ is bounded in absolute value by t². Twice differentiating gives twice a time-ordered integral over a simplex of area t²/2; every intervening propagator is contractive and ||P||₂≤1. The mean second derivative is bounded by the midpoint mean of t², which is at most T²/3. Linear interpolation between the two damping endpoints therefore encloses each arm with an additional error at most γ_max² T²/24. The combined interpolation allowance is 1/3072. Comparing the smaller target endpoint with the larger endpoint of each control gives a uniform result for each arm’s damping chosen independently in [0,1/512].

After subtracting two arithmetic allowances, 1/3072 for interpolation, and the original timing, mismatch, offset and noise allowances, the depth-three floors are **0.0543102417 versus the filled carrier** and **0.0587109715 versus the fixed reference**. Both clear 3/64 under the same conditional noise guarantee. The undamped table above records the looser calculation as a diagnostic control.

## Replay and next discriminant

Run `PYTHONDONTWRITEBYTECODE=1 python3 check_refinement_sweep.py` with SymPy 1.14. The replay verifies all labeled subsets with exact signed integer propagation and rational comparisons. The fixed reference was frozen in prior work. Run `PYTHONDONTWRITEBYTECODE=1 python3 check_deep_uniform_window.py` for the two deeper uniform cases. The first-level result covers every subset. Run `PYTHONDONTWRITEBYTECODE=1 python3 check_damped_depth_three.py` for the improved damping bound. The deeper calculations cover equal depths.

**Next step.** Use the four-terminal structure to reduce the frequency-dependent response and extend the certified midpoint test beyond uniform depth three.
