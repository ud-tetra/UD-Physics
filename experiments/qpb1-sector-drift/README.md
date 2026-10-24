# Time-varying sector mismatch certificate v1.0

**RESULT — EXACT / CONDITIONAL.** The proposed balanced classical meter's
constant three-sector box extends to independent time-varying mismatches:

$$
|\epsilon_k(\tau)|\le\frac{11}{1000},\qquad
|\epsilon_k(t)-\epsilon_k(s)|\le\frac{|t-s|}{200000}
\quad(0\le s,t\le H=5107/700).
$$

With the inherited preparation, plant-gain, window, reset and 26-bit sensor
budgets, the circular phase error is **<1/260 rad <0.004 rad**. Observed
endpoint visibility remains **>0.99**, and every link **>0.999**. A
conservative decimal upper bound is0.003760595rad. This is a sufficient
continuous-domain theorem for an assumed classical model, not a measured
instrument tolerance or a maximal allowable drift rate. Physical promotion0.

The total possible gain change from the beginning of warmup is at most
H/200000, approximately0.000036479. This has native gain per native time
units, with no established SI clock map. The absolute0.011cap must hold
throughout; a slope bound alone does not enforce it. Constant values on the
box boundary remain allowed.

Base `ud-tetra/UD-Physics@407fe6da298ea3362886075fdd696bf1dfefd2fb`;
2026-10-24, America/Chicago. [SOURCES.json](SOURCES.json) pins36 dependency
files. [SOURCE_ROWS.json](SOURCE_ROWS.json) preserves13 literal archivev0.85
rows/scientificrevisionv0.43. Uploaded historicalv0.39ledger and CRL2proposal
bytes match repository imports. G06 remains frozen; eta_A is numerically OPEN.
The unavailable Genesis PNG and placeholder documents provide no law.

## 1. Objects and retained model

Import the filled-tetrahedron real15-register carrier, active projectorP
of rank14, Euclidean metric, ascending simplex orientations, J=A/2 with
J squared=-P, and three orthogonal J-invariant projectors Pk of ranks6,6,2.
The harmonic line remains separate. Add the proposed15-register meter:

$$
x'=G(\tau)x-m/4,\qquad
m'=[G(\tau)+2J\sum_k\epsilon_k(\tau)P_k]m+x/4-m.
$$

G=sum gk Kk, Kk=2JPk, nominal g=(1,1,3/2), each absolute plant gain error
<=1/100, including bounded piecewise-continuous drift. Port1/4 and damping1
remain exact engineered assumptions. The positive storage derivative is
-||m|| squared, including time-varying skew detuning. In the commuting plant
frame, each sector has a complex scalar state yk=(ak,bk), initialized(1,0):

$$
a_k'=-b_k/4,\qquad b_k'=a_k/4-b_k+i\omega_k(\tau)b_k,
\qquad\omega_k=2\epsilon_k.
$$

The structured meter is m=sum bk U Pk seed, U'=GU. A complex scalar acts
as its real part timesI plus its imaginary part timesJ. The initial active
seed is in the inherited radius1/10ball, with norm[9/10,11/10] and hidden
sector fraction r3 in[1/3,2/3]. All within-sector directions are allowed.
The comparison phase is the same seed's Q0=exp(-2pi*i*r3), not universally-1.

Warmup is one native time unit, followed by |T-2pi|<=1/100,128links and
maximum gap<=Tplus/128, Tplus=4407/700. All meter times are within[1,H].
Use the same positive nominal calibration1/b0(tau), b0=b(0,tau)>1/8. The
finite polygon uses endpoint overlap times conjugated adjacent overlaps,
with h(u,v)=<u,v>+i<Ju,v>, conjugate-linear first. Only circular phase,
modulo2pi, is certified, not unwrapped winding or physical action.

## 2. A real Volterra kernel with a finite exact norm bound

Let L0=[[0,-1/4],[1/4,-1]], Q=diag(0,1), and write b=R+iI.
Variation of constants yields

$$
b(t)=b_0(t)+i\int_0^t k(t-s)\omega(s)b(s)\,ds,
\qquad k(u)=(e^{L_0u})_{22}.
$$

Set alpha=(2-sqrt3)/4 and beta=(2+sqrt3)/4. Then

$$
k(u)=\frac{\beta e^{-\beta u}-\alpha e^{-\alpha u}}{\beta-\alpha}.
$$

Since12/7<sqrt3<7/4, one has alpha>1/16, beta>9/10,
beta/(beta-alpha)<9/8 and alpha/(beta-alpha)<1/12. These inequalities
reduce to positive rational square comparisons. Consequently

$$
\int_0^t|k(u)|\,du
\le\frac54+\frac{t}{12}\le\frac54+\frac H{12}<2=:J_V.
$$

The slow exponential was bounded by1 before integration; the fast
exponential was integrated to infinity. This is a continuous-time operator
bound, independent of a trajectory grid or assumed drift waveform.

Passivity gives |a|<=1 for the zero-meter unit initial condition. The upper
Dini derivative of |b| obeys Dplus|b|<=1/4-|b|, so |b|<=1/4 for any real
bounded measurable detuning. This applies separately to the drifting and
constant-reference trajectories; it does not include the separately
budgeted nonzero reset remainder.

## 3. Separate real and imaginary transfer differences

For each sector choose its initial frequency c=omega(0). Put
Omega=11/500 and nu=1/100000. Lipschitz drift implies
|omega(t)-c|<=nu H=:Delta, with |omega|,|c|<=Omega. More generally, the
proof below only needs this bounded excursion, so arbitrary measurable
changes of that size about a fixed c are also covered.

Let Rc+iIc be the constant-c solution. The real kernel gives

$$
R=b_0-V(\omega I),\quad I=V(\omega R),\quad
\|I_c\|_\infty\le J_V\Omega/4=\Omega/2.
$$

Subtracting the constant equations, and taking norms over[0,H], yields

$$
\|\delta R\|\le2\Omega\|\delta I\|+\Omega\Delta,
\qquad
\|\delta I\|\le2\Omega\|\delta R\|+\Delta/2.
$$

Because4Omega squared<1, solve these two scalar inequalities and use
1/b0<8 on the sampled interval. For z=b/b0 and zc=bc/b0:

$$
|\Re(z-z_c)|\le X=\frac{16\Omega\Delta}{1-4\Omega^2},\qquad
|\Im(z-z_c)|\le Y=\frac{4\Delta(1+4\Omega^2)}{1-4\Omega^2}.
$$

The separation retains the extraOmega factor in the real response.
Treating both differences as arbitrary state errors discards this useful
structure. No assertion that changing a skew generator is itself a scalar
phase rotation is used for differential sector errors.

The inherited512-cell rational enclosure is rerun by [audit.py](audit.py).
It proves 1-a<=|zc| squared<=1, a=3Omega squared/2, as well as
|arg zc-c f(t)|<=10|c| cubed and |f(t)|<1 throughout[1,H]. Thus
|arg zc|<=2Omega, |Im zc|<=2Omega, and Re zc>=1-4Omega squared.
The continuous argument branch is fixed by this positive real part.

It follows that

$$
\big||z|^2-|z_c|^2\big|\le E_A:=2X+X^2+4\Omega Y+Y^2,
\qquad
|\arg z-\arg z_c|\le E_\chi:=\frac{X+Y}{1-4\Omega^2-X}.
$$

The first inequality expands the squared norm with the component bounds.
For the second, integrate the argument derivative along the straight
segment from zc toz; its real part stays above the denominator. All
expressions are exact fractions in the checker. In particular every
sample has amplitude squared in[mA,MA]=[1-a-EA,1+EA], with mA>0.

## 4. Transfer to the finite-polygon phase and data gates

At two sample times, the overlap weights are proportional to
rk sqrt(Ak(s)Ak(t)), whose multiplier lies in[mA,MA]. Let wA=MA-mA.
The inherited elementary variance and normalized-positive-vector proof
gives

$$
L_A=\frac{w_A}{2m_A},\qquad
K_A=1-\frac{w_A^2}{2m_A^2}.
$$

Here LA bounds the L1 distance of any overlap's weights from fixed seed
fractionsr, and KA bounds its amplitude coherence factor. The same proof
applies after rescaling the multiplier interval byMA; a common scale
cancels from normalized weights. The active raw norm is conservatively
s0=(9/10)mA, since sqrt(mA)>=mA for0<mA<=1.

Let Dc,dc be the previous constant-box endpoint and per-link halfspreads.
A sample's additional phase in each sector is bounded byEchi, so an
endpoint difference or any link difference changes by at most2Echi:

$$
D=D_c+2E_\chi,\qquad d=d_c+2E_\chi.
$$

This uses no derivative of the measured phase and no rate assumption
between samples beyond the bounded-excursion theorem. It charges a full
2Echi per link and is therefore conservative; increasing the link count
without revising this estimate is not automatically beneficial.

Use the exact finite-polygon identity from the constant-sector report,
with the new weights and spreads. The structured phase bound is

$$
b_s=\frac{D^3}{3(1-D^2/2)}+
\frac{128d^3}{3(1-d^2/2)}+L_A(D+128d).
$$

Structured visibilities are at least KA(1-D squared/2) and
KA(1-d squared/2). These estimates include the inherited plant-gain and
window errors, changing sector weights and finite sampling.

Retain the separate arbitrary actual/reference passive-generator
remainder delta_o<=1/10000000 and initial meter norm e0<=9/12800000000.
Both full flows must remain contractions. Duhamel gives calibrated
sample error B=8(e0+H delta_o*11/10), unchanged from the parent. With
ve=KA(1-D squared/2)-4B/s0, vl=KA(1-d squared/2)-4B/s0 and eta=B/(s0-B),
the parent homotopy theorem gives

$$
b_o=2\eta[q_{3/20}(v_e)+128q_{1/25}(v_l)],\quad
q_c(v)=\frac{1-v^2+c^2}{2cv}.
$$

For 26-bit nearest-even ADC on[-2,2), combined calibrated per-register
sensor/reference error r=9/320000000, and
zeta=(31/2)(r+2/2^26)/(s0-B), the final bound is

$$
b_{\rm total}=b_s+b_o+\frac{\zeta}{v_e-\zeta}
+128\frac{\zeta}{v_l-\zeta}<\frac1{260}<\frac1{250}.
$$

The exact computed value is about0.0037605946303rad. Observed endpoint
visibility is >0.99009065 and links >0.99956734. Active support remains
in(0.8,1.2), the ADC does not saturate and |Qhat-1|>1.7. Data gates do not
establish that an unknown instrument meets the gain, drift or noise limits.

The same gain, channel-jitter, additive/reference allocation is retained:
S=11/10+e0, eps_gain=r/(24S), j=r/[120S(1+eps_gain)], nu_noise=r/3.
The time-dependent meter generator still has ||mprime||<5S, since only
bounded detuning amplitude enters this first-derivative bound; no extra
clock precision is silently presumed. Calibration and finite-memory errors
must fit the stated combined budget. The previous64-native-unit reset,
off-port leakage and residual-preserving preparation remain requirements.
The arbitrary-channel budget has not been enlarged to the structured0.011
amplitude or its drift rate.

## 5. Limits, nulls and verification

At zero drift, audit.py recovers the parent's exact rational budget
identically. Doubling the selected rate to1/100000 produces a sufficient
phase bound about0.004177242rad and therefore **fails certification**.
This is a failure of this bound, not an exhibited trajectory failure or
an impossibility theorem. No maximal rate, unlimited-time guarantee,
unrestricted amplitude drift or port/damping tolerance box is claimed.

If all sectors have the same time-dependent detuning, their zero-reset
transfer b(t) is a common complex scalar and the analog normalized polygon
phase cancels it exactly whenever the samples are nonzero. This null
holds even for fast common detuning; for |omega|<=Omega, the Volterra
bound |b-b0|<=Omega/2<b0 ensures nonzero samples afterwarmup. Differential
sectors generally do not share that scalar. Sensor/reset errors remain
separate. The new theorem also admits abrupt bounded excursions of size
H/200000 about each fixed initial gain; Lipschitz continuity is one
sufficient way to enforce that excursion, not a necessary condition.

```bash
python3 experiments/qpb1-sector-drift/audit.py --out /tmp/ud-sector-drift
```

The deterministic constructor checks36 source hashes,13 literal ledger
rows, all512 parent rational interval cells, the rational Volterra/budget
comparisons and zero-rate identity. Numerical RK4 checks use13 changing
profiles, three windows, five preparations and three plant-gain triples:
585 exact-integer readout windows. The profiles include eight endpoint
ramps, inward boundary drift, a differential tent and sine, and two common
controls. Scalar paths include the zero-reset structured model and a
commuting additional-generator/reset subset; the full arbitrary-error
scope is analytic. Six substep-doubling comparisons and a constant-path
closed-form comparison check the ODE implementation. Binary64 trajectories
are not interval-validated. The tent has a derivative corner, so fourth-order
convergence is not asserted there. Quantization and integer phase replay
are exact after the approximate analog trajectories. Norm and phase
comparison tolerances are2e-9 and5e-9 respectively.

All thresholds were exposed development targets. Four initial rational
slope probes1/100000,1/200000,1/250000,1/500000 are preserved in the journal;
1/200000 was selected for useful passing margin, not from physical data.
The source/archive, SI clock, signed sensor, calibration, native coupling
selection and hardware realization remain OPEN; non-constructor review
and physical experiments are NOT_RUN. This is development with no registry
entry or inherited mainline physical promotion.

See [contract](DRIFT_CONTRACT.json),
[candidate](../../candidates/qpb1-sector-drift/candidate.json),
[receipt](../../sessions/qpb1-sector-drift-20261024-a1/mathematical_receipt.json)
and [run](../../artifacts/qpb1-sector-drift-20261024-a1/exact-001/manifest.json).

Next discriminant: replace the conservative per-link phase-excursion charge
with a time-dependent Volterra phase-rate bound, testing whether a materially
larger differential drift rate can be certified with the same hardware model.
