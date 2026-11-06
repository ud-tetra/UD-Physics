# Q170 complete shell-current interface and second-order K4 obstruction v1.9

**2026-11-05 — EXACT / CONDITIONAL / SCOPED NO-GO.** Held claim `klein-tetra-face-flip-20261103` at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`, session `ktff-20261103-01`, isolated draft PR #301. Verified main `b04652406b5579ca172564d0e3a6fe3aca75693a`; task original base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`. Frozen ledger and shared state remain unchanged. Physical promotion 0.

## Source and typed interface

Source-bound Q165/Q166/Q169/Q170/Q171 ledger v0.39; exact QPB1 unit signed generator `A_K=D_K-D_K^T`, original filled K4 `C_old=R15` and centroid refined `C_new=R29` with *independent unit chain coefficient metrics*. Prior `CROSS_COMPLEX_NATIVE_TRANSFER_v1.7.md`, `Q171_SIGNED_ADMISSION_v1.8.md` derive the signed subdivision `F:C_old→C_new` with `F^TF-I15=3e_top e_top^T`, and the **candidate** top-zero admission gate `a=<e_top,x>=0`. The continuous parameter `u` is formal, not SI time.

Let `T:R14→R29` be F restricted to the 14 original vertex/edge/outer-face coordinates, and `N=I29-TT^T` the projector on the 15 newly created registers. A top-zero parent state `(z,0)` is transferred to `Tz`. The 14 original lower-grade simplices are carried with unchanged amplitudes and identical internal incidence matrix:
```
T^TT=I14,  T^T A_new T = (A_old)_shell,shell.
```
At the event removed old top and every new register have amplitude zero. Consequently **for every subset U of the original 14 shell registers**, Q165 shell stock and Q170 instantaneous signed cut currents agree on old and new sides: both old-top and new-born cut terms vanish. The first derivative of every shared-shell stock agrees. This proves a *zero-jet/first-jet current receipt* for a **postulated event**, not a source-selected global current law. A fixed rational preparation was also exhaustively checked over all `2^14=16384` subsets.

## All-depth-independent local cone lemma — exact second-order obstruction

Every old 0-,1-,2-simplex `sigma` has exactly one *new* cone simplex `sigma∪{4}` of degree one higher, with native skew incidence coefficient `(-1)^(dim(sigma)+1)`. The 14 cone simplices are distinct and the remaining centroid vertex is initially uncoupled from original shell registers. Thus the new transverse derivative `Lnew=N A_new T:R14→R29` is a **signed isometric embedding**:
```
Lnew^T Lnew = I14,  rank(Lnew)=14.
```
In the old complex, only the old top cell lies outside the 14-shell. Let `b=(partial_3 e_top)/2` (unit outer-face signed mode). The old top derivative map is
```
Lold=e_top^T A_old T=-2 b_sh^T,
Lold^T Lold = 4 b_sh b_sh^T.
```
Since both original and new matrices are skew, exact multiplication yields:
```
M := T^T A_new^2 T - (A_old^2)_shell,shell
   = Lold^T Lold - Lnew^T Lnew
   = 4 b_sh b_sh^T - I14.
spec(M) = {3 (multiplicity1), -1 (multiplicity13)}, rank M=14.
```
**NO-GO, exact hypotheses:** No **nonzero** parent state eligible under `a=0` has identical second derivatives of *all original shell amplitudes* on both unmodified native flows. Any claim of generator-smooth cross-complex continuation needs a new coupling, metric, mapping, or additional dynamical operation. This does not forbid a discrete nonsmooth event.

For shell initial state `z` and `beta=<b,z>`, the removed old top and the newly born 15D support obey:
```
S_old_removed_top(u) = 4 beta^2 u^2+O(u^3);
S_new_born(u) = ||z||^2 u^2+O(u^3).
```
Both cut currents are zero at the switch, but their formal slopes are `8 beta^2` and `2||z||^2`. For normalized `z=b`, these are exactly `S_old_top=sin^2(2u)`, `S_new_childtops=sin^2(u)`, and cut currents `2 sin(4u)` versus `sin(2u)`. For a nonzero `z⊥b`, the old top remains silent while new cone support begins as `||z||^2u^2`. Even if some state's aggregate second stock changes happen to match, M is invertible and its full shared-shell amplitude acceleration cannot match.

**Signed-current proposal for source review:** `Q171_DIRECTION_AMENDMENT_PROPOSAL_v0.39a.md` retains frozen wording and proposes positive `2B3 cface ctop` as *face gain/top outward current* while `dot S_top=-2Σ B3 cface ctop` in the source Q169 `A=D-D^T` convention. A separately typed `B3_Q171=-B3_Q169` is an alternate candidate resolution. No source-authoritative decision has yet been received.

## Decision, reproducibility and next gate

**EXACT/CONDITIONAL:** Q165 and every Q170 original-shell cut match at the candidate event instant, and all shared-shell stock first derivatives match. The new signed cone incidence is an isometry rank14 while old removed-top excitability is rank1; the full-rank second-derivative mismatch gives a **NO-GO for dynamically smooth continuation under both unchanged generators**.

**OPEN:** Source-authoritative Q171 direction amendment; truly selected top-zero event and its time; alternative cross-complex action/current/metric; physical observation and SI unit bridge. Physical promotion 0.

Locally executed: `current_interface_v19.py`, independent cone derivation `independent_cone_current_v19.py`, regression suite 12/12 PASS including 16,384 Q170 subset fixtures; exact results and SHA-256 manifest bundled in downloadable `UD_K4_Q170_INTERFACE_v1.9.zip`. GitHub independently authored concise replay and machine result are source-equivalent, not claimed byte-identical with local package. Independent non-constructor review NOT_RUN; integrity CI checks structure only.