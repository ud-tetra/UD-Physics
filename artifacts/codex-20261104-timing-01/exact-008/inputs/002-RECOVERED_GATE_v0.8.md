# Recovered Q169–Q173 derivation trace v0.8

**CANDIDATE observer recovered; native Pachner startup remains SOURCE-BLOCKED.**
The four byte-bound mainline documents in [manifest](recovered/manifest.json)
are pinned to UD commit `a78193d420f3bac957be081aed0525fbc1457825`.
The recovered amplitude/readiness audit directly reports its v0.86 ledger
inspection and identifies Q173's remaining gate-transition receipt and
manuscript v9's conditional gate. This is an October derivation/audit chain,
not a claim that the original August working files or the entire v0.86
ledger were recovered in this run.

| Recovered document and section | Supplies | Missing for the bipyramid test |
| --- | --- | --- |
| Amplitude, readiness and binary-interface audit v0.1, Inspected source boundary | v0.86 Q169–Q173 and v9 readiness provenance; Q173 assumes a gate | Selected transition/reset and sampling law |
| Phase-aware gate-transition audit v0.1, §§1–2, 6–7 | Ungated current-crossing latch, reusable credit, candidate cell-root port and explicit publication constraints | Pachner event transfer/preparation and a no-missed-crossing observation contract |
| Conserved support and event capacity source audit, Analytic obstruction | Same state and support recur with unbounded completed crossing count; arbitrarily small support permits transverse roots | No native event capacity or retained count from instantaneous stock |
| Contact transitions and persistent agreement, Recruitment and Pruning | Exact mismatch invariance and restricted external reset witness on independent copies | No native reset/trigger or phase step on the present glued carrier |

The isolated-cell example observes the **ungated** current, synchronizes
four flags, reserves one credit on an upward opportunity and returns it on
a downward opportunity. This is a real conditional observer construction.
It leaves amplitudes continuous. It does not execute a topology-changing
Pachner move. If readiness gates its own only observation input, an unready
face sees identically zero gated current and cannot acquire its first flag
through that input.

## Exact audit on the two-cell carrier

Use ascending oriented cells 0123 and 0124, shared face 012, and unit simplex
metric. Let (B_3) be face-by-cell incidence and (B_2) edge-by-face incidence.
The exact Gram matrix is (egin{pmatrix}4&1\\1&4end{pmatrix}).
The top mode (e=(1,-1)^\top) has squared frequency 3 and
((B_3e)_{012}=0). Under the ungated flow with top seed e and zero face seed,
the shared face and its two directed currents vanish at all times.
An all-face latch can therefore wait forever on a nonstationary state.
At a different instantaneous state (f=B_3(1,1)^\top, u=(1,-1)^\top),
the directed currents are (+4,-4); net support can also hide active ports.

The cell root test (u_t=0,\ (B_3^\top f)_t\ne0) detects that blind-face mode.
Writing (F_t=2u_t(B_3^\top f)_t), its slope at the root is
(2((B_3^\top f)_t)^2>0). This gives an event predicate conditional on the
observer, not a reset, phase-zero Pachner receipt, retained publication, or
sample-phase bound. A current zero alone does not imply a cell root.

**New exact extension:** of the 128 binary masks (H_f) on the seven
geometric faces, exactly two satisfy (B_2 H_f B_3=0) as an operator:
all off and all on. Within each tetrahedron, each edge sees two boundary
faces with opposite incidence signs, so cancellation forces their mask
bits to agree. The four faces are connected by such edge adjacencies;
their bits are constant per cell. The shared bit forces the two constants
to agree. The other 126 masks permit lower-sector leakage from some top
preparation, although reciprocal masking preserves skewness and support.
This is an operator-wide result on this carrier, not a claim that every
initial condition leaks under each mask.

## Disposition

The recovered observer refines v0.7's inventory but leaves its source gate
closed. It supplies neither the required topology/preparation event nor
a guarantee that a finite observer cannot miss crossings or a full winding.
The v0.1–v0.6 conditional boundary protocol is preserved; autonomous native
startup stays parked. No cross-carrier clock law or physical promotion follows.

Replay: `python3 -B experiments/pachner-timing-budget/recovered_gate.py`.
This independently reconstructs the incidence matrices, checks the mode
and current examples, enumerates all masks and verifies four Git blobs.
It is constructor verification, not a replay of all upstream releases.
