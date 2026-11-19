# Integral Klein–K4 subdivision equivalence v0.6

**Discovery / EXACT CONDITIONAL / physical promotion 0.** Task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, HELD claim `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Source: v0.4 72-tetrahedron Klein×I Δ-complex and v0.5 pulled-back orientation character. The seam gluing is a declared hypothesis, not a native K4 law.

## Exact construction

The orientation-twisted simplicial complex has cell dimensions (18,102,156,72), with integral boundary squares zero and rank sequence (18,83,72). An intermediate two-triangle prism cellular complex has cell dimensions (2,7,7,2). Its cell-local *forward* barycentric subdivision map S assigns each oriented d-cell the signed sum of flags of original incident cells, with coefficient sign `(-1)^(d(d+1)/2) times product of incidence signs`. Every boundary commutes exactly. S has matrix shapes 18×2,102×7,156×7,72×2 and nonzero counts (2,14,48,72).

Select ±1 unit pivots in S, giving an integral direct-sum decomposition into cellular image and complement N of dimensions (16,95,149,70). An exact 165-pair integral algebraic Morse elimination cancels all of N: 16 pairs in degree 0↔1, 79 in 1↔2, 70 in 2↔3. All four remaining dimensions are zero, with no division beyond ±1. Recover the integral complement contraction h with `d_N h+h d_N=I`.

For split differential `d=[[d_c,X],[0,d_N]]`, define `K_n=-X_(n+1) h_n`, `P_big(c,n)=c+K_n n`, `H_big(c,n)=(0,h_n n)`. The exact integer matrix calculations prove `P_big S=I` and `d H_big+H_big d=I-S P_big`.

Three further unit-incidence cancellation pairs remove the diagonal edge x and one triangle/prism pair in the coarse CW model, reducing (2,7,7,2) to minimal Klein CW×I dimensions (2,5,4,1). The signed basis permutation W matches the existing v0.4 minimal CW basis. Write final maps `S_fin=S_big I_small W^-1`, `P_fin=W P_small P_big`, `H_fin=H_big+S_big H_small P_big`. Exact integral computations verify:

```
P_fin S_fin = I
d_min P_fin = P_fin d_72
d_72 S_fin = S_fin d_min
d_72 H_fin + H_fin d_72 = I - S_fin P_fin
```

The complete composite into the previous formal 60-coordinate twisted Klein×K4 packet chain is an **integer chain map** of graded ranks (2,5,4,1). Independent matrix-certificate read-back verified all four identities and the 60D composition. The locally executed full replay also regenerated the matrix JSON byte-for-byte.

## Integral result and limitations

The maps form a **strong deformation retract over Z**. Consequently, all integral homology is preserved, including twisted `H0=Z/2Z`; the minimal cellular groups give `H1=Z,H2=Z,H3=0`. This supersedes the limited rational-only comparison of v0.5 without rewriting its historical record.

**OPEN:** The forward subdivision S is geometrically cell-local. The integral reverse P is an algebraic Morse contraction; its bounded geometric support radius has NOT been proved. Neither direction is established as an isometry or a dynamical intertwiner for the physical K4 generator. The nonorientable 72-cell gluing and even-S4 packet completion remain source-unselected. No physical clock, energy, reference frame measurement, matter retention or empirical bridge is derived. Independent non-constructor review NOT_RUN.

## Reproduction

Standalone package `KLEIN_INTEGRAL_CHAIN_RETRACTION_v0.6.zip` (generated in this session) contains eight executable Python sources, exact sparse integer matrices for P/S/H/60D composite, local read-back verifier, logs, README and SHA-256 manifest. Locally tested with SymPy 1.14: full integral replay PASS, read-back PASS. File-byte identity with repository sources is not claimed.

**Next discriminant:** check strict locality of the integral reverse map and source a physical framed loop comparator with explicit unit/clock readout before physical promotion.
