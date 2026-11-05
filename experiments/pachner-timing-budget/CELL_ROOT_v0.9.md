# Cell-root observer on the signed Pachner probe v0.9

**EXACT / NO-GO for robust coincidence with the declared reserve event.**
Use the v0.2 preparation \(c=c_0+e_3/4\), ascending orientations, old generator
\(A_o\), transport \(M\), full target generator \(A_n\), and projected \(K_0\).
The recovered candidate tests a top-cell amplitude zero with nonzero slope;
it does not use the reserve predicate \(F=R-c^\top Gc\).

The old top amplitudes are both \(\sin(\sqrt5\,t)/\sqrt5\). The verifier
checks initial values and derivatives and the oscillator recurrence through
23 Krylov powers, sufficient by Cayley–Hamilton. Both roots at the nominal
reserve event \(t=0\) are transverse, with slopes \(+1,+1\) in the declared
bases. For the nominal transported preparation all three target top amplitudes
are identically zero in both continuations, certified by 27 and 23 Krylov
powers respectively. Zero amplitudes with zero slope do not qualify as events.

**Counterexample with fixed reserve.** Add \(\epsilon(e_{0123}-e_{0124})\) at
nominal time zero with \(\epsilon=1/10^9\), or equivalently transport that
perturbation back to the original preparation time by old isometric evolution.
The added mode has squared frequency 3 and contributes opposite
\(\epsilon\cos(\sqrt3\,t)\) terms to the old top amplitudes. This follows
from the exact generator-square identity checked in the replay. At zero the
perturbed obligation is \(9/10+\epsilon^2\). Keep \(R=9/10\).
The v0.2 crossing proof applies: the preparation error is at most \(2\epsilon\)
and \(F'>2\) throughout its bracket. The unique crossing moves to
\(0<t_*\le\epsilon^2/2\). The common sine term has magnitude at most \(t_*\);
the cosine term has magnitude at least
\(\epsilon(1-3t_*^2/2)>t_*\). The two old amplitudes therefore have opposite
nonzero signs at the reserve event. The observer has no qualifying cell root
there. The two roots straddle zero: at \(t=\pm 2\epsilon\) the common sine
term dominates the perturbation (use \(\sin x\ge x-x^3/6\) for positive
small \(x\)); the slopes remain positive there by the cosine lower bound
and \(|\sin x|\le |x|\).

**Publication.** If each root toggles its own binary register, simultaneous
publication preserves shared XOR for every initial bit pair. Serial
publication exposes an intermediate XOR flip, but the actor of that flip
depends on which root is published first. An atomic compound record can
retain both cell IDs and slopes without imposing a serial order. It must
distinguish two root occurrences from one publication batch. This is a
candidate record format, not a native ordering law or a repair for the
perturbed event mismatch.

The nominal coincidence does not license substitution of the observer
for the reserve trigger. Autonomous startup remains parked. The conditional
paired-readout protocol is preserved. No physical promotion.

Replay: \`python3 -B experiments/pachner-timing-budget/cell_root_probe.py\`.
Source: recovered phase-aware gate audit §§6–7, pinned in v0.8's source
manifest; preparation and crossing bracket: v0.2. Constructor verification.
