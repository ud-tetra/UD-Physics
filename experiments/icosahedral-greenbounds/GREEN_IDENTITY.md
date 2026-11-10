# Forced mean-volume response v1.0 — recovery checkpoint

**EXACT/CONDITIONAL identities; NUMERICAL evaluations.** Basece89a9cd15439463d9a64d983d91c22ea4368726; unchanged MountLoss model at seed10422-0-boundary2,nu=.05,beta=.05,c_f=.001,T100. Retain280 configuration coordinates,560 mechanical phase variables and all reactions. Diagnostic heat does not feed mechanics.

For a specified reference yhat, let A(t)=Df(yhat(t)),U(t,s) its full evolution operator, and l(t) the derivative of the arithmetic mean of20 normalized oriented cell volumes. With positive generalized mass matrix M, acceleration source BF=[0;M^(-1/2)] has280 mass-normalized force channels.

\[
P(s)=\int_s^T U(t,s)^Tl(t)^Tl(t)U(t,s)\,dt,\qquad
-P'=A^TP+PA+l^Tl,\quad P(T)=0.
\]

P is an output observability Gramian. It may be semidefinite and is not a positive full-state continuation norm.

For the existing energy-normalized housing injection B:R180->R560,

\[
Q_B=\frac1T B^TP(0)B
=\frac1T\int_0^T(l(t)U(t,0)B)^T(l(t)U(t,0)B)\,dt.
\]

This permits complementary backward560x560 and forward560x180 computations on the same reference.

Partition BF into alpha1, primary39, device150 and housing90 columns. Define

\[
\gamma_j^2=\frac1T\int_0^T\operatorname{tr}(BF_j^TP(s)BF_j)\,ds.
\]

The Volterra kernel l(t)U(t,s)BF_j for s<=t has this Hilbert–Schmidt norm from input L2(du) to output RMS(du/T). Cauchy–Schwarz gives

\[
\left[\frac1T\int_0^T\left|l(t)\int_0^tU(t,s)BFu(s)\,ds\right|^2dt\right]^{1/2}
\le\sum_j\gamma_j\|u_j\|_{L^2}
\le\sqrt{\sum_j\gamma_j^2}\|u\|_{L^2}.
\]

These are sufficient, generally nonoptimal gains. Arbitrary mathematical source checks may inject net force; no such external forcing is added to the passive constitutive model.

Normal full-state Hermite interpolation has a kinematic defect and acceleration sources cannot cover its complete reference error. The refined cubic reference uses positional Hermite q and v=q' exactly. Its defect then has only an acceleration block. The error-equation source is -sqrt(M)d_v. Nonlinear Taylor remainder also has acceleration support, but its norm on a true-state tube remains to be bounded.

All evaluated gains use float64, not validated integration. Four deterministic smooth forcing checks passed numerically. Composite3/5-point Gauss defect norms give a scalar cubic-reference HS expression~.005032, larger than the approximate remaining breathing margin~.001764. This rejects that coarse sufficient error-budget route; it is not the actual defect response or a dynamical counterexample.

A later C2 quintic-reference diagnostic reduces measured defect norms substantially. **Do not transfer cubic-reference Green gains to the quintic reference.** Its Gramian, continuous geometry and validated error enclosure remain uncomputed.

The scalar gains do not supply primary-position sup-time bounds, a positive full-state norm, nonlinear Hessian bounds or an all-phase/continuous-property certificate. See [recovery results](README.md).
