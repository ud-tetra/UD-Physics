# G0 weak-field burden candidate v0.1

Session `cosmology-g0-weakfield-candidate-20261106-01`. **CANDIDATE / EXACT conditional mathematics / NO-GO scoped.** Physical promotion 0. No galaxy data or fitted constants.

## Source boundary

The memory-level phrase `∇²Φ_DD=χ_DD (1/a) G_edge B` is a historical weak-field proposal, not a recovered accepted constitutive equation. The uploaded `Unified Dynamics (Distinction Theory) v2.2 — Master Manuscript.pdf` (SHA-256 `01ac4d1daceed22cfac52233de05f7e16a49626d2d1e1ada1b57003f2f29f3ef`, Part V) proposes a *different* curvature-defect Hamiltonian with `κ=1/(9π²)`; it does not define the displayed source/force operator. Uploaded `master_action.md` and `packet_field_equation.md` are reconstruction placeholders. See [G0 audit](G0_SOURCE_AUDIT_v0.1.md) and [operator recovery](G0_OPERATOR_RECOVERY_v0.1.md) for provenance and metric nonselection. Q119's Poisson jump clock is a distinct object from a gravitational Poisson equation.

## Explicit changed-assumption candidate

Let `K=(V,E)` be a finite connected oriented graph, with vertex potential space `C⁰(K;R)` and edge difference space `C¹(K;R)`. Let `D:C¹→C⁰` be oriented incidence, `W=diag(w_e)` with `w_e>0` an **assumed** edge conductance/metric choice, `B∈S_K` a **proposed** burden stock, and `J:S_K→C⁰` an **assumed** linear source map. Neither `W` nor `J` is selected by the current UD gravity sources. Take symbolic coupling `χ` and define

`L_W=D W Dᵀ : C⁰→C⁰`, `L_W φ=χ J(B)`.

`L_W` is positive semidefinite, `ker L_W=span{1}` for connected `K`, and its range is the zero-sum vertex subspace. Thus a closed carrier admits a solution iff `1ᵀJ(B)=0` (or `χ=0`); a positive isolated source requires a compensating source, boundary flux, or a changed carrier. Solutions differ by an additive constant; edge differences `Dᵀφ` are unique only after `W,J,χ` and boundary/neutralization choices are fixed. The candidate sign convention for attractive response would require a separate test-body rule `a=−γ grad_g φ`, with `γ>0` and geometry `g`; `grad_g`, `γ`, physical mass coupling, and circular equilibrium are **OPEN**, not consequences of `L_W`.

For a Dirichlet boundary `V_boundary` with fixed `φ`, the interior principal Laplacian is positive definite if every connected component touches the boundary. Its inverse supplies a *conditional* potential. `R=ℓ_* r`, `t=τ_* s`, physical stock and `χ` remain independent calibrations; the graph's edge count is not a length or physical clock.

## Exact two-edge counterexample and selection test

Take path `0—1—2`, vertex 2 Dirichlet at `φ₂=0`, `J(B)=(1,0)` on interior vertices, and `χ=1` as **illustrative native normalization**. Incidence signs are arbitrary because `D W Dᵀ` is orientation invariant. Exact interior solution gives flux `w₀₁(φ₀−φ₁)=1`, `w₁₂(φ₁−φ₂)=1`, hence `φ₁=1/w₁₂`, `φ₀=1/w₀₁+1/w₁₂`.

| Assumed weights `(w₀₁,w₁₂)` | `(φ₀,φ₁,φ₂)` | Edge differences `(φ₀−φ₁,φ₁−φ₂)` |
| --- | --- | --- |
| `(1,1)` | `(2,1,0)` | `(1,1)` |
| `(2,2)` | `(1,1/2,0)` | `(1/2,1/2)` |
| `(1,2)` | `(3/2,1/2,0)` | `(1,1/2)` |

All satisfy the same specified source and boundary and yield different potential gradients. They are **mathematical controls**, not galaxy models. The source can be unchanged even when the metric changes; no amplitude, radial shape or force is selected by topology and incidence alone. Independently, scaling `χ↦cχ` scales potential differences by `c`; unless `J`, `χ`, `γ`, `ℓ_*`, and `τ_*` have independent source rules, only their composites can be inferred from an observed acceleration. This is an identifiability obstruction, not a universal physical no-go.

## Admission and falsification gate

Before using a galaxy target, provide a versioned constitutive derivation of `W`, `J`, `χ`, and the physical force/metric readout, plus boundary conditions on an assembled disk-galaxy carrier. Prove the source-neutralization or boundary flux mechanism and demonstrate a source-defined circular equilibrium rule. Record dimensions and independent calibration for burden-to-mass, radius, time and force; check central regularity, asymptotic scaling, conservation, and equivalence under graph refinement. Then freeze a target-blind prediction and compare with baryons-only, conventional dark-matter and empirical baselines under matched nuisance freedoms.

**Disposition:** retain the finite-graph Poisson equation as a transparent **CANDIDATE** and its solvability/selection counterexample as **EXACT under stated assumptions**. **NO-GO under the admitted source set** for an independently derived dimensional galactic force profile. Physical promotion 0.

Verification: exact rational replay `weakfield_exact.py`; source-bound review against the G0 audits and ledger v0.39 G01/G03/G05, Q119/Q165/Q169. No test against physical measurements.
