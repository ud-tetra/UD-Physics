# Phase-007 — Source closure versus minimal local quartic constitutive law

**RESULT — EXACT / CONDITIONAL source closure; HYPOTHESIS nonlinear extension; FAILED unique physical attribution.** Higher polynomial/analytic powers of the original 15D incidence generator cannot produce multi-rate detuning. A local signed-S4-equivariant quartic energy extension gives a preparation-dependent two-state response absent from a *fixed linear* oscillator model, but not absent from a matched conventional nonlinear Hamiltonian system. It also breaks the earlier J-based fiber equivariance. No new physical bridge or independent prediction is established.

## Source/version, question and conventions

Read-only source is the original [local generator classification](../qpb1-local-generators/README.md), at integrated revision 41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb, §§1–4, plus this branch's [phase-006 multiport analysis](MULTIPORT_DISCRIMINANT.md) at a2e3d8846104811c67559b0d3233c8a758dbccd9. Existing phase-001 to phase-006 artifacts are untouched. Source audit of [unit preparation](../qpb1-unit-preparation/README.md) and [impedance selection](../qpb1-impedance-selection/README.md) confirms that physical source amplitude, constitutive law, charge map and clock remain OPEN in their recorded scope; it does not establish that all conceivable UD sources are exhausted.

Define the original oriented filled simplex chain carrier C = direct sum of C_0..C_3 over real coefficients, dimensions (4,6,4,1), with ascending vertex orientations, Euclidean metric H=I, signed S4 action rho, incidence differential d and skew A=d-d-transpose. Let P=-A^2/4 be the rank-14 active projector and J=A/2, J^2=-P. Time t is continuous and dimensionless; physical time t_physical=tau0*t has unknown tau0. A physical amplitude/port map is also unknown.

## 1. No source-selected detuning from analytic closure of A

The exact original matrix satisfies A^3=-4A. Its distinct complex eigenvalues are 0, +2i and -2i, and its real polynomial algebra is span{I,P,A}, with harmonic projector I-P. Any real analytic function f(A) defined on its spectrum therefore has the form
\[
f(A)=f(0)(I-P)+\operatorname{Re}f(2i)\,P+
\frac{\operatorname{Im}f(2i)}{2}\,A.
\]
For f(A) to be skew-adjoint in H=I, its symmetric coefficients must vanish, leaving f(A)=cA. In particular, every real odd polynomial reduces to cA, as can be seen from A^(2n+1)=(-4)^n A. Every nonzero active mode then has the same angular frequency 2|c|, every native ray under its flow is constant, and the open-path geometric phase of the previous J quotient is trivial. This statement is EXACT for *one operator A and functional calculus*. It does not prohibit a new degree-dependent operator, state-dependent generator, non-Euclidean metric, source bath or different carrier. Those are changed premises.

Even the broader source-classified signed-S4 linear skew-incidence family G=sum g_kK_k permits three independent rates but **selects none of them**. Using a different positive degree metric merely reparameterizes this free family; it does not derive the gains. Thus the exposed detuning g=(1,1,3/2) remains an assumption/FIT rather than a source-constrained physical frequency selection.

## 2. Added local nonlinear Hamiltonian (new premise, not native law)

To test the nearest minimal constitutive alternative using the existing register stocks and incidence bonds, POSTULATE for lambda >=0
\[
\mathcal H_\lambda(x)=\sum_{i=1}^{15}\left(\frac{x_i^2}{2}+
 \frac{\lambda x_i^4}{4}\right),\qquad
\dot x=A\nabla\mathcal H_\lambda(x)
=A\left(x+\lambda x^{\odot3}\right).
\]
Lambda is an unselected new dimensionless coupling. The illustrative lambda=1/4 was chosen after exposure to the earlier phase targets, and no data were fitted. H=I is still the coordinate metric, but the new physical Hamiltonian need not be the previous positive quadratic H_g. Since A is constant skew, it defines a Poisson bracket and the flow conserves H_lambda exactly. For lambda>=0, H_lambda is nonnegative and coercive, so finite-energy trajectories remain bounded and the polynomial ODE has global solutions. It need not conserve the old Euclidean norm or individual sector stocks.

The vector field is incidence-local (coordinate i depends only on codimension-one neighbors), and signed-S4 equivariant because coordinatewise odd powers commute with signed permutations and A commutes with rho. Define local positive energy stock h_i=x_i²/2+lambda*x_i⁴/4 and y_i=x_i+lambda*x_i³. Then
\[
\dot h_i=\sum_j A_{ij}y_iy_j,\quad
j_{i\leftarrow j}=A_{ij}y_iy_j=-j_{j\leftarrow i}.
\]
Thus every subset obeys exact boundary flux conservation. This is a *new conventional Hamiltonian constitutive model* written on UD registers, not a derived microscopic material law.

## 3. Closed top-cell/face manifold and preparation discriminant

Set e_c to the oriented top-cell unit vector, f=Je_c equal to half the alternating sum of its four oriented faces, and x=q e_c+p f. This two-coordinate manifold remains invariant under the new nonlinear flow and obeys EXACTLY
\[
\dot q=-2\left(p+\frac{\lambda p^3}{4}\right),\qquad
\dot p=2(q+\lambda q^3).
\]
It preserves the signed (+,-,+,-) face pattern and keeps all edge/vertex amplitudes zero for this special preparation. The relevant conserved energy is (q²+p²)/2+lambda(q⁴+p⁴/4)/4, not necessarily norm q²+p².

At preparations (q,p)=(a,0), the exact normalized initial face-plane growth rate is \(\dot p/a=2(1+\lambda a^2)\). With chosen lambda=1/4, a=1 gives 5/2 and a=1/2 gives 17/8; the **exact difference is 3/8**. A fixed time-independent linear three-tone model with one unchanged face-cell rate cannot reproduce these two normalized short-time slopes simultaneously. This is an observable **conditional preparation-scaling discriminant against a fixed-linear baseline only**. It assumes controlled physical amplitude and phase preparation; neither is presently operationally mapped.

Sensitivity/alternatives: lambda=0 reduces to the original common-rate source and removes the effect. For arbitrary lambda the rate difference scales as 3lambda/2; choosing lambda to match any observed nonlinear slope would be FIT. The original phase-006 zero-edge selection rule survives for this top-cell manifold; nonlinear effects may be sought in other preparations, but no new unique spectral prediction follows.

## 4. Important failure: original J gauge equivariance

The earlier U(1) geometric-phase interpretation presupposes a dynamical compatibility with fiber rotations x -> exp(theta J)x. The local quartic vector field fails this already for x=e_c:
\[
F_\lambda(Je_c)-J F_\lambda(e_c)=\frac{3\lambda}{2}e_c.
\]
At lambda=1/4, this is 3/8 e_c, a **nonzero exact defect**. Hence the nonlinear flow does not in general descend to the earlier ray quotient as an autonomous law. The previous phase-001 to phase-006 fixed-generator holonomy and calibration certificates cannot be inherited. A new phase/readout contract and metric/gauge analysis are necessary before making phase claims.

## 5. Stronger classical null and scientific disposition

For the entire state space, a conventional real nonlinear Hamiltonian with **the same constant Poisson tensor A and energy H_lambda** follows precisely the same ODE. All modal, port, intervention, energy and phase-space trajectories therefore coincide for every initial condition. A Duffing-like classical system supplies the same preparation-scaling behavior. The new model is a useful local nonlinear falsification *hypothesis*, but unique UD physics is **FAILED** under an incidence-matched nonlinear classical null. It is not an independently source-selected constitutive mechanism.

No physical apparatus, time/energy unit calibration, state-amplitude calibration, held-out dataset, external reviewer or mainline promotion is claimed. PARK unique UD attribution for this local quartic model unless a source-selecting rule or independently distinctive response is supplied.

## Reproduction and record

From repository root, run:

python3 experiments/qpb1-finite-window-phase/constitutive_audit.py --out /tmp/qpb-constitutive-phase007.json

The exact-Fraction constructor checks A^3=-4A, cross-sector K products, 24 full signed-S4 equivariance transformations, 16 exact invariant-plane fixtures, 6 control-volume energy flux cuts, the two preparation rates and the 3/8 J-gauge defect. Its positive-energy and nonlinear classical-equivalence theorems use the analytic arguments above; the finite fixtures are constructor validation, not peer review. See [immutable run](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-007/manifest.json) and [mathematical receipt](../../sessions/qpb1-finwindow-20261023-gpt6-b6f2/constitutive_receipt.json).

**Next discriminant (priority 99/100):** seek a versioned native source/constitutive restriction selecting lambda or a different nonlinear coupling *without target calibration*, plus a measurable signed response that survives comparison to a physically realistic, parameter-budgeted nonlinear classical null. Otherwise close this family as a structural analogue rather than a physical bridge.
