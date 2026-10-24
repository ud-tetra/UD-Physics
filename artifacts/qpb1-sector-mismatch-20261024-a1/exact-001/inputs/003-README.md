# Uniform three-sector meter detuning certificate v1.0

**RESULT — EXACT / CONDITIONAL.** On the declared balanced classical meter,
all three independent **constant native gain mismatches** may satisfy
|epsilon_k|<=11/1000. The previous passing point (0,0,1/100) lies strictly
inside this box: its open max-norm neighborhood of radius1/1000 is covered.
The parent preparation, independent plant-gain and finite-window timing
ranges are retained. With 26-bit acquisition, an additional arbitrary
passive-generator remainder of norm<=1/10000000 and the declared reset/noise
budgets, the circular phase error is **<1/290 rad**, below the0.004-rad
target. Observed endpoint visibility stays >0.99 and links >0.999.

This is a structured constant-error certificate. It does not enlarge the
arbitrary-channel allowance to0.011 or certify time-varying differential
detuning. Signed sensors, calibration, physical units, native selection and
hardware realization remain OPEN. Physical score **UNSCORED**, promotion **0**.

Base `ud-tetra/UD-Physics@5fd737fda4dadd6f1cc3d9c3c6c086473b7f72bb`;
2026-10-24, America/Chicago. [SOURCES.json](SOURCES.json) pins30 dependencies;
[SOURCE_ROWS.json](SOURCE_ROWS.json) preserves13 literal archive-v0.85 rows
with scientific revisionv0.43. Fresh historical ledger/governance upload
bytes match imports. G06 remains frozen and no physical eta_A is inferred.
The unavailable Genesis PNG and placeholder documents supply no law.
No mainline, source-ledger or shared CURRENT edits are made.

## 1. Model, domain and the three-sector reduction

Retain the filled tetrahedron's real15-register chain carrier, ascending
orientations, Euclidean metric, J=A/2 and orthogonal active projectors P_k
of ranks6,6,2. The local skew generators are K_k=2JP_k. Add the previous
15-register meter with balanced same-register ports kappa=1/4 and meter
damping gamma=1. The proposed model is

$$
x'=G(s)x-\tfrac14m,\qquad
m'=(G(s)+2J\sum_k\epsilon_kP_k)m+\tfrac14x-m.
$$

Here G(s)=sum g_k(s)K_k, g*=(1,1,3/2), and each
|g_k(s)-g_k*|<=1/100, including bounded piecewise-continuous plant drift.
Each epsilon_k is constant, with |epsilon_k|<=11/1000. It is an absolute
native gain error, not a percentage or a physical frequency. Its frequency
mismatch is omega_k=2epsilon_k, |omega_k|<=Omega=11/500.

Total storage (||x||^2+||m||^2)/2 dissipates at rate -||m||^2. Because G(s)
and all sector projectors commute, the meter contribution from an active
seed v is

$$
m(\tau)=\sum_k\beta(\omega_k,\tau)U(\tau)P_kv,
\quad U'=G(s)U.
$$

Complex multiplication means (Re beta)I+(Im beta)J. For each sector,
(a,beta)'=L(omega)(a,beta), initialized at(1,0), with

$$
L(\omega)=\begin{pmatrix}0&-1/4\\1/4&-1+i\omega\end{pmatrix}.
$$

One native unit of warmup precedes the measured window. The window length
satisfies |T-2pi|<=1/100, with128 links and maximum gap<=T_plus/128,
T_plus=4407/700. Hence all meter times lie in[1,H], H=5107/700. The seed
is in the parent's active radius-1/10 preparation ball. Norm is in[9/10,11/10]
and its fixed sector fractions r_k obey r_3 in[1/3,2/3]. The proof below
allows arbitrary within-sector directions and all such fractions.

## 2. Exact rational enclosure of transfer amplitudes and phases

Write b0(tau)=beta(0,tau)>1/8 on[1,H], as established by the parent and
checked again here. Let

$$
A(\omega,\tau)=|\beta(\omega,\tau)|^2/b_0(\tau)^2,
\qquad \chi(\omega,\tau)=\arg[\beta(\omega,\tau)/b_0(\tau)].
$$

[enclose.py](enclose.py) proves, throughout the continuous time/detuning box,

$$
1-\tfrac32\omega^2\le A\le1,\qquad
|\chi-\omega f(\tau)|\le10|\omega|^3,\qquad
|\partial_\tau\chi|\le2|\omega|,
$$

where f=b1/b0 is the first detuning coefficient. At the start and throughout
the possible endpoint range, it also proves

$$
2/5<f(1)<1/2,\quad
7/10<f(\tau)<4/5\ (699/100\le\tau\le H),\quad
|f(\tau)-f(1)|<2/5.
$$

The true endpoint lies in this range since pi>3; the upper endpoint uses
the parent's pi<22/7 argument. A regular inscribed hexagon supplies the
elementary lower bound pi>3. Positive real part of beta/b0 throughout the
box fixes a continuous phase branch; no hidden phase unwrap is assumed.

The enclosure uses exact Fraction arithmetic and outward rounding to a
rational grid of denominator10^12. It is not a binary64 parameter scan:

1. Set L0=L(0), Q=diag(0,1). Expand exp((L0+zQ)tau)(1,0) in z. Its real
   coefficient vectors y_r have norms<=tau^r/r!, by iterated variation of
   constants and contraction of exp(L0*t). Physical z=iomega gives
   beta=sum(iomega)^r b_r(tau).
2. Compute the first six coefficient functions through time Taylor order100
   using exact rational matrix-power recurrences. Since ||L0||<=5/4 and
   (9/4)H<17, every retained coefficient's time truncation error is at most
   `3^17*17^101/101! < 10^-18`. The exponential tail bound follows by summing
   the noncommutative word norms; e<3 gives the displayed integer majorant.
3. Cover[1,H] with512 closed rational cells. At each midpoint evaluate the
   coefficient polynomials exactly. Coefficient derivatives use
   y_r'=L0 y_r+Q y_(r-1); their point error is bounded by(9/4) times the
   time-tail bound. The second-time-derivative bound is

$$
\|y_r''\|\le\frac{25}{16}\frac{H^r}{r!}
+\frac52\frac{H^{r-1}}{(r-1)!}
+\frac{H^{r-2}}{(r-2)!},
$$

   omitting negative-index terms. Taylor's theorem then encloses every
   point of each cell, including shared endpoints.
4. The omitted detuning tail after degree5 is at most
   rho6=(Omega*H)^6/[6!(1-Omega*H)]. Its time derivative is bounded by
   (5/4)rho6+Omega*rho5, with the analogous degree5 tail rho5. These follow
   from the same contraction-based coefficient norms.
5. Form exact outward interval polynomials for |beta|^2 and
   Im(beta' conjugate(beta)), retain their even/odd cancellations, include
   both tails, and divide only by intervals bounded away from zero.
   The code proves the inequalities above. For the phase approximation it
   bounds the real denominator and uses |atan(y)-y|<=|y|^3/3.

The resulting coefficient of omega^2 in A-1 lies inside approximately
[-0.821,-0.049], strictly within[-3/2,0]. The computed cubic phase coefficient
is <1.624 and the phase-rate coefficient <0.925;10 and2 are deliberately
looser proof constants. Captured enclosure.json records exact rational
bounds, worst cells, tail specifications and endpoint receipts. The complete
deterministic checker regenerates all cells; CI checks artifact integrity,
not the truth of this proof or a physical identification.

## 3. Variable sector weights and overlap coherence

Calibrate the raw meter with the same positive nominal gain1/b0(tau),
bounded by8. Put a=(3/2)Omega^2=363/500000. Its normalized sector weights are

$$
p_k(\tau)=\frac{r_k A_k(\tau)}{\sum_l r_l A_l(\tau)}.
$$

For any two sample times s,t, the overlap has positive magnitude factor K_st
and phase of a convex sum with weights

$$
C_k=\sqrt{A_k(s)A_k(t)},\quad
w_{st,k}=\frac{r_k C_k}{\sum_l r_l C_l},\qquad1-a\le C_k\le1.
$$

A variable in an interval of width a has variance<=a^2/4, hence mean
absolute deviation<=a/2. Since its mean is>=1-a, this gives

$$
\|w_{st}-r\|_1\le L_a:=\frac{a}{2(1-a)}.
$$

The factor K_st=sum sqrt(p_k(s)p_k(t)) has the stronger quadratic bound

$$
K_{st}\ge K_a:=1-\frac{a^2}{2(1-a)^2}.
$$

For proof, set z_k(t)=sqrt(r_k A_k(t)). The unnormalized difference norm
is<=a/[2sqrt(1-a)]. Normalization changes this by at most2/sqrt(1-a), so
the squared distance of the two unit positive vectors is<=a^2/(1-a)^2.
Their inner product K is one minus half this squared distance. Using the
much weaker bound K>=1-a would unnecessarily lose the endpoint gate.

## 4. Direct finite-polygon phase bound

Sector phases are theta_k(tau)=2 integral g_k ds+chi_k(tau). The filter's
endpoint phase increment is bounded by

$$
F_e=(2/5)\Omega+20\Omega^3=0.00901296.
$$

Let D0=2291/17500 be the parent's plant gain/timing halfspread. Set

$$
D=D_0+F_e,\quad \sigma=13/25+2\Omega,\quad
d=\sigma T_+/128.
$$

The endpoint phase errors relative to reference advances(4pi,4pi,6pi)
have halfspread<=D. Each link's phase advances have halfspread<=d, even
with bounded plant drift. The normalized endpoint and link magnitudes are
therefore at least K_a(1-D^2/2) and K_a(1-d^2/2).

For a convex phase sum with halfspread b, subtract its weighted mean.
The centered variance is<=b^2, third absolute moment<=2b^3, so its argument
differs from that mean by at most b^3/[3(1-b^2/2)]. This is the same
elementary centered-moment argument as the parent's certificate.

Here each overlap has its own weight w. Let q_k be endpoint phase errors
after removing reference advances and let Delta_j theta_k be link advances.
Collecting the endpoint and link means gives the exact error identity,
modulo2pi,

$$
F-F_0=E_e-\sum_j E_j
+\sum_k(w_{e,k}-r_k)q_k
-\sum_{j,k}(w_{j,k}-r_k)\Delta_j\theta_k.
$$

F0=-2pi*r3 is the same seed's nominal phase. Weight differences sum to zero,
so their pairings are bounded by phase halfspread times their L1 norm.
Consequently the complete structured-meter polygon error is at most

$$
\boxed{b_{\rm sector}=
\frac{D^3}{3(1-D^2/2)}+
\frac{128d^3}{3(1-d^2/2)}+
L_a(D+\sigma T_+)}.
$$

This accounts for both time-varying weights and finite sampling. No
continuous-connection acquisition assumption is required, and the same
state error is not charged independently at every link.

## 5. Separate arbitrary-error, reset and sensor budgets

In addition to the constant sector errors, allow any further balanced
passive generator perturbation of norm<=delta_o=1/10000000. Both actual
and reference propagators must remain contractions. Retain the parent's
initial meter residual e0=9/12800000000 and finite reset preconditions.
The calibrated sample norm error is bounded by
B_o=8(e0+H*delta_o*(11/10)). This budget is not enlarged to0.011.

Use s0=(9/10)(1-a) as a rational raw active-norm lower bound. Applying the
previous projective homotopy theorem around the structured path, put

$$
v_e=K_a(1-D^2/2)-4B_o/s_0,\quad
v_l=K_a(1-d^2/2)-4B_o/s_0,\quad
\eta=B_o/(s_0-B_o).
$$

With q_c(v)=(1-v^2+c^2)/(2cv), the extra phase allowance is
b_o=2eta[q_(3/20)(v_e)+128q_(1/25)(v_l)]. This covers arbitrary perturbation
directions and harmonic leakage before active projection; the numerical
campaign uses a commuting subset.

Retain 26-bit nearest-even sampling on[-2,2), combined calibrated
per-register sensor/reference error r=9/320000000 and half-step2/2^26.
After active normalization the additional complex-overlap error is bounded
by zeta=(31/2)(r+2/2^26)/(s0-B_o). Thus

$$
\boxed{b_{\rm total}=b_{\rm sector}+b_o+
\frac{\zeta}{v_e-\zeta}+128\frac{\zeta}{v_l-\zeta}
<\frac1{290}<\frac1{250}\quad\mathrm{rad}.}
$$

| Contribution | Conservative decimal upper bound, rad |
| --- | ---: |
| Structured sector/plant/timing/sampling | 0.003174140 |
| Further arbitrary generator and initialization | 0.000057539 |
| Sensor/reference and digitization | 0.000128853 |
| Exact total, rounded upward | 0.003360530 |

Exact rational comparisons are in audit.py and captured budget.json.
Observed endpoint visibility is >0.99018; link visibility >0.99958. Raw
active support is in(0.8,1.2), no saturation occurs, and |Qhat-1|>1.7 on
the declared domain. These gates qualify data; they do not verify that
unknown hardware parameters lie within the certified box.

For a concrete sensor allocation put S=11/10+e0,
eps_gain=r/(24S), j=r/[120S(1+eps_gain)] and nu=r/3. With inverseb0<8 and
||m'||<5S, gain, native timing and additive/reference contributions sum to r.
Amplitude-calibration and memory errors must also fit the combined budget.
The previous64-native-unit damped reset, bounded off-port leakage, positive
storage and residual-preserving preparation assumptions remain. Keep the
finite classical reference buffers and exact Gaussian integer phase output;
no unbounded history, physical quantum copying or erasure-energy law follows.

The same full-box allocation at21bits is not certified by this bound.
This is a failed sufficient extension, not a detector impossibility theorem.
Port/damping constants1/4 and1 are engineered assumptions, not UD-selected
couplings. Differential time drift is outside the constant-sector theorem.

## 6. Reproduction, exposure history and negative controls

```bash
python3 experiments/qpb1-sector-mismatch/audit.py --out /tmp/ud-sector-mismatch
```

Standard-library Python only. **EXACT constructor:**30 source hashes,
13 literal ledger rows,512 outward rational time cells with analytic
time/detuning tails, transfer/phase inequalities and rational total budget,
plus20 exact scalar weight fixtures. The interval calculation covers the
whole continuous declared box; it is not interpolation between trajectories.

**NUMERICAL constructor cross-check:**1,350 windows combine30 detuning
triples,5 preparations,3 plant-gain triples and3 endpoint choices. The
detuning set contains the{-0.011,0,0.011}^3 grid and the three earlier0.01
single-sector points. Added generator error, initial residual and sensor
error are included; structured, other and sensor phase contributions are
checked separately. Exact digitization/phase processing follows binary64
path construction. Maximum displayed total error is about0.000827017rad.
135 common-sector detuning checks preserve the raw phase to about1.925e-15.
80 independent closed-form/series comparisons have maximum difference
about6.511e-12, inside the proven detuning remainder plus display tolerance.
This different evaluation is a constructor check, not non-constructor review.
Numerical norm/phase checks use5e-13/5e-11 tolerances. A captured integer
witness replays without constructing analog trajectories.

The out-of-box hidden detuning0.05 control passes data gates but has phase
error about0.009124747rad, failing the0.004screen. It is preserved alongside
the failed21bit sufficient extension. Earlier generic-error and stock-only
obstructions retain their original scopes.

Target exposure is explicit:0.01 and the earlier phase/readout budgets were
known. The first enclosure covered|epsilon|<=0.01; after checking its margin,
the selected box was expanded to0.011 to place the previous point strictly
inside. All proof constants, domain choices and numerical probes are
development choices, not blind predictions or measured hardware tolerances.
No frozen run was rewritten. The exact interval certificate validates its
mathematical model, not the physical truth of its premises.

See [contract](SECTOR_CONTRACT.json),
[candidate](../../candidates/qpb1-sector-mismatch/candidate.json),
[receipt](../../sessions/qpb1-sector-mismatch-20261024-a1/mathematical_receipt.json),
and [immutable run](../../artifacts/qpb1-sector-mismatch-20261024-a1/exact-001/manifest.json).

**Next discriminant:** derive an explicit drift-rate budget for slowly
time-varying sector mismatch epsilon_k(s), testing whether the constant-box
certificate survives realistic differential drift while preserving its
separate arbitrary-channel and calibration requirements.
