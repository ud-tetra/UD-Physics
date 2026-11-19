# Coupled K4 parity clock — frame-memory lower bound and event-selection audit v1.4

2026-11-05. UD-Physics Discovery. **EXACT/CONDITIONAL; candidate finite successor; source-selection NO-GO/OPEN; physical promotion 0.** Same held task klein-tetra-face-flip-20261103, session ktff-20261103-01, claim SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4, isolated draft PR #301. Original task base 0eef9a3f77198810b35bee8d3ef578ebc3af403a; current source main 9d934337c0a9f7a6341b20cf116c8b6cd31c79eb.

## Source-bound objects and firewalls

- Source QPB1 local generators v1.0 §§1–3: signed filled K4 real C15, H=I, A=d−d^T, J=A/2, formal parameter u. This source does not define a parity counter.
- Source QPB1 native events EVENT_CONTRACT.md v1.0: quadrature zero-crossing observer rules are **added**, not self-selected physical clocks; adapter to F2 parity remains OPEN.
- Separate parity-dynamics-gauge v0.1: **illustrative**, not native, raw F2^4 vertex and F2^6 edge-bit state with opposite-edge XOR projection to Theta=F2³. Its provided toy update is an involution, not an eight-cycle.
- Frozen ledger v0.39 P01–P06: |Theta|=8 finite labels, 24 signed S4 orientations and N1=24×8=192 local capacity.
- Same-branch prime clock v1.3: no eight-cycle under a deterministic S4-equivariant update of Theta **alone**; native chosen π/4 strobe has projector period2, amplitude period4.
- Same-branch native eight-projector theorem v1.1: native C15 has eight orthogonal projector subspaces of ranks (1,2,2,2,2,2,2,2), whose parity-label assignment is CANDIDATE. These are not categorical states of the exploratory 6-edge-bit model.

## Theorem A — minimum effective coupled frame information

Let the effective action of S4 on the three opposite-edge pair positions be G=S3. Its kernel is the four-element Klein **group** V4 (not Klein-bottle topology). Let M be any finite G-set and T:Theta×M→Theta×M a deterministic G-equivariant map. Suppose T admits an eight-period orbit whose parity projection visits all eight Theta labels.

The stabilizer H of the full state is constant along a periodic orbit: if g fixes T^k(s), apply T^(8−k) and equivariance to show g fixes s, and conversely. The orbit visits the three weight-one labels 100,010,001, whose individual G stabilizers have trivial triple intersection. Therefore H is trivial. At the orbit's 000 state, its stabilizer equals Stab_G(m), so the frame memory M must contain a free G orbit. **Necessarily |M|≥6**. This no-go holds for all finite G-sets under the declared product action, not only fixed-frame updates.

Taking M=G itself (left regular six-element torsor) attains the bound. For m∈G and theta∈Theta define the relative coordinate eta=m^(-1)theta. For **any deliberately selected** permutation f of the eight local labels, define

    T_f(m,theta)=(m,m f(m^(-1)theta)).

This map commutes with every G action. Choosing f as an eight-cycle produces six disjoint eight-cycles on the 48 effective states. Using the original 24 S4 orientation labels instead produces 24 eight-cycles across all 192 frame×parity labels, with four orientation labels for each effective pair-order frame. Thus **the existing 192-address architecture has sufficient orientation-tag capacity** without inserting new categorical labels, but neither S4 nor signed incidence selects f or makes those tags physically available as memory. The new transition law is not a native UD consequence.

## Theorem B — affine Boolean obstruction and a parity-local Gray example

A deliberately chosen cyclic increment by +5 on a frame-relative numeric encoding Z8 yields 0→5→2→7→4→1→6→3→0. On local little-endian bits (a,b,c) this requires a quadratic carry:

    a' = a XOR 1
    b' = b XOR a
    c' = c XOR 1 XOR (a AND b).

This changes two or three parity bits in some steps. Exhaustively all invertible affine F2³ maps x↦Ax+b number 168×8=1344; **none is an eight-cycle**. In particular an affine 8-cycle would be an element of order8 in GL4(F2) via homogeneous coordinates; in characteristic2 its nilpotent part N=M+I would require N^4≠0, impossible for a 4×4 nilpotent matrix. Therefore a reversible eight-cycle on three Boolean coordinates needs non-affine transition logic.

A stronger one-bit-flip candidate is the Gray cycle:

    000→100→110→010→011→111→101→001→000.

Its update changes exactly one opposite-pair bit per step; the changed pair schedule is 0,1,0,2,0,1,0,2. There are **12 directed / 6 undirected** Hamiltonian cycles of the three-cube, so even requiring one-pair-flip locality does not select the cycle. Its F2 algebraic normal form has degree2. Applying the same frame-relative conjugation T_f produces exact S4 covariance on the 48 effective and 192 full frame-labelled states.

As a **separate illustrative exploratory microcarrier** use full π∈S4 plus six unoriented raw edge bits e∈F2^6. The chosen Gray successor selects exactly one of the three reference edges 01/02/03 in its local pair frame, then toggles the π-transformed physical edge bit. This yields one physical-graph edge-bit toggle and one opposite-pair parity flip each step. Exhaustively 24×64=1536 states return after eight steps; all 24×1536=36864 S4-covariance checks PASS. This is **not** the original 192-state architecture nor the real native QPB1 flow; binary raw-edge flips are only permitted in the prior **assumed** model.

## Theorem C — current accounting on the assumed address graph

For a nonnegative stock distribution p_s on 48 framed-parity addresses and a chosen reversible T, set p'_(T(s))=p_s and define directed transition current j_(s→T(s))=p_s. The sums Σp and Σp² are conserved; for any subset U,

    ΔΣ_(s∈U)p_s = Σ_(s∉U,T(s)∈U)p_s − Σ_(s∈U,T(s)∉U)p_s.

An exact positive integer fixture gives change +14, incoming59, outgoing45. This is valid **categorical transfer accounting**, but does NOT derive Q170–Q179 cell-owned burden or an SI energy flow. A relative frame readout eta=m^(-1)theta is invariant under simultaneous frame relabeling and resolves all eight chosen cycle states if m is retained. Physical observability of the frame is OPEN.

## Theorem D — exact native whole-projector obstruction

The separate native real K4 eight-projector resolution has ranks 1,2,2,2,2,2,2,2. Any invertible real linear operator conjugating the complete eight projectors must preserve rank; the unique rank-one harmonic projector Q000 cannot move into a rank-two sector. Therefore **no single invertible real operator on the original C15 can cyclically permute all eight whole native projector ranges**. In particular this is impossible for native orthogonal exp(uA), which fixes the harmonic direction. This does not preclude a particular **state trajectory** entering different sector ranges, a nonlinear/output-dependent readout, or a larger/open carrier. It prohibits a *whole-sector reversible permutation* on the declared native carrier.

## Reproducibility and disposition

Standalone exact local scripts coupled_clock_v14.py (minimum 6-frame proof controls, 48/192 eight cycles, 4608 covariance checks, 1344 affine no-go, 48-address flux) and gray_locality_v14.py (12 directed Gray cycles, 1536 raw states and 36864 covariance checks), with test_clock_v14.py and machine JSONs. Ten exact local regression tests PASS. Full executable user package UD_PACKET_COUPLED_PARITY_CLOCK_v1.4.zip has verified per-file SHA-256 manifest; archive SHA256 2a2e7d2697c0b2d2f9feb011c918cf7bfb077092478cbbc58c8634eb4e781c79. These are constructor computations, not external non-constructor review.

**Exact scoped outcome:** six effective frame states are necessary and sufficient for a fully projected eight-state cycle under G-equivariant deterministic coupled-state dynamics; a one-pair-local cycle exists after choosing a nonlinear successor. **Source selection fails:** QPB1 has not selected that nonlinear carry, edge event preparation or frame readout; categorical current is not a native source/energy law. The 192-state architecture gives room for a candidate clock, not an operational tick or Planck floor. Physical promotion=0.

**Next discriminator:** derive an actual source-selected edge/face event selector from QPB1 quadratures or another admitted K4 action, prove symmetry, reversible/current receipts, phase robustness and a physical event-time interface; if absent AUTO_FREEZE claims of a native eight-tick physical clock while retaining the conditional automaton mathematics.
