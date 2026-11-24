# Nonlinear local incidence and active-interface weight robustness v0.1
**EXACT / CONDITIONAL / NO-GO_SCOPED. Physical Promotion = 0.**
Source: UD-Physics main `80525f1296a15f4a87f0efecc491679deec39b9b`; `experiments/four-cell-tetrahedron/README.md` v1.0 blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e`. PR #480 second-generation Gram and PR #481 two-face-glued invariant are draft research, not mainline source truth.

## Typed model
Fixed 16-top complex `f=(9,26,34,16)`, signed `B3:R^16→R^34`, unit coefficient face/top metric, top state `q`, face state `f`, formal parameter `s`. Let `G=B3ᵀB3`, `H=B3B3ᵀ`, `S=||q||²+||f||²`. The baseline `f'=B3q,q'=-B3ᵀf` conserves both S and `E_G=qᵀGq+fᵀHf`.

Assume **candidate** local nonlinear weights `g_j(q_j)=1+κ q_j²` and `W(q)=B3 diag(g_j)`, with evolution `f'=Wq,q'=-Wᵀf`. κ is an unselected dimensionless coefficient and not a physical prediction or native UD law. Sparsity, signed relabeling covariance and current-state locality are preserved.

**EXACT:** `S'=0`. Also `E_G'=2 fᵀ(HW-WG)q`, generally nonzero. An exact rational signed-incidence witness sets top amplitudes `q_0=1,q_4=2` and shared-face `f_(2,3,5)=1`, all others zero: `S=6,E_G=18,E_G'=-18κ`. This disproves preservation of the *fixed* E_G under every norm-conserving incidence-local skew law.

For the exterior-only initial condition `q=(1,1,1,1,0×12),f=0`, the exact initial derivatives are `E_G'(0)=0`, `E_G''(0)=24κ(κ+1)`; initial `S=4,E_G=16`. For κ>0 E_G initially increases. This is NOT a trajectory to the user-reported candidate endpoints `13a²→4a²`, which were not reconstructed or scored here.

**NO-GO_SCOPED:** If instead `g_j(q_j)=q_j²`, then `q_j'=-q_j²(B3ᵀ f)_j`; each `q_j=0` hyperplane is invariant for this smooth ODE, so strictly empty internal top coordinates cannot be funded by pure self-gating. Some nonzero coupling at zero amplitude, cross-state dependence or distinct initialization would be necessary.

## Interface robustness control
Two glued tetrahedra `[0123] U [0124]` give `(5,9,7,2)`, 23 chain dimensions, unit-metric skew `A=Dᵀ-D`. Let v be common face `[012]`, u=Av, P=vvᵀ+uuᵀ/5. At unit weights P is a rank-2 invariant projector. Uniform positive rescaling `B3→rB3`, keeping B1/B2 fixed, preserves chain nilpotency and full face-glued symmetry. But **EXACT** `||[A_r,P]||_F²=(24/5)(r−1)²`. For r>0,r≠1, `A_r²v` also develops six exterior-triangle components proportional to `r²−1`. Thus the **specific** active interface plane is not protected against symmetry-preserving coupling changes. This does not rule out alternative invariant subspaces of the perturbed operator.

## Governance
Both models are finite, pre-metric computational controls. No native 29→85 event admission, 13→4 endpoint connection, unit-to-Whitney metric bridge, universal recurrence or physical particle inference is derived. The original 23-entry spectral catalogue remains SOURCE_BLOCKED and nuclear/fission claims remain quarantined. Physical Promotion=0.

## Reproducibility
Exact independent-from-prior-script SymPy construction is in local artifact `UD_NONLINEAR_ACTUATION_AND_INTERFACE_ROBUSTNESS_v0.1.zip` SHA-256 `048d5c68d7fdd4fda29d4651f37515ac95efebc7052acbd0f13d15bf0981b97d`. Constructor local PASS; independent non-constructor mathematical review and a future native source test NOT_RUN.
