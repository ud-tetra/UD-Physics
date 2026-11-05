# Native eight-projector K4 leakage theorem v1.1

**2026-11-05 — Discovery / EXACT-CONDITIONAL / CANDIDATE parity interpretation / NO-GO multilevel invariance. Physical promotion 0.**

## Source, scope and amendment

Claimed task klein-tetra-face-flip-20261103, session ktff-20261103-01, HELD claim SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4; existing isolated branch and draft PR #301. Original task base 0eef9a3f77198810b35bee8d3ef578ebc3af403a; current examined main 698d6d66147131d43e364a1736ca07ad0f3fa9d4.

The exact native inputs are the filled K4 real chain carrier C=R15 with graded dimensions (4,6,4,1), unit Euclidean metric and signed S4 action, and A=d−dᵀ, J=A/2, J³=−J (experiments/qpb1-local-generators/README.md v1.0 §§1–3). The separate frozen coefficient ledger v0.39 P01–P06 defines the opposite-pair parity alphabet Theta=F2³, eight finite labels, not an existing projector formula. The actual K4 centroid-refinement residuals R01, R12 and R02 with norm squares 13, 52 and 151/4 are source-bound in K4_MULTILEVEL_METRIC_CLOCK_v0.9.md.

**Versioned amendment:** PARITY_13_OVER_8_SOURCE_AUDIT_v1.0 could only demonstrate eight orthogonal sectors in an added real fiber. The v1.1 construction below obtains eight orthogonal projectors directly within C=R15, with no added fiber. This does not remove the earlier objections to a physically forced parity interpretation, universal equal-sector weight, refinement invariance or Planck-length promotion.

## Theorem A: native 15D orthogonal resolution

Let h=(e0+e1+e2+e3)/2 be the unit constant-vertex harmonic, v=e0123 the oriented top-cell unit vector. Let E_A=[e01,e23], E_B=[e02,e13], E_C=[e03,e12] be the three native 15-by-2 opposite-edge coordinate embeddings. Exactly J maps their six mutually orthogonal edge vectors isometrically into C0⊕C2; the six J-edge images are mutually orthonormal, orthogonal to edge space, and orthogonal to h and the top/Jtop two-plane.

Define eight native real projector matrices:

- Q000 = h hᵀ (rank 1).
- Q100 = E_A E_Aᵀ, Q010 = E_B E_Bᵀ, Q001 = E_C E_Cᵀ (rank 2 each).
- Q011 = J E_A E_Aᵀ Jᵀ, Q101 = J E_B E_Bᵀ Jᵀ, Q110 = J E_C E_Cᵀ Jᵀ (rank 2 each).
- Q111 = v vᵀ + (Jv)(Jv)ᵀ (rank 2).

Exactly Qthetaᵀ=Qtheta, Qtheta²=Qtheta, Qtheta Qphi=0 if theta differs from phi, and the sum of the eight Q matrices equals I15. All 24 actual signed S4 simplex relabelings covariantly permute the weight-one and complementary weight-two labels; singleton 000/111 are fixed.

These projectors are constructed from **admitted native K4 geometry, J and the source metric**. The identification of their subspaces as constitutive finite parity *states* is CANDIDATE, not specified by ledger P04.

## Theorem B: source-native dynamics and invariant paired carriers

For each opposite pair p, J Q_weight1,p Jᵀ=Q_weight2,p and vice versa. Their four-dimensional sum commutes with A=2J, but each individual weight-one or weight-two projector does not commute with A. The 000 harmonic is static; the 111 top/Jtop plane is invariant. Thus the eight projectors are orthogonal instantaneous readouts, **not eight individually conserved dynamical states**. Source continuous flow rotates each weight-one/weight-two pair at native formal rate 2; no physical time or Hamming event rule follows.

## Theorem C: exact partial-isometry leakage identity

With the source unit metric and integral degree-one K4 first centroid subdivision F01:R15→R29, let G01=F01ᵀF01=diag(1 repeated14,4), A1=d1−d1ᵀ and

R01 = A1 F01 − F01 G01⁻¹ F01ᵀ A1 F01.

Full exact integer/rational matrices verify the previously unrecorded identity

**R01ᵀR01 = I15 − Q111.**

Therefore R01 has singular value 1 with multiplicity13 and 0 with multiplicity2, and it annihilates the top/Jtop plane. The first-refinement leakage-Gram observable commutes with all eight projectors and the parent native generator A. Its sector traces are:

| Label | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tr(Qtheta R01ᵀR01) | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 0 |

Thus 13=1+6×2+0, and the unweighted arithmetic **mean per eight labels** is exactly 13/8. The leakage operators R01 Qtheta are orthogonal in the Hilbert–Schmidt inner product, and the leakage Gram itself has no cross-sector blocks. This is a stronger genuinely native basis for the mean than the added uniform fiber from v1.0, but individual sectors are not equally loaded, and a mean over eight labels is not a physical length.

The alternative uniform average per *real dimension* is 13/15, demonstrating the importance of the precise averaging measure. Parent-native conservation of xᵀR01ᵀR01x under x'=Ax is an exact formal dynamic fact, not evidence that the fine-scale residual is a physical stored energy.

## Theorem D: multilevel obstruction

Under the same unit fine-metric conventions, direct K0→K2 residual R02:R15→R85 has norm²151/4 and parent-sector traces

| Sector class | 000 | Each weight-one label | Each weight-two label | 111 |
|---|---:|---:|---:|---:|
| tr(Qtheta R02ᵀR02) | 4 | 6 | 5 | 3/4 |

Its mean is 151/32 rather than 13/8. The composite leakage Gram fails to commute with the three weight-two Q matrices (each commutator rank4), and [R02ᵀR02,A] has rank14. The v1.1 first-level leakage invariant does not extend unchanged to this composite.

For the K1→K2 residual R12:R29→R85, transport the native parent Q projectors into the 15D embedded parent image using the isometry T=F01 G01⁻¹/². Their sum is TTᵀ, **not I29**. Exact inherited contributions are 3 for 000, 4 for each weight-one, 15/4 for each weight-two, and 3/4 for 111: total 27. The new, unassigned 14D complement contributes **25**, giving the full norm²52. This is the explicit obstruction to declaring eight exhaustive native sectors at the refined 29D carrier without a new admissibility rule.

## Normalization, verification and verdict

The projection identities depend on H=I and J=A/2. Scaling native generator by g multiplies leakage squared norms by g²; scaling a measurement metric by c multiplies them by c. In particular the eight-label mean becomes 13/2 for g=2 or 13/4 for c=2. A nonuniform metric requires new metric-adjoint and orthogonality calculations. Hence 13/8 is an **EXACT first-refinement native-unit arithmetic mean**, not a normalization-independent physical or Planck-scale constant.

Executable NATIVE_EIGHT_PROJECTORS_v1.1.py verifies all projector and signed S4 identities, exact R01ᵀR01 equation, native A dynamics, next-level residual and complement. An independent prior v0.9 matrix construction was used to compare full R01/R12/R02 matrices, not just norms. Eight locally executed regression tests PASS; non-constructor mathematical review NOT_RUN. Reproducible standalone source, results and SHA256 manifest are released separately; GitHub CI is an integrity check only.

**Disposition:** EXACT/CONDITIONAL source-constructible native eight-projector orthogonal resolution and rank13 first-refinement Gram theorem. Preserve the earlier no-go for individually conserved parity sectors, second-refinement invariant 13/8, and physical Planck emergence. Physical promotion remains 0.

**Next gate:** Source a constitutive rule selecting the Theta-label assignment and a complete refined-carrier projector resolution and evolution; preregister a fixed sector measure and physical unit bridge before any empirical claim.
