# Signed eight-sector readout across the first K4 refinement v0.1

Development, no registry entry. EXACT under stated coefficient metrics and
readout. No physical target used; physical promotion 0.

## Objects and source boundary

Use the integral degree-one centroid transport F from [Pachner state transport
v0.1, 1→4](../pachner-state-transport/README.md), with ascending simplex bases
and unit coefficient metrics on C0=R15 and C1=R29. Both complexes are filled;
the outer shell is fixed and no forcing is applied. D is the oriented boundary
and A1=D1−D1ᵀ is skew, preserving fine unit stock with formal parameter u.
No event trigger, physical sampling clock, or SI units are assumed.

Read-only draft import: [Native eight-projector K4 leakage v1.1, Theorems A–D](https://github.com/ud-tetra/UD-Physics/blob/6606617f8274f435b42d28fefbd2786cf56142c4/experiments/klein-tetra-face-flip-20261103/NATIVE_EIGHT_PROJECTOR_LEAKAGE_v1.1.md).
The eight Q labels form a real parent projector resolution. Their identification
with the ledger's discrete parity states (v0.39, P03–P06) is a candidate.
The 13 here is first-refinement leakage rank/trace, not recursion depth.

Let N=I−F(FᵀF)⁻¹Fᵀ be the unit-orthogonal projection onto the 14D new
complement. Let R=NA1F and set the signed receiver C=Rᵀ. The eight labeled
readouts are QθCy, where y is a fine-state perturbation; these are vectors
in parent sectors, not eight scalar samples or apparatus measurements. All 24
signed relabelings transport the readout covariantly, without adding rank.

## Exact result and check

Reconstruction from signed incidence independently recovers
RᵀR=I−Q111 and traces (1,2,2,2,2,2,2,0) in binary order.
Thus rank C=13, C=CN, and on im N there is exactly one invisible direction:
the centroid vertex c=e4. In fact Fᵀc=0 and Rᵀc=0 by the boundary incidence,
so dimension identifies the full kernel on im N.

For y'=A1 y with y(0) in im N, the signed first derivative is CA1 y(0).
Since C=CN, the instantaneous derivative on im N can also be written
C(NA1N)y(0). The extra scalar port hᵀCA1 uses the parent unit constant-vertex
harmonic h=(e0+e1+e2+e3)/2. Each old vertex sends unit positive leakage into
its outward-oriented radial edge (i,4), while A1c is minus the sum of those
edges. Thus CA1c=−(e0+e1+e2+e3) and hᵀCA1c=−2. This scalar derivative
alone kills the remaining kernel; its sign reverses with preparation c→−c.
The full stacked exact rank is 14. This is an ideal local observability
result with known clock coordinate and signed linear readout.

The instantaneous data recover the component in im R, since R is a partial
isometry. The derivative recovers the remaining signed centroid coefficient
after subtracting the derivative contributed by the recovered component.
Equivalently, the measured vector plus one scalar derivative defines a
positive Gram on im N after specifying relative observation weights.
Such a Gram measures distinguishability under that observation convention.

## Metric selection and physical gate

The above computation holds the fine unit metric fixed. It does not select
the physical metric, nor can its unit-metric derivative be substituted into
another generator without recomputation. In the separate Discovery
*UD K4 intercomplex action and positive metric source-selection audit v2.1*
(2026-11-06, §§3–5), the metrics H_t agree on inherited states but differ
on the newborn ker(P) of a different projector; the fine generator is
identical for all t>0 within that family. For any fixed readout L and fixed
preparation y, L exp(u A_t)y is then independent of t. Even perfect signed
state reconstruction in that family cannot identify t by this data alone.
A readout that explicitly uses H_t would require an independent physical
definition and calibration. Do not infer that the centroid witness above
selects t or identifies either new complement with physical displacement.

Next: independently specify a newborn support/energy measurement or calibrated
work input, with fixed preparation and a matched control, that changes across
the H_t family. Freeze the discriminant before acquiring physical targets.
No 13-layer sweep is justified by the observed rank or by the eight-label mean.

Replay: python3 experiments/ud-channel-metric-bridge/replay.py
Exact stdlib Fraction checks; constructor verification only.

Follow-up: [centroid work port v0.1](WORK_PORT_v0.1.md) conditionally
identifies the dimensionless newborn metric weight and tests a uniform
coefficient-energy control. No apparatus data have been acquired.

The [two-port capacitor emulator](CAPACITOR_PORT_v0.1.md) specifies
two concrete fixtures, a signed charge audit, and a sufficient
deterministic decision margin. Bench performance remains unmeasured.

The [signed acquisition replay](ACQUISITION_SIM_v0.1.md) exercises
independent synthetic charge and work channels, certificate gates,
and the strict sign rule on fault and boundary controls.

The [frozen blind bench protocol](BLINDED_BENCH_v0.1.md) adds trial
inventory, identity custody, endpoint/work gates, and a replayable scorer.
No hardware run or allocation has been made.

The [qualification and review handoff](QUALIFICATION_HANDOFF_v0.1.md)
converts the frozen bench limits to instrument units and identifies
the raw evidence required before a concealed assignment.

[Independent review intake](REVIEW_INTAKE_v0.1.md) records the submitted
scope and holds physical qualification open pending measured evidence.
