# Ideal passive reservoir port and action calibration v1.0

**EXACT / CONDITIONAL / OPEN — development, no registry entry.** A balanced ideal passive LC network realizes the previously proposed local reservoir generator exactly under an explicit canonical state map. Absolute energy calibration can determine a chosen preparation's action reference. The circuit does not select which reference is the universal UD unit: its linear amplitude freedom remains.

This is **inverse design against a known native operator**, not an independent discovery that a measured device follows UD. The matching condition, source phase convention and reference preparation are declared design choices. Candidate eta_A=2 was exposed before this work; no numerical hbar, physical measurements or fitted apparatus parameters are used.

Base UD-Physics `127c5fb995cdd218fecc479bccec8ed7a2c2bad0`. [Source bindings](SOURCES.json), [external primary-source notes](EXTERNAL_SOURCES.json), [exact audit](audit.py), [calibration contract](CALIBRATION_CONTRACT.md), [receipt](../../sessions/qpb1-passive-port-20261022-a1/mathematical_receipt.json), [captured run](../../artifacts/qpb1-passive-port-20261022-a1/exact-001/manifest.json). The [previous reservoir model](../qpb1-source-reservoir/README.md) supplies the addressed top-cell/face plane and resource boundaries. This two-node circuit represents that plane plus its reservoir; it is not a physical implementation of the full15-dimensional tetrahedral chain or the distinct Stage0 K4 bench network.

## 1. Physical topology and conventional input

Use two nodes with equal ground capacitors C0>0, one coupling capacitor Cc>0 between them, and two grounded magnetically coupled coils. Define their capacitance and signed inductance matrices by

\[
\mathsf C=\begin{pmatrix}C_0+C_c&-C_c\\-C_c&C_0+C_c\end{pmatrix},
\qquad \boxed{\mathsf L=Z^2\mathsf C},\quad Z>0.
\]

Thus each coil has self-inductance Z^2(C0+Cc), and the signed off-diagonal entry is -Z^2*Cc. The mutual-inductance magnitude is positive; the sign in these branch references follows the winding/dot convention. It is not a negative self-inductor or capacitor. The coupling-magnitude ratio is Cc/(C0+Cc)<1. Both matrices are positive definite, with eigenvalues C0,C0+2Cc and their Z^2 multiples.

Conventional ingredients are documented in [MIT8.02, Chapter11, §§11.1 and11.5](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/f5c35823a7faac0d893754ab42804e7e_chap11inductance.pdf): mutual coupling and ideal LC energy/evolution. The signed mutual-energy convention and passive bound are covered in [F.Obeidat, Electric CircuitsII, slides7 and17–18](https://www.philadelphia.edu.jo/academics/fobeidat/uploads/Electric%20Circuits%20II%20Course2/14%20Magnetically%20Coupled%20Circuits.pdf), PDF pages7 and17–18. These sources support the ordinary circuit ingredients; the balanced matrix construction and UD map below are constructor deductions. A positive ideal matrix does not certify a fabricated device's bandwidth, losses, tolerances or parasitics.

For node flux Phi and canonical charge Q, postulate the ideal lumped equations and Hamiltonian

\[
\dot\Phi=\mathsf C^{-1}Q,\qquad
\dot Q=-\mathsf L^{-1}\Phi,
\]
\[
H_{\rm phys}=\tfrac12Q^T\mathsf C^{-1}Q+
\tfrac12\Phi^T\mathsf L^{-1}\Phi.
\]

Here Phi=L*I and Q=C*V reconstruct canonical coordinates from branch currents and node voltages in the stated references. The inductive energy is also I^T*L*I/2. No native B0 is identified with capacitance or inductance; B0 retains its mass-like source type.

## 2. Exact map to the reservoir generator

Define W=C^{-1}/Z and write

\[
W=\begin{pmatrix}\bar\omega&\kappa\\\kappa&\bar\omega\end{pmatrix},\quad
\bar\omega=\frac{C_0+C_c}{ZC_0(C_0+2C_c)},\quad
\kappa=\frac{C_c}{ZC_0(C_0+2C_c)}.
\]

The two normal-mode frequencies are

\[
\omega_+=\bar\omega+\kappa=\frac1{ZC_0},\qquad
\omega_-=\bar\omega-\kappa=\frac1{Z(C_0+2C_c)}.
\]

Choose an independent positive reference flux Phi_ref. For each node define X_i=Phi_i/Phi_ref and Y_i=-Z*Q_i/Phi_ref. The matching L=Z^2*C gives

\[
\dot X=-WY,\qquad\dot Y=WX.
\]

Let r=(X1,Y1), t=(X2,Y2), j=[[0,-1],[1,0]], and choose the source dictionary y=j*t. With

\[
\tau_0=2/\bar\omega,\qquad
g=2\kappa/\bar\omega=\frac{2C_c}{C_0+C_c}\in(0,2),
\]

the native-time equations are exactly

\[
r'=2jr+gy,\qquad y'=2jy-gr.
\]

This matches the four addressed reservoir coordinates of the preceding model. The source dictionary is a quarter-turn of its flux/charge pair; it is not silently the same coordinate labeling as the target. Matrix intertwining, canonical one-form pullback, full energy Hessian and normal-mode frequencies are checked in six rational component families. No rotating-wave approximation is used in this ideal matched model.

The exact match requires the designed relation between electric and magnetic matrices. A simpler positive coupling capacitor plus a positive ordinary edge inductor has C^{-1} off-diagonal positive and the edge-inductance inverse off-diagonal negative. Those cannot satisfy L^{-1}=C^{-1}/Z^2 in this fixed local dictionary. This scoped sign obstruction does not address other canonical transformations or approximate models.

## 3. Preparation is a two-node condition

The prior empty-target/unit-source input r=0,y=(1,0) requires

\[
\Phi=(0,0),\qquad Q=(0,\Phi_{\rm ref}/Z),
\]
\[
V=\mathsf C^{-1}Q
=\Phi_{\rm ref}(\kappa,\bar\omega),\qquad
\frac{V_1}{V_2}=\frac\kappa{\bar\omega}=\frac g2.
\]

Both coil currents start zero. **The target node voltage generally starts nonzero even though its canonical target coordinates vanish.** Conversely, merely setting V1=0,V2 nonzero gives Q1=-Cc*V2, so it prepares an occupied target mode. Its initial target modal fraction is

\[
\frac{C_c^2}{C_c^2+(C_0+C_c)^2}>0.
\]

All six preparation families check this counterexample. The ratio g/2 is derived from the empty canonical target condition, not selected from the eta target. The overall voltage magnitude remains an external choice.

The corresponding classical canonical readout is

\[
p_1=\frac{\Phi_1^2+Z^2Q_1^2}
{\Phi^T\Phi+Z^2Q^TQ},
\qquad Q=\mathsf CV,\quad\Phi=\mathsf LI.
\]

It is not one node's voltage-squared fraction. Coupled capacitor/coil field energy and native modal support are different typed objects. A Born interpretation is an additional hypothesis; this remains the direct-sum modal analogue, not a tensor-product quantum reset channel.

## 4. What independent energy calibration can determine

The physical canonical one-form pulls back as

\[
\tfrac12(Q^T d\Phi-\Phi^T dQ)
=\mathcal A_{\rm map}\,\tfrac12
\bigl(r_1dr_2-r_2dr_1+y_1dy_2-y_2dy_1\bigr),
\]
\[
\boxed{\mathcal A_{\rm map}=\frac{\Phi_{\rm ref}^2}{Z}}.
\]

The energy is (A_map/tau0)*H_native. For the specified reference preparation D=0,N=1,

\[
E_{\rm ref}=\frac{\bar\omega\Phi_{\rm ref}^2}{2Z},\qquad
\mathcal A_{\rm map}=\frac{2E_{\rm ref}}{\bar\omega}.
\]

Consequently an independently calibrated absolute energy and angular frequency can identify A_map **for the frozen preparation**. No action constant is required inside this estimator. That identifiability must not be understated: the numerical preparation scale is measurable in principle. What is missing is the source rule identifying this particular scale with the universal source A0.

At equal unit modal support the normal-mode energies are A_map*omega_±/2, hence

\[
\frac{E_+-E_-}{\omega_+-\omega_-}=\frac{\mathcal A_{\rm map}}2.
\]

This agrees with the preceding conditional differential scale. It is an ideal classical identity under the declared reference convention, not independent evidence for hbar. The physical preparation conditions and energy measurements for both modes must actually be supplied. Computing energy from the same calibrated C,L,V,I used to infer the state provides an algebraic cross-check; independent work/energy evidence requires its own chain and shared-error accounting.

For positive energy/frequency intervals a deterministic enclosure is [2E_L/omega_U,2E_U/omega_L]. Four synthetic corners verify the arithmetic. Actual uncertainty coverage, correlations, SI/quantum-standard traceability and model corrections are not certified by that formula. Frequency is angular frequency; Hz conversion must retain2pi. No energy measurement has been executed here.

## 5. The amplitude test and its exact scope

With one fixed physical map, scaling the actual prepared flux and charge by c changes native support to c^2 and physical energy/loop action by c^2. It leaves component frequencies and normalized populations unchanged. Dividing by the retained support recovers the same A_map.

If instead a different physical reference c*Phi_ref is declared to represent native support1, the map scale becomes c^2*A_map. That changes the reference map, not the fixed map's unit merely because another state was prepared. Twenty-four exact amplitude interventions preserve this distinction.

Thus absolute energy calibration fixes a selected reference, but the linear circuit does not privilege a reference amplitude. Unit source support was supplied to the reservoir model; the circuit gives an operational realization of a chosen source, not a derivation of its universal unit status. Choosing Phi_ref=sqrt(2*hbar*Z) would backsolve A_map=2*hbar. It cannot independently test that same relation.

A dimensional check reinforces the missing input. In M,L,T,I exponents, every C,L,R and time unit obeys mass exponent plus half the current exponent=0. Any homogeneous monomial of them inherits that relation. An action unit has exponents(1,2,-1,0), for which the same expression equals1. An additional flux, charge, energy or other physical primitive is therefore needed in this parameter family; component/time data alone do not yield an action scale. Flux_ref^2/Z has precisely the required action units. This is a scoped dimensional obstruction, not a statement about models containing additional physical primitives.

## 6. Closing the port is coordinated control

At fixed Z and baromega, the prior native coupling g can be represented by the static family

\[
\kappa=g\bar\omega/2,\quad
C_0=\frac1{Z(\bar\omega+\kappa)},\quad
C_c=\frac\kappa{Z(\bar\omega^2-\kappa^2)},\quad
\mathsf L=Z^2\mathsf C.
\]

Four rational members include g=0. Opening only the coupling capacitor while leaving the inductance matrix fixed does not produce g=0 under the same map; a magnetic port remains and the matching changes. Thus the previous prescribed gate requires coordinated parameter control or another explicitly modeled isolation mechanism. A static family is not an actuator/clock derivation. Finite-rate control, source disconnection, outgoing records and refresh costs retain their earlier open status.

## Decision and reproduction

```bash
python3 experiments/qpb1-passive-port/audit.py --out /tmp/ud-passive-port
```

Retain this construction as an exact ideal classical port and calibration baseline. **Park the linear passive circuit as a stand-alone universal action-unit derivation:** its amplitude freedom fails that role. Reopen that question only with an independent unit-preparation/source law or additional physical primitive that removes the free reference assignment. A valid analogue experiment can proceed under its own scope; analogue agreement alone does not supply the missing law.

All results are constructor work. No named built device, hardware qualification, independent review, empirical score, registry advancement or mainline export. Physical promotion0. The [calibration contract](CALIBRATION_CONTRACT.md) lists the missing evidence.
