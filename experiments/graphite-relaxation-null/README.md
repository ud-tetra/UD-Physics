# A passive first-harmonic control for graphite drag

**Status: EXACT / CONDITIONAL conventional null; source-rounded numerical ratio; UD-specific residual OPEN.** The [registry/source cross-spectrum](../graphite-registry-convolution/README.md) is a static selection condition. A nonzero harmonic port does not itself dissipate energy. This calculation gives the smallest passive dynamical control that can generate a nonzero velocity-odd mean force from an ordinary periodic graphite potential. It is deliberately **not** called a UD mechanism.

## Physical input and declared assumptions

Lebedeva *et al.*, [arXiv:2511.01338v1](https://arxiv.org/html/2511.01338v1), Eq. (2) and Sections 3.2/3.4, find that the rigid and relaxed `(2,1)` and `(3,1)` PESs are closely described by first spatial Fourier harmonics. Their Table 6 reports **DFT-derived ideal rigid static shear strengths** of `1.39×10⁴` and `6.68×10³ Pa`, respectively. These are not the kinetic force measurements of Chen *et al.*, [PRL 137, 166201 (2026)](https://doi.org/10.1103/ly48-b4l2), whose public abstract reports detectable paired peaks and negligible load dependence. The PRL force tables, force threshold, and supplement were not available in this source check.

For a **one-dimensional cut**, set `x=vt` and let the energy **per upper atom** be

`E_N(x,q;P)=U_(0,N)(x;P)+(κ_N(P)/2)q²−λ_N(P) A_N(P) q cos(k_N x)`.

Here `q` is a dimensionless internal coordinate, `A_N` and `κ_N` have energy per atom units, `k_N` is inverse length, `λ_N` is dimensionless, and `P` is normal pressure. Assume a passive Rayleigh coefficient `η_N≥0` with units energy·time per atom and first-order evolution `η_N q̇=−∂_q E_N`. Thus `τ_N=η_N/κ_N` has time units if `κ_N>0`. The coupling, mode and relaxation law are explicit **assumptions**; they have not been identified from UD or measured graphite modes. `U_0` is periodic and its derivative averages to zero over a complete steady sliding period. If `A_N` is calibrated from rigid DFT, internal relaxation must not be silently counted again in a relaxed DFT PES.

## Exact steady response and energy balance

For constant `v`, put `ω_N=k_N v` and `z_N=ω_N τ_N`. After transients,

`q_N(t)=(λ_N A_N/κ_N)[cos(ω_N t)+z_N sin(ω_N t)]/(1+z_N²)`.

With `F_x=−∂_x E_N` at fixed `q`, the mean over a period is

`⟨F_x⟩_N=−[λ_N² A_N² k_N² τ_N/(2κ_N)] v/[1+(k_N v τ_N)²]`.

The mean dissipated power is `⟨η_N q̇²⟩=−v⟨F_x⟩_N≥0`; the conservative periodic force has zero cycle mean. Therefore the low-speed drag coefficient is

`γ_N^0 := lim_(v→0) (−⟨F_x⟩_N/v) = λ_N² η_N (A_N k_N)²/(2κ_N²)`.

All signs and factors of two follow from harmonic balance and period averaging. This is a per-atom **viscous coefficient**, with units energy·time/length² per atom. Multiplying by the participating number of atoms and specifying contact motion/transfer would be necessary before comparing a measured force. If `η_N=0` at fixed `κ_N`, this particular open-mode drag vanishes. A conservative static energy profile by itself has no cycle-averaged force for prescribed steady translation.

There is also a useful *self-sourced* cancellation: on a periodic PES, `∫U″(x)U′(x)dx = [U′(x)²]/2` at the boundaries and hence zero. In two dimensions, `Σ_j(∂_i∂_j U)(∂_j U)=∂_i(|∇U|²/2)`, whose cell average is zero. A first harmonic sampled at `N=7,13,19` equally spaced phases has this cancellation exactly. Thus matching Fourier sectors is necessary for a static product to survive, but is not sufficient: conservative quadrature phase can cancel it. This scalar Hessian/gradient identity is an analogy for possible material sourcing, not a proof that the separately defined UD incidence port has these derivatives.

## Conditional angle contrast and load response

Let `G_N=A_N k_N` be the peak force amplitude per atom along this scalar sinusoidal path. If the same `λ,η,κ`, participating area-per-atom conversion and low-speed regime apply at both angles, **and** `G_N` is proportional to the published rigid ideal shear strength using a common proportionality, then

`γ_7^0/γ_13^0=(13900/6680)²=483025/111556≈4.329888`.

This is a calculation from **source-rounded theoretical static strengths under extra transfer assumptions**, not an observed kinetic-friction ratio, a UD prediction, or a bound. The authors' PES is two-dimensional, while this surrogate is one-dimensional; orientation, saddle path, relaxation and contact can change the transfer. The published Table 2 corrugation ratio `0.347/0.027≈12.85` must **not** be squared to replace this force-gradient ratio because the spatial periods and PES topology differ. At finite `v`, the drag ratio additionally contains `[1+(k_13 vτ_13)²]/[1+(k_7 vτ_7)²]` and shared-bath assumptions alone do not remove it.

For differentiable nonzero factors and `G_N=A_Nk_N`, the exact low-speed logarithmic pressure slope is

`∂_P ln γ_N^0 = 2∂_P ln|λ_N| + ∂_P ln η_N + 2∂_P ln|G_N| − 2∂_P ln κ_N`.

At fixed `v`, subtract `2z_N²/(1+z_N²)·∂_P ln|k_Nτ_N|` for the finite-speed force magnitude. A nearly zero measured load slope therefore constrains a **combination** of PES response, coupling, stiffness and damping derivatives. None of those derivatives is supplied by the public PRL abstract. It cannot be inferred from small rigid static friction alone. This simple passive model can in principle put the seven-cell response above a shared detection threshold while the thirteen-cell response is below it; that does not attribute a residual to UD.

## Reproducible checks and gate for the paper

Run `python3 experiments/graphite-relaxation-null/replay_relaxation.py`. Exact `Fraction` harmonic balance at `z=0,1/2,1,2` verifies the ODE and `−v⟨F⟩=⟨ηq̇²⟩`. The source-rounded shear ratio is squared exactly. The [immutable capture](../../artifacts/graphrelax-20261024-bb53/exact-001/manifest.json) and [mathematical receipt](../../candidates/graphite-relaxation-null/mathematical_receipt.json) retain inputs, assumptions and verification.

Before calling any leftover signal UD-specific, use a common independently fixed two-dimensional PES, contact area/geometry, velocity history, passive loss spectrum and load derivatives at both angles; compute the same force observable as the experiment with uncertainty and detection limits. Only then test a **separately specified** UD source/loss term on held-out signed force and load data. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` Q22 leaves nonuniform edge stiffness unsourced; Q77–Q84 do not provide this graphite bath. Independent physics review NOT_RUN; physical promotion 0.
