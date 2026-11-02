# Prepared harmonic-square graphite source v0.1

**Date:** 2026-11-02. **EXACT** finite-carrier algebra and ungated conservation; **CANDIDATE** material identification; graphite force and load response **OPEN**. Target exposure: the 21.8°/38.2° pair was known. No angle or force value enters the calculation. Physical promotion 0; independent physics review NOT_RUN.

## Source and typed setup

The carrier is the periodic honeycomb 0/1/2 chain complex for `(m,n)=(2,1),(3,1),(3,2)` and `N=m²+mn+n²=7,13,19`, as constructed in [graphite packet reciprocity](https://github.com/ud-tetra/UD-Physics/blob/3b9f6dee5e8c69cf9b4d11787966bda05f99137d/experiments/graphite-packet-reciprocity/README.md) and its `verify_reciprocity.py`. The edge basis is oriented `A_r→B_(r-s_t)` for `s=(0,m+n,n)`. The **unnormalized** harmonic embedding `H:R²→R^(3N)` assigns the three edge classes `h_0=(1,1)`, `h_1=(-1,1)`, `h_2=(0,-2)`. This is the `HARMONIC` report basis of that verifier, equal to `sqrt(N)` times its prior normalized `M`. The unit chain inner product gives `B₁H=0`, `B₂ᵀH=0`. These are native, dimensionless chain spaces; a lateral Cartesian metric, physical registry, and material units are not supplied.

Take the fixed-mask-free native generator in dimensionless parameter `s`:

`x'=-B₁y,  y'=B₁ᵀx-B₂z,  z'=B₂ᵀy`, with `x∈R^(2N)`, `y∈R^(3N)`, `z∈R^N`.

Define a **chosen**, orientation-even edge weight `w_e(q)=y_e²≥0` and the formal port `S(w)=Hᵀ diag(w) B₁ᵀ:R^(2N)→R²`. This is the even candidate of the [reciprocity note](https://github.com/ud-tetra/UD-Physics/blob/3b9f6dee5e8c69cf9b4d11787966bda05f99137d/experiments/graphite-packet-reciprocity/README.md), in an unnormalized report basis. It does not canonically define ledger Q25 `w_ij`, and it is not a physical stiffness.

## Preparation, persistence, and no spontaneous creation

Choose the particular initial state `q_a=(0,Ha,0)` with `a=(a,b)∈R²`. Then `A q_a=0` because `B₁H=B₂ᵀH=0`. The edge weight `w_e=(h_t·a)²` is **exactly stationary** in this isolated native system. More generally,

`d(Hᵀy)/ds=HᵀB₁ᵀx-HᵀB₂z=0`.

Thus an ungated trajectory with `Hᵀy(0)=0`, including the usual `y(0)=0` preparation, never develops a harmonic component. A nonzero `a` must be prepared initially or supplied through a specified symmetry-breaking gate, boundary, drive, or open-system source. A changed generator or reciprocal material backreaction requires this conservation result to be rechecked.

## Exact source matrix and rank

Every A site and every B site has one incident edge in each of the three classes. Therefore the columns of `S(w)` are `-v(a)` at every A site and `+v(a)` at every B site, where

`v(a)=Σ_(t=0)^2 h_t(h_t·a)²=(4ab, 2(a²-3b²))`.

Equivalently, `S(w)=v(a)[-1_Nᵀ,1_Nᵀ]`. For real `a≠0`, `v(a)≠0`: `4ab=0` forces `a=0` or `b=0`, and `a²-3b²=0` then forces both to zero. Hence **rank `S(w)=1` for every nonzero prepared harmonic amplitude**. Its only site input is the uniform A-versus-B sum, and its native lateral output is along `v(a)`. For `a=0`, `S=0`. In this declared unit site metric, `||S||_F²=2N||v||²`; the `N` factor is a report-size effect and not contact-area scaling.

The form and nonzero-rank criterion are common to `N=7,13,19`. This candidate cannot select the observed `(2,1)` pair from these other commensurate quotients. C3 symmetry rotates the prepared `a`; a nonzero selected direction is an extra preparation, not spontaneous selection from a symmetric seed.

If one **assumes separately** the reciprocal physical cross-Hessian `C_a=λ TᵀS(w)R_h` with dimensionless material registration maps `T,R_h`, `λ` in energy per upper atom per length squared, stable stiffness `K≻0`, and dissipative `D_h⪰0`, then `rank C_a≤1` and the conditional added **self-loss** `Γ_self=C_aK⁻¹D_hK⁻¹C_aᵀ` has rank at most one. Every vector in `ker(C_aᵀ)` is in `ker(Γ_self)`; in a declared Euclidean lateral metric and with nonzero registered port this includes the direction perpendicular to `Tᵀv(a)`. This does **not** imply zero total force or a rank-one conventional-subtracted damping: if the existing contact coupling is `C₀`, the signed residual includes `C₀ L C_aᵀ+C_a L C₀ᵀ` with `L=K⁻¹D_hK⁻¹`. Nor does a stationary edge weight make the *coupled* native-material dynamics stationary; reciprocal backreaction must be included as in the source note.

## Reproduction and disposition

Run `python3 experiments/graphite-harmonic-preparation/replay_harmonic_edge_source.py` (SHA-256 `88dce69f3905c97966965fd7b2f670ae799027d7d0955789c2bbee8d7d253994`). The exact Fraction/integer checks verify `B₁H=B₂ᵀH=0`, the port columns, and `||S||_F²` on all three quotients for `a=(1,0),(1,1),(2,-1)`. For `(1,0)`, `v=(0,2)` and `||S||_F²=8N`, giving respectively `56,104,152`. The symbolic derivation above is the independent general check beyond those cases.

**Decision:** AUTO_LOCK only the finite algebra and conservation within this declared carrier and ungated generator. Keep `w=y²` as a CANDIDATE choice, the nonzero harmonic preparation as externally supplied, and all physical material mapping, bath, load slope and signed force OPEN_GATED. A native preparation/selection rule and an independently measured or derived material cross-Hessian are still required before a graphite-specific `mu1` can be frozen. The Q22 source-zero result retains its own scope; this construction does not amend ledger Q22/Q24–Q26.

