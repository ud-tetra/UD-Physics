# Global icosahedral flat-cell energy: rank-free Gram relaxation fails

**RESULT — EXACT / CONDITIONAL / FAILED RELAXATION; separate NUMERICAL exploratory search.**

- Session/claim: `phasewindow-20261022-gpt6-7c41`; held task `icosahedral-phasewindow-20261022`.
- Work branch: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
- Verified current `main`: `1b214f66e00e8430fed0ce7c23506da7965bc977`; original mechanical model and source graph imported at its SHA, read-only.
- Question: can a barrier calculation establish that no *three-dimensional* cell can flatten with energy below the original pulse energy? In particular, is dropping spatial-rank constraints in a positive-semidefinite Gram relaxation sound for a positive certificate?
- **Finding: no**. A mathematical rank-four Gram witness has an exactly flattened face and primary spring energy strictly below the pulse budget. This falsifies a rank-*unrestricted* Gram energy lower bound, **not** the sought three-dimensional barrier and **not** a physical four-dimensional model.

## Typed spaces and energy

Let \(C\in\mathbb R^3\) be the original icosahedral centre and \(X_1,\dots,X_{12}\in\mathbb R^3\) shell vertices. Fix translation by \(C=0\), so the physical primary geometry is a \(3\times12\) matrix \(X\). Its symmetric Gram \(G=X^TX\in\mathbb S_+^{12}\) has **rank at most three**. The shell graph has exactly twelve spokes and thirty exterior edges; twenty exterior triangles label the centre-to-face tetrahedra.

At reference exterior-edge length \(\ell_0=1\), \(R^2=(5+\sqrt5)/8\) and original constitutive energy

\[
 U_{\rm primary}=\tfrac12\left[\alpha^2+\sum_{i=1}^{12}\left(\frac{|X_i|}{R}-1\right)^2+\sum_{i=1}^{12}g_i\left(\frac{|X_i|}{R}-1-\alpha\right)^2+\sum_{(i,j)\in E}k_{ij}(|X_i-X_j|-1)^2\right].
\]

Use the **allowed** lower endpoints \(g_i=19/20\), \(k_{ij}=19/50\). Other device/housing storage is nonnegative and can be zero in a static primary configuration by selecting consistent internal coordinates; no 4D dynamics are implied. Initial original pulse plus previously enlarged housing phase energy is bounded by

\[
 E_{\rm pulse}\le\frac{1,360,051}{20,000,000}=0.06800255.
\]

A collapsed original centre-face tetrahedron has rank \(\le2\) for its three vectors \((X_i,X_j,X_k)\); equivalently, the \(3\times3\) principal face Gram determinant is zero.

## Exact rational counterexample **only to rank-free Gram optimization**

The file `gram_rank_witness.json` contains eleven 4D vertex vectors with rational components of denominator 10000; the twelfth (`k=2`) is set **exactly** as \(X_k=pX_i+qX_j\), where \(p,q\in\mathbb Q\) are frozen rational coefficients. The scalar \(\alpha\) is frozen to a rational. No floating-point coordinates enter the exact checker.

The standard-library `gram_rank_witness.py` verifies:

1. The three selected vectors have rank **exactly two**; their Gram determinant is zero over \(\mathbb Q\).
2. Four shell vectors have a nonzero \(4\times4\) determinant, so \(\operatorname{rank}(X)=\operatorname{rank}(X^TX)=4\). The resulting \(G=X^TX\) is positive semidefinite and **cannot** represent the original 3D geometry.
3. The original 12-vertex / 30-edge combinatorial graph is constructed from exact \(\mathbb Q(\sqrt5)\) squared distances, with frozen canonical vertex order. All twelve radial and thirty exterior edge lengths are strictly positive.
4. Every irrational length in the energy is enclosed between rational square-root bounds, including the reference circumradius. Interval upper bounds on the actual squared strains prove, using `fractions.Fraction` only,

\[
 \boxed{U_{\mathrm{4D\;relax\;witness}}<\frac1{20}<\frac{1,360,051}{20,000,000}=E_{\rm pulse}.}
\]

The strict numeric upper bound shown by the exact checker is about `0.047842110843` (display only). A separately authored SymPy checker confirms face rank 2, total rank 4, exactly 30 graph edges, and high-precision energy `0.047842110842368...`. The SymPy decimal is only a cross-check: the **strict** energy inequality is certified by the rational enclosures in the primary checker.

### Logical implication

Consider the relaxed problem over **all** \(G\succeq0\), imposing the same graph-length strain energy and \(\det G_{F,F}=0\) for one selected face but *not* \(\operatorname{rank}G\le3\). The rational witness is feasible and lies below the pulse budget. Thus **no globally valid lower bound above the pulse budget can be proved for that rank-free feasible set**, even with an ideal exact semidefinite solver. This says nothing adverse about the original rank-three feasible set.

For a PSD Gram, \(\operatorname{rank}(G)\le3\) is equivalent to **all \(4\times4\) principal minors vanishing**: represent \(G=B^TB\); if the rank were at least four, four independent columns of \(B\) would give a positive principal determinant. Conversely, all these minors zero force rank at most three. A globally valid Gram certificate must retain this rank restriction or a comparably strong intrinsically 3D geometric condition. The resulting optimization is nonconvex; a plain semidefinite constraint alone cannot do the job.

## Numerical search provenance — developmental, not a proof

The prior **3D** constrained optimization located a candidate flat-cell energy `0.12442609484`, with a separate coplanarity-parameterized cross-check. It never proved this was the global three-dimensional minimum. The present follow-up tested 17 **rank-relaxed** starts over coordinate dimensions `d∈{3,4,5,8,12}` (one 3D seed and four seeds per higher dimension; scales `{0,.1,.5,1}`, RNG seed 20261023). In 4D, a nontrivially lifted initial seed finds `0.047842091456`; dimensions 5/8/12 find about `0.047458500687`. These are NUMERICAL values with optimizer selection freedom and **not** rigorous optima. Their role was only to supply a candidate for later exact rationalization. The rational rank-four witness is the consequential verified result.

All physical 3D dimensions, the original mass, spring, damping and readout laws, the original low-mass/friction failures, and the separate held PR #44 recovery track are preserved. A rational Gram witness in 4D must **not** reopen the parked physical-4D hypothesis.

## Limitations and next discriminant

- **OPEN:** global lower bound on 3D flattened-cell energy relative to `0.06800255`. In particular, the old numerical 3D value around `0.124426` remains only NUMERICAL, not an infimum certificate.
- **OPEN:** all-time original-pulse cell orientation, all 120 housing-strut lengths, nonlinear u=100 breathing/coherence, 50% energy ringdown, and physical UD identification.
- The witness rejects only **rank-free Gram relaxation**; rank-3-constrained Gram or interval branch-and-bound, with proof of global coverage, is a viable but harder follow-up.
- Source and comparator exposure: rank-4 was specifically targeted after knowing the pulse threshold; g/k selected at allowable minima; coordinate denominator and alpha were rationalized from a fitted numerical low-energy point. This is an adversarial certificate check, **not** a holdout prediction.

**Recommended next action, priority 97/100:** Formulate a rank-3-preserving global barrier certificate, or produce a true 3D rational flattened counterexample below the pulse energy. Use the rank-four witness as a mandatory adversarial unit test rejecting invalid rank-free certificates; independently recover PR #44 full nonlinear Green bounds only under its owning claim.
