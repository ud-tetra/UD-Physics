# Packet-to-material reciprocity and time-reversal gate

**EXACT native parity and reciprocal-energy algebra / CONDITIONAL new even coupling / physical calibration OPEN.** This follows the [native support-current port](../graphite-native-support-current/README.md), [directional packet](../graphite-directional-packet/README.md), and [force contract](../graphite-packet-force-contract/README.md). The known graphite angle pair and weak load response were exposed; neither selects a coefficient here.

## Why the literal edge-current weight is not an equilibrium Hessian

For the fixed-mask full-chain carrier, `q=(x,y,z)`, `qdot=A_H q` in dimensionless native `s`, `A_H^T=-A_H`, and the involution `R_n=diag(I_0,-I_1,I_2)` obeys `R_n A_H R_n=-A_H`. A packet prepared with `y(0)=z(0)=0` has `y(-s)=-y(s)`. The earlier formal port `S(y)=M^T diag(y) B1^T` is consequently odd under this **native** reversal. Its signed current projection `2S(y)x` is also odd and has zero Cesàro mean in the fixed, finite closed model.

Suppose physical lateral and height *displacements* are even under the same reversal, the interface is in zero-drive equilibrium, and its conservative energy is time-reversal invariant. Then a proposed stationary energy term `u^T T^T S(y) R_h h` is odd in `y` and is forbidden unless its coefficient vanishes or a separate reversal-odd external bias is specified. The result is conditional on identifying `R_n` with the interface's physical time reversal. It does not rule out a driven, magnetic, chiral, or explicitly biased material law; it rules out silently treating the transient signed edge amplitude as an equilibrium elastic coefficient under the stated symmetry. A constant `C_add` is also not derived by multiplying the native current by a dimensional factor.

## A minimal even completion, declared as a new hypothesis

Let `u∈R²` be physical lateral displacement and `h∈R^m` labeled vertical or mode displacement, both in Å. `T:R²_cart→R²_direct` and `R_h:R^m→R^(2N)_site` are independently registered dimensionless maps. Define the **candidate**, not a Q24/Q166 consequence,

`C_a(q)=λ T^T S(w(y)) R_h`, `w_e(y)=y_e²`, `S(w)=M^T diag(w) B1^T`,

where `λ` has units meV Å^-2 per upper atom. `w` is even under `R_n`, nonnegative, and preserves the carrier's bond labels. Other even functions are possible, so squaring is a model choice, not a unique UD selection. In particular `w=y²` is an amplitude-square register, not the native signed current or a measured edge stiffness.

One reciprocal local energy realizing the term is

`E=E0 ||q||²/2 + u^T K0 u/2 + u^T C0 h + h^T K h/2 + λ (T u)^T S(y²) R_h h`,

with native energy scale `E0>0` in meV per upper atom, `K>0`, and a separately specified bath `D⪰0`. Put `a_e=(M T u)_e (B1^T R_h h)_e`. The packet gradient is

`∂E/∂y_e=E0 y_e+2λ y_e a_e`.

The **reciprocal** packet equation must then be `dq/dt=(E0 τ)^-1 A_H ∇_q E` for a physical clock `τ>0`; it reduces to the previous `dq/ds=A_H q` only when the interface term is absent or has no gradient. The material equation is `M_h hddot+D hdot+∂_h E=0` and the applied lateral reaction is `F=-∂_u E`. With `u(t)` externally driven, fixed mask, and no other sources,

`d/dt [E+hdot^T M_h hdot/2] = -F·udot - hdot^T D hdot`.

The identity follows from skewness of `A_H` and is valid for this stated local model; a fixed energy coupling that changes `F` while leaving the packet equation unmodified would omit its backreaction. The polynomial energy is intended near the reference configuration and is not asserted globally bounded or stable for arbitrarily large `u,h,q`. For `D=0` it supplies no irreversible bath loss. Its graphite value still requires `T,R_h,E0,τ,λ,K,D`, site registration and a stable operating state from independent sources.

There is an additional equilibrium obstruction. At `u=h=0`, the unconstrained zero-temperature minimum of the chosen native quadratic energy is `q=0`, hence `C_a=0`. For the **isotropic canonical ensemble** of that same quadratic energy at temperature `T_b`, every edge has `⟨y_e²⟩=k_B T_b/E0`. Consequently `⟨S(y²)⟩=(k_B T_b/E0) M^T B1^T=0`, because `B1 M=0`. This holds for every listed quotient and any fixed contact mask in the stated equilibrium ensemble. A nonzero stationary *mean cross-Hessian* needs a separately sourced anisotropic edge covariance, boundary preparation or altered energy measure. The identity does not say the mean of the nonlinear damping tensor vanishes: `⟨C_a L C_a^T⟩` may remain positive and requires a dynamic bath calculation.

## Small-time carrier result and its limit

For the prior boundary preparation `x(0)=e_A0+ε Σ_t d_t e_B(-s_t)`, `y(0)=z(0)=0`, with `d₁=(2,-1,-1)`, `d₂=(0,1,-1)`, the uncoupled initial response is `y(s)=s B1^T x(0)+O(s³)`. Under the *illustrative* identity site preparation `R_h h=x(0)`, identity direct frame, and the normalized native report `Q_N(s)=2 sqrt(N) M^T diag(y(s)²) B1^T x(s)`, its coefficient linear in the two `ε` directions begins

`Q_N(s)|linear = s² [[18,-6],[18,18]] a + O(s⁴)`, for `N=7,13,19`.

The [exact replay](verify_reciprocity.py) computes this matrix from the integer edge incidence and verifies the energy/power identity on a rational witness. This even readout can have a nonzero time average despite the signed current's zero mean. It does **not** identify `C_a` from graphite, predict kinetic friction, or select the N=7 angles: its leading matrix is common to all three quotients, the site preparation is supplied, and its amplitudes are free. Moreover, when `C_a(t)` varies, one cannot generally replace the bath response by a static `Γ=C_a K^-1 D K^-1 C_a^T`; its memory, modulation frequency and packet backreaction must be solved. Even in an adiabatic approximation `⟨C_a L C_a^T⟩` need not equal `⟨C_a⟩L⟨C_a⟩^T`.

The prior [four-site pure-source constraints](../graphite-source-constraints/README.md) concern a C3-equivariant stationary seven-cell map. A directionally prepared `y²` need not be C3 invariant, so applying those two relations to this transient map without checking its registration and symmetry would be invalid. For a stationary candidate, first independently specify how an even packet weight survives and is registered, then calculate its full `2×14` cross-Hessian against a separately calibrated conventional baseline. Independently measure complex mode response at pressure offsets and freeze all maps before a signed held-out angle/speed/load test. No independent physics review; physical promotion 0. See the [mathematical receipt](../../candidates/graphite-packet-reciprocity/mathematical_receipt.json) and [immutable capture](../../artifacts/graphrecip-20261024-01/exact-002/manifest.json).
