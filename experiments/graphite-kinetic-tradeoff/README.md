# Reciprocal kinetic-metric tradeoff for a local graphite odd readout

**EXACT/CONDITIONAL** finite positive-metric compatibility theorem; **NUMERICAL/FIT** conventional registered KC-plus-plate Hessian evaluation. This tests one proposed escape from the [endpoint-local readout bound](../graphite-local-readout-bound/README.md). It is not a measured friction or native UD constitutive result. Physical promotion 0; independent physics review NOT_RUN.

## Question and declared model

If a correlated site velocity replaces the isotropic velocity assumed in the previous local-readout bound, can the literal local odd gradient have the conventional nonuniform bond covariance **while** preserving the registered height covariance and bond dynamics?

Let $B:\mathbb R^{21}\to\mathbb R^{14}$ be the oriented seven-cell honeycomb incidence. It has rank 13, $B^Tu=0$ for $u=\mathbf1/\sqrt{14}$, and its image covers the nonuniform site subspace. The exposed conventional $K\succ0$ has units meV/Å² per mean upper atom. The physical benchmark is $E_{\rm phys}=7x^TKx+p^Tp/(2m)$, $\Theta_{\rm bar}=k_BT/14$, $q=B^Tx$, and

$$Q:=\operatorname{Cov}(q)/\Theta_{\rm bar}=B^TK^{-1}B,\quad q''=-aB^TKx,\quad a=14\tau^2/m>0,\tag{1}$$

where $s=t/\tau$ and prime denotes $d/ds$. No physical value of $m$ or $\tau$ is inferred.

Consider a **new assumed** reciprocal Hamiltonian with positive symmetric vertex and kinetic metrics $V,G\succ0$:

$$E_n=\tfrac12x^TVx+\tfrac12\pi^TG\pi,\quad x'=G\pi,\quad\pi'=-Vx,\quad x''=-GVx.\tag{2}$$

At canonical equilibrium with $\Theta_n=a\Theta_{\rm bar}$, $\operatorname{Cov}(x)=a\Theta_{\rm bar}V^{-1}$ and $\operatorname{Cov}(x')=a\Theta_{\rm bar}G$. Set $V=aK$ using the exposed target, which preserves the complete site height covariance. To make the *local* odd readout dimensional, choose an otherwise arbitrary positive stiffness scale $\kappa$ and put

$$r_\kappa=\frac{B^Tx'}{\sqrt{a\kappa}},\qquad
\operatorname{Cov}(r_\kappa)/\Theta_{\rm bar}=\frac1\kappa B^TGB.\tag{3}$$

$a\kappa$ is dimensionless, so $r_\kappa$ has length units. Its parity under the stated physical reversal is odd. $\kappa$ is a chosen material normalization, not a native coefficient.

## Exact compatibility theorem

Require the registered **bond acceleration for every initial site displacement** $x$: $B^TGV=B^TaK$. With $V=aK$ and invertible $K$, this gives $B^T(G-I)=0$. Symmetry of $G$ and $\ker B^T=\operatorname{span}\{u\}$ then force

$$G=I+\gamma uu^T,\quad\gamma>-1.\tag{4}$$

The unconstrained uniform-mode factor $\gamma$ has no effect on the internal odd gradient: $B^TGB=B^TB$. Each internal bond has equal variance $2\Theta_{\rm bar}/\kappa$ in (3), so the prior variance port cancels. Exact matching of the target $Q$ would require $Q=\kappa^{-1}B^TB$. This is a *necessary* condition under the stated full-preparation bond-acceleration and canonical covariance requirements. It is false for the registered conventional $K$. The proof is structural and does not require a fitted damping parameter.

## A positive covariance fit that loses the spectrum

The explicit target-informed alternative $G=\kappa K^{-1}$ is positive and gives $\operatorname{Cov}(r_\kappa)=\Theta_{\rm bar}Q$ exactly. It also leaves the even $q$ covariance correct because $V=aK$. But

$$GV=a\kappa I,\qquad
C_{q,\rm fit}(\Delta s)=\Theta_{\rm bar}Q\cos(\sqrt{a\kappa}\,\Delta s),\tag{5}$$

whereas the registered conventional process has $C_{q,\rm phys}=\Theta_{\rm bar}B^TK^{-1}\cos(\sqrt{aK}\,\Delta s)B$. The fit collapses every site frequency to the same value. It changes the physical kinetic energy/mass map and cannot be interpreted as the same oscillator.

The lag-zero covariances agree by construction. Their second derivatives would agree only if $\kappa Q=B^TB$. Minimizing $\|B^TB-\kappa Q\|_F/\|B^TB\|_F$ over positive $\kappa$ yields $\kappa_*=578.218475$ meV/Å² and an irreducible **79.0298372%** short-time curvature defect for the registered model. Its $K$ eigenvalues range from about 9.999 to 4250.978 meV/Å² in the reconstructed normalization. The archived nominal/alternate Hessian steps at relative pressures $-2.5,0,+2.5$ MPa give curvature defects between **79.0292486% and 79.0304160%**. This sensitivity range is within the same exposed conventional reconstruction, not an experimental confidence interval. The symbolic theorem does not depend on those numerical values.

The [replay](replay_kinetic.py) also verifies the positive uniform-mode freedom in (4), exactly vanishing local source, target-matched covariance for $G=\kappa K^{-1}$, and the flat frequency operator. The fitted $\kappa$ is chosen from the exposed $Q$ and $B^TB$ for the curvature comparison. No scalar choice repairs the full spectrum.

## Scope and next discriminant

This closes the **particular** correlated-kinetic escape in which $x$ retains its physical height meaning, $V=aK$, the odd map is a local $B^Tx'$ with one common scale, equilibrium is canonical, and the full bond acceleration holds for every initial site displacement. A weaker observable-only match, a changed even readout, shared edge/bath states, memory, nonreciprocal driving, or a nonlocal/controlled-range odd map changes the premises. Each such proposal must supply its own positive energy, preparation, power balance, and full covariance/spectrum test. The present model has no damping, signed measured friction, load law, or UD-specific explanation of the 21.8°/38.2° pair beyond the conventional $(2,1)$ geometry.

[Results](KINETIC_RESULTS.json), [mathematical receipt](../../candidates/graphite-kinetic-tradeoff/mathematical_receipt.json), and [immutable capture](../../artifacts/graphkin-20261028-01/kinetic-001/manifest.json) record the proof scope and replay. Independent physics review NOT_RUN.
