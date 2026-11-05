# Klein–K4 scale-aware locality and induced evolution contract v0.8

**2026-11-04 — Discovery / EXACT-CONDITIONAL mathematics / dynamical-persistence and physical bridge OPEN. Physical promotion 0.** This extends the same held task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`; claim `refs/heads/claims/klein-tetra-face-flip-20261103` held at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`, isolated draft PR #301. Original main base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; resumed main `e400dfb715262a44b3bbb2e929c7b438028af67e`. No integration, source ledger amendment or site release.

## 1. Source, carrier, typed locality and goal

Original read-only source: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3, signed filled K4 incidence and unit metric, source-type skew `A=d-d^T`; it does not select a Klein seam or 3D physical clock. Discovery dependencies: `INTEGRAL_SUBDIVISION_STRONG_RETRACT_v0.6.md` supplies the exact integral P,S,H equivalence from the **assumed** Klein×I 72-tetra twisted simplicial chain `C_s` to minimal CW chain `C_c`; `REFINEMENT_LOCALITY_AND_DYNAMICS_v0.7.md` identified nonintertwining under unrelated unit metrics.

- Fine carrier `C_s`: real coordinate vector space of dimension348, graded (18,102,156,72), integer signed boundary `D_s`, chosen **unit Euclidean chain metric** `H_s=I`, formal evolution `A_s=D_s-D_s^T`.
- Coarse carrier `C_c`: real coordinate vector space of dimension12, graded (2,5,4,1), integral minimal CW boundary `D_c`. Exact integral barycentric subdivision `S:C_c→C_s`, reverse integral retraction `P` satisfying `PS=I`, `D_sS=SD_c`. P is not the metric adjoint of S.
- **Scale-aware locality** must specify the notion: (a) CW **incidence locality** (couplings between boundary/coface cells), (b) original-cell neighborhood support locality, (c) refined graph-hop locality, and (d) physical length/time locality. These are different types. Only (a) and the prior finite tests of (c) have exact results. No SI length or speed is imported.

## 2. Exact induced coarse metric and projected generator

Define the coarse pulled-back inner product by `G=S^T H_s S=S^TS`. Direct calculation from **every column** of the v0.6 signed integral S gives

```
G = diag(1,1,2,2,2,2,2,8,8,12,12,72).
```

These weights count the squared amplitudes in the signed barycentric flag subdivision of each cellular generator under **H_s=I**. They are **NOT** geometric physical volumes, conductances, masses, temporal rates or fitted constants. Define the metric left inverse `L=G^-1 S^T` and orthogonal fine projector `Π=SL`; `LS=I`, `Π^2=Π=Π^T`. The unique coarse generator obtained by orthogonal Galerkin projection of the declared fine `A_s` is

```
A_G = L A_s S = G^-1 S^T A_s S.
```

Using exact `D_s S=S D_c` and its transpose gives the **identity**

```
A_G = D_c - G^-1 D_c^T G
    = D_c - D_c^(dagger_G).
```

Thus this is the **unit-fine-metric-induced Hodge-skew** coarse generator; it does not require arbitrarily replacing `D_c-D_c^T` or fitting a rate. It obeys

```
A_G^T G + G A_G = 0,
d/d u (y^T G y) = 0  for y'=A_G y.
```

The coarse CW incidence graph has **11 undirected boundary/coface pairs**; exactly 22 oriented entries in `A_G` are nonzero, and no nonincidence entries appear. Since G is diagonal, for each such pair (i,j) the algebraically signed native quadratic-support current

```
J_(i←j) = 2 G_ii (A_G)_(i,j) y_i y_j = -J_(j←i)
```

has exact antisymmetry and ensures cell-wise continuity `d(G_ii y_i²)/du=Σ_j J_(i←j)`. This is incidence-local **native stock accounting**, not a physical energy flux.

The naive unit-coarse metric generator `A_0=D_c-D_c^T` is different: `rank(A_G-A_0)=5`, with `||A_G-A_0||_F²=151/18`. Thus the v0.7 skew mismatch cannot be resolved by pretending coarse unit weights were already compatible.

## 3. Exact nonclosure despite the best metric projection

The fine image of S is **not A_s-invariant**. The leakage operator is

```
R = A_s S - S A_G = (I-Π) A_s S.
```

Exact matrix calculation proves `S^T R=0`, `rank_Q(R)=11`, `||R||_F²=157`, and weighted input Hilbert–Schmidt quantity `Tr(R G^-1 R^T)=242/3`. Thus the coarse generator is orthogonal-projection optimal in the chosen metric, but **not an exact evolution intertwiner**:

```
A_s S ≠ S A_G.
```

For formal native u, Duhamel's identity and the two respective skew-unitary flows give the *conditional* estimate

```
|| ( exp(u A_s) S - S exp(u A_G) ) G^-1/2 ||_F
    ≤ |u| sqrt(242/3).
```

This is an a priori discrepancy bound in native dimensionless units and is generally not a useful long-time accuracy guarantee. It is not a calibration to seconds or evidence for physical wave propagation.

**NO-GO, scoped:** The exact 72-simplex to 12-CW integral chain-homotopy equivalence does not yield autonomous exact coarse evolution under the chosen fine unit-metric generator; this remains true with the canonical induced metric. A changed microscopic generator, memory kernel, open-system environment or additional dynamically invariant subspace is a separate branch.

## 4. Independent refinement control: a physical clock does not come free

Take an oriented interval subdivided into m fine *unit-weight* edges, retain its two endpoints and use coarse edge as the oriented sum of all m fine edges. The exact subdivision gives `G_m=diag(1,1,m)` and

```
A_(G,m) =
[ 0    0   -1
  0    0    1
  1/m -1/m  0 ].
```

Its nonzero angular frequency squared is `2/m`; the exact fine-image leakage norm-squared is `2(1−1/m)`, zero only at m=1. For m=(1,2,4,8,16,32,64), frequencies squared (2,1,1/2,1/4,1/8,1/16,1/32) and leakage norms squared (0,1,3/2,7/4,15/8,31/16,63/32). These are exact **combinatorial** values, not SI frequencies.

This demonstrates a different structural gate from the v0.7 hop-distance no-go: even when metric weights are induced from S and the coarse generator preserves its own induced norm, the native unit-weight oscillator frequency changes under subdivision and the coarse image is not invariant. To claim a scale-independent clock, a new refinement law for metric, incidence gains and/or physical time must be sourced. Selecting a compensating m-dependent gain after seeing this dependence would be a **candidate calibration**, not an independently derived universal time.

## 5. What UD may claim and what remains OPEN

- **EXACT-CONDITIONAL:** Under the assumed Klein×I gluing, integral S and fine unit metric, G is fixed, A_G is a uniquely defined Galerkin generator, and coarse incidence currents conserve induced quadratic stock.
- **NO-GO-SCOPED:** Coarse image not invariant, residual R nonzero, exact microscopic/coarse flow equivalence fails; no refined-hop or native frequency invariance is established under the tested unit-weight model.
- **OPEN:** The metric G is mathematical subdivision multiplicity, not a source-selected physical material metric; reverse P has not been shown refinement-uniformly local; no source-selected face-flip event/physical clock, independent orientation frame preparation or measured bridge. The earlier native 5D K4 invariant hull remains a **separate source-conditional carrier**, not a dynamically complete model of the 348D Klein network.

## Reproduce

```bash
# Standalone exact 12D code (repository dependencies only)
python3 experiments/klein-tetra-face-flip-20261103/metric_coarse_generator_v08.py
python3 experiments/klein-tetra-face-flip-20261103/scale_interval_control_v08.py

# Full exact 348D metric/flux/leakage replay requires the v0.6 standalone ZIP inputs
python3 induced_generator_v08.py
python3 interval_scale_control_v08.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The complete v0.8 standalone package contains exact locally executed v0.6/v0.7 sources, new 348D derivation, interval controls, outputs and file digests. Equivalent local code PASS; this is a constructor calculation, not external peer review. GitHub CI status recorded per latest SHA and is an integrity test only. Physical promotion=0.

**Next discriminant:** identify a source-admitted coarse metric/current normalization and dynamics across *two distinct* refinement levels whose observation law commutes to an explicitly bounded error. Freeze readout, metric and event clock before comparing any physical data. If no source selects the scale factors, park the Klein sector as mathematically consistent but physically underdetermined.
