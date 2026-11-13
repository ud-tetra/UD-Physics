# Incidence-local quartic clock classification v0.1

**RESULT — EXACT / CONDITIONAL.** On the fixed single-tetrahedron active clock, the only homogeneous quartic Hamiltonian supported on individual registers and nearest Hasse-incidence pairs that produces one common signed rate for every active preparation is the zero polynomial. This classification includes all odd-power pair terms and needs no symmetry assumption. In the broader pair-supported distance-cutoff family, a nonzero common-rate quartic first becomes representable at distance 4, the full register-graph diameter. It remains a freely chosen collective interaction.

## 1. Source, types and scope

Resume main `ud-tetra/UD-Physics@e400dfb715262a44b3bbb2e929c7b438028af67e`, research parent `64e16f695b5d9aa16a613921eb980b44ab749e09`, same task/held claim `clock-matrix-question-20261104` / `72863501bd80db6aae1fd9b68467de48e92cb42c`. Sources: [local-generator v1.0](../qpb1-local-generators/README.md) §§1–4; [common-rate v0.1](COMMON_RATE.md) §§1–4; [mediator v0.1](LOCAL_MEDIATOR.md) §§2–5. Historical supplied ledger v0.39(2), Q166/Q169/Q170, defines incidence stock currents, generator and control-volume balances, not quartic coefficient selection. Supplied master-action and packet-field attachments inspected in the preceding step are placeholders. The designated public portal's last inspected edition was Papers I–III 1.1.1 / IV 0.1 on 2026-11-05, review pending, physical promotion 0; no mediator law imported from the homepage.

Let C=direct sum C_k(Delta^3;R)=R^15 with counts (4,6,4,1), ascending simplex orientation and unit positive metric. The harmonic vector h has entries 1/2 on the four vertices and zero otherwise. V=h-perp, dim V=14; P=I-hh^T. A=d-d^T, J=A/2, J^2=-P. J restricted to V is an invertible skew complex structure. All coefficients/stocks are formal dimensionless quantities; exact polynomial matrices over Q, states and coefficients over R. Fixed native continuous parameter s; physical time, action and energy maps OPEN.

Take H(x)=H0(x)+Q(x), H0=||x||^2=2I, I=||x||^2/2. Q:R^15->R is homogeneous degree four. The evolution is x'=J grad H(x), x(0) in V, no external drive or boundary flux. J kills h and keeps V invariant. Hamiltonian H is conserved. The quadratic stock I is not automatically conserved for arbitrary Q; it is conserved under the common-rate conclusion below. Readout: fixed oriented phase planes of J; all active initial states, rather than one prepared mode or one orbit. An overall common rate may depend on x; it must apply to every active plane at that state. Positivity of the total rate, when needed for forward clocks, is an additional domain restriction.

## 2. Exact locality family

The Hasse graph has one vertex for each chain register and an undirected edge for each codimension-one simplex incidence: 12 vertex-edge, 12 edge-face, 4 face-cell edges, total 28. This graph locality is a declared algebraic locality, not measured spatial range or a causal cone.

Define nearest-incidence energy locality to mean Q is a sum of single-register and incident-pair functions. In the homogeneous quartic class this is exactly

    Q=sum_i a_i x_i^4 + sum_{i~j} sum_{p=1}^3 b_ij,p x_i^p x_j^(4-p).

There are 15+3*28=99 independent ambient monomials. Odd powers p=1,3 are included. No S4 restriction, positivity or sign restriction is imposed, so any such subclass inherits the obstruction. The locality of an energy functional is stronger than the sparsity of its generated vector field; these must not be interchanged.

For a distance-r family, allow any register pair with shortest Hasse distance <=r. Still only one-register or two-register monomial support; this does not classify arbitrary multi-register neighborhoods, new mediators, changing metrics or Poisson tensors, glued carriers, effective reductions or restricted-preparation clocks.

## 3. Radial necessity and sufficiency

**Theorem 1 — EXACT / CONDITIONAL.** The all-active-state common-rate property

    J grad Q(x)=deltaOmega(x) Jx for every x in V

is equivalent to

    Q|V=c ||x||^4,
    deltaOmega(x)=4c||x||^2=8c I,

for a real constant c; the rate at x=0 has no nonzero clock readout. To prove it, multiply the vector identity by -J on V, obtaining grad_V Q=deltaOmega x. Every tangent derivative on each sphere in V vanishes. Spheres are connected, so Q is constant on each sphere; degree-four homogeneity gives c||x||^4. Differentiation gives the converse and displayed rate. This is stronger than S4 invariance and not a source-selected interaction.

**Theorem 2 — EXACT / CONDITIONAL.** In the 99-dimensional nearest-incidence family, the common-rate property forces Q=0 as an ambient polynomial.

First choose two opposite edge registers e=(01), f=(23). Each coordinate axis lies in V, while their Hasse distance is 4. On x=u e+v f, every nearest-incidence Q reduces to a u^4+b v^4. Radial necessity instead gives c(u^2+v^2)^2, whose mixed coefficient is 2c. Equality for all u,v forces c=0; hence Q|V=0.

It remains to exclude nonzero local polynomials hidden in the harmonic constraint. The exact restriction map substitutes x_vertex3=-x_vertex0-x_vertex1-x_vertex2, leaving 14 independent variables. Its 99 coefficient columns have rational rank 99, so its kernel is zero. This is a complete finite linear classification, not a random coefficient search. Independently, direct evaluations of the original monomials on 120 hyperplane points over F_1009 give augmented rank 100 after adding ||x||^4; this proves all 100 columns independent over Q, hence over R. The second calculation constructs values directly rather than using polynomial expansion. Both are constructor checks, not independent review.

A direct kernel argument corroborates the rank: a mixed coefficient involving a fixed nonvertex register depends on at most its two incident vertices; an unused vertex can enforce the harmonic constraint while those vertices remain arbitrary. Thus all vertex/nonvertex mixed terms vanish. Setting all vertex coordinates zero removes every pure nonvertex and nonvertex-pair coefficient. What remains is sum of four vertex fourth powers; evaluating e_i-e_j for all pairs forces a_i+a_j=0 and therefore every a_i=0. No nonzero local Q is invisible solely through the harmonic constraint.

## 4. Interaction range and complete restricted classification

| Maximum pair distance | Allowed pairs | Ambient quartic coefficients | Restriction rank | Null dimension on V | Radial target representable? |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 28 | 99 | 99 | 0 | No |
| 2 | 70 | 225 | 218 | 7 | No |
| 3 | 98 | 309 | 295 | 14 | No |
| 4 | 105 | 330 | 312 | 18 | Yes |

For distances 1–3, the opposite-edge two-coordinate proof still forces c=0. Hence uniform-rate quartics in these classes are exactly the null polynomials on V: zero physical clock effect within the declared readout, with coefficient dimensions 0,7,14 respectively. Null polynomials may affect off-V states, which are outside this active-clock contract. At distance4 the graph is complete; the exact expansion

    ||x||^4=sum_i x_i^4+2 sum_(i<j) x_i^2 x_j^2

is available. All common-rate quartics are c||x||^4 plus a restriction-null polynomial. Their coefficient-space dimension is 1+18=19; their distinct active dynamics have just one free nonlinear rate coefficient c. The code verifies this expansion and every table rank exactly. Distance4 is measured in the fixed chain-register graph, not physical length, signal travel time or a universal UD bound.

## 5. Smooth extension and sparsity distinction

The basic obstruction extends to C2 sums of unary and nearest-pair energies on all of R^15, with the same all-state common-rate condition on V. Radiality gives H|V=f(I). On the opposite-edge plane a local H has no mixed u,v term, while

    partial_u partial_v f((u^2+v^2)/2)=f''((u^2+v^2)/2) u v.

For every I>0 choose nonzero u,v on that circle; f''(I)=0. Thus f is affine, and only a constant active clock rate survives. This conclusion assumes smoothness and the global all-preparation domain; a lower-dimensional restricted preparation changes the problem. It does not assert that every ambient local Hamiltonian with zero active effect is zero outside the quartic class.

A collective Q=c||x||^4 nevertheless has

    x'=(2+4c||x||^2)Jx=(1+2c||x||^2)A x.

Every nonzero entry of A is still a Hasse incidence. Writing stock current as j_(i<-j)=2(1+2c||x||^2) A_ij x_i x_j gives an antisymmetric incidence current and exact stock conservation. But the gain depends on total stock: changing a remote register changes the coefficient of a local current. Sparse current support therefore does not establish local constitutive dependence. Since I is conserved, supplying that gain externally for one preparation reproduces its trajectory; it supplies neither a derived mediator nor a physical clock effect.

## 6. Consequence for the proposed bridge

The previous passive-mediator counterterms contain I_L^2 and I_R^2. Under the present fixed V,J,metric and energy-locality hypotheses, a nonzero such self term cannot be assembled from nearest-incidence quartics while preserving one rate for every active preparation. The collective counterterm construction remains algebraically valid with its stated stronger interactions. This result does not classify all two-clock/glued-carrier interactions or disprove an effective mediator that changes the premises.

**NO-GO, scoped:** exact all-mode uniform nonlinear clock modulation plus nearest-incidence unary/pair Hamiltonian locality fails in this model. The branch is PARKED as a native nearest-incidence implementation. Reopen with an explicit changed premise: a local mediator and controlled effective limit, a restricted physically prepared clock mode, or an allowed approximation with a measured dispersion bound. Do not promote a packet-wide scalar gain to a local mechanism by looking only at generator sparsity.

**OPEN:** native preparation, permitted interaction support, coefficient selection, physical unit/readout maps and independent test. No empirical data fitted or inspected. No registry promotion; physical promotion 0. The next useful route is to quantify the tradeoff between mean frequency shift and mode distortion in a locally coupled, explicitly prepared clock sector, rather than repeat this closed all-preparation search.

## 7. Reproduction and evidence

Run `python3 experiments/clock-matrix-question/local_quartic.py`. Standard-library Fraction polynomial elimination classifies the complete four finite coefficient spaces; a separate modular evaluation implementation supplies the central independence certificate (prime1009, verified by trial division, seed20261105,120 points). A nonzero minor modulo a prime certifies a nonzero integer minor, so this check is exact, not statistical evidence despite the deterministic point generator. Polynomial ranks, common-rate proofs and null-space scope are separate from physical evidence. Independent review NOT_RUN.
