# Symmetric parity event hypothesis v0.1

**HYPOTHESIS.** A local event is an integer-tick transfer of one dimensionless occupancy unit between one addressed opposite-edge parity register and a nonnegative reserve. The address is part of the pre-event state. A transfer occurs only when the address is unique and the reserve can supply an opening. Multiple or absent addresses and an empty reserve at a proposed opening return HOLD. This is a deliberately new constitutive rule, not Q198, Q205 or Q208.

## Sources, target exposure, and types

Base `ud-tetra/UD-Physics@8b11c934e7960b2b57d147e1364aaea195397998`; source [orbit arithmetic v0.1](../ud-native-orbit-arithmetic/README.md) identifies the three coordinates with opposite-edge matchings of K4. [Polarity gate v0.2](../ud-native-orbit-arithmetic/POLARITY_GATE_v0.2.md) demonstrates endpoint ambiguity under net Hamming budget. Recovered ledger v0.85 at `experiments/action-normalization-audit/sources/ledger_v0.85.json`, SHA-256 `8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec`, Q194–Q214 supplies a conditional Q198 interface, Q204's typed latent receipt and Q210's obstruction. The binary address below is a new *candidate input* and is not identified with Q204's obligation. No Gibson fraction, measured constant, endpoint record, or target-selected coefficient enters the rule.

Let `P` be the three labeled opposite-edge matchings and `Theta={0,1}^P`. The coefficient domain for stock is the nonnegative integers. The state is `X=(theta,r,a) in Theta x N0 x Theta`; `r` is a dimensionless reserve count and `a` is an immutable address mask. It has no assigned physical energy or mass. The integer index `n` increments once per call to `F:X -> X x {EVENT,HOLD_ADDRESS,HOLD_STOCK}`; there is no clock-duration map. S4 acts on `theta,a` through the induced permutation of P and fixes `r`. No metric or sign orientation is used. The readout is `theta` and the event verdict. The conserved stock is `N=|theta|+r`.

## The parity-only obstruction

**EXACT / NO-GO under stated hypotheses.** If `f:Theta -> Theta` is deterministic, commutes with all induced S4 permutations of P, and conserves Hamming weight `|f(theta)|=|theta|`, then `f=id`.

Proof: S4 induces all S3 permutations on the three matchings. For input `000` and `111`, weight conservation fixes the image. For `100`, the stabilizer includes the swap of the other two coordinates. Among weight-one outputs only `100` is fixed by that swap. Equivariance fixes the images of `010,001` by permutation. The same argument for `011` fixes all three weight-two inputs. Thus every input is fixed. This obstruction concerns a parity-only, globally S4-equivariant, Hamming-conserving deterministic map. Adding an address, reserve, a nonconserving source, or restricting symmetry changes the hypotheses.

## Addressed one-tick rule

**CANDIDATE / exact conditional mathematics.** For `|a| != 1`, return `(theta,r,a,HOLD_ADDRESS)`. Otherwise write `a=e_p`. If `theta_p=0,r=0`, return `(theta,r,a,HOLD_STOCK)`. In every other case set

`theta'_p=1-theta_p`, `theta'_q=theta_q (q != p)`, `r'=r+2 theta_p-1`, `a'=a`, verdict `EVENT`.

The opening case subtracts one reserve unit; the closing case adds one. The guard makes `r' >= 0`. In both cases `|theta'|+r'=|theta|+r`. Permuting both masks commutes with this rule; the reserve is scalar. At a fixed address and fixed spectator bits of weight `m`, for total stock `N=m` the only state holds (`theta_p=0,r=0`). For each `N>m`, the two states `(theta_p,r)=(0,N-m)` and `(1,N-m-1)` alternate with period two. Other address masks hold. Hence `F^2` returns the state (the verdict is not a stored component). There is no attractor, growth, unique clock rate, or independent physical prediction.

The eight starting `theta` states are explicitly replayed at `a=100`, `r=0,1` in [results.json](results.json). The exhaustive check covers all `8 x 4 x 8=256` states for `r=0..3`, all six induced coordinate permutations, conservation and two-tick return; the proof covers all nonnegative reserves. The address is held fixed by this candidate and may be an externally prepared pre-event condition. The law does not select address preparation or evolve the underlying C0/C1/edge-integrity fields. Its finite-state autonomy is conditional on a fixed address; it is not a closed packet-plus-environment dynamics.

**OPEN / source gate.** No source theorem selects the flip rule, the reserve interpretation, or address preparation. Q198's continuation `T:L^- -> L^+`, burden `W^B2`, and obligation semantics remain separate and unconstructed. This toy cannot be counted as a Q198 replay or a physical correspondence. Physical promotion 0. To outperform the identity baseline, a source-complete independent event record must test the pre-frozen address, reserve and endpoint without selecting them from outcomes.
