# Source-matched exact symmetric peak-slab trajectory certificate — checkpoint 027

**RESULT: EXACT / CONDITIONAL (declared uniform 3D MountLoss surrogate).** The actual symmetric reference trajectory, from the prescribed alpha(0)=1/10 preparation, is enclosed through **u=187/40=4.675** with a rigorously derived energy-metric error **strictly below 3×10⁻²⁸**. This is a source-state theorem, **not** a source-to-frozen-spline Jacobian comparison or the nonlinear full-180-phase u=100 theorem.

## Provenance, scope and dimensions

- Repository: `ud-tetra/UD-Physics`, read-only integrated main observed `3b9f6dee5e8c69cf9b4d11787966bda05f99137d`; unchanged source blobs `model.py c480411dea76a32b0703651744fd66549fc7df4e`, `network.py 010629e4239c012048ff3cf49196099e3502eb4f`, `hardware.py 663ee8cd3a059920e3463fd33307d4908f6743d2`, `mountloss.py aa4ad28348e22733340aad0cde6ae33a633f0b75`, and icosahedral `analyze.py da375361c20c089409e84197c720026aadc93c9e`.
- Claim: `claims/icosahedral-phasewindow-20261022`, held owner `phasewindow-20261022-gpt6-7c41`; work branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`; PR #45 draft. Separate held PR #44 is unmodified.
- Reference geometry: regular icosahedron in **physical 3D Euclidean mathematical reference space**, reference edge length 1. No 4D physical structure or SI time conversion is assumed. Model time u is an uncalibrated Newtonian parameter. The invariant uniform symmetry subfamily is a *selected preparation*, not a claim about the generic 560-phase flow.
- Fixed exposed selection: `g=m=1`, `k=2/5`, reciprocal gain 1, auxiliary z=0, `beta=1/200`, `nu=1/20`, `cf=0`, housing weights 1, `omega_h=10`, alpha(0)=1/10, all velocities zero, shell/housing scale 1.

## Exact six-state reduction from unchanged model

Let `v_i` be the twelve reference vertices, `A_e=(v_i+v_j)/2` for edge e, and `X_i=b v_i`, `H_e=c A_e`. Set state `y=(alpha,b,c,alpha_dot,b_dot,c_dot)` and `delta=b-1`. All 150 auxiliary transmissions remain exactly zero for this uniform-scale preparation because every radial and exterior strain equals `delta` and all signed difference gains equal one.

Define `r=(5+sqrt(5))/8`, `m=(3+sqrt(5))/8`, `s=(1+sqrt(5))/8`, housing effective inertia `m_c=(3/50)(m/r)` and moving-axis loss coefficient `eta=1/(10000 r)`.

The two anchor types per housing have squared lengths

```
e = r b² + m c² - 2m bc = b²/4 + m(c-b)²,
o = r b² + m c² - 2s bc.
```

For each type, let `u_e=(rb-mc, m(c-b))`, `u_o=(rb-sc,mc-sb)` (here `m` is **midpoint-radius squared**, not primary mass) and `w_e=u_e·(b_dot,c_dot)`, `w_o=u_o·(b_dot,c_dot)`. With two anchors of each type for all 30 edges,

```
f_b=60eta[ u_e,b w_e/e + u_o,b w_o/o ],
f_c=60eta[ u_e,c w_e/e + u_o,c w_o/o ].
```

The exact reduced equations and energy are

```
alpha'' = -13alpha + 12delta
b''     = [12alpha - 36delta +100m_c(c-b) - f_b]/12
c''     = 100(b-c) - f_c/m_c
E=1/2 [13alpha² -24alpha delta +36delta²
       +100m_c(c-b)² +alpha_dot² +12b_dot² +m_c c_dot²]
E' = -eta sum_120 [(n·relative_velocity)²] <=0.
```

The 3×3 quadratic stiffness K in `(alpha,delta,c-1)` is `[[13,-12,0],[-12,36+100m_c,-100m_c],[0,-100m_c,100m_c]]`, with mass `M=diag(1,12,m_c)`. The reference starts at E=13/200. Its exact positive strut domain for symmetric states was previously certified in checkpoint019; the proof here rechecks a sufficient energy sublevel.

## Source-equation defect certificate — all 187 slabs

Construct piecewise degree-20 Taylor polynomials `P_j(z)` on normalized z∈[0,1], u∈[j/40,(j+1)/40]. The coefficients are first constructed with 100-digit arbitrary precision, **then rounded to rational integers /10⁷⁵**. Subsequent certification treats every rounded coefficient as an *exact* rational number; it does not assume the coefficient generator or its local error estimates are correct.

`validated_peak.py` performs these exact tests on **all 187 slabs**:

1. `P_0(0)=(1/10,1,1,0,0,0)` and **exact C⁰ continuity**: `P_j(1)=P_{j+1}(0)` as rational vectors, including the incremental run boundaries.
2. The polynomial total energy `E(P_j(z))` is **strictly below 7/100 for every z∈[0,1]**, by computing all degree-40 Bernstein coefficients exactly and checking their maximum.
3. The full polynomial tube has `b>37/40`, `b<43/40`, and `|c-b|<1/5`; the distance denominators satisfy `e>b²/4>1/5`, `o>m b²>1/2`. Thus every residual denominator is valid on the entire segment, not just the endpoints.
4. The exact residual numerator polynomial is expanded over `Q`; its coefficient ℓ₁ norm gives a rigorous supremum on [0,1], divided by the above strict denominator bounds and physical step `h=1/40`.

The exact maximum recorded from these **187 tested rational polynomial residuals** is

```
max || P'(u) - F_rat(P(u)) ||_infinity
       = 3.272329094714965e-30  (decimal display of rational upper bound)
       < 3.3e-30.
```

Here `F_rat` substitutes the rational lower truncation `S/10⁷⁵` for sqrt(5), where the script proves `S² < 5·10¹⁵⁰ < (S+1)²` using exact integers.

### Parameter quantization is controlled, not ignored

`source_param_derivative_gate.py` checks a generous bound `||dF/d(sqrt(5))||_infinity<4` on the `E<7/100` domain, using the explicit rational factor bounds. In particular, `r>9/10`, `m_c>43/1000`, `eta<1/9000`, `|b_dot|<1/9`, `|c_dot|<2`, `|c-b|<1/5`, each `|u|<2`, each rate `<5`, and denominator derivative `(b-c)²/8<1/200` imply endpoint and opposing-anchor loss-factor derivatives `<3` and `<1`, respectively. The derivative of the total damping generalized force is `<1/10`; the derivative of `c''` is `<4`. Since the root truncation gap is `<10⁻⁷⁵`, the additional true-source residual is `<4·10⁻⁷⁵ <10⁻⁷³`.

## Uniform error growth bound in the positive energy metric

Let `||z||_E²=z_q^T K z_q+z_v^T M z_v`, with the *actual* source K and M. On the convex physical sublevel `E<7/100`, `b>37/40`, `||v||_M<3/8`, and all 120 struts have length `>37/80`. The latter follows from the exact endpoint and opposite-face geometry.

The mechanical conservative part is constant quadratic and cancels identically in the norm derivative. The damping is `D(q)=eta sum_120 g_a(q)g_a(q)^T`, a positive semidefinite matrix. For `delta q` with unit K-norm, the geometry yields:

```
||delta d|| < (2/3)||delta q||_K
||M^(-1/2)g_a||² <= r/12 +m/m_c <16
||delta g_a||_(M^-1) <= (2/3)/(37/80)*4 ||delta q||_K
||v||_M <3/8, eta<1/9000.
```

Here `K^-1_bb=13/324<(21/100)²` and `K^-1_cc=13/324+1/(100m_c)<(53/100)²`; `sqrt(m)<5/6`, `sqrt(r)<1`. For the difference of two source flows, the dissipative term has a nonpositive sign; bounding only the `D'[delta q]v` cross term gives an **exact one-sided logarithmic growth rate**

```
mu < (1/2)*[2*(1/9000)*120*16*(2/3)/(37/80)*(3/8)]
   = 64/555 < 1/8.
```

The full six-state error forcing norm is less than `11` times its componentwise infinity norm, because `sum_ij|K_ij|+tr(M)<121`. Using `T=187/40`, `exp(T/8)<2` (verified by a positive-term Taylor series rational upper) yields

```
||y_true(u)-P(u)||_E
 <= 88*[max rational-polynomial residual + 1/10^73]
 = 2.8796496033491693e-28... (exact rational display)
 < 3/10^28,   for every 0<=u<=187/40.
```

Each *coordinate* error is strictly `<5` times the energy-norm error (using the K inverse diagonal and positive M), hence `<1.5e-27`. The energy-domain assumptions bootstrap continuously: the exact source is passive with E(0)=13/200, while the rational piecewise polynomial has separately certified `E(P)<7/100`; the positive quadratic sublevel is convex.

## Independent checks and end-state

`independent_anchors.py` rebuilds the actual icosahedral 30 edges and their four anchors, computes all **120** loss forces by direct 3D vectors, and compares with the reduced rational expressions at 18 seeded states. Max force difference `2.538e-16`, energy-plus-heat identity `4.133e-17`. Independently integrated DOP853 reference through u=4.675 gives maximum endpoint difference `6.982e-14` against the rigorously enclosed rational Taylor centre. These are useful NUMERICAL checks, **not the rigorous error premise**.

Final centre at u=187/40, displayed numerically:

```
alpha=0.03229467472480984
b=1.005931678339038
c=1.004656821017584
alpha_dot=0.328070384452674
b_dot=-0.031660278764803
c_dot=-0.039859565140705
```

## What this does *not* certify

- The **frozen 21 MB sector-4 spline coefficient array from checkpoint026 was unavailable in this execution environment**. Accordingly, the original-source-vs-spline Jacobian defect hypothesis `eta<=1e-8` on `[4.65,4.675]` is still **NOT_VERIFIED**. This result supplies a very accurate certified reference trajectory, which is only one prerequisite for that comparison.
- No rigorous bounds on source sector-4 matrix entries, spline reconstruction, or 4,000-slab global propagator composition have been established here.
- No proof for scattered-property or arbitrary 180-housing-phase nonlinear flow through u=100, nor native UD constitutive/clock mapping or laboratory realization.
- The choices of pulse, housing coefficients, peak slab and 10^-8 target are previously exposed development settings, not independent predictions.

**Next discriminant (priority 99/100):** Reconstruct/obtain the frozen checkpoint026 21 MB binary64 spline and apply interval evaluation of the exact rationalized source sector-4 Jacobian on the certified trajectory enclosure through `[4.65,4.675]`. Test `sup ||B_true-B_spline||<=1e-8`; if false, record the smallest provable correction and move to validated transfer composition. PR44 stays under its own held claim.