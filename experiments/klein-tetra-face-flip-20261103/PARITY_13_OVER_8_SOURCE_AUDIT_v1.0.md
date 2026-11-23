# K4 13/8 parity-sector and refinement leakage audit v1.0

**Date: 2026-11-05. UD-Physics Discovery — EXACT / CONDITIONAL / NO-GO / OPEN. Physical promotion 0.**
Existing HELD task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, claim SHA `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Same isolated branch and draft PR #301. Source main checked `698d6d66147131d43e364a1736ca07ad0f3fa9d4`; original task base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`. No mainline export or accepted ledger amendment.

## Source-bound types
1. `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md` P01–P06 defines K4 4 vertices, 6 edges, symmetry S4=24, finite opposite-edge parity cardinality |Theta|=2³=8, capacity N1=24·8=192. P04 does **not** define an 8D Hilbert space or an orthogonal projector on native K4 chains.
2. Separate read-only `experiments/parity-dynamics-gauge-20261103/README.md` v0.1 defines an expressly assumed illustrative binary model `S=F2^4×F2^6`, with opposite-pair projection P(e)=(e01+e23,e02+e13,e03+e12) mod 2, rank3, fibers128. Neither this raw state model nor its micro-evolution is canonical.
3. `experiments/klein-tetra-face-flip-20261103/K4_MULTILEVEL_METRIC_CLOCK_v0.9.md` at the current claimed branch gives native **real** unit-incidence residuals `R01:C15→C29` norm²13, `R12:C29→C85` norm²52, and `R02:C15→C85` norm²151/4. These are different typed operators. S4 equivariance and unit coefficient metrics were tested.
4. `experiments/qpb1-local-generators/README.md` v1.0 §2 separately derives `dim End_S4(C15)=13`. That integer is NOT identical to the K4 refinement residual squared norm.
5. Designated research homepage checked on 2026-11-05: papers I–III 1.1.1 / IV 0.1, promotion0 and independent review pending. No parity-to-leakage operator supplied by these sources.

## Group action and an exact auxiliary construction
The three disjoint opposite-edge pairs A=(01,23), B=(02,13), C=(03,12) are permuted by S4 through S3. Exact exhaustive permutation checks give four Hamming-weight orbits of Theta: `{000}`, `{001,010,100}`, `{011,101,110}`, `{111}` (sizes 1,3,3,1).

In the *assumed* raw binary carrier S with 1024 states, P fibers have cardinality128. If we separately add the counting-metric real function space `ell²(S)=R1024`, the fiber indicator projectors are orthogonal, each of rank128, and covariant under S4. But they do NOT act on native real K4 C15/C29 and no source-defined map intertwines the native residual with them.

For a clean candidate lift, introduce a new orthonormal eight-label fiber `H_Theta=R8` with basis |theta>, and let `Q_theta=|theta><theta|⊗I29` project on `H_Theta⊗C29`. For nonnegative weights `p_theta`, sum p=1, define chosen isometry `J_p v=Σ_theta sqrt(p_theta)|theta>⊗v`. Then exactly
```
Q_theta Q_phi = delta_theta_phi Q_theta,   ΣQ_theta=I,
||Q_theta J_p R01||_F² = p_theta ||R01||_F² = 13 p_theta.
```
S4 acts on H_Theta by pair-bit permutation and on C29 by the native signed action. If weights are constant on the four S4 orbits, J_p is equivariant. Thus **orthogonal decompositions can be manufactured in an explicitly enlarged carrier**. No native source selects J_p, this fiber's metric, or p_theta.

Uniform p=1/8 gives 13/8 in *each* sector, as proposed. A strictly-positive nonuniform S4-invariant counterexample has `p000=p111=1/4`, every other p=1/12: contributions are 13/4 on 000/111, 13/12 on the other six, all 24 S4 permutations still pass. Even delta mass on 000 alone is S4-invariant. **NO-GO to claiming S4 forces 13/8**: symmetry requires only orbitwise constant weights, leaving three independent real allocation parameters after normalization.

## Normalization and second-level falsification
Using the **same uniform lift** for each independently typed residual gives:

| Residual | Native total norm² | Equal sector share |
|---|---:|---:|
| R01 (1→4) | 13 | 13/8 |
| R12 (4→16) | 52 | 13/2 |
| R02 (1→16 directly) | 151/4 | 151/32 |

To re-obtain 13/8 from R12 one can additionally divide by its four coarse top cells: `52/(4·8)=13/8`. That changes the observable to **per-coarse-top-cell sector average**, not invariant total-sector leakage; no source law selects that normalization. The composed R02 does not obey this recipe: `(151/4)/8=151/32`; dividing again by sixteen descendants gives 151/512.

Changing the unit-rate normalization to `A→gA` changes the residual to gR and each uniform sector norm² to g²·13/8. For g=2 it is 13/2. If the fine coefficient metric is changed globally from I to cI, the *metric-measured* squared residual becomes c·13, and the equal-sector share c·13/8, e.g. c=2 gives 13/4. These are deliberate changed hypotheses; no physical normalization is imported. Under the original frozen unit metric and unit gains, 13 is exact, but division by 8 is not a source-selected operator measurement.

## Disposition, checks and reopening
**EXACT:** Theta has 8 finite labels; S4 orbit sizes (1,3,3,1); illustrative raw toy fiber128; source-native unit first-refinement squared leakage13. Under added counting/sector real spaces, eight orthogonal coordinate projectors exist.
**CANDIDATE:** uniform equal-sector isometric lift of the K4 real residual, yielding 13/8 as a sector mean.
**NO-GO, scoped:** S4 does not determine uniform weights; the numerical sector share is not normalization-invariant and is not the same at second refinement under fixed total-residual normalization.
**OPEN_GATED:** a native C15/C29↔Theta linear or observable interface, native orthogonal projectors, constitutive dynamics/admissibility, a uniquely selected sector measure, and any Planck-length physical units bridge. **Physical promotion 0**.

Local exact reproducibility: `K4_PARITY_LEAKAGE_13_OVER_8_AUDIT_v1.0.zip` includes full `sector_audit_v10.py`, `raw_projection_control_v10.py`, independent full K4 matrix script `repository_replay_v10.py`, frozen v0.9 source input, exact results, six passing unittest controls, README and SHA256 manifest. This repository record and `parity_results_v10.json` retain the exact results; external non-constructor mathematical review NOT_RUN. Reopening requires a source-defined native projector or physical bridge, not a numerical resemblance to the Planck coefficient.
