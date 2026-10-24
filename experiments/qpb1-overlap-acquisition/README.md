# Local overlap acquisition and integer phase contract v1.0

**RESULT — EXACT / CONDITIONAL.** Seven local amplitude/quadrature pairs
recover the complete rank-14 active carrier, including its edge-hidden
plane. A signed 15-register sampler realizes these pairs through one-hop
incidence sums. All overlap, support, visibility and phase-direction
processing after digitization can use exact integers. Under the explicit
sensor and memory assumptions below, a 26-bit design meets the preceding
one-part-per-million link-overlap budget. A separately amended 21-bit design
meets the overall 0.004-radian phase requirement. These are sufficient
mathematical designs, not measured sensor capabilities.

Base `ud-tetra/UD-Physics@53460195f74411ce764b24e0ab9d4fd772c4bd6f`;
2026-10-23, America/Chicago. [SOURCES.json](SOURCES.json) pins 21 dependencies;
[SOURCE_ROWS.json](SOURCE_ROWS.json) preserves 13 literal archive-v0.85 rows,
including scientific revision v0.43 and the frozen G06 convention. Uploaded
v0.39/governance bytes were freshly compared to their committed imports.
Missing Genesis PNG and placeholder physics documents provide no law.
Physical score **UNSCORED**, promotion **0**. No mainline export or shared
CURRENT/source-ledger change is made.

## 1. Typed carrier and complete local channels

Retain the filled tetrahedron's real chain carrier C=R^15, ascending simplex
orientations, Euclidean metric, incidence generator A=d-d^T, J=A/2 and
active projector P=-J^2 of rank 14. The remaining harmonic line is separate.
These are the existing audit's objects, not spatial detector coordinates.
For the six oriented edges and the oriented top cell, use anchor a and set

\[
q_a=x_a,\qquad p_a=(Jx)_a=\tfrac12\sum_\sigma A_{a\sigma}x_\sigma.
\]

An edge p uses its two vertices and its two incident faces. The top-cell p
uses its four faces. Each is a signed, one-hop Hasse-incidence operation,
not an edge in physical spacetime. In particular the two hidden channels
are the top-cell amplitude and its signed boundary-face combination.
Do not substitute x'/2 for Jx under unequal gains.

Let T:C->R^14 stack these q,p rows, with top-cell pair last. Exact rational
matrix calculation gives

\[
TT^T=I_{14},\quad T^TT=P,\quad
Px=\sum_a(q_a e_a-p_a Je_a),\quad
\|Px\|^2=\sum_a(q_a^2+p_a^2).
\]

Thus T is an isometry on the active space and a contraction on C. Its
kernel is precisely the harmonic line. Edge-only pairs have rank 12;
omitting either hidden row leaves rank 13. Active normalization is not
the full 15-register norm when harmonic support is present.

For two nonzero active projections, their Hermitian overlap is

\[
h_J(\widehat x,\widehat y)=\frac{C+iS}{\|Px\|\|Py\|},\qquad
C=\sum_a(q_a u_a+p_a v_a),\quad
S=\sum_a(p_a u_a-q_a v_a),
\]

where (u,v)=Ty and hats denote unit active states. Equivalently complex
coefficients are q-ip. Seven local block products and an aggregate sum
replace an assumed overlap oracle. This still requires simultaneous,
calibrated, **signed amplitude** access: it is distributed full active
readout, not a demonstrated physical measurement mechanism.

## 2. What instantaneous stocks cannot supply

**Scoped NO-GO.** The active states x+=e01+e02 and x-=e01-e02 have identical
all-15 coordinate squares and equal norm squared 2. Their normalized complex
overlap is zero; x+ has overlap one with itself. Even a known reference
therefore cannot recover arbitrary overlaps from one snapshot of stocks
alone. Preparation constraints, extra observables or known time histories
could change this obstruction's hypotheses.

More generally any real linear snapshot map from E=im P to R^m, m<14, has
a unit kernel vector v. Choose unit u perpendicular to v,Jv and let
x±=sqrt(1-t^2)u±tv, 0<t<1. They give identical linear observations and unit
norms, yet h_J(x+,x-)=1-2t^2. Thus fewer than 14 real linear channels cannot
recover every instantaneous active overlap, even with known norm. This is
not a minimum for nonlinear or dynamical tomography, and says nothing about
physical quantum-state measurement counts.

## 3. Digitization, exact gates and phase output

Sample all 15 raw registers at each of 129 common native instants. Use a
b-bit signed uniform grid of range [-2,2), step Delta=4/2^b, nearest-even
rounding, and reject saturation. If c_sigma are integer sample codes, decode
in coefficient unit u=Delta/2=2^(1-b):

\[
Q_a=2c_a,\quad P_a=\sum_\sigma A_{a\sigma}c_\sigma,\quad
N=\sum_a(Q_a^2+P_a^2).
\]

The raw count c, coefficient P_a, active projector P and physical units are
distinct typed objects. The coefficient integers supply C,S by the formula
above; normalized visibility squared is exactly (C^2+S^2)/(N_x N_y).
No square root is needed for these strict gates:

| Qualification | Exact integer comparison |
| --- | --- |
| Active norm in (4/5,6/5) | 16*2^(2b-2) < 25N < 36*2^(2b-2) |
| Endpoint visibility >99/100 | 10000(C^2+S^2) >9801 N_x N_y |
| Every link visibility >999/1000 | 1000000(C^2+S^2) >998001 N_x N_y |

Endpoint times conjugated adjacent overlaps gives the Gaussian integer

\[
B=(C_{0M}+iS_{0M})\prod_{j=0}^{127}(C_j-iS_j).
\]

Return its nonzero integer pair (Re B,Im B), interpreted up to a positive
scale, as the exact phase direction. Positive gcd reduction after each
multiply limits growth without changing direction. There is no arithmetic
roundoff after digitization; optional atan2 display is outside the
certificate. SATURATED, LOW_SUPPORT or LOW_VISIBILITY returns no phase.
These gates check data qualification, not truth of the sensor-error model.

The exact geometric estimator is invariant under independent snapshot
phase changes and signed S4 relabeling, as in the parent. Nearest-even
quantization commutes with signed register permutations while unclipped.
A finite Cartesian quantizer does not commute with arbitrary continuous
U(1) rotations: acquiring and requantizing in another phase frame creates
a different noisy dataset. Each is covered by the same error contract;
bit-identical outputs are not claimed. Exact postprocessing frame changes
of an already decoded dataset retain the geometric invariance.

## 4. Sensor, normalization and phase-error certificate

Retain all parent preparation, gain, native-window and maximum-gap
assumptions from finite-window README sections 4-5. In particular an active
raw state has norm s in [9/10,11/10], M=128, gain errors <=1/100, and
|T-2pi|<=1/100. The underlying comparison is the same preparation's
Q0=exp(-2pi*i*r_hidden); it is -1 only at the central preparation.

Assume a combined raw sensor plus decoded-reference perturbation at each
register of absolute magnitude <=r, before the final quantization error
is counted. Bit-exact storage is the default, with zero additional memory
perturbation. If bounded decoded-memory perturbations are instead allowed,
they consume this same combined budget; quantization is still counted once.
No independence, averaging benefit or statistical noise law is assumed.
Let a=r+2/2^b and s_min=9/10. Contraction of T gives coefficient error
e<=sqrt(15)*a. For x nonzero and x+evec nonzero,

\[
\left\|\frac{x+evec}{\|x+evec\|}-\frac{x}{\|x\|}\right\|
\le \frac{2\|evec\|}{\|x\|}.
\]

This follows by inserting (x+evec)/||x|| and using reverse triangle
inequality for the two norms. Cauchy-Schwarz bounds complex overlap error
by the sum of the two unit-state errors. Since sqrt(15)<31/8 (960<961), a
uniform sufficient absolute complex-overlap error is

\[
\zeta=\frac{31a}{2s_{\min}}.
\]

The same contraction ensures observed active norms in (4/5,6/5), and
per-register range remains strictly within the ADC range. Use the parent's
exact bounds v,v_l,b_g,b_s, explicitly pinned in SOURCES.json:

\[
b_{\rm total}=b_g+b_s+\frac{\zeta}{v-\zeta}
 +128\frac{\zeta}{v_\ell-\zeta}.
\]

| Profile | b | Combined r | Uniform overlap bound zeta | Total phase bound |
| --- | ---: | --- | --- | --- |
| STRICT_A | 26 | (9/10)/32000000 | 4707443/4718592000000 <10^-6 | <1/500 rad |
| REALLOCATED_B | 21 | (9/10)/8000000 | 2707571/147456000000 <0.000018362 | <1/250 rad |

STRICT_A meets the earlier 10^-6 link budget and gives a stronger endpoint
budget too; its exact total is approximately 0.001597183 radians, rounded
up here. REALLOCATED_B is an **explicit protocol amendment**, relaxing the
link budget while strengthening the earlier 10^-3 endpoint budget. It does
not meet the original strict link condition. Its exact total is about
0.003838092 radians, rounded up. Both preserve endpoint visibility >0.99,
link visibility >0.999 and |Qhat-1|>1.7 over the declared continuous domain.

At the same r, 25 bits fail this sufficient strict-link bound while still
passing the total phase budget. At the amended r, 20 bits fail this total
bound. Neither failure proves hardware impossibility or optimal bit depth.
These controls were chosen after exposure to the parent's budgets and
reference candidate; no target-blind or empirical success is claimed.
Resolution alone establishes neither analog accuracy nor synchronization,
loading, gain calibration, clock calibration or access to signed values.

## 5. Finite reference memory and reset

A streaming implementation keeps initial, previous and current raw records:
45 b-bit classical words. Retain the initial record throughout T<=4407/700
native units and the previous record for one gap. Compute the link product,
then endpoint factor; after committing the result, qualification status and
calibration metadata, reset/reuse the buffers. The exact final phase pair
can then be retained without the entire trajectory.

Under the observed norm gate, each decoded coefficient is <2^b in
magnitude and N<2^(2b+4), a deliberately loose bound. Cauchy-Schwarz gives
|C+iS|<2^(2b+4). For 129 factors a safe signed bound per final component is
129(2b+4)+1 bits: 7,225 for STRICT_A, 5,935 for REALLOCATED_B. STRICT_A's
raw buffers use 1,170 bits; its two bounded phase components plus those
buffers use 15,620 bits, excluding calibration, counters and intermediate
working storage. These are data-width bounds, not entropy, energy or a
complete physical memory design. Stored records are classical numbers;
copying an unknown physical quantum state is not posited.

No physical reference lifetime, fault tolerance, erasure energy or signed
amplitude transducer follows from this digital protocol. A record corrupted
beyond the declared budget invalidates the certificate even if gates pass.

## 6. Reproduction, limits and next discriminant

From repository root with standard-library Python:

```bash
python3 experiments/qpb1-overlap-acquisition/audit.py --out /tmp/ud-overlap-acquisition
```

**Exact constructor checks:** 21 source hashes, 13 literal ledger rows,
complete rational matrix identities/ranks, 100 decoder/overlap fixtures,
all 24 signed S4 actions, 420 exact quantizer fixtures, strict visibility
equality rejection, and rational profile comparisons. General proofs above
cover the stated continuous error domain; samples alone do not establish it.
The source code's T-row preparation basis was corrected before the first
successful audit and capture. No frozen run was modified.

**NUMERICAL constructor cross-check:** two bit profiles, 29 preparations
and four bounded commuting drift/window profiles produce 232 windows of
129 raw snapshots each. Synthetic binary64 trajectories and imposed sensor
errors feed exact rational nearest-even digitization, then the exact integer
estimator. Optional phase display is checked with tolerance 5e-11 rad;
maximum observed display error is about0.000100196 rad. This is neither
interval validation, an independent review nor an experiment. The captured
worst-case raw integer record reproduces its exact phase direction without
the numerical trajectory generator. LOW_SUPPORT and SATURATED controls
return no phase; gate equalities are rejected exactly.

Limits: simultaneous calibrated signed access and bit-exact classical
storage remain assumptions. The protocol observes the full active carrier,
including the hidden plane; it does not evade full information access.
Backaction/loading, mode mixing, changing metric, actual clock/analog
calibration, detuning selection, physical normalization and eta_A remain
OPEN. It gives phase modulo2pi, not lifted winding, native action magnitude,
spin quantization or a spacetime law.

See [contract](ACQUISITION_CONTRACT.json),
[candidate](../../candidates/qpb1-overlap-acquisition/candidate.json),
[receipt](../../sessions/qpb1-overlap-acquisition-20261023-a1/mathematical_receipt.json),
and [immutable run](../../artifacts/qpb1-overlap-acquisition-20261023-a1/exact-001/manifest.json).

**Next discriminant:** specify an explicit local meter/reference coupling
and bound its loading, synchronization and calibration errors against this
contract. Test whether signed sampling, especially the hidden pair, is
realizable within the allowed dynamics rather than merely assumed.
