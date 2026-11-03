# Pachner switch support ledger v0.1

**2026-11-03 — exact finite calculation, conditional hybrid law; physical promotion 0.** Source base `3026f7a673dbec6103aae2a68a20bb94b61b61ae`. The read-only *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165/Q169/Q170/Q177/Q178, specifies unit quadratic coefficient stock, a skew fixed-complex generator, local incidence support balance, and ownership of existing stock. [Prior exact chain maps](../pachner-state-transport/README.md) specify the 1→4 integral and 2→3 rational full-symmetry transports on two snapped balls. They do not specify an event trigger, event time, reservoir, or physical energy.

## Object, conditions, and question

For each fixed finite complex `K`, let `V_K=⊕_(k=0)^3 C_k(K;Q)` in ascending oriented simplex bases, with declared unit coefficient metric `S_K(c)=cᵀc`. Between switches, the source generator is `dc/dt=A_K c`, `A_K=B_K−B_Kᵀ`, hence `dS_K/dt=0` for its formal parameter `t`. This `t` has **no calibrated seconds**. At a prescribed 1→4 or 2→3 event let `c⁺=M c⁻`, where `M` is exactly the previously declared boundary-fixed chain map, block diagonal by degree. The shell, coordinate sets, maps and symmetry groups are those in the prior note. Here `M:V_old→V_new` is linear over `Q`; there is no source-selected switch condition. Define the **exact jump form**

`ΔS(c)=S_new(Mc)−S_old(c)=cᵀQ_M c`, where `Q_M=MᵀM−I`.

The question is whether the same Q165 stock survives each move and, if not, what a *separately assumed* support reservoir would have to supply. An equal shell chain or preserved relative fundamental class is a different typed object from this scalar stock. No physical charge or heat is identified.

## Exact finite result

| Move and transport | Old/new chain dimensions | `rank M`, `dim ker M` | Spectrum of `Q_M` (multiplicity) | Fundamental top stock `old→new` |
| --- | ---: | ---: | --- | ---: |
| 1→4 integral S₄ equivariant | 15 / 29 | 15, 0 | `3 (1), 0 (14)` | `1→4`, jump `+3` |
| 2→3 rational S₃×C₂ equivariant | 23 / 27 | 21, 2 | `3/2 (1), 1/2 (1), −1 (2), 0 (19)` | `2→3`, jump `+1` |

**DERIVED / exact under the stated metric and maps:** A 1→4 event increases stock by `3a²`, with `a` the old top coefficient. The 2→3 jump is indefinite: the old positive fundamental top chain gains `1`, but the opposite top chain `U−D` has old stock `2` and maps to zero, losing `2`. Thus the same move has no state-independent scalar jump. For unit old stock, the maximum required positive support is `3` (1→4) or `3/2` (2→3), by the spectral bound. These are native coefficient-stock units, not joules.

The 2→3 old internal face has image on six **boundary** faces with coefficients of absolute value `1/2`. Although every old boundary simplex basis vector maps to itself, an arbitrary old state with internal-face amplitude can change boundary-face amplitudes. Fixed boundary geometry and boundary basis identity therefore do not imply a fixed boundary *state*. The full map is not injective (`dim ker M=2`).

Independent algebraic check: the 1→4 form is `3` on the one old top dimension and zero elsewhere. For 2→3, the top block has eigenvalues `1/2,−1` (both old top cells map to one half of the three-cell fundamental chain). The face block couples the old internal face to six boundary faces: its off-diagonal vector has squared norm `3/2` and its internal diagonal is `1/2`, giving eigenvalues `3/2,−1`; other coordinates contribute `0`. The exact rational rank, eigenspace multiplicities, and annihilating polynomial are separately replayed in [audit.py](audit.py) and [results.json](results.json).

## Conditional support bookkeeping and obstruction

**CANDIDATE / not source-selected:** Introduce an auxiliary scalar `R≥0` measured in **the same defined coefficient-stock units**. During each fixed-complex interval set `dR/dt=0`. At the prescribed switch set `R⁺=R⁻−ΔS(c⁻)`; admit it only if `R⁻≥max(0,ΔS(c⁻))`. Then `S+R` is exactly conserved during the formal flow and at the switch. For the two fundamental inputs, minimum initial reserves are `3` and `1`; for `U−D` the reserve receives `2`. Universal admission for every old state with `S_old≤s` needs reserve at least `3s` or `3s/2`, respectively. This is an algebraic feasibility condition, not a prediction that a reservoir exists.

**NO-GO / scoped to the specified 2→3 map and scalar update:** A scalar `R` does not recover the lost two-dimensional kernel. The distinct states `U−D` and `−U+D`, starting with the same `R`, both map to `c⁺=0` and `R⁺=R+2`. Any injective linear auxiliary carrier must retain at least two independent old-state coordinates; a scalar quadratic reserve cannot record the sign even on this explicit pair. Adding such memory would still leave its coupling and dynamics unspecified.

Q177's `1/n₃(σ)` shares each existing simplex stock among its incident top cells. Summing the cell-owned stocks gives exactly `S_K(c)` *within* either complex; the calculation checks this for each example. It supplies neither an inter-complex transfer nor the positive support needed at a switch. Q170's local control-volume continuity applies to its declared fixed incidence geometry; its support flux cannot be relabeled as a cross-move actuator without an interface definition. The exact balance above is **not** a sourced event law.

## Disposition and discriminant

AUTO_LOCK only the scoped finite jump spectra, counterexamples, ownership sum and conditional conservation identity after exact replay. Keep the existence and selection of `R`, event schedule, memory carrier, and physical observable **OPEN_GATED**. AUTO_FREEZE any claim that Q177 itself pays the stock jump, or that conserved `S+R` already describes energy/electric charge. No fit or measured target entered the calculation. Independent non-constructor review NOT_RUN.

Next discriminant: give a source-bound local switch interface, including a state-dependent trigger, a carrier supplying at least the required gain, explicit boundary support flux, and a memory rule for the 2→3 kernel. Check its conservation and reversibility on these exact balls *before* proposing a physical readout. Run `python3 experiments/pachner-switch-ledger/audit.py`; the immutable captured run records code, source inputs, exact outputs, and checksums.
