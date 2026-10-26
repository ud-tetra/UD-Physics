# Positive edge metric and a minimal external contact: graphite bridge audit

**EXACT/CONDITIONAL** finite-graph constructions; **NUMERICAL/FIT** use of the registered conventional KC-plus-plate Hessian. This result does not derive a graphite friction force, a native constitutive law, or angle selection. Physical promotion 0; independent physics review NOT_RUN.

## Question and conventions

The [vertex-metric audit](../graphite-metric-locality/README.md) left two scoped gaps: a unit edge Gibbs metric has equal bond variances and zero proposed source, and a 13-coordinate closed gradient oscillator cannot exactly carry all 14 spectral-weight coordinates of the registered conventional bond process. Can a positive edge metric and one additional contact solve these **mathematical** gaps, and what physics is imported when they do?

Let the oriented integer incidence be $B:\mathbb R^{21}\to\mathbb R^{14}$, $L=BB^T$, $P=I-uu^T$, $u=\mathbf1/\sqrt{14}$, $G=\operatorname{im}B^T$, and $P_G=B^TL^+B$. Then $\operatorname{rank}B=13$, $P_G$ has rank 13, and its orthogonal complement $P_C=I-P_G$ has rank 8. The archived conventional positive $K$ is measured in meV/Å² **per mean upper atom**, with $E_{\rm total}=7h^TKh+p^Tp/(2m)$ and $\Theta_{\rm bar}=k_BT/14$. The *assumed proxy* is $q=B^Th$, so $\operatorname{Cov}(q)=\Theta_{\rm bar}Q$, $Q=B^TK^{-1}B$. The port $S=M^T\operatorname{diag}(\operatorname{diag}Q)B^T$ is the earlier assumed harmonic readout. It is not an observed force.

## Exact positive metric for the exposed covariance

$Q$ is positive on $G$ and zero on the cycle sector. Choose any $\eta>0$ with the units of $Q^+$ and define

$$H_{e,\rm cov}=Q^++\eta P_C.\tag{1}$$

This full 21-dimensional matrix is positive definite. If a **separately assumed** canonical edge equilibrium has energy $y^TH_{e,\rm cov}y/2$ and temperature scale $\Theta_{\rm bar}$, its covariance *conditioned on* $G$ is exactly $\Theta_{\rm bar}P_GH_{e,\rm cov}^{-1}P_G=\Theta_{\rm bar}Q$. An unconstrained 21-edge Gibbs state has an additional cycle covariance $\Theta_{\rm bar}\eta^{-1}P_C$ and does **not** match the proxy; the gradient constraint is essential.

The inverse metric has a useful explicit expression. Since $u$ need not be an eigenvector of registered $K$, let

$$K_{\rm eff}=PKP-\frac{(PKu)(u^TKP)}{u^TKu},\qquad Q^+=B^TL^+K_{\rm eff}L^+B.\tag{2}$$

This is the positive Schur complement of the uniform site coordinate. It exposes the imported conventional stiffness and its uniform-mode mixing. The [replay](replay_edge.py) agrees with (2) to relative $2.49\times10^{-15}$, and the covariance to $3.01\times10^{-15}$. The imported source has rank 2 and norm $8.82972\times10^{-5}$ in the earlier uncalibrated port convention, versus zero for the unit edge metric; the bond-weight coefficient of variation is 0.9391%. These are **model outputs constructed to match $K$**, not new predictions. Among the 21×21 inverse-metric entries, 168 unordered pairs of bonds that do not meet at a vertex have nonzero entries at a $10^{-10}$ relative threshold. Thus this *specific exact inverse design* is not a diagonal or one-hop edge metric. Other local metrics or enlarged states are not excluded.

## One grounded contact completes the missing coordinate

Every closed internal-incidence column sums to zero. Thus a 14-site system with only such columns has rank at most 13, whatever positive edge metric is selected. Appending **one** external-reference contact $a=e_{A0}$ gives $A=[B\;a]\in\mathbb R^{14\times22}$ with rank 14 and $L_A=AA^T\succ0$. One is the minimum number of additional columns that can increase this rank. This grounded edge is an **assumed open-system coupling**, not another honeycomb bond; the alternative $a=u$ is a global rather than site-local contact.

With $R=A^TL_A^{-1}A$ and any $\zeta>0$, define the positive edge metric

$$H_{e,\rm contact}=A^TL_A^{-2}A+\zeta(I-R),\qquad AH_{e,\rm contact}A^T=I_{14}.\tag{3}$$

For a positive vertex metric $H_v$, the reciprocal continuous native *candidate* with dimensionless $s=t/\tau$ is

$$E_n=\tfrac12(x^TH_vx+y^TH_{e,\rm contact}y),\quad x'=AH_{e,\rm contact}y,\quad y'=-A^TH_vx,\quad x''=-H_vx.\tag{4}$$

Its energy is conserved and its generator is skew-adjoint in the positive energy metric. The physical harmonic equation from the above $E_{\rm total}$ is $\ddot h=-(14/m)Kh$. If $x=h$ is **assumed** and $H_v=(14\tau^2/m)K$ is **set using the conventional target**, (4) reproduces that oscillator exactly for *any* positive $K$. It says nothing about the parity-compatible bond readout or equilibrium source under the same 22-edge state. The native unit of $x$, the energy scale multiplying $E_n$, $m$, $\tau$, and a material grounding mechanism have not been supplied by UD.

For $a=e_{A0}$, $\lambda_{\min}(L_A)=0.0514040$ and $\kappa_2(L_A)=118.89$; for the nonlocal $a=u$, $\kappa_2=6$. Numerical errors in (3), metric skew-adjointness, and the conditional oscillator identity are below $2\times10^{-14}$ relative. The grounded construction's $H_e$ is another nonlocal inverse design. Equations (1) and (3) are **different metrics** and have not been shown to give covariance, spectrum, native source, and reciprocal friction simultaneously.

## Bridge decision and next discriminant

The earlier 13-versus-14 budget is a closed-incidence constraint, and one externally referenced contact evades it. The nonuniform stationary port can be represented with a positive edge metric, but the exact construction imports the conventional $K$ and its registry dependence. These existence results do not select the 21.8°/38.2° pair, whose complementarity already follows from conventional $(2,1)$ triangular commensurability. They also add no positive loss: (4) is conservative. A useful next step is to specify one **native sourced** edge/contact metric and preparation, establish the joint covariance and spectral readout, then independently determine complex loss/contact transfer and test a frozen signed conventional-subtracted force/load residual. The missing experimental force and linewidth data prevent a numeric friction claim here.

Run `python3 experiments/graphite-edge-metric-contact/replay_edge.py` from repository root. [Results](EDGE_RESULTS.json), [mathematical receipt](../../candidates/graphite-edge-metric-contact/mathematical_receipt.json), and [immutable capture](../../artifacts/graphedge-20261026-01/edge-001/manifest.json) give reproducibility and provenance.
