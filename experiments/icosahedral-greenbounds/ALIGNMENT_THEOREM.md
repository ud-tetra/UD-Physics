# Proper-alignment remainder v1.0 — recovery checkpoint

**EXACT/CONDITIONAL.** The theorem concerns a primary-position readout. All560 mechanical variables, momenta and kinetic energy remain in the original ODE. It does not establish an actual-flow tube.

## Definitions

Let A be a centered13-by3 real reference matrix, including the hub. Centering is arithmetic over13 points, not mass weighting. Suppose sigma_min(A)>=s>0 and ||A||_2<=a. Let E be centered, ||E||_F<=r, with ar<s^2. All lengths use the unchanged internal edge scale.

Let Q minimize ||(A+E)Q-A||_F over SO(3). Let N be the Frobenius orthogonal projection within centered matrices normal to {A Omega:Omega^T=-Omega}. Define Z=(A+E)Q-A and

\[
q_*=\frac{2ar}{2s^2-ar}.
\]

Then Q is unique, proper, and smooth on this domain, and

\[
\|Q-I\|_F\le q_*,
\qquad
\boxed{\|Z-NE\|_F\le\frac1{\sqrt2}\left(\frac a2q_*^2+rq_*\right).}
\]

## Proof

Put S=A^TA and C=(A+E)^TA=S+E^TA. The path S+tau E^TA has smallest singular value>=s^2-ar>0 for0<=tau<=1. Its determinant stays positive. Its unique polar factor Q is therefore in SO(3), and gives the unique Procrustes optimum. Write C=QH,H positive definite,W=Q-I.

\[
\langle C-S,Q-I\rangle
=\operatorname{tr}[(H+S)(I-\operatorname{Sym}Q)]
\ge\frac{\sigma_{\min}(C)+\sigma_{\min}(S)}2\|W\|_F^2.
\]

Indeed I-Sym Q is positive semidefinite, with trace ||W||_F^2/2. Cauchy–Schwarz, ||E^TA||_F<=ar and sigma_min(C)>=s^2-ar imply ||W||_F<=q_*; W=0 is immediate.

Since A^T(A+E)Q=C^TQ=H, A^TZ is symmetric. Thus NZ=Z. N annihilates A Skew W, so

\[
Z-NE=N[A\operatorname{Sym}W+EW].
\]

Orthogonality gives Sym W=-W^TW/2. In SO(3), Q fixes an axis and rotates its orthogonal plane. Hence W has two equal nonzero singular values, or is zero, and

\[
\|W\|_2=\|W\|_F/\sqrt2,\qquad
\|\operatorname{Sym}W\|_F=\|W\|_F^2/(2\sqrt2).
\]

Contractivity of N, ||A Sym W||_F<=a||Sym W||_F, and ||EW||_F<=r||W||_2 prove the claim. Without the proper3D sharpening, the still-valid general majorant is a q_*^2/2+r q_*.

## Stored reference-curve specialization

The two retained primary-node NPZ datasets define cubic Hermite position curves at rational steps1/20 and1/40 on[0,100]. Coordinates and velocities are interpreted as exact dyadic data. This describes these stored curves, not certified exact-ODE solutions.

The original exact Fraction checks completed before the runtime disconnected. They showed nodal singular values strictly between187/100 and97/50. On every interval, the three Bernstein control differences from the first node have Frobenius norm<1/100. Convexity and Weyl perturbation give continuously

\[
\sigma_{\min}(A)>187/100-1/100>37/20,\qquad
\|A\|_2<97/50+1/100=39/20.
\]

For s=37/20,a=39/20,r=4/125,

\[
q_*=\frac{624}{33913},\quad
\|Z-NE\|_F
\le\frac{132102048}{143761446125\sqrt2}
<\frac{13}{20000}=0.00065.
\]

The last rational comparison follows by squaring positive quantities; the earlier unsharpened bound<23/25000 also remains valid.

For centered true error E=E_1+E_2, the sufficient split is

\[
\|E\|_F\le4/125,\quad
\|NE_2\|_F\le7/20000
\quad\Longrightarrow\quad
\|Z-NE_1\|_F<1/1000.
\]

E_2 must include nonlinear dynamics, reference defect, initial mismatch and derivative-flow error. These true-flow conditions remain **OPEN**. A sampled linear radius does not prove them. This proper-frame readout operation does not remove mechanical energy.

## Recovery status

This proof was reconstructed from the completed work after the compute workspace became unavailable. The exact binary primary data were preserved byte-for-byte before disconnection. The newly authored recheck_geometry.py is **NOT_RUN after reconstruction**. Original executed source files and full raw JSON/log capture remain to be recovered. Constructor proof/checks are not independent replication. See [recovery checkpoint](../../sessions/icosahedral-greenbounds-20261022-a1/CHECKPOINT.md).
