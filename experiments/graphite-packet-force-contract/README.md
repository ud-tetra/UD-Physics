# Closed packet current and a reciprocal graphite force contract

**EXACT within the declared finite carrier and linear material model / CONDITIONAL physical interface; measured friction OPEN.** This note follows the [directional packet](../graphite-directional-packet/README.md) and its [identifiability audit](../graphite-packet-identifiability/README.md). The observed complementary angles and weak load trend were known before this calculation. No force trace or material coefficient is fitted.

## Finite carrier: a transient current has zero steady mean

For any of the previously fixed N=7,13,19 full 0/1/2 honeycomb quotients, let `q=(x,y,z)` and hold a real diagonal contact mask `H` fixed. In the unit chain metric and dimensionless native time `s`, use the already declared generator

```
A_H = [[0, -B1 H, 0], [H B1^T, 0, -B2], [0, B2^T, 0]],
q'(s)=A_H q(s),     q(0)=(x0,0,0).
```

Here `x0` can be the symmetric seed or the previously supplied directional B-neighbor packet. `A_H^T=-A_H`, so `||q||²` is conserved. Let `R=diag(I_0,-I_1,I_2)`. The exact identity `R A_H R=-A_H` and `R q(0)=q(0)` imply `x(-s)=x(s)`, `z(-s)=z(s)`, and `y(-s)=-y(s)`. Therefore the previously defined signed edge stock current `J_e(s)=2h_e y_e(s)(B1^T x(s))_e` and its fixed linear harmonic projection `P_N(s)=sqrt(N) M^T J(s)` are **odd** in native time. This includes a permanently supplied one-edge gate; it does not require C3 symmetry.

A finite real skew matrix is orthogonally diagonalizable into rotation blocks and zero blocks. Each component of `q(s)` is a finite trigonometric sum; hence `P_N(s)` is a bounded finite trigonometric sum. Oddness eliminates its zero-frequency term, so its Cesàro mean is exactly zero:

`lim_(T→∞) (1/T) ∫_0^T P_N(s) ds = 0`.

The statement is about the **signed native stock-flow projection**, not the mean of its magnitude or a measured drag. It requires a fixed mask, closed finite generator, and initial zero edge amplitude. It also applies in physical time only if `s=t/τ` with a constant positive `τ` for the averaging interval. Time-dependent driving, switching, resetting, an infinite bath, a nonlinear clock, or a force estimator other than this projection requires separate analysis. In particular, an arbitrary multiplication of a transient native `P_N` by a force scale is not a reciprocal energy coupling.

## Minimal reciprocal material completion

For a local stable graphite registry, let lateral displacement `u∈R²` and material height/mode coordinates `h∈R^m` be in Å. Assign energy in meV per upper atom and Rayleigh loss

`E(u,h)=1/2 u^T K0 u +u^T C h+1/2 h^T K h`, `R_diss=1/2 hdot^T D hdot`,

with `K=K^T>0`, `D=D^T⪰0`, `C` a `2×m` **force-versus-height cross-Hessian**, and `K0=K0^T`. The terms `K,K0,C` have units meV Å^-2 per upper atom, `D` has meV ps Å^-2, and mass `M` in meV ps² Å^-2. With `M hddot+D hdot+K h=-C^T u` and reciprocal lateral force `F=-K0 u-C h`, a low-frequency expansion after stable transients gives

`F=-(K0-C K^-1 C^T)u-Γ v+O(ω² u)`, `Γ=C K^-1 D K^-1 C^T`, `v=udot`.

Thus `v^T Γ v=||D^(1/2) K^-1 C^T v||²≥0` and `Γ=0` when `D=0`. The finite native `J` supplies neither `C` nor `D`; a map from packet, registry, load and physical clock to these dimensional objects is an **additional constitutive hypothesis**. The archived [linewidth transfer](../graphite-linewidth-transfer/README.md) calibrates this formula for a conventional KC-plus-plate `C,K` under conditional measured mode widths; those numbers must not be relabeled a UD contribution.

If a separately fixed UD cross-Hessian `C_a` adds to a conventional `C_0` while `K,D` are held common, let `L=K^-1 D K^-1`. The **signed residual damping tensor** is

`ΔΓ=(C_0+C_a)L(C_0+C_a)^T-C_0 L C_0^T`

`   =C_a L C_a^T+C_0 L C_a^T+C_a L C_0^T`.

It need not be positive even though each total `Γ` is positive semidefinite. For the scalar example `L=C_0=1`, `C_a=-1/2`, one has `Γ_total=1/4`, `Γ_0=1`, and `ΔΓ=-3/4`. This interference is why an added source cannot be inferred by taking a square root of a nonnegative friction difference. The formula assumes an unchanged bath; if the UD hypothesis changes `K` or `D`, subtract separately evaluated complete models instead.

For differentiable load `p`, `B=K^-1`, `L=B D B`, the full local derivative is

`L'=-B K' L-L K' B+B D' B`,

`Γ'=C' L C^T+C L C'^T+C L' C^T`.

Zero or weak load slope therefore does not follow from native quotient geometry: the cross-Hessian, stiffness and dissipative loss slopes all enter. For a signed sliding force residual at speed `v`, subtract the independently calibrated full conventional `F_0(v,p)` from measured `F(v,p)` before fitting any added `C_a` and bath. Freeze the packet-to-`C_a` map, clock, mode response, contact preparation, and uncertainty model on disjoint calibration data, then forecast held-out signed forces across the paired angles, nearby commensurate controls, direction, speed and load.

The [exact verifier](verify_contract.py) checks generator skewness, grading anticommutation and current parity on N=7,13,19 for the open and a fixed one-edge mask, and rational matrix identities for `Γ`, its load derivative and the signed-residual counterexample. Its [receipt](../../candidates/graphite-packet-force-contract/mathematical_receipt.json) and [capture](../../artifacts/graphforce-20261024-01/exact-001/manifest.json) specify the assumptions. No graphite force data or independent physics review were obtained; physical promotion 0.
