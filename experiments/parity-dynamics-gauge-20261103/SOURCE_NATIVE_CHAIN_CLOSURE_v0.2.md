# Source-native K4 edge-history closure and coefficient-domain obstruction v0.2

**2026-11-03 — Discovery / EXACT-CONDITIONAL / development only / physical promotion 0.**

## Sources and boundary

- Repository base `2207611450df9106adccaf8189a50734fef5a46b`.
- `experiments/qpb1-local-generators/README.md`, v1.0, §§1–3 (filled-simplex unit-metric generator and S4 classification).
- `experiments/qpb1-native-events/EVENT_CONTRACT.md`, v1.0, Native flow / Observed quadratures / Visibility.
- `experiments/qpb1-loop-history/HISTORY_CONTRACT.md`, v1.0, native orbit receipts and noninvertible adapter constraints.
- `experiments/four-cell-tetrahedron/README.md`, v1.0, full-versus-relative flow warning.
- New script `native_chain_probe.py`, exact data `native_chain_results.json`.

The **QPB1 unit-incidence law** is an actual explicit mathematical model in the repository; it is not evidence of a universal UD evolution on the separate raw binary register `F2^10`. There is no authorized bridge silently identifying these coefficient domains.

## Exact chain carrier and first closure obstruction

Let `C=⊕_{k=0}^3 C_k(Δ³;R)`, with ascending simplex orientations, coordinate dimensions (4,6,4,1), unit Euclidean inner product, and degree-lowering signed incidence `D=D1+D2+D3`. Set `A=D−Dᵀ`, and let `E:C→R⁶` extract the six edge coordinates. The model evolution is `x'(u)=A x(u)` for dimensionless continuous parameter `u`; initial state is any `x(0)∈R¹⁵`; no boundaries or physical unit map are supplied.

The edge derivative is

```
q = Ex,       q' = EAx = D2 x_face − D1ᵀ x_vertex.
```

Consequently `q` alone is not autonomous. The exact witness `x=0` and `x'=basis_vertex0` have the same `Ex=0` while their edge derivatives are respectively `0` and `(1,1,1,0,0,0)` under the declared orientation. This is a **NO-GO** for instantaneous edge-only closure under this specific generator.

## Exact sufficient two-quadrature readout

Let `J=A/2`, `p=EJx` and `q=Ex`. Direct incidence multiplication gives `A³+4A=0`, and `EA²+4E=0`. Therefore

```
q' = 2 p,             p' = (1/2)EA²x = −2q.
```

Thus `(q,p)` is a closed 12-dimensional real-valued state. The exact observability matrix

```
O_edge = [E ; EA ; EA² ; ... ; EA^14]
```

has ranks `6,12,12,12,...,12` at successive derivative orders. Since the first two blocks already have rank 12 and all later blocks lie in their span, the full edge history identifies exactly 12 real state dimensions. This is **not** the binary 16-state quotient `(theta,q_vertex)` from the prior illustrative F2 countermodel.

## Exact invisible subspace and gauge caution

Define `h0 = sum of all four oriented vertex basis vectors`, `z3 = top tetrahedron basis vector`, and `z2=D3 z3`, its oriented boundary face chain. These vectors are linearly independent. Signed boundary composition yields `D2 z2=D2D3z3=0`. Under `A`, the span `H=span(h0,z3,z2)` is invariant: `Ah0=0`, `Az3=z2`, `Az2=−4z3`. Every edge coordinate of each of these vectors vanishes at every `u`. Because `dim ker O_edge=15−12=3`, we have proved

```
ker O_edge = H,       dim H = 3.
```

This is an exact **observer-dependent hidden sector**, not necessarily gauge redundancy. The conserved unit-norm quantity `xᵀx` distinguishes `x=0` from `x=z3`, although their edge histories are both identically zero. If this norm is included among declared observables/action data, identification of those states as gauge is invalid. A candidate gauge group must preserve the chosen full action, preparation, and readout, not merely edge projection.

## Exact coefficient-domain obstruction

No nonzero additive group homomorphism `f:(R⁶,+)→(F2³,+)` exists. For any `x∈R⁶` one has `x=2(x/2)`; hence `f(x)=2 f(x/2)=0` in characteristic two. In particular the F2 opposite-edge parity map cannot be directly transferred as an additive readout of real chain coordinates. A quantizer, integer register, lattice-preserving update, or nonlinear branch/interface must be independently defined and audited for equivariance, admissibility, and dynamical closure. This is a **NO-GO** under additive-map hypotheses only; nonlinear readouts are not excluded.

## Reproduction and verdict

```bash
python3 experiments/parity-dynamics-gauge-20261103/native_chain_probe.py
```

Requires SymPy for exact integer/rational matrix rank; local execution PASS with `(rank D1,rank D2)=(3,3)`, edge-history rank 12, invisible dimension 3, and the above explicit witness. The script checks `D²=0`, `Aᵀ=−A`, `A³+4A=0`, `EA²+4E=0`, and the three independent null vectors. Constructor calculation only; independent review and repository CI are NOT_RUN.

**Disposition:** Scoped source-native theorem established for QPB1 unit metric. The complete UD finite-register `Adm`, `T`, and a typed parity-to-chain adapter remain OPEN. Neither the binary model's 128-fold fibers nor the 15-dimensional flow's 3-dimensional hidden subspace has physical interpretation without additional bridge evidence. Next discriminant: source an explicit state-encoding/quantizer and native constitutive update, then rerun lumpability with declared action/readout invariance.
