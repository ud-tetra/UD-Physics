# Six symmetry-adapted adjoint seeds for the 3D icosahedral moving baseline

**RESULT — EXACT / CONDITIONAL algebraic six-sector reduction, NUMERICAL constructor verification at u=0, nonlinear u100 OPEN.** Versioned follow-up to `symmetry-channels-020` on the held branch, with separate PR44 ownership untouched.

## Goal and setup

In the exactly uniform 3D passive icosahedral system, the rank24 non-affine output carries the real \(A_5\) representation \(3+3'+2\cdot4+2\cdot5\). The full energy-normalized initial housing phase is \(\mathbb R^{180}\). For any time \(u\) on the exact globally safe moving symmetric reference (checkpoint 019), the full nonlinear flow derivative defines an equivariant linear map \(L(u):\mathbb R^{180}\to Z_{24}\). We need to compute its operator norm using at most six **fixed compatible output test vectors**, not 24 generic output adjoints.

The reduction is algebraically exact under these premises, but evaluating \(L(u)\) for arbitrary \(u\) still needs a time-dependent propagator and error enclosures.

## Canonical representation construction

The twelve-vertex icosahedron adjacency matrix \(A\) has exact spectrum \(5\,(1),+\sqrt5\,(3),-\sqrt5\,(3),-1\,(5)\), with multiplicity in parentheses. The rank-eight vertex projector \(P=I-P_0-P_V\) selects the \(-\sqrt5\) and \(-1\) eigenspaces. Tensor with the physical Cartesian \(3\)-vector representation:

\[
Z_{24} = \bigl(E_{-\sqrt5}\otimes\mathbb R^3\bigr)\oplus\bigl(E_{-1}\otimes\mathbb R^3\bigr).
\]

As \(A_5\) representations, \(E_{-\sqrt5}\otimes\mathbf3\cong\mathbf4\oplus\mathbf5\) and \(E_{-1}\otimes\mathbf3\cong\mathbf3\oplus\mathbf{3'}\oplus\mathbf4\oplus\mathbf5\). Therefore, the adjacency eigenspaces separate the two copies of each multiplicity-two sector \(\mathbf4,\mathbf5\).

Use the exact (representation-theoretic) character central projector on each irreducible type:

\[
\Pi_\rho=\frac{d_\rho}{60}\sum_{g\in A_5}\chi_\rho(g)\,U_Z(g).
\]

For each of the unique 3 and 3' sectors choose one normalized output seed. For \(d=4,5\), project the two copies separately using \(\Pi_\rho(E_{-\sqrt5}\otimes I_3)\) and \(\Pi_\rho(E_{-1}\otimes I_3)\), each rank \(d\). Construct a nonzero intertwiner \(T:W_1\to W_2\) by averaging a rank-one map over the 60 rotations:

\[
T=\sum_{g\in A_5}U_Z(g)\,b a^T\,U_Z(g)^T,
\quad a\in W_1,\ b\in W_2.
\]

By real Schur's lemma, \(T^T T\) is a scalar times the identity on \(W_1\). Thus for a unit \(e_1\in W_1\), \(e_2=Te_1/\|Te_1\|\) is the **compatible partner** in the second copy. This alignment is necessary: taking an arbitrary independent vector in the second copy would not, in general, recover the off-diagonal block coefficient correctly.

For each of the six seeds \(e_i\), compute the adjoint response \(r_i(u)=L(u)^T e_i\in\mathbb R^{180}\). The two unique sector gains are \(\|r_3\|^2\) and \(\|r_{3'}\|^2\); each multiplicity-two block is recovered from the two-by-two matrix \(B_d=[r_i^T r_j]_{i,j=1}^2\). Hence

\[
\boxed{\|L(u)\|_2^2=\max\{\|r_3(u)\|^2,\ \|r_{3'}(u)\|^2,\ \lambda_{\max}(B_4(u)),\ \lambda_{\max}(B_5(u))\}.}
\]

**This is an exact conditional identity for all times on the symmetric reference.** No six-adjoint time integration through \(u=100\) has yet been executed.

## Executed numerical constructor test at u=0

`python six_seed_gain.py --out six_seed_result.json` (NumPy, NetworkX) reconstructs every one of the 60 proper rotations, their real central projectors, the two adjacency-vertex eigenspace projectors, the group-averaged copy intertwiners, and six unit-norm output seeds. It then computes the source-analytic full \(36\times180\) *initial non-affine acceleration* map for the uniform reference at \(\beta=.005,\nu=.05,c_f=0,E_h=51/20000000\). The six-seed sector calculation is compared with a separate full \(180\)-column SVD/eigenvalue calculation. Results:

- Full singular gain: `0.0009605640670680957`.
- Six-seed reconstructed gain: `0.0009605640670680953`.
- Relative difference: `3.386142193913581e-16`.
- Reconstructed 24 nonzero eigenvalues match the full output Gram within the captured floating error, including multiplicities `3,3,4,4,5,5`.
- The six rows are 180-dimensional dual responses; the model has not been reduced to six physical degrees of freedom.

These are **NUMERICAL constructor checks** at the initial instant, not validated long-time dynamics. The exact algebraic block formula is not inferred from the numerical agreement; it follows from the symmetry proof of 020 plus the copy-intertwiner construction above.

## Limitations and negative controls

- The construction assumes completely uniform coefficients and exact radial-symmetric moving reference; source-frozen scattered coefficients break \(A_5\) and require explicit perturbation bounds.
- Nonlinear second-order coupling does **not** reduce to these six linear probes: checkpoint 020 found the symmetry-permitted Hessian map space has dimension 6516; checkpoint 016 measured nonzero curvature in mixed housing position/velocity nullspace directions.
- Continuum-time gain, trajectory-wide strut domain for **all** phases, nonlinear Hessian/remainder and physical readouts through \(u=100\) remain OPEN.
- The six-seed prototype uses group action reconstructed numerically for projector matrices, with exact algebraic group identities proved in checkpoint 020. The `u=0` constructor uses previously exposed targets; no holdout or independent empirical claim.

**Next action (99/100):** Integrate the six symmetry-adapted *moving* adjoint rows through \(u=100\) at a first uniform coefficient set, cross-check at selected times against the old 24-output adjoint, and provide validated continuous-time errors. In parallel derive a coupled shell/housing-relative nonlinear tube (not inferred from six linear rows).
