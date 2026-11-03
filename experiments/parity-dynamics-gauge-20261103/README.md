# Parity dynamics closure and gauge-quotient test v0.1

**Discovery only — EXACT/CONDITIONAL, canonical source OPEN, physical promotion 0.** Based on main revision `2207611450df9106adccaf8189a50734fef5a46b`, BOOTLOADER v1.1, UD_DISCOVERY v1.2, UD_MATHEMATICAL_METHOD v1.0 and adjacent `experiments/pachner-boundary-observability/README.md` (2026-11-03). No canonical total raw K4 update/admissibility law was identified in reviewed source locations; nothing below is asserted as canonical dynamics.

Let `S=F2^4 ⊕ F2^6` with four vertex bits b and six unoriented edge bits e, and `P:S→F2^3` the XOR of opposite edge pairs (01,23), (02,13), (03,12). Each fiber has size `2^7=128` since P has rank 3. The S4 group simultaneously permutes vertex and edge labels, and permutes the three pair labels; it does not fix each fiber pointwise. Exhaustive permutation orbits: `90`; histogram orbit-size:orbits `1:4,3:4,4:12,6:12,12:42,24:16`.

**Lumpability theorem (EXACT).** A deterministic induced `t` on P(A) exists for a specified `T:A→A` precisely iff `P(s)=P(s') ⇒ P(Ts)=P(Ts')` for all s,s' in A. This is an elementary well-definedness equivalence.

**Illustrative countermodel (ASSUMED).** Define `T(b,e)=(b,e+δb)`, `(δb)_ij=b_i+b_j` over F2. It is S4-equivariant and involutive. Let `q(b)=Σb_i mod2`. The disjoint opposite-edge parity obeys `P(Ts)=P(s)+q(b)(1,1,1)`. States `(b=0000,e=000000)` and `(b=0001,e=000000)` both have P=000 but successors P=000 and 111. Thus P is not closed for this assumed T on all S. The refined `(P,q)` has 16 states and exact update `(P,q)→(P+q111,q)`; all 16 projected fibers contain 64 raw states.

**Distinct equivalences.** Binary shifts h with P(h)=0 number `128`; those that preserve the entire projected time history additionally require q(h)=0 and number `64`; the P-preserving shifts commuting with T require δ(h_vertex)=0 and number `16`. Neither all of ker P nor the 64 history-invisible shifts can automatically be called a physical gauge group. Action, transport, admissibility and complete readouts must be source-checked. A raw edge-bit-count readout is not invariant under every P-kernel shift. The `24*8=192` tagged count is not a quotient of the 1024 raw states.

**Verification:** Python integer exhaustive audit, 1024 raw states × 24 relabelings, PASS. Run source code in `audit.py`; expected receipt in `results.json`. No fitted parameters or physical readout. Constructor verification only; external independent review NOT_RUN.

**OPEN gate:** retrieve UD-native raw-state `Adm` and total evolution `T` from source, including updates to burden/framing/transport; retest projected closure over `Adm`; define genuine gauge transformations by preservation of admitted action and all declared observables. Do not promote toy-model counterexample to canonical obstruction.
