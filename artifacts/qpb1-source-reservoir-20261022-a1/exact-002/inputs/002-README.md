# Local source/reservoir preparation v1.1

**EXACT / CONDITIONAL — development, no registry entry.** A local matched reservoir can replace one active tetrahedral mode with a prepared incoming state through an exact reversible swap. The old addressed state leaves in the reservoir. Closing the coupling retains the preparation; reusable operation requires incoming resources, outgoing-state handling and a controller. The model transfers a supplied unit of support; it does not derive its dimensional physical action.

Base: UD-Physics `2b133c7889cde7aae9127d0c0fa2036c278884a9`. Dependencies: [unit-preparation audit](../qpb1-unit-preparation/README.md), [carrier/readout audit](../qpb1-carrier-anchor/README.md), pinned action sources listed in [SOURCES.json](SOURCES.json). [Exact code](audit.py), [cycle contract](CYCLE_CONTRACT.md), [receipt](../../sessions/qpb1-source-reservoir-20261022-a1/mathematical_receipt.json), [latest captured run](../../artifacts/qpb1-source-reservoir-20261022-a1/exact-002/manifest.json). Candidate eta_A=2 was exposed before this construction. No physical measurements or numerical hbar input are used.

Version1.1 adds explicit direct-sum versus tensor-product readout scope and24 normalized swap checks. The [initial run](../../artifacts/qpb1-source-reservoir-20261022-a1/exact-001/manifest.json) remains immutable; its transfer identities are unchanged. Use exact-002 for the amended readout record.

## 1. Local port and its symmetry condition

Keep the original oriented filled tetrahedron, unit chain metric and real chain dimension15. Write

\[
A=d-d^T,\qquad P=-A^2/4,\qquad J=A/2.
\]

Let e be the unit oriented top-cell vector, f=Je, and E=[e,f]. Then

\[
E^TE=I_2,\qquad AE=2Ej,\qquad
j=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The port uses only the top cell and its four boundary faces: f is their normalized signed sum with coefficients of magnitude1/2. Define r=E^Tx and x_perp=x-Er. The active orthogonal complement has dimension12 and is unaddressed by the port.

The port also has an exact symmetry characterization. For the oriented chain action rho of S4,

\[
\rho(\sigma)E=\operatorname{sgn}(\sigma)E,\qquad
EE^T=\frac1{24}\sum_{\sigma\in S_4}
\operatorname{sgn}(\sigma)\rho(\sigma).
\]

All24 permutations and the projector identity are checked exactly. **If** both reservoir coordinates transform by the sign representation, equivariance confines their target coupling to this rank2 plane. This is a conditional channel-selection result; the source representation is an explicit hypothesis. Equivariance alone permits every port E*M. Requiring compatibility with the declared complex rotations further restricts M to alpha*I+beta*j. Neither condition fixes the coupling magnitude, reservoir amplitude or source phase. The chosen real g port below sets beta=0 by a declared source-phase convention.

## 2. Joint generator, conservation and energy

Add a real two-coordinate reservoir y with matched native frequency2. Postulate

\[
\frac{d}{ds}\begin{pmatrix}x\\y\end{pmatrix}
=G_g\begin{pmatrix}x\\y\end{pmatrix},\qquad
G_g=\begin{pmatrix}A&gE\\-gE^T&2j\end{pmatrix}.
\]

This is an added reciprocal, simplex-local port model. It is not claimed to be the Hodge generator of an augmented simplicial complex. Original boundaries and d^2=0 remain unchanged; no new boundary operator is asserted.

G_g is skew, so N=||x||^2+||y||^2 is conserved. The exact port balance is

\[
\frac d{ds}\|x\|^2=2g\,r\cdot y,
\qquad
\frac d{ds}\|y\|^2=-2g\,r\cdot y.
\]

On the active joint carrier define Jbar=diag(J,j), Pbar=diag(P,I2), and K_g=-Jbar*G_g. Then Jbar^2=-Pbar and K_g is symmetric. The full joint carrier is real17-dimensional, with one real harmonic mode; the active real16-dimensional sector can be viewed intrinsically as C8. No complex structure is asserted on all17 real coordinates.

For 0<=g<2, K_g is positive on the active sector and equals the positive frequency operator there. Its eigenvalues are2 with multiplicity12 and2±g with multiplicity2 each. The original harmonic mode has eigenvalue0. Thus

\[
\det(\lambda I-G_g)=
\lambda(\lambda^2+4)^6
\bigl(\lambda^2+(2-g)^2\bigr)
\bigl(\lambda^2+(2+g)^2\bigr).
\]

For active x, the canonical spectral Hamiltonian is

\[
H_g=\tfrac12 z^TK_gz=N+gD,\qquad
D=r_1y_2-r_2y_1,
\]
\[
H_g\ge(1-g/2)N.
\]

Four rational g examples verify the spectral projectors, ranks, current and energy identities. If x has a harmonic component, that component contributes to total support but not to this Hamiltonian; it remains untouched. A physical energy map E_phys=(A0/tau0)*H_g is an additional dimensional correspondence.

## 3. Exact preparation and overwrite

Allow a prescribed scalar gate envelope g(s), with matched source frequency and 0<=g(s)<2. Let

\[
\Theta(s)=\int_0^s g(u)\,du,\qquad R(\phi)=e^{\phi j}.
\]

The free and port generators commute. For arbitrary old addressed state r0 and incoming source y0,

\[
r(s)=R(2s)\,[\cos\Theta\,r_0+\sin\Theta\,y_0],
\]
\[
y(s)=R(2s)\,[-\sin\Theta\,r_0+\cos\Theta\,y_0].
\]

At pulse area Theta=pi/2,

\[
r_{\rm out}=R(2s)y_0,\qquad
y_{\rm out}=-R(2s)r_0.
\]

An incoming unit reservoir therefore gives addressed target support1 even when the old addressed state is occupied. The old state is exported, including its phase information, rather than erased. This is how the joint model avoids treating a fresh unit injection as an additive support increment. For an incomplete transfer the interference term remains:

\[
\|r\|^2=\cos^2\Theta\,\|r_0\|^2
+\sin^2\Theta\,\|y_0\|^2
+2\sin\Theta\cos\Theta\,r_0\cdot y_0.
\]

The unaddressed x_perp continues its original free motion. A unit spectator edge plus a unit incoming source leaves full target support2 after transfer. The swap prepares one mode, not the entire target carrier. The harmonic component is also unaffected. There are192 rational transfer cases, including24 perfect-swap cases.

## 4. Retention, errors and detuning

Keeping g constant makes the exchange reverse: from an empty addressed target, support is N_in*sin^2(gs), reaching zero again at gs=pi. Retention therefore requires g=0 after the transfer or a different latch model. The prescribed envelope supplies that isolation; no autonomous controller is derived.

For an empty addressed target and area error epsilon,

\[
\Theta=\pi/2+\epsilon,
\quad a_{\rm out}=N_{\rm in}\cos^2\epsilon,
\quad N_{\rm in}-a_{\rm out}\le N_{\rm in}\epsilon^2.
\]

This quadratic loss bound must not be reused for an arbitrary occupied target. For unit incoming support and old norm R0,

\[
|a_{\rm out}-1|\le
\cos^2\Theta\,|R_0^2-1|
+2|\sin\Theta\cos\Theta|R_0.
\]

The interference term can be first order in epsilon. There is no uniform imperfect-swap bound for unbounded old norm. Forty-eight extremal rational cases check the bound; the derivation uses Cauchy–Schwarz.

For constant source detuning delta, replace2j by(2+delta)j. With empty target and constant g, define kappa^2=g^2+delta^2/4. Directly squaring the rotating-frame generator gives -kappa^2*I, hence

\[
\frac{a_{\rm target}(s)}{N_{\rm in}}
=\frac{g^2}{g^2+\delta^2/4}\sin^2(\kappa s).
\]

Its maximum is g^2/(g^2+delta^2/4), strictly below1 for nonzero detuning. Twelve exact cases check this algebra. This is a maximum over time for a constant-coupling model, not a guaranteed result at one fixed gate time or a no-go for arbitrary shaped controls. Joint pulse, loading, loss and calibration tolerances remain unassessed.

## 5. Gate work, outgoing records and reuse

D is conserved for every matched scalar envelope. The time-dependent Hamiltonian obeys

\[
\frac{dH_g}{ds}=g'(s)D,
\qquad W_{\rm ideal,sys}=D\,[g_{\rm final}-g_{\rm initial}].
\]

A pulse beginning and ending at g=0 has zero net ideal system work. For an empty addressed target D=0 throughout. These statements do not determine the physical clock, actuator, switching losses or memory-reset costs. An ideal zero interaction-work result cannot certify free control.

At isolated endpoints the addressed target/source energies are proportional to their supports. If an incoming source has support1 and the old addressed target has support a_old, the swap gives

\[
a_{\rm target,out}=1,\quad
a_{\rm source,out}=a_{\rm old},\quad
\Delta E_{\rm target}=\frac{\mathcal A_0}{\tau_0}(1-a_{\rm old}).
\]

Restoring the outgoing source to a unit reference requires the same modeled energy change, plus a physical procedure handling its old-state record and phase. When a_old=1 this energy difference is zero while the old state can still be unknown. Energy bookkeeping alone is not reset bookkeeping. Four budgets cover empty, smaller, equal and larger old supports. The signed energy change is not a total thermodynamic reset cost.

A closed invertible evolution cannot send all different old target states to one fixed target state while also restoring every auxiliary to one fixed state. Such a map would identify different inputs. The swap instead puts the old state in y_out. A repeated preparation protocol must retain/export that state, change another degree of freedom, or supply an explicitly open reset process. Fresh unit reservoirs are resources; their preparation is not generated by this model. A delivery process that also empties the target needs an outgoing target channel and its accounting.

## 6. What becomes observable, and what still does not

The target-plane projector diag(EE^T,0) commutes with Jbar. Its normalized population is invariant under a common joint complex phase and therefore can descend to a projective Born readout under a proposed quantum map. It does not commute with G_g for g!=0. Population can consequently vary even though a global phase is unreadable. With empty target and unit source, the native population is sin^2(Theta).

This added interaction changes the hypotheses of the earlier isolated-sector obstruction; that obstruction remains valid. Classical coherent oscillators have the same transfer law. No quantum identity follows from population transfer.

The swap is between real modal amplitudes in a direct-sum carrier. It is not asserted to be a tensor-product quantum reset channel. For an occupied addressed input with support a_old and unit incoming source, the perfect swap gives raw target support1 but normalized target Born population1/(1+a_old), before any spectator support is added to the denominator. For example, a_old=5 gives probability1/6. Twenty-four normalized swap cases check this distinction. The empty-target formula sin^2(Theta) below has total support1 and is not a general occupied-target reset probability.

For an explicitly **additional** quantum correspondence, choose i=-Jbar and the normalized energy operator M=K_g/2, with physical energy operator (A0/tau0)*M. Then the Schrodinger law would scale the native generator by eta_A/2 and predict

\[
p_{\rm target}=\sin^2[(\eta_{\mathcal A}/2)\Theta].
\]

Eta_A=2 reproduces the declared native generator under that correspondence. At one full-transfer endpoint, eta_A=2,6,10,... are aliases; one endpoint cannot identify the value. A curve near zero has leading coefficient eta_A^2/4 relative to the native curve, but calibration of g, physical time and the energy operator must be independent. Otherwise the coupling scale and eta remain confounded. This is an exploratory conditional extension, not an independent prediction or an automatically inherited source theorem.

The coupled normal modes also give an exact differential scale. At equal unit support their normalized energies differ by g and their native frequencies by2g. Under the same physical map,

\[
\frac{\Delta E_{\rm phys}}{\Delta\omega_{\rm phys}}
=\frac{\mathcal A_0}{2}.
\]

Unlike the isolated common phase, the frequency splitting can affect a population readout. But the equal-unit-support physical preparation and energy map are still assumptions. Classical reference amplitudes can change the dimensional energy difference without changing the normalized native dynamics. No physical hbar is recovered here.

## Reproduce and continue

```bash
python3 experiments/qpb1-source-reservoir/audit.py --out /tmp/ud-source-reservoir
```

The model supplies a local conditional transfer mechanism, a symmetry-conditioned channel, exact reset/export balances and a useful population readout. It leaves the source's unit preparation, physical action conversion, actuator/clock and autonomous isolation mechanism open. All checks are constructor work; hardware NOT_EXECUTED, empirical UNSCORED, physical promotion0.

Next discriminant: give the isolation gate and source refresh a defined local dynamical model, then test retention and repeatability with bounded old-state support, detuning and pulse-area error. A finite prescribed envelope is not an autonomous gate derivation.
