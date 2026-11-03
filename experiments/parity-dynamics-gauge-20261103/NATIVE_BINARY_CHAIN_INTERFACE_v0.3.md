# Native binary-to-chain interface audit v0.3

**2026-11-03 | UD-Physics Discovery | EXACT / CONDITIONAL / NO-GO / OPEN | physical promotion 0.**

## Scope and sourced generators

Verified integration base `2207611450df9106adccaf8189a50734fef5a46b`; working task `parity-dynamics-gauge-20261103`; active claim `d0950c1c5376a31b483908c819123914ae59c404`. Source: `experiments/qpb1-local-generators/README.md` (v1.0 §§1–3), `experiments/qpb1-native-events/EVENT_CONTRACT.md` and `experiments/qpb1-loop-history/HISTORY_CONTRACT.md`. Prior conditional F2 model in this task remains **distinct**.

Question: is there a source-justified, nontrivial binary-register-to-real-chain map that intertwines the actual QPB1 flow with an admissible finite-register update? No complete binary update or quantizer has been sourced; the following gives rigorous obstructions and a candidate sampled alternative, **not** a canonical interface.

1. Binary carrier `B = F2^4 ⊕ F2^6`, 1024 raw assignments, assumed for this comparative test. Binary opposite-edge parity `P:B→F2^3` is the XOR of three disjoint opposite edge pairs.
2. Real chain carrier `C=⊕_{k=0}^3 C_k(Δ³;R)≅R^15`, ordered oriented simplex basis of sizes (4,6,4,1). Signed incidence `D`, `A=D−Dᵀ`. Unit metric `H=I` and dimensionless continuous time `u`; `Φ_u=exp(uA)`.
3. Edge readout `E:C→R^6`; no physical clock, spacetime metric, energy unit, charge observable or unearned physical identification.

## Theorem 1: additive coefficient-domain obstruction (EXACT / NO-GO)

Every additive group homomorphism `f:B→C` is zero because `2b=0` implies `2f(b)=0`, and additive `C` is torsion-free. Conversely every additive `g:C→F2^3` is zero because every `x∈C` equals `2(x/2)`, so `g(x)=2g(x/2)=0`. The same argument applies to `R^6` edge amplitudes.

Consequently no **nonzero additive** interface in either direction can be silently imported. Nonlinear and quantization interfaces are not excluded.

## Theorem 2: continuous full-time finite-image obstruction (EXACT / NO-GO)

Suppose `ι:B_adm→C` is any embedding of a finite admitted register alphabet with `Φ_u(ι(B_adm))⊂ι(B_adm)` for **all real u≥0**. For any `b`, the map `u↦Φ_u(ι(b))` is continuous into a finite subset of Euclidean space and therefore constant. Thus `Aι(b)=0` for every admitted b. Every such embedded state is fixed. Since `dim ker A=1` for the QPB1 filled-simplex model, an all-time invariant finite image can carry no nontrivial QPB1 flow. This theorem is scoped to continuous exact flow and a finite set embedded as points; it does not exclude discrete sampling or a nonfinite/continuous fiber interface.

## Constructive sampled test (EXACT / CONDITIONAL)

Use the explicitly **assumed encoding** `ι_0(b,e)=(b,e,0_face,0_cell)`, mapping each of the 1024 bit assignments to the corresponding 0/1 coordinates in the 15D real chain. This is not a group homomorphism over F2 and is not source-selected. By `A³=-4A`, the exact half-period map for `u=π/2` is

`M_{1/2}=exp(πA/2)=I+A²/2`,

an orthogonal involution. Exhaustive exact arithmetic over 1024 embedded binary states gives **exactly eight** states that return to this alphabet after one half-period, with integer bit patterns `{0,3,5,6,9,10,12,15}` (vertex bits occupy low four bits). Of these, `0` and `15` are stationary; the six weight-two vertex subsets are paired by complementation. Every surviving state has all six edge bits zero, hence **all eight have opposite-edge parity 000**. The particular eight-state alphabet is therefore **not UD's 8-state opposite-edge θ-fiber** and does not solve the demanded interface.

Explicit nonclosure witness: the vertex-0 basis vector is sent to `(-1/2,1/2,1/2,1/2;0^11)`, outside the binary embedded alphabet. The test imposes one hand-chosen sample step, not a physical clock or a parameter-free dynamic selector. It demonstrates a possible finite sampled subalphabet, but a degenerate parity readout.

Reproduce: `python3 experiments/parity-dynamics-gauge-20261103/interface_audit_v03.py`. Exact local constructor output: 1024 tested, 8 survivors, 2 stationary, `dim ker A=1`, algebraic orthogonality and involution verified. A separate four-test local unit suite (using an independently constructed incidence matrix) PASS; full GitHub repository tests are tracked separately. No physical target was consulted.

## Gauge invariance and original workload dispositions

An invisible edge-history subspace `H=ker O_E` of dimension 3 is established in `SOURCE_NATIVE_CHAIN_CLOSURE_v0.2.md`. It is **not** necessarily gauge: full norm/energy differentiates states with the same edge history. An attempted gauge quotient must declare action, admissibility, preparations, full readout and transport and prove preservation; a projection kernel is insufficient.

- **Workload 1:** native 12-real-dimensional QPB1 quadrature closure established; a complete finite-register `Adm,T` and commutative binary-to-chain diagram remain OPEN.
- **Workload 2:** exact closure reread and four constructor unit checks PASS; an independent non-constructor mathematical review is still NOT_RUN. GitHub CI had a failed earlier run due to invalid task status and missing candidate baseline; both metadata defects were repaired in this branch and require new CI confirmation.

**Next discriminant:** select and source (not fit to a target) a finite-register admission and transition rule or an explicit nonlinear/quantized encoding `ι`; specify observation timing, units and invariant set, prove `Φ_τ∘ι=ι∘ T_B` and transport/action invariance on the admitted domain. If impossible under declared assumptions, preserve the scoped no-go and change the branch assumptions explicitly.
