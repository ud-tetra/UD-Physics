# Projected non-affine shell coercivity in the original 3D UD surrogate

**RESULT: EXACT / CONDITIONAL** for the equilibrium-linearized 560-mechanical-phase passive model. **OPEN** for the entire nonlinear original-amplitude heart pulse.

**Question.** Can every allowed initial housing-phase perturbation be bounded in the 24-dimensional non-affine shell observable, for all time, without enumerating all 180 housing phase directions? Does this by itself certify the previous flat-cell exclusion criterion through u=100?

**Live provenance.** UD-Physics, main `79fd6d6cc8f2d40d516df0074e728e3f9428f60b`; full original ico/primary/port/mount/damping model source blobs match older integrated base `a4ae75dd55cd2b691c811c4d6eeae1367fcba015` exactly. Task `icosahedral-phasewindow-20261022`, held session `phasewindow-20261022-gpt6-7c41`, isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Separate PR44 forced-Green recovery remains held and untouched.

## 1. Typed geometry and actual linearized potential

Work with the original regular icosahedral reference shell `v_i in R^3`, 12 vertices and 30 graph edges of unit rest length, `R²=(5+sqrt(5))/8` and reference moment `sum_i v_i v_i^T=4R² I_3`; reference coordinate field `Q(sqrt(5))`. Let each physical shell and centre displacement be `delta X_i`, `delta C`, and let `Y_i=delta X_i-delta C`; there are 36 relative shell coordinates. The original scalar heart displacement is `alpha` (NOT physical time). To make all coefficients algebraic set `h=R² alpha`; the 37-vector is `q=(h,Y_1,...,Y_12) in R^37`. Linearized spoke strain is `s_i=(v_i·Y_i)/R²`, and original exterior edge strain is `e_ij=(v_i-v_j)·(Y_i-Y_j)`. Euclidean spatial metric +++; Newtonian time u=t/t0 is separate and uncalibrated.

At the qualified minimum `g_i=g_min=19/20`, `k_ij=k_min=19/50`, the primary quadratic potential is exactly

```
U_min,lin(q) = 1/2 [ (h/R²)^2 + sum_i s_i^2
       + (19/20) sum_i (s_i-h/R²)^2
       + (19/50) sum_(i,j) in Edges e_ij^2 ]
             = 1/2 q^T K_min q.
```

For every larger allowed spoke/edge stiffness, `K_actual-K_min` is a sum of nonnegative rank-one matrices, so `U_primary,lin>=U_min,lin`; added reciprocal port and housing-mount storage is also nonnegative. No strain prestress is present at the reference equilibrium alpha=0. Changing the scalar heart coordinate is merely an invertible normalization.

Define `P0=11^T/12`, `PV=VV^T/(4R²)` (here `V` is 12x3 with rows `v_i`), `P=I_12-P0-PV` and `Z=P Y in R^(12x3)`, with rank24. Its norm is `||Z||_F²=q^T W q`, `W=diag(0, P tensor I_3)`. These projectors are exactly orthogonal over `Q(sqrt5)`. The output is a kinematic non-affine observable, not the cell-volume signal.

## 2. Reproducible exact matrix certificate

Three linearly independent infinitesimal spatial rotations are `r_a=(0,(e_a cross v_i)_i)`, with `r_a·r_b=8R² delta_ab`. Let `P_rot=(sum_a r_a r_a^T)/(8R²)` on R37. Because all reference springs are unstressed, `K_min r_a=0`; because rotations are reference affine shell displacements, `W r_a=0`.

The checked 37x37 exact matrix is

```
M = K_min - (1/4) W + P_rot.
```

`exact_certificate.py` explicitly constructs every element in `Q(sqrt5)` from the 12 shell vertices, all 30 graph edges and the source elastic potential. It performs **exact unpivoted LDL^T factorization**, proves the sign of every algebraic pivot by exact rational comparisons of `p²` and `5q²` for `p+q sqrt(5)`, and verifies `M=L diag(D) L^T` entrywise without floating arithmetic. All 37 pivots are strictly positive, hence M is positive definite. No floating eigenvalue comparison enters this certificate.

For arbitrary q, project away its rotational component. On the orthogonal complement of the three rotations, `P_rot=0` and the matrix inequality reduces to `q^T(K_min-W/4)q>0` for any nonzero vector. On rotations, both forms vanish. It follows for every q that

```
K_min - (1/4) W >= 0,
U_primary,lin(q) >= (1/8) ||Z||_F².
```

The independent NumPy double-precision check gives `lambda_min(M)=0.13` (not a proof premise). Nine independent small-displacement trials through the prior full-model potential, with auxiliary and mount storage set to zero by their actual rest constraints, agree with `q^T K_min q/2` to a maximum relative ~1.43e-6, as expected from the cubic-and-higher Taylor terms. These are constructor checks, not independent mathematical peer review.

## 3. Entire housing-phase ball, all future time — linearized only

Linearize the **unchanged full** 280-configuration/560-phase passive mechanical system at the reference rest state (`alpha=0`). Fix all primary, scalar-heart and 150 auxiliary initial perturbations to zero; allow all 90 housing displacement and 90 housing velocity perturbations (all 180 initial phase coordinates), with the original positive mount/kinetic energy metric and total `E_h<=51/20000000` — the previously target-exposed enlarged design allowance.

The **linearized** mechanical energy `E_lin` is nonnegative; because every viscous path, auxiliary damper and ordinary dashpot is reciprocal/passive, `E_lin'(u)=-qdot^T C_eq qdot<=0` for `nu>=0`, `c_f>=0`. It retains all 560 mechanical coordinates and their rigid-momentum energy. The old homogeneity argument applies to all 180 housing phase directions, with no zero-momentum or symmetry preparation. For every `u>=0`:

```
(1/8) ||Z_housing,lin(u)||_F²
      <= U_primary,lin(u) <= E_lin(u) <= E_lin(0) <= E_h.
```

Therefore, **exactly**

```
||Z_housing,lin(u)||_F² <= 8 E_h <= 51/2500000
||Z_housing,lin(u)||_F <= sqrt(51/2500000) ≈ 0.0045166359163
                                            < 1/40 = 0.025.
```

This is a uniform, all-time and all-initial-phase equilibrium-linearized perturbation certificate across the continuous qualified stiffness box, not a finite numerical sweep. `m`, `beta`, housing weights and gains influence the positive initial energy and the passive evolution but not the coercivity constant. Lower bounds of the specified physical masses and positivity of device coefficients remain assumed. Parameter `nu` and `c_f` may be any nonnegative values (including their original target window and c_f=0).

### What is **not** proved

The actual heart-pulse nonlinear initial state has `alpha0=1/10`, not reference alpha=0, and may have asymmetric 3D properties. Its baseline non-affine response and the nonlinear difference between housing-perturbed and reference trajectories are **not** governed by this quadratic energy subtraction. Writing `Z_total,linear=Z_alpha,linear+Z_housing,linear` is valid for the *reference-equilibrium linearized model*, but the first term has no uniform all-property bound in this record. Consequently, no combined `||Z_full(u)||<=1/40` is established. In particular the previously exact low-energy static 3D witness with `||Z||>1/40` remains an energy-only no-go for nonlinear actual configurations and is not contradicted.

The earlier EXACT/CONDITIONAL implication `flattened cell under original pulse energy => ||Z||>1/40` can be combined with this certificate **only after** a bound on the total non-affine response of the actual nonlinear pulse has been established. There is no inferred nonlinear all-phase u100 cell-orientation, housing-strut safety, mean-volume breathing retention, housing ringdown, physical realization or native UD dynamics selection.

## 4. Reproduction and target exposure

Run `python3 exact_certificate.py --out /tmp/projected-exact.json` with Python3 standard library. Run `OPENBLAS_NUM_THREADS=1 python3 independent_check.py --out /tmp/projected-independent.json` with NumPy/SciPy and the captured byte-identical `nonaffine_audit.py` supporting source adjacent to both scripts. Exact output and construction scripts are all archived in the immutable `projected-coercivity-012` artifact with SHA-256 hashes.

Source coefficients came from versioned read-only integrated files. The selection of output `Z`, threshold `1/40`, original housing energy and original alpha amplitude are previously exposed development targets. The convenient `gamma=1/4` is a conservative post-exposure exact certificate choice, not a uniquely selected physical constant or an independently validated prediction. No unreported parameter/phase optimization was run in this certificate. Plain matrix eigenvalue approximation is separately labeled NUMERICAL.

**Next discriminant (priority 98/100):** Compute and validate the *reference-pulse* non-affine operator and its dynamically forced nonlinear remainder in a positive full-state frame-aware norm, coordinating PR44 recovery under its independent claim. Compare the exact 0.0045167 housing-phase linear allowance with the available 0.025 total non-affine budget, and preserve the exact static counterexample as a negative control. No mainline export.