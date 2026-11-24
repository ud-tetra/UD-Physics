# 85D native-incidence normalized gate screen v0.1

**EXACT mathematical obstruction and activation classification / NUMERICAL exploratory 85D replay. No physical promotion.**

## Source pins
- UD-Physics main `80525f1296a15f4a87f0efecc491679deec39b9b`, `experiments/four-cell-tetrahedron/README.md` v1.0, blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e`, sections *Definition and scope* and *Exact sharing, geometry and recursive counts*.
- `experiments/pachner-local-jump-current/README.md` v0.1, blob `047db9ebafb0192fcf7bc72bf43506a3dee2c2ec`, sections *Exact Hasse cut* and *Interior-sensitive guard observable*.
- User-reported four parameter-free rational gates are original scratch **candidate definitions**, not verified source-derived constitutive laws. PR #483 head `51e259ac32614327f673d5c00a5c2d59b2397475` is an open draft; its zero-state analysis is not an accepted theorem.

## The exact coefficient selection no-go
For `g:R²\{0}→R` with `g(tz)=g(z)` for all `t>0`, continuity of the *coefficient* at the origin implies `g(z)=lim_{t→0}g(tz)=g(0)`; hence g is constant. Unit normalization at equal support selects `g≡1`. Nonconstant scale-independent ratio gates cannot all be continuous at their empty two-port state. This does NOT rule out a continuous or locally Lipschitz **vector field** `g(z)Jz` because the pair vanishes at the origin.

A face/top incidence connects distinct grades `C2` and `C3`; simplicial automorphisms preserve grade, so swapping the two coordinates is not an automatic symmetry requirement. Signed orientation covariance and typed donor/recipient selection remain distinct. Comparing `x²` and `y²` between grades relies on the declared unit coefficient metric, not a derived Whitney/physical normalization.

## Full computational model
Two centroid refinement generations of the initial tetra produce `f=(9,26,34,16)`, hence 85 chain coordinates. Build all signed oriented incidence matrices `B1:9×26`, `B2:26×34`, `B3:34×16`. Exact integer `B1B2=B2B3=0`, ranks `(8,18,16)`. The prescribed complex is *already present*; this calculation does NOT perform the 29→85 geometry-creation event.

Take formal `s∈[0,2]`, unit quadratic stock `S=||c||²`, the all-grade skew incidence flow, and replace each face/top incidence coefficient independently by `g(f_i,q_j)`; all other incidences retain unit weights. The four candidate rules:
- null `g=1`;
- lower `g=2f_i²/(f_i²+q_j²)`;
- higher `g=2q_j²/(f_i²+q_j²)`;
- overlap `g=4f_i²q_j²/(f_i²+q_j²)²`.
Assign `g(0,0)=1`: it does not affect the paired current. Each resulting vector field is an incidence-sparse sum of pointwise skew transfers and conserves S exactly. All quantities are formal, dimensionless and measured under the chosen unit simplex metric.

Seed four exterior *coherently ambient-oriented* top amplitudes as +1, twelve interior tops as zero, all faces/edges/vertices as zero. Signed ascending-basis top amplitudes are adjusted using tetra geometric determinant signs. Total initial S=4. This orientation control is essential for the correct symmetric null.

## Exact activation controls
- Lower weighting: all initial faces are zero and every face-top current vanishes. Full initial state is stationary.
- Overlap weighting: vanishes if either port is empty; full initial state is stationary.
- Higher weighting: exterior top→face transfer occurs, but `g(f,0)=0`; zero interior top-coordinate hyperplanes remain invariant. Therefore interior top amplitudes remain zero at every finite time for the stated deterministic locally Lipschitz state flow.
- Uniform null: nonzero interior top stock develops through ordinary incidence; this is the native unmasked baseline and obeys the earlier exact bound `S_internal/S_initial ≤4/7` for the symmetric face/top-only trajectory. All-grade lower coordinates remain zero in this particular symmetric null because `B2 B3=0`.

The three nonuniform laws thus fail the specific *empty interior top activation* requirement irrespective of their arbitrary equal-support normalization. Their lack of coefficient continuity at zero does not by itself make the pair-rotational vector fields ill-posed: angular-ratio times a vanishing pair has a locally Lipschitz continuous extension in this finite construction.

## Numerical exploratory replay
SciPy DOP853 `rtol=2×10⁻¹¹, atol=10⁻¹²`, observation times `0,1/2,1,2` on the same full 85D carrier and fixed initial vector. For the null, matrix-exponential `exp(2A)c_0` provides independent integration control. All four maintain quadratic stock within `2×10⁻¹⁰` at the sampled times.

| Rule | Interior top S at s=1 | Face S at s=1 | E_G at s=1 | Interior top S at s=2 | Face S at s=2 | E_G at s=2 |
|---|---:|---:|---:|---:|---:|---:|
| null | 1.246483 | 2.332409 | 16.000000 | 0.504054 | 3.385450 | 16.000000 |
| lower | 0 | 0 | 16 | 0 | 0 | 16 |
| higher | 0 | 3.970222 | 18.977667 | 0 | 3.994678 | 18.996009 |
| overlap | 0 | 0 | 16 | 0 | 0 | 16 |

`E_G=||B3q||²+||B3ᵀf||²` is the *fixed-generator* weighted quantity; it is not forced conserved by nonlinear skew gates. The synthetic all-16 top amplitudes of common oriented magnitude 1/2 provide an equal-stock **diagnostic** only. They are not a sourced 29→85 endpoint or the original 13a²→4a² pair. Do not infer target achievement from a smaller synthetic distance if the required interior activation remains zero.

## Model-selection outcome
**NO-GO_SCOPED:** Locality, grade-typed structure, unit equal-support normalization, scale invariance and total quadratic conservation do not yield a nonconstant continuous gate coefficient; requiring only regularity of the vector field leaves many candidate gates and does not uniquely select any. These three normalized nonuniform gates fail the exterior-only interior-funding test; no statement excludes other laws, pre-event receipts, different initial states, nonunit metrics or new incidence contacts.

**OPEN:** Source-derived coefficient law; initial event trigger; autonomous 29→85 transition; reachability of the historical candidate endpoint; independent performance advantage; physical correspondence. The 23-entry spectral catalogue remains SOURCE_BLOCKED and nuclear/fission interpretations remain quarantined. Physical Promotion = 0.

## Reproduction and capture
Local reproducible archive `UD_85D_LOCAL_GATES_v0.1.zip`, SHA256 `2ce33cf3fe68eb8b6153e0cda8cd57aade5648c8f7f957130c17d83d93056bd5`, includes `verify.py, results.json, verify.log, REPORT.md, MANIFEST.json`. Local constructor replay PASS; independent science review and GitHub fresh checkout replay NOT_RUN.
