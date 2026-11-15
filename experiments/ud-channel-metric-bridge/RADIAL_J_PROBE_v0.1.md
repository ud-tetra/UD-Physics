# Charge-bounded radial probe for pure J v0.1

**EXACT / conditional.** Agile prospective design. Live main 2ab32f5;
draft baseline bfcad4f; claim 577b2d5 held. Read main's CURRENT.md
(Fixed-shell Pachner observability audit and Boundary-fixed Pachner state
transport audit) and PR #349 discussion. The related results distinguish
structural observability from metric/stock tests but provide no transferable
work-error improvement or bench qualification. No empirical target or
data was used. The witness and planning budget were known before design.

## Two amplitudes, one charge direction

Use the same normalized terminal coordinates, corrected work units W*,
and bounded errors as [joint work probe](JOINT_WORK_PROBE_v0.1.md).
Put p=(1,1), r=4/5, and define T_r=W(p)−W(rp)/r². Both commands
respect the original per-terminal charge bound. Any homogeneous
quadratic Q cancels. Along the ray, the declared polynomial
J=P(4−5uv)/9 satisfies J(tp)=t⁶(4−5t²). Hence a pure departure
W=Q+bJ gives T_(4/5)=−(4149/3125)b, so |b|=1/2 has signal 4149/6250.
Either sign is covered. The residual also responds to P: its value on P
is 9(1−r⁴); this is a pure-J detection certificate, not a J-only
estimator in the presence of unknown P.

## Separate null and alternative enclosures

At radial command tp the transferred quadratic-side receipt radius is
B(t)=8ηt+16η²+1/32, η=1/100, assuming the declared stiffness row-sum
and non-preparation budget. Thus E0=B(1)+B(r)/r²=84537/320000.
Reject zero only if |T_reported|>E0.

For each t, expand J(t+e1,t+e2) in e1,e2 and bound the difference by
L(t), the sum of absolute nonconstant coefficients weighted by
η to their total degree. Expand and combine coefficients before
taking absolute values; this certifies each endpoint box and retains
local cancellations. J is even under simultaneous sign reversal,
so the negative-command bound is identical. One loaded and three
zero-command endpoint terms suffice per corrected work.
The alternate-side radius is E0+|b|[L(1)+L(r)/r²+
3L(0)(1+1/r²)]. At |b|=1/2 the extra radius is
1426962762411241/16000000000000000
and the strict worst-case rejection margin (signal minus the sum of
the null and alternative radii) is 740777237588759/16000000000000000
in W* units. This certifies disjoint enclosures.

The exact replay searches the 99-point rational grid r=k/100,
1≤k≤99, on this single ray. Its largest certified margin occurs
at 39/50; 4/5 is retained as a simpler command with positive margin.
No global optimum is claimed. The original tolerance transfers only
if both paths' work, voltage and loss certificates are achieved.
The frozen bench, hardware hold, and physical promotion 0 stand.

Replay: python3 experiments/ud-channel-metric-bridge/radial_probe_replay.py
