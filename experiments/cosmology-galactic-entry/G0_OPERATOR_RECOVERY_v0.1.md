# G0 operator recovery and metric selection addendum v0.1

Session `cosmology-g0-operator-recovery-20261106-01`; source decision **SOURCE_BLOCKED** for an autonomous disk-galaxy force law. Physical promotion 0. This extends [G0 source audit v0.1](G0_SOURCE_AUDIT_v0.1.md) without replacing its bounded finding.

## Additional source recovery (2026-11-06)

| Versioned source | Exact location and finding | Disposition |
| --- | --- | --- |
| Library `UD_K4_ACTION_METRIC_SELECTION_AUDIT_v2.1.zip`, SHA-256 `37077981370f88ee62f0e24234c782ebb63d24ea57b03560b10fe36f0f79ef46`, `ACTION_METRIC_SOURCE_AUDIT_v2.1.md` §§1–5 | Source audit of Q165/Q169, action O09–O15, K4 1→4 contact; exact continuum of positive `H_t` compatible with integral map, chain and generator; no source selection of newborn metric/contact | Mathematical nonuniqueness; no galactic gravitational metric |
| Library `UD_K4_CROSS_COMPLEX_CONTACT_METRIC_v2.0.zip`, SHA-256 `a8bf4b76dd692cb73534e67bc5d434050e4f9cdfb89e5a376d9296bd0ec238d4`, `PROOF_v20.md` Theorems A–C | Original unit-metric subdivision has second-jet mismatch; coherent and changed-metric completions are constructed with changed assumptions | Conditional contact constructions, not selected force law |
| `ud-tetra/UD-Physics@4145ce012c3d8a91ea9e8dd53f5b923455b0e1c2`, `experiments/action-normalization-audit/sources/IDENTIFIABILITY_THEOREM.md` v0.1 | `A0=B0 a0²/τ0` is identifiable from independent monomial anchors iff exponent row `w_A=(1,2,-1)` is in their row span; physical action anchor remains open | Dimensional action bridge does not supply mass-to-force or gravitational coupling |
| Uploaded `master_action.md` and `packet_field_equation.md`, SHA-256 `88cefa4f89a3cec06e39eb2e5d12ac87ff1d18eff0875dea1ac04fca18cce1ea` and `b71fa5cf7c5ad3d70af25ce18494e67485f7fd9c6f742708c86d6316fdf285b1` | Reconstruction placeholders, not executable field/action equations | No operator recoverable from these files |
| Uploaded `DistinctionDynamics_Full_Repository_v1.zip`, SHA-256 `e4bffc290d854eadcbd524741250544031837b34d67f90e1e737f3fcb22b04f4`, `05_cosmology/effective_friedmann_equation.md` | Reconstruction placeholder; no galactic source law | Historical title supplies no equation |

The memory-level weak-field proposal `∇²Φ_DD=χ_DD (1/a)G_edge B` is treated as **CANDIDATE** only: no accepted versioned source in the above files defines all symbols, domains, units, boundary data, test-body coupling and selection of `χ_DD`. The symbol `Poisson` in ledger Q119 denotes a unit-normalized jump-count process, not this gravitational PDE. No equation is promoted by conflating them.

## Exact mathematical obstruction inherited from v2.1

Let `C0=R^15`, `C1=R^29`, with signed differentials `D0,D1`, integral degree-one chain map `F:C0→C1`, and a **constructed** rational retraction `P:C1→C0` obeying `PF=I` and `PD1=D0P`. Put `Q=I−FP`. For every real `t>0`, define `H_t=PᵀP+tQᵀQ` on `C1`.

**EXACT conditional algebra:** `x=F(Px)+Qx`, with `Px=0` and `Qx=0` only when `x=0`; hence `xᵀH_t x=||Px||²+t||Qx||²>0`. Also `QF=0` implies `FᵀH_tF=I`. The decomposition `im F ⊕ ker P` is `D1` invariant, and in that decomposition `H_t=diag(I,tI)`; therefore the metric adjoint of `D1` and `A_t=D1−H_t⁻¹D1ᵀH_t` are independent of `t`. The old and new carrier metrics remain typed separately. This reproduces the source's direct-sum proof, without independently rerunning its full 29×29 matrix tests.

**NO-GO under the stated selector list:** isometry, boundary commutation, generator intertwining, positive metric and S4 covariance do not select `t`, since all positive `t` satisfy them. The v2.1 full-matrix replay and ten local tests are reported in that archive; this addendum verifies only the symbolic implication. In particular one cannot identify a unique physical metric or radial gradient from these conditions alone. This is a source-selection obstruction for the 1→4 interface, not a universal theorem against every new constitutive law or against a galactic metric built on a different carrier.

## Minimal operator receipt still required

1. **State/source:** define assembled carrier `K`, conserved matter stock `b∈S_K`, mass map `M:S_K→kg` or justified native analogue, source coupling `J:S_K→F_K`, and evolution/field equation `L_K φ=J(b)` with boundary conditions and kernel/gauge handling.
2. **Metric/readout:** select one positive metric and radial geometry from source law, identify signed physical force `g_R` as a declared gradient or transport-cost variation, and specify a test-body coupling and circular equilibrium rule. Contact `H_t` alone is not a spatial or Lorentzian gravitational metric.
3. **Units/identification:** specify independent anchors for `ℓ_*`, `τ_*`, matter scale and coupling, with uncertainty and target independence. Check dimensional rank/degeneracy before comparing any held-out galaxies.
4. **Verification:** derive central and large-radius limits, source scaling, conservation and null family; freeze predictor and nuisance ranges before exposed target rows.

**Decision:** No source-selected dimensional radial profile was derived. No SPARC rows were read or fitted. Reopen when an explicit, versioned constitutive rule and complete operator receipt exist; the historical weak-field wording is a hypothesis to formalize, not a fitted shortcut.
