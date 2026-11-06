# Twisted Klein × K4 packet-chain operator — exact source-gated audit v0.3

**2026-11-04, UD-Physics Discovery. EXACT/CONDITIONAL mathematical calculation; CANDIDATE as a UD transport law; physical promotion 0.** Claimed task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, claim ref HELD at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`; isolated branch and draft PR #301. Base source revision `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; main advanced, so rebase before integration. No shared mainline changes.

## 1. Source scope, typed objects and purpose

- **Native K4 packet factor**, source `experiments/qpb1-local-generators/README.md` v1.0 §§1–3: real filled tetrahedron `C_*(Delta³;R)` with chain dimensions (4,6,4,1), oriented signed boundary `d_K` (`d_K²=0`), unit Euclidean coefficient metric and source generator `A_K=d_K-d_Kᵀ`.
- **New Klein seam base**, from this branch's `README.md` v0.1 and `DOUBLE_COVER_AND_TRANSPORT_v0.2.md`: an explicitly **new** edge identification of two adjacent K4 triangular patches, not the intact K4 shell or a three-dimensional gluing. Equivalent small CW presentation `<h,v | h v h^-1 v>`: one vertex, two 1-cells and one 2-cell.
- **Orientation character** `rho_tw(h)=-1, rho_tw(v)=+1`, into units of Z. The orientable null control uses `rho_0(h)=rho_0(v)=+1`.
- **Research object (CANDIDATE)** is the integral `C_*^{rho}(Klein;Z) tensor C_*(Delta³;Z)` graded CW chain complex, and its real extension after selecting the unit coefficient metric. The product has top *chain degree* 5. This is NOT a five-dimensional physical spacetime, a geometric 3D tetrahedral mesh, or a native 15D K4 packet already proved to evolve on a Klein network.
- No physical time, length, energy, mass, external preparation, or fitted physical constant. `rho` and the CW-cell metric are declared assumptions.

## 2. Twisted cellular boundary from the Klein relation

For the group relator `h v h^-1 v`, ordinary Fox derivatives are `1-h v h^-1` with respect to h and `h+h v h^-1` with respect to v. Evaluating under the orientation character gives:

```
 twisted:   d1=[-2,0],  d2=[0,0]^T;
 untwisted: d1=[ 0,0],  d2=[0,2]^T.
```

Both have `d1*d2=0`, but they carry distinct integer homology:

- Twisted: `H0=Z/2Z, H1=Z, H2=Z`.
- Untwisted: `H0=Z, H1=Z⊕Z/2Z, H2=0`.

These are *local coefficient* homology groups of the Klein CW complex, not the ordinary homology of the tetrahedral shell. The factor of two is fixed by the declared CW loop relation; it is not a native K4 incidence coefficient or a physical coupling.

## 3. Exact K4 packet-chain extension

For `b in C_p^{rho}(Klein)` and `k in C_q(Delta³)`, define

```
  d_total(b tensor k)
      = (d_rho b) tensor k + (-1)^p b tensor (d_K k).
```

The two terms anticommute, so `d_total²=0` over Z for either rho. Dimensions by total degree are

```
n       0   1   2   3   4   5
dim     4  14  20  15   6   1         total=60.
```

Exact integer and rational matrix ranks:

| Model | rank d1 | rank d2 | rank d3 | rank d4 | rank d5 | betti degrees 0..5 over R |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Twisted | 4 | 9 | 10 | 5 | 1 | (0,1,1,0,0,0) |
| Untwisted | 3 | 10 | 10 | 5 | 1 | (1,1,0,0,0,0) |

Integral groups follow the exact contractible K4 factor and CW Künneth deformation: the integral twisted/untwisted groups above survive, including torsion, although the real Betti table necessarily omits Z/2. Do not conflate real rank with torsion.

## 4. Conditional native-form evolution, conservation, and isospectral obstruction

Declare unit Euclidean metric on the full 60D real chain coordinates, and adopt the source-type skew generator

```
A_rho = d_total - d_total^T : R^60 -> R^60.
```

Then `A_rho^T=-A_rho`, so `x'=A_rho x` conserves `||x||²` exactly. Every nonzero matrix entry joins a boundary/coface pair in the **declared product CW incidence**, which constitutes CW incidence locality rather than physical spatial proximity. For any subset of 60 registers, currents `j_(i<-j)=2(A_rho)_(ij) x_i x_j` are antisymmetric and sum to a signed incidence-cut flux. A source or physical clock has not been established.

The exact ungraded Hodge Laplacian `L_rho=-A_rho²` satisfies `L(L-4I)(L-8I)=0`. Trace `L=344` and trace `L²=2272` give

```
 eigenvalue      0        4        8
 multiplicity    2       30       28
```

**for both twisted and untwisted models**. Thus their ungraded spectra are *identical* even though their integer homology and graded zero modes differ. This is an exact negative control: a spectral agreement cannot uniquely identify the seam twist, and orientation-sensitive or grade-resolved data are required.

A separate spectral derivation constructs the **4-dimensional base Hodge Laplacian** and **15-dimensional K4 factor Laplacian**. Both base choices have spectrum `0^(2),4^(2)` (on different degrees), and K4 has `0^(1),4^(14)`. The product Laplacian eigenvalues add, yielding `0^(2),4^(30),8^(28)` without diagonalizing the 60D matrix. This is a second algorithm within the same research session, **not** an external peer review.

## 5. Orientation transport and observable firewall

The flat orientation character acts on an attached full packet by `U_h=-I_15`, `U_v=+I_15` (conditional on a uniform rank-one orientation line tensored with packet carrier). Klein's contractible relator has `U_{h v h^-1 v}=I_15`, and `U_h²=+I_15`. The twist-loop sign is invariant under scalar local-frame conjugation. This is **not** an independent matrix induced by K4 S4 face permutations.

A norm-squared or source support readout cannot detect `U_h=-I`: `||U_h x||²=||x||²`. A sign/phase-sensitive framed comparison of path histories *could* distinguish +I and -I if an independent reference and readout is specified. In projective or sign-insensitive readouts, the twist may also be observationally trivial. No physical measurement or retained-stock preference follows from the algebra.

## 6. Scope and failure conditions

- The base **Klein gluing is assumed**. Neither K4 incidence nor local Pachner moves selects it.
- The tensor-product carrier is a mathematical graded 60D CW model, not a sourced finite 3D K4 packet network or compact physical 5D manifold. It does not prove a *full geometric gluing law* from tetrahedral 3-cells.
- The metric, local coefficients and source-type skew evolution on this new carrier are additional choices; equality of native-unit spectra is conditional.
- Native QPB1 loop-history edgewise -1 gives nonflat *triangle* curvature. That source connection is distinct from this flat orientation cocycle and cannot be silently reused.
- A physical bridge must still define preparation, local seam generator, source/stock continuity, units, baseline and falsifiable response. Physical promotion remains 0.

## 7. Verification

```bash
python3 experiments/klein-tetra-face-flip-20261103/twisted_packet_chain_v03.py
python3 experiments/klein-tetra-face-flip-20261103/spectral_crosscheck_v03.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p test_twisted_packet_v03.py -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

See exact expected results `twisted_packet_results_v03.json` and typed receipt `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.3.json`. Scripts were independently expressed in two computational formulations and equivalent exact local code passed. Non-constructor mathematical review NOT_RUN; GitHub CI validates records, not proof.

**Disposition:** EXACT/CONDITIONAL for the explicitly defined 60D twisted and untwisted CW–K4 product complexes, spectra and loop characters. **OPEN:** a source-selected 3D tetrahedral seam network, a true native interface or selection law and any physical test.
