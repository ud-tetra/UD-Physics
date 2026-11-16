# Adaptive AW5 resolvent enclosure at depths six and seven

**EXACT** overlap bound and static residue. **NUMERICAL / CONDITIONAL** finite-window enclosures and a Gaussian counterexample within the declared noise model. **Physical Promotion = 0.** Constructor verification. No hardware evidence or fitted parameters.

The calculation keeps the original 256 midpoint times, probe maps and 3/64 gate. It adapts the Fourier cutoff used to evaluate the same sample means. This avoids changing the measurement grid to get a stronger bound. The [prior recursion](RECURSIVE_FREQUENCY_RESPONSE.md) supplies the 14-coordinate leaf transfer, the 16-face AW5 resolvent, the arithmetic residual model, and the acquisition budgets.

## Sharper operator and inversion bounds

Local Schur backward corrections lift into the full chain space with support on their local graded skeleton. If at most m embedded skeletons in a level contain any one coordinate, then their aggregate correction satisfies

    ||sum_j E_jᵀ D_j E_j||₂ ≤ m max_j ||D_j||₂.

Cauchy–Schwarz on the sum of the bilinear forms gives the inequality since sum_j E_jᵀ E_j ⪯ mI. Each original AW5 vertex starts in at most three leaves. A pre-existing vertex lies in three children per containing tetrahedron at each split. A vertex inserted at a later level starts in four children of its parent. Hence after r stellar levels any vertex is in at most 3^(r+1) cells. Every higher-degree simplex is contained in no more cells than any vertex of that simplex. This bounds the overlap of embedded skeletons. The depth-zero child elimination error has face-face support only: the bare boundary block is exact at the represented frequency and the only new term is the signed face outer product divided by s. A face belongs to at most two terminal tetrahedra, so that error receives multiplier two on the full AW5 assembly. The remaining Schur and assembly corrections use the geometric vertex multiplicity, with the final 42-coordinate and 16-face assembly error added separately.

For frequency s=α+iω, bound the smallest singular value of the unperturbed shifted operator below by max(α, |ω|−||G||₂). Use this bound in both the full-operator perturbation and final solve residual denominators, with an outward allowance for the represented frequency. This discounts high-frequency numerical residuals where the full resolvent is small. All local correction bounds remain smaller than α for the lifted Schur identity. The same incidence counting as before gives ||G||₂<95 at depth seven, since max(2[6+2(3^7−1)],3[6+4(2^7−1)],8)<94². The depth-six cap 56 and filled cap 8 are applied separately. The face probe derivative bound carries to depth seven because the twelve original exterior faces are unchanged and each meets a distinct terminal tetrahedron.

Accumulate modes in batches to K=4096, 8192 and 16384. Use the depth-seven norm cap in the rational high-frequency remainder. The common radius includes the tail, periodic aliasing, and a scalar summation reserve of 3·10⁻⁹(2K+1)·33/256+10⁻⁶. Intersect each new interval for each arm and damping endpoint with previous intervals. Stop once the upward-rounded common radius is at most 1/10000. At K=16384 that radius is 0.000063 per arm. The maximum weighted resolvent allowance across all arms and endpoints is below 0.000891. The proof uses normal binary64 arithmetic and the inherited dot-product envelope. Shallow full-matrix checks are constructor checks.

## Results

| Uniform depth | Budgeted lower vs. filled | Budgeted lower vs. fixed reference | Undamped fixed-reference interval |
| ---: | ---: | ---: | ---: |
| 6 | 0.179859 | **0.060216** | [0.122407, 0.123535] |
| 7 | 0.179187 | **0.020637** | [0.082828, 0.086642] |

The depth-six certified headroom increases from 0.000240 to 0.013341. Depth seven clears the gate on the undamped finite window against both controls. The filled-control clearance follows even after the full loss budget, since the budget includes the undamped endpoint. Its stationary residue is 64/2315, obtained from 1/[2(1+(3/2)^7)]. The depth-seven sampled clearance in the ideal model therefore depends on the nonstationary part of the response. The calculation makes no attribution to specific modes.

### The original uniform probability guarantee fails at depth seven

Choose target damping 1/512 and fixed-reference damping zero. Set both target drive and sensor gains to 1−1/512 and both fixed-reference gains to 1+1/512. Take target mean bias −1/256 and fixed-reference bias +1/256. Set timing and operator mismatch to zero. These choices lie within the declared tolerances. Use independent Gaussian sample noise of standard deviation 1/16 in each arm, which obeys the declared sub-Gaussian bound.

The damped endpoint enclosures with the gain and bias values bound the mean gap above by 0.074377. The noise standard deviation of the difference of means is √2/256, and the replay proves that the margin of the upper bound above 3/64 is less than five of these standard deviations. Thus the probability of failing this one comparison is greater than the one-sided standard-normal tail at five. Integration by parts gives the Mills lower bound Q(5) ≥ (5/26) exp(−25/2)/√(2π) > 2 exp(−16). The strict comparison follows from exp(7/2)>32 and √(2π)<13/5, checked with rational bounds. Failure of either comparison fails the gate, so this is a witness against a uniform depth-seven pass at the original probability level.

One sufficient alternative keeps the same window and deterministic allowances while using an independent sub-Gaussian noise proxy σ≤1/128. It replaces the adverse noise allowance 1/32 by 1/256 at exponent 16, yielding a conservative overall floor **0.047980**. This is a theoretical sufficient condition and has no measured calibration evidence.

Replay with `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 adaptive_dtn_enclosure.py`. The archived depth 4–6 replay is unchanged by the new option. Next discriminant: derive a sharper deterministic or noise budget by identifying the spectral weight contributing to the fixed-reference contrast, then test that budget against independent bench evidence.
