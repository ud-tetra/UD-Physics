# Joint conservative quadrature on the graphite carrier

**EXACT/CONDITIONAL** finite-carrier identity; **NUMERICAL/FIT** replay of an exposed conventional KC-plus-plate Hessian. This is a single positive reciprocal oscillator with an assumed, nonlocal observable. It is not a native material-source law, measured friction prediction, or selection of a twist angle. Physical promotion 0; independent physics review NOT_RUN.

## Question, provenance, and normalization

The [edge-metric/contact audit](../graphite-edge-metric-contact/README.md) exhibited two *different* metrics: one reproduced the conventional bond covariance, the other restored the fourteenth oscillator coordinate. Can **one** positive reciprocal system reproduce the registered conservative bond spectrum and nonuniform covariance? What happens if its native edge coordinates are used instead of a target-informed readout?

Let $B:\mathbb R^{21}\to\mathbb R^{14}$ be the oriented seven-cell honeycomb incidence and $M:\mathbb R^2\to\mathbb R^{21}$ the harmonic port basis. Both are the previously declared carrier. The conventional $K\succ0$ is in meV/Å² **per upper atom**; $E_{\rm phys}=7x^TKx+p^Tp/(2m)$, and $\Theta_{\rm bar}=k_BT/14$. Its archived Cartesian reference was selected in earlier development; its values are not independent targets here. The physical bond-height proxy is $q=B^Tx$. A signed friction force, complex loss, and measured pressure derivatives are unavailable.

For an **assumed** external grounded contact $e_{A0}$, set $A=[B\;e_{A0}]$, $L_A=AA^T$, $P_A=A^TL_A^{-1}A$ and choose any $\zeta>0$. Define

$$H_e=A^TL_A^{-2}A+\zeta(I-P_A),\qquad AH_eA^T=I_{14}.\tag{1}$$

Let $s=t/\tau$, $a=14\tau^2/m>0$, and set the **target-selected** vertex stiffness $H_v=aK$. The positive reciprocal candidate has $x\in\mathbb R^{14}$, $y\in\mathbb R^{22}$ and

$$E_n=\tfrac12(x^TH_vx+y^TH_ey),\qquad x'=AH_ey,\quad y'=-A^TH_vx.\tag{2}$$

The cycle/kernel sector may be initialized at zero; $y\in\operatorname{im}A^T$ then stays there, because $y'$ lies in that subspace. If $y=A^Tv$, then $x'=v$, $E_n=(a x^TKx+|x'|^2)/2$, and $x''=-aKx$. Multiplying the energy by $m/\tau^2$ and identifying $p=(m/\tau)x'$ reproduces $E_{\rm phys}$ and $\ddot x=-(14/m)Kx$. This is an exact isomorphism to the conventional oscillator **by inverse design**. It imports $K$, $m$, $\tau$, and an external reference; the graph alone supplies none of them. The generator is skew-adjoint in $\operatorname{diag}(H_v,H_e)$ and conserves $E_n$.

## Odd readout and the exact conservative process law

Define an **assumed material observable** from the native state:

$$r=\frac{1}{\sqrt a}B^TK^{-1/2}x'
=\frac{1}{\sqrt a}B^TK^{-1/2}AH_ey.\tag{3}$$

$r$ is odd under the declared physical time reversal $x\mapsto x$, $y\mapsto-y$. Its units are Å, as are those of $q$. The symmetric positive inverse square root is fixed by the exposed conventional $K$; it is **not** a native incidence identity or a locally sourced UD readout. At canonical equilibrium, $\Theta_n=(\tau^2/m)k_BT=a\Theta_{\rm bar}$ in the units of $E_n$, so $\operatorname{Cov}(x)=\Theta_{\rm bar}K^{-1}$ and $\operatorname{Cov}(x')=a\Theta_{\rm bar}I$. Consequently, with $Q=B^TK^{-1}B$,

$$\operatorname{Cov}(q)=\operatorname{Cov}(r)=\Theta_{\rm bar}Q.\tag{4}$$

More strongly, their **individual** stationary two-time covariance matrices coincide for every lag $\Delta s$:

$$C_q(\Delta s)=C_r(\Delta s)=\Theta_{\rm bar}B^TK^{-1}\cos(\sqrt{aK}\,\Delta s)B.\tag{5}$$

The equality follows from Gaussian canonical preparation and the matrix functional calculus for $K$. It includes the weak fourteenth conventional mode, whose $B^T$ projection is small but nonzero in the registered model. It is an equality of the separate conservative Gaussian process laws; their mixed $q$–$r$ covariance and instantaneous trajectories differ. The cosine kernel is lossless and cannot determine a positive drag coefficient.

The prior assumed port $S=M^T\operatorname{diag}(w)B^T$ gets the same **model-derived** weights $w_e=Q_{ee}$ from either (4) readout. Its rank is two and its uncalibrated norm is $8.82971824\times10^{-5}$ in the existing port convention. Because $K^{-1/2}$ is selected from conventional material stiffness, this is a reconstruction of that proxy, not a residual after a conventional subtraction.

## Native edge identity obstruction in the same construction

For the invariant row sector, $y=A^Tx'$ and the quadratic energy in $x'$ is isotropic. Thus

$$\operatorname{Cov}(y)=a\Theta_{\rm bar}A^TA,qquad
\operatorname{Var}(y_e)=2a\Theta_{\rm bar}\quad(e\leq21).\tag{6}$$

All 21 internal bonds have equal variance, so $M^T\operatorname{diag}(\operatorname{Var}(y_{1:21}))B^T=0$. This holds for **any** $H_e$ giving $AH_eA^T=I$ when the canonical ensemble is restricted to $y\in\operatorname{im}A^T$: write $y=A^Tv$ and integrate the unit quadratic form $|v|^2/2$. Allowing kernel preparation, a different kinetic metric, or a different readout changes the premises. In particular, equation (3) solves the covariance/spectrum matching problem by changing the observable; it does not turn the literal native edge $y_e^2$ into the nonuniform source.

## Replay and decision

In a numerical replay with $a=\Theta_{\rm bar}=1$, the positive metric and reciprocal generator pass at relative error below $2\times10^{-14}$; the even/odd covariance agreement is $2.6\times10^{-15}$ or better, and tested lag matrices agree to $2.6\times10^{-15}$. Raw internal-edge variance is exactly 2 to numerical precision and its port is zero. The $K^{-1/2}$ map has 79.12% of its Frobenius norm off the site diagonal in this conventional model. These figures are constructor checks, not empirical accuracy or a bound on material-model error.

The conditional bridge can now carry the full conservative covariance and frequency content in **one** positive oscillator, but only through a nonlocal target-informed quadrature. Supplied ledger v0.39(2) Q22 records a zero seam-pairing current in its scope; Q24–Q26 do not derive the graphite edge weight/route law; Q166/Q167/Q170 describe native stock flow without physical damping. None selects the contact, $K^{-1/2}$, or $\tau$. The ordinary $(2,1)$ triangular coincidence already explains the 21.8°/38.2° angle complement; the present construction adds no angle-dependent residual force.

The next discriminant is a **sourced local or controlled-range readout and contact law** that predicts nonuniform covariance without importing $K^{-1/2}$, followed by an independently identified material loss/contact tensor and a frozen signed conventional-subtracted force/load test. [Replay](replay_joint.py), [results](JOINT_RESULTS.json), [receipt](../../candidates/graphite-joint-quadrature-contact/mathematical_receipt.json), and [immutable capture](../../artifacts/graphjoint-20261027-01/joint-001/manifest.json) record the scope.
