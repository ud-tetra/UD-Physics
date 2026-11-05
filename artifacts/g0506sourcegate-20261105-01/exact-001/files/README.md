# G05/G06 packet-to-Hodge source and unit gate v0.1

2026-11-05 · Discovery base `ud-tetra/UD-Physics@738b9d205fd9f9735a05d4976de70f1519474bff` · physical promotion **0**.

## Question, source scope, and types

Can the four source packet sites select an active Hodge map and the absolute action unit, while passing directional reversal, finite-step sampling and all-sector tests? The historical `ud-tetra/UD@a78193d420f3bac957be081aed0525fbc1457825`, `docs/UD_Master_Full.tex` §§Foundational Axioms, Packet Action, Transport Seed and Obstruction (captured SHA-256 `4c93f63cb57f9de7959919e20a7d2811f6a29832701b20aa98c4de4c99e4feb3`) gives packet `X_i=(ρ_i,θ_i,χ_i,σ_i,b_i)`, neighboring `U_ij`, a phase-difference-squared action and `T/T0=exp[-(σ_O+σ_B+σ_C)]`. It gives neither a packet amplitude into the chain complex nor the three numerical obstruction functions. The current recovered ledger v0.85 (captured SHA-256 `8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec`) explicitly marks O07 open; O09 is the lifted Hodge action, Q136 the scalar history, Q137 only a conditional normalized coordinate, Q139 the dimensional action scale open, and Q141–Q145 bar direct even-diagnostic/operator substitution. Q181 and Q282–Q286 normalize an *already chosen* positive ray; they do not prepare that ray in a physical apparatus. The supplied ledger v0.39 (2026-08-22), §§G05/G06/O07/Q136–Q146, is a historical source stratum, not a replacement for v0.85. The supplied Governance CRL-2 v1.0 §6 leaves nonconstructor review required. The public portal landing status checked 2026-11-05 is Papers I–III 1.1.1, IV 0.1, physical promotion 0; its landing page provides no map. This is a bounded inspection of these sources and the cited prior audits, not an exhaustive claim about all project history.

Native carrier: the oriented filled K4 real chain `C=R^15` in ascending simplex basis and unit coefficient metric. `A=d−d^T`, `J=A/2`, `P_k=−(d_k−d_k^T)^2/4` have mutually orthogonal active ranks `6,6,2`. Native evolution is `x'=Ax` in dimensionless parameter `s`; `a=<x,x>` and `ϑ=<Jx,dx>/2` have no physical units here. Packet `ρ` is a source burden stock, not automatically the squared amplitude `a`. The map below **assumes** `z_i=√ρ_i exp(iθ_i)` and imports the native generator; the known O09 target influenced its form. No parameter is fitted to physical data.

## 1. A canonical restricted construction and its obstruction

Let `u=Re z`, `v=Im z` in `R^4`, and `P0=I4−11^T/4` be the vertex mean-zero projector, embedded in `C`. Define the **CANDIDATE / target-informed** linear map

`F:C^4→E`, `F(z)=P0u+J P0v`.

**EXACT under the declared carrier:** `rank F=6`, `P_1 F=F`, `P_2 F=P_3 F=0`; signed simplex `S4` action intertwines the site relabeling. The native support is

`a(Fz)=Σ_i |z_i−z̄|²=Σ_i ρ_i−(1/4)|Σ_i z_i|²=(1/4)Σ_(i<j)|z_i−z_j|²`.

The last equality uses four sites. It is an exact pair-difference identity, not a source equation for burden. If the **imposed** site update is `z'=2iz`, then `F(z)'=AF(z)`, so the image is dynamically invariant. The historical packet postulate does not impose this common rotation, determine initial `z`, supply an open-system source/sink or specify boundary conditions. `F` kills the common site mode and all of sectors 2 and 3. A full-active correspondence needs eight more real directions (at least four additional complex orbit planes under a J-intertwining linear construction), with source-defined edge/face/top variables or a declared restricted physical scope.

**EXACT pullback:** For two site states `z,w`, the preceding Hasse step obeys `q_H(Fz,Fw)=1/2 Im Σ_i conjugate(z_i−z̄)(w_i−w̄)`. This is incidence-local on the image, S4 invariant, reversal odd, and integrates `F*ϑ` on the straight chord. It retains the previous [finite-step alias](../g0506-step-kernel-unitgate/README.md) §1: two antipodal endpoints do not reveal lifted winding, and a native common-orbit arc needs `|Δs|<π/2` per sample plus a known same-orbit premise. A source directional obstruction would still need a packet-to-`Σ` allocation and a temporal phase/connection rule; identifying `Σ` with this `q_H` is an O09-targeted proposal, not Q136's derivation. Its reciprocal orientation weights can exceed the seed ratio on the reverse path. If all three obstructions are nonnegative penalties on both directions, this signed identification has only the zero case.

## 2. Unit-selection and common-mode counterexamples

Fix **the same** four burdens `ρ_i=1/4` and vary only phases `θ_i∈{0,π}`. All have `Σρ=1`, yet `a(Fz)` is `0` for phases `(0,0,0,0)`, `1` for `(0,π,0,π)`, and `3/4` for `(0,0,0,π)`. **EXACT / NO-GO under the F hypothesis:** total burden one does not select native support one. A phase-balanced condition `Σz=0` would select `a=1` at that burden total, but neither the packet source nor the physical preparation selects that condition. General scaling `z→cz` multiplies `a` and the loop action by `c²`.

The earlier site one-form `β_pkt=1/2 Im Σ conjugate(z_i)dz_i` and the actual pullback obey

`F*ϑ=β_pkt−2 Im(conjugate(z̄)d z̄)`.

Thus an equal-site common-phase quarter turn with `ρ_i=1/4` has naïve packet step `1/2` and Hodge step **0**: the common packet phase is in `ker F`. The candidate cannot use that phase-area expression as a universal obstruction without a sourced treatment of the kernel. A local phase-frame change also requires a compensating temporal connection; spatial `U_ij` holonomy alone does not supply it. None of these equal native numbers fixes O10's dimensional `A0=B0 a0²/τ0`, O14's `A0/ħ`, or an LC flux magnitude.

## Disposition and reproducibility

**NO-GO, scoped:** This four-site vertex construction cannot be a full `E14` map or select a unique support-one physical preparation. It is a valid six-dimensional, target-informed analogue under the stated `z` and `z'=2iz` assumptions. The historical source and recovered ledger do not choose `F`, a temporal update, an obstruction map, an absolute unit, or a device. A different packet assembly/edge-face source, restricted image, or a sourced phase-balanced preparation is a new branch; the previous dimension and parity gates remain under their hypotheses. No physical promotion or mainline registry amendment.

`python3 experiments/g0506-packet-hodge-sourcegate/audit.py` replays rational projector ranks, the 24 signed S4 actions, intertwining, q pullback and three same-burden unit counterexamples. The proof of the pair identity and the frame/source observations are analytic in this report. The audit is a constructor check, not independent mathematical or empirical review. The [receipt](../../candidates/g0506-packet-hodge-sourcegate/mathematical_receipt.json), [run manifest](../../artifacts/g0506sourcegate-20261105-01/exact-001/manifest.json) and [result](results.json) carry exact inputs and checks.

**Next discriminant:** source a packet evolution/temporal transport rule and at least the missing sector channels, or declare a restricted P1 target. Freeze an independently prepared support/phase reference before testing an obstruction or LC action scale; reject any proposed map if common-mode, sign reversal or sampled-winding controls fail.
