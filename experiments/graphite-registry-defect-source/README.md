# Registry defect behind a declared graphite bond-variance source

**Status:** EXACT finite-carrier symmetry theorem; NUMERICAL conventional KC-plus-plate reconstruction; CONDITIONAL physical proxy. Physical promotion 0; independent physics review NOT_RUN. The measured friction residual and native packet-to-material map remain OPEN.

## Question and dependencies

The [matched stationary Hessian](../graphite-matched-hessian-reconstruction/README.md) provides a registered positive $14\times14$ height stiffness $K$ at one model point. Its [declared proxy](../graphite-matched-hessian-reconstruction/analyze_proxy.py) chooses the physical bond observable $q_e=h_{B(e)}-h_{A(e)}$, and feeds its harmonic variance into a putative two-component port. What creates the nonuniform edge weights in that *assumed* construction? This note identifies the precise symmetry defect of the conventional $K$ responsible for them. It does not derive $q_e$ from a native UD signed edge variable, choose the seven-cell carrier over other indices, or identify a dissipative law.

## Exact group and cancellation

Number vertices $A_i,B_k$, $i,k\in\mathbb Z/7\mathbb Z$, and put an oriented edge $A_i\to B_k$ when $(i-k)\bmod7\in\{0,1,5\}$. The incidence $B_1:\mathbb R^{21}\to\mathbb R^{14}$ has $-1$ at $A_i$ and $+1$ at $B_k$. The existing embedding $M:\mathbb R^2\to\mathbb R^{21}$ assigns the three edge classes respectively $(1/2,1/2)$, $(-1/2,0)$ and $(0,-1/2)$, so $B_1M=0$ exactly.

Two graph automorphisms are

$$T:(A_i,B_k)\mapsto(A_{i+1},B_{k+1}),\qquad R:(A_i,B_k)\mapsto(A_{4i},B_{4k-1}),$$

with subscripts modulo 7. They obey $T^7=R^3=1$ and $RTR^{-1}=T^4$. The 21 distinct $T^tR^r$ are transitive on all 21 edges: $R$ permutes the three difference classes $0\to1\to5\to0$, and $T$ visits the seven bonds in each class. Integer incidence permutations verify $P_g B_1=B_1Q_g$.

For *any* positive definite $K$ in this registered basis, define $\overline K=\frac1{21}\sum_gP_gKP_g^T$, a positive definite group-invariant stiffness. The coefficients $\overline w_e=[B_1^T\overline K^{-1}B_1]_{ee}$ are equal on the transitive edge orbit. Consequently

$$S(\overline K)=M^T\operatorname{diag}(\overline w)B_1^T=\overline w\,(B_1M)^T=0.$$

The covariance coefficient is per $\overline\Theta=k_BT/14$, because the saved $K$ is the Hessian of energy per upper atom. Physical bond variance is $\overline\Theta w_e$. This symmetry result holds for the declared variance-to-port rule regardless of the numerical KC parameters; it says nothing by itself about measured friction.

Put $\Delta K=K-\overline K$. The resolvent identity is exact, with no small-defect expansion:

$$K^{-1}-\overline K^{-1}=-\overline K^{-1}\Delta K K^{-1},$$

$$S(K)=M^T\operatorname{diag}\!\left[\operatorname{diag}\{B_1^T(-\overline K^{-1}\Delta K K^{-1})B_1\}\right]B_1^T.$$

Thus every nonzero contribution to this *proxy* source is attributable to the conventional stiffness departure from the 21-element graph average. The inverse is nonlinear: the first-order substitution of $\overline K^{-1}$ for the rightmost $K^{-1}$ is only an approximation.

## Numerical replay at the registered stationary point

The [audit script](audit_registry_defect.py) reads the committed matched $K$ and independently builds the integer graph action. Its [results](REGISTRY_DEFECT_RESULTS.json) are:

| Diagnostic | Result |
| --- | ---: |
| $\|\Delta K\|_F/\|K\|_F$ | 0.00522957825 |
| Translation defect $\|TKT^T-K\|_F/\|K\|_F$ | 0.00798831273 |
| Rotation defect $\|RKR^T-K\|_F/\|K\|_F$ | $4.37\times10^{-10}$ |
| Smallest eigenvalue of $K$, $\overline K$ | 9.99899791, 10.04973177 meV/Å² per upper atom |
| Original bond coefficient mean and CV | 0.00211103749 Å²/meV; 0.93909% |
| Group-mean bond coefficient range | $5.20\times10^{-18}$ Å²/meV |
| $\|S(K)\|_F$, $\|S(\overline K)\|_F$ | $8.82972\times10^{-5}$, $4.34\times10^{-18}$ Å²/meV in native basis |
| Relative first-order source error | 7.48768% |

Although $\|\Delta K\|_F/\|K\|_F$ is 0.523%, $\|\overline K^{-1}\Delta K\|_2=0.7149$. The exact resolvent is therefore the reported decomposition; the first-order error should not be inferred from the Frobenius fraction alone. The group mean is fitted numerically by $10.04973178I-2.57621639L+118.23281239L^2$, $L=B_1B_1^T$, with relative residual $2.88\times10^{-12}$. This polynomial is a property of this numerical $K$, **not** a general group-theory theorem or a native UD stiffness law.

The counterfactual $\overline K$ is a group average, not a prepared graphite specimen or an observed load. It removes registry differentiation while preserving the seven-cell graph. The reconstructed conventional model is nearly $R$ invariant but differs under $T$; the proxy nonuniformity tracks that translation symmetry breaking. No parameter has been fitted to a friction trace in this audit.

## Force and damping gate

To obtain a physical signed residual, a native even packet observable must be shown to map to this covariance rather than merely permit it by parity; a force coefficient and frequency-dependent loss matrix must follow from material data or a constitutive derivation; and contact transfer must be measured. For an *independent* passive height bath $D_h=dI$ and separately assumed $C_{\rm port}=\beta\overline\Theta S$, the prior conditional $\Gamma_{\rm port}=\beta^2d\overline\Theta^2SK^{-2}S^T$ has a positive self-loss. A baseline-subtracted experiment with shared damping includes cross terms and need not have a positive signed residual. The [packet force contract](../graphite-packet-force-contract/README.md) and [cross-loss audit](../graphite-cross-loss/README.md) specify those missing conditions.

The graphite angle pair already follows conventional triangular reciprocal geometry via $\cos\theta=13/14$ and $60^\circ-\theta$. The published experimental report calls the pair sharp friction **peaks** with weak load dependence. This audit supplies neither their selection nor a prediction of remaining friction at them. Its next discriminant is an independent, registration-preserving measurement of bond-height covariance and complex loss versus load and direction, followed by a frozen parameter residual test against conventional moiré predictions.

Run `python3 experiments/graphite-registry-defect-source/audit_registry_defect.py` at repository root. The [mathematical receipt](../../candidates/graphite-registry-defect-source/mathematical_receipt.json) and [immutable capture](../../artifacts/graphdefect-20261025-01/registry-001/manifest.json) preserve the run inputs and result.
