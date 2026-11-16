# AW5 bipyramid phase dynamics and compactification obstruction

**EXACT_INTERNAL / CONDITIONAL / NO-GO. Physical Promotion = 0.**

Use the [pinned bipyramid construction](https://github.com/ud-tetra/UD-Physics/blob/c9c5baa756ae4bc22658c7086ae0e8ea72886e87/candidates/aw5-gap4-native-holonomy/AW5_DEFECT_SELECTION_AND_BIPYRAMID_HOLONOMY.md), tetrahedra 0123 and 0124 with ascending simplex orientations and unit simplex inner products. Let $f=012$, $x=B_2e_f$, and $A=B^\mathsf{T}-B$. Use native dimensionless time $s$.

## Exact current-to-face response

Signed incidence gives $B_1x=0$, $x^\mathsf{T}x=3$, and $B_2B_2^\mathsf{T}x=5x$. Set $y=B_2^\mathsf{T}x/\sqrt5$. Since $B_2B_3=0$, the two-grade plane has $Ax=\sqrt5\,y$ and $Ay=-\sqrt5\,x$. For initial edge current $j(0)=\beta x$ and all other grades initially zero, the exact evolution is

$$
j(s)=\beta x\cos(\sqrt5s),\qquad q(s)=\frac{\beta B_2^\mathsf{T}x}{\sqrt5}\sin(\sqrt5s).
$$

The face state is $q(s)$. The real edge coboundary $F(s)=B_2^\mathsf{T}j(s)$ is a separate quantity and equals $\dot q(s)$ in this plane. On the shared face, $q_f(s)=3\beta\sin(\sqrt5s)/\sqrt5$ and $F_f(s)=3\beta\cos(\sqrt5s)$.

For arbitrary real edge-only initial data $j_0$, the shared-face signal is $F_f(s)=\langle x,j_0\rangle\cos(\sqrt5s)$. The edge cut part evolves with vertices and is invisible to the face coboundary. The edge-cycle part has squared-frequency operator $B_2B_2^\mathsf{T}$, and its overlap with $x$ follows the shared mode. The shared face has recurring nonzero coboundary exactly when $\langle x,j_0\rangle\ne0$. Its time mean is zero, its RMS is $|\langle x,j_0\rangle|/\sqrt2$, and it crosses zero every half period. More generally, even with initial face data, the observable $\langle x,j(s)\rangle$ satisfies $F_f''=-5F_f$ because $A^2x=-5x$. A persistent nonzero DC component or an asymptotically selected phase does not arise from this oscillator.

## Conditional Wilson readout

Import the compact connection convention and choose an explicit conversion $\kappa$ from native current amplitude to turns. With fixed real $\kappa$, set $a(s)=\kappa j(s)+B_1^\mathsf{T}\chi\bmod 1$. For the shared cycle,

$$
W_x(s)=\exp\!\left(2\pi i\,\kappa\langle x,j_0\rangle\cos(\sqrt5s)\right).
$$

The phase $-i$ occurs exactly when the turn in the exponent belongs to $3/4+\mathbb Z$. Over a full native cycle this happens if and only if $|\kappa\langle x,j_0\rangle|\ge 1/4$. The value is a recurring readout at specific times under the declared conversion. It supplies no unique $\kappa$, preparation amplitude, readout time, or asymptotically selected phase. Nonzero real coboundary can also give $W_x=1$ when its normalized face turn is integral. The exact compact statement on this loop is $W_x\ne1$ if and only if the compact curvature on $f$ is nonzero modulo a turn.

### The native flow does not descend to the edge-only compact quotient

In turns, let $Z=\ker B_1$ in the real edge space, $Y=\operatorname{im}B_2^\mathsf{T}$, and $P_Z$ be the orthogonal projection. After removing vertex coboundaries, the compact edge identification on $Z\oplus Y$ is by translations in $(P_Z\mathbb Z^9)\oplus\{0\}$. It contains $(x,0)$ because $x$ is an integer edge cycle. The representatives $0$ and $(x,0)$ are therefore equivalent initially. At $s=\pi/(2\sqrt5)$, they evolve to $0$ and $(0,y)$, which have distinct face coordinates. At $s=\pi/(3\sqrt5)$ their shared-face compact edge readouts also differ, because the edge difference is $x/2$ and its shared-face turn is $3/2$. The same real flow cannot define an autonomous flow on the declared edge-only compact quotient. A real-lift state can supply the conditional readout, or a separate compact dynamics must be specified and tested.

## Verification

The accompanying exact constructor replay assembles signed incidence from the two oriented tetrahedra using the pinned predecessor's incidence routine. It verifies the paired-plane identities, both grade amplitudes in an unnormalized rational basis, the integer shift and nonintegral Wilson discrepancy, and the quarter-turn witness. No experimental target or numerical tolerance enters the replay.
