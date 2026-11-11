# Native K4 parity-orbit arithmetic v0.1

2026-11-11; session `ud-native-orbit-arithmetic-20261111-01`; base `ud-tetra/UD-Physics@ec37b23b1ef9dc4f7bd8f58c91daa547e8664b10`; [tracking issue #357](https://github.com/ud-tetra/UD-Physics/issues/357). **EXACT finite kinematics; physical promotion 0.** Target-blind construction: no Gibson constants, measured couplings, or particle masses enter the definitions or calculation.

## Sources and typed objects

The supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, P06 and C01–C06 distinguishes the three-bit fiber, `7/192` structural ratio, five-dimensional response-space dimension, and `7/960` normalized internal ratio from physical couplings. The [QPB1 loop-history audit](../qpb1-loop-history/README.md), opposite-edge parity classes, identifies the three labels with opposite-edge matchings. This receipt uses only that labeled fiber and the natural action of vertex relabelings; it does not invoke Q169 evolution or Q194–Q210 event receipts.

Let `V={0,1,2,3}`; the three perfect matchings of the six K4 edges are `01|23`, `02|13`, `03|12`. Let `Θ={0,1}^3`, assigning one bit to each matching. Each `p∈S4` induces a matching-label permutation and an action `p·θ` by permuting bit positions, with domain and codomain `Θ`. Restricting to the even subgroup `A4` represents orientation-preserving relabelings. These are group actions on *labels*, not physical motion, event time, energy, or a measured clock. No XOR translation is included.

## Exact classification

Hamming weight is preserved. Both `S4` and `A4` induce a transitive action on each of the weight-one and weight-two triples, while weights zero and three are singleton orbits. Thus orbit sizes are `1,3,3,1`. The relation `R_G={(θ,p·θ):θ∈Θ,p∈G}` contains exactly `1²+3²+3²+1²=20` of the `8²=64` ordered state pairs for either group. The remaining 44 pairs do not arise from *pure relabeling*. `S4→S3` and `A4→C3` have distinct acting groups but identical orbits on this fiber; therefore endpoint reachability does not distinguish them. This result does not supply an order-four element to `A4×(Z2)^3` or a four-phase port clock.

The [independent exhaustive replay](orbits.py) constructs matchings from K4 edges, all 24 vertex permutations and 12 even permutations, and all 64 ordered fiber pairs; it asserts equality with the Hamming-weight relation. It checks `(000,001)` as a negative control. The proof and enumeration agree exactly.

## Decision and reopening

**AUTO_LOCK / EXACT:** scoped orbit classification for the stated label action. **OPEN:** a source-selected local transition rule, generator, initial/boundary conditions, clock, conserved stock and HOLD state. It would be improper to call the 44 non-relabeling pairs physically forbidden without proving that all physical changes are pure relabelings; an independently sourced parity-changing event would be a new branch. The ledger's `7/192` and `7/960` remain typed structural ratios. No native `3^9` ternary address or orphan predicate appears in this source-bound construction, so a `709` match is **SOURCE_BLOCKED** here. Future comparison must predefine the UD selector and normalization before exposing Gibson's counts or empirical targets.
