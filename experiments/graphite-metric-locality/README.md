# Can a local positive UD metric carry the graphite height spectrum?

**EXACT/CONDITIONAL** finite-carrier metric identities; **NUMERICAL/FIT** inverse design from the registered conventional KC stiffness. The construction is a bridge test, not a native selection or measured friction model. Physical promotion 0; independent physics review NOT_RUN.

## Question and typed setup

The [quadrature audit](../graphite-quadrature-obstruction/README.md) found an 18.7354% best scalar-clock operator defect when the native fixed-mask, unit-metric incidence packet is identified with the graphite bond-height oscillator. Here the only allowed change in the first test is a symmetric positive **vertex energy metric** $H_v$; the edge energy metric stays $H_e=I$. Can a short-range $H_v$ reproduce the model spectrum while retaining a reciprocal, positive native generator? Does it also reproduce the registry-dependent even source?

Use the 14-site/21-edge real carrier with integer incidence $B:\mathbb R^{21}\to\mathbb R^{14}$, $L=BB^T$, and the 21-element bond-transitive group from the [registry audit](../graphite-registry-defect-source/README.md). The registered conventional positive $K$ has units meV/Å² per mean upper atom; $E_{\rm tot}=7h^TKh+p^Tp/(2m)$. All model numbers come from the [matched stationary reconstruction](../graphite-matched-hessian-reconstruction/README.md), whose archived Cartesian reference was selected in earlier development. The physical mass $m$, clock $\tau$, bond map and dissipation are not supplied by UD.

For the gradient edge sector $y\in\operatorname{im}B^T$ with $z=0$, define the **new candidate** native energy $E_n=(x^TH_vx+y^Ty)/2$ and reciprocal skew-incidence update in dimensionless $s$:

$$x'=By,\qquad y'=-B^TH_vx,\qquad y''=-B^TH_vBy.$$

For any $H_v\succ0$, the quadratic energy is conserved and the generator is skew-adjoint in the $\operatorname{diag}(H_v,I)$ metric. This is not the original unit-metric $H=I$ packet. If $s=t/\tau$ and the [odd physical quadrature](../graphite-quadrature-obstruction/README.md) is still identified with $y$ for all momentum preparations, an exact dynamical match requires

$$B^TH_vL=c^{-1}B^TK,\qquad c:=\frac{m}{14\tau^2}>0.$$

Equivalently we fit an unscaled stiffness-shaped $G=cH_v$ to $B^TGL=B^TK$. No value of $c$ or physical time is inferred. The diagram is a conditional intertwining requirement, not a definition of physical friction.

## A two-hop positive solution for the symmetry average

Let $\bar K$ be the average of $K$ over the 21 carrier automorphisms. The [exact integer replay](replay_metric.py) verifies

$$\operatorname{spec}(L)=\{0^{(1)},(3-\sqrt2)^{(6)},(3+\sqrt2)^{(6)},6^{(1)}\}.$$

On the positive spectrum $\lambda^3-12\lambda^2+43\lambda-42=0$, so $\lambda^{-1}=(\lambda^2-12\lambda+43)/42$. The **numerical** group mean in this conventional model is $\bar K\simeq aI+bL+c_2L^2$, with $(a,b,c_2)=(10.049731775,-2.576216393,118.232812394)$ meV/Å² and relative Frobenius discrepancy $2.88\times10^{-12}$. Consequently the vertex-metric *inverse design*

$$G_{\rm sym}=g_0I+g_1L+g_2L^2,\quad
(g_0,g_1,g_2)=\left(b+\frac{43a}{42},\ c_2-\frac{2a}{7},\ \frac{a}{42}\right)$$

has numerical coefficients $(7.712794710,115.361460458,0.239279328)$ in the units of $K$. It is positive on all 14 modes (smallest eigenvalue $7.712794710$) and has support no farther than two graph hops. $B^TG_{\rm sym}L=B^T\bar K$ to relative $2.25\times10^{-12}$ in the numerical reconstruction. Dividing by any positive $c$ makes a dimensionless positive $H_v$ once physical mass and time units are fixed. This **exists** for the conventional symmetry average; the coefficient values are selected from its $K$, and the polynomial representation is not a theorem for arbitrary graphite.

The averaged $\bar K$ gives *uniform* bond covariance and zero proposed source. A vertex-only metric does not repair that: in its separable canonical native energy with $H_e=I$, unconstrained edge Gibbs variance is uniform. Even if the gradient subspace is imposed, its covariance is proportional to the edge projector $B^TL^+B$, whose 21 diagonal entries all equal $13/21$. Therefore $M^T\operatorname{diag}\langle y_e^2\rangle B^T=0$ independently of $H_v$. Matching the averaged frequency bands does not produce the sought nonuniform source. An edge energy metric, open-system preparation, or other constitutive change would have to supply it.

## The actual registered stiffness

The conventional $K$ has a small but nonzero registry defect. Let $P=I-\mathbf1\mathbf1^T/14$. An **exact** solution with symmetric vertex-only $G$ requires both $PK\mathbf1=0$ and $[PKP,L]=0$ on $P\mathbb R^{14}$: $L$ has no uniform-mode input, and $PKL_P^{-1}$ must be symmetric. The numerical $K$ violates both conditions. In particular its $K\mathbf1$ row-sum span is $17.0272$ meV/Å² per atom, and $\|[PKP,L]\|_F/(\|K\|_F\|L\|_F)=8.72827\times10^{-4}$. These are properties of the chosen conventional finite-Hessian model, subject to its finite-difference and parameter accuracy.

The best positive symmetric fit $G_{\rm opt}$ is explicit. In an eigenbasis $Lv_i=\lambda_i v_i$ on $P\mathbb R^{14}$,

$$\langle v_i,G_{\rm opt}v_j\rangle=\frac{2\langle v_i,Kv_j\rangle}{\lambda_i+\lambda_j},\qquad \lambda_i,\lambda_j>0.$$

It uniquely minimizes $\|B^T(GL-K)\|_F$ on this subspace; its uniform-mode eigenvalue is freely chosen positive. It is positive because $G_{\rm opt}|_P=2\int_0^\infty e^{-Lt}(PKP)e^{-Lt}\,dt\succ0$. This general fitted matrix need not be local. The [numerical replay](METRIC_RESULTS.json) compares constrained fits:

| Positive metric, all fitted to conventional $K$ | Relative $\|B^T(GL-K)\|_F/\|B^TK\|_F$ |
| --- | ---: |
| Scalar $G=cI$ (one fitted scale) | 18.7354% |
| Two-hop, group-mean polynomial $G_{\rm sym}$ (three model-derived coefficients) | 0.385813% |
| One-hop symmetric $G$ (35 fitted site/bond entries) | 0.219415% |
| Arbitrary symmetric positive $G_{\rm opt}$ | 0.170910% |

The latter residual has an irreducible uniform-input component $0.089710\%$ and a noncommuting component $0.145474\%$ in quadrature under this Frobenius objective. The 35-parameter one-hop fit is positive in this model, but its flexibility and exposure to $K$ make its small residual **fit quality**, not predictive UD physics. Adding edge metrics or extra state changes the model and can evade this scoped obstruction.

There is a separate *mode budget* constraint on any closed gradient-only vertex/edge oscillator with the same readout. Its positive dynamical subspace has 13 oscillator coordinates. The actual $K$ does not preserve the uniform site vector. No $K$ eigenvector is therefore completely invisible to $B^T$, and the spectral-weight ranks of the registered physical bond process sum to **14** across its ten distinct model frequency groups. The softest mode has small but nonzero edge projection norm $0.0145636$, versus $0.0145628$ under the archived alternate Hessian step. A 13-coordinate gradient oscillator cannot reproduce all these independent spectral weights exactly under the same linear readout. This is a model-specific statement: the full native edge/face sectors have additional coordinates and a different constitutive extension could couple them. It does not establish that the extra weak mode is experimentally resolved.

## Bridge decision

Positive, finite-range native metric *existence* removes the simplistic claim that the three-band frequency mismatch alone forbids a UD bridge. It does not select that metric, generate the registry source, or derive material damping. A useful next test must source a positive edge metric or contact preparation and include the cycle/face sector only if its mode and power balance are specified; then independently calibrate complex loss and contact transfer before a frozen signed force/load prediction. The measured 21.8° and 38.2° pair is already geometrically explained by conventional triangular commensurability, so this inverse-designed metric does not select the angles.

Run `python3 experiments/graphite-metric-locality/replay_metric.py` from repository root. The [mathematical receipt](../../candidates/graphite-metric-locality/mathematical_receipt.json) and [immutable capture](../../artifacts/graphmetric-20261026-01/metric-001/manifest.json) record dependencies, proof scope, exact incidence, and numerical checks. Independent physics review NOT_RUN.
