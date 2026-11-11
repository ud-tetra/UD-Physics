# Constitutive retention-current gate v0.5 — exact receipt, no native selector

**2026-11-03 / UD-Physics Discovery / EXACT–CONDITIONAL / SELECTION OPEN / physical promotion 0.**

## Source authority and types

Verified source basis: `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md`, ledger Q169–Q179 (especially Q170, Q171–Q173 and Q177–Q179), and `experiments/four-cell-tetrahedron/README.md` v1.0, section “Definition and scope.” These provide exact incidence-current accounting and equal-share ownership, but not an open-system retention threshold, environmental source law, or a physical clock. Task claim `refs/heads/claims/parity-dynamics-gauge-20261103` HELD by session `pdyg-20261103-01`; existing isolated branch, PR #284. No mainline changes.

Let K be the **finite** 1→4 subdivision of a tetrahedron, with four maximal 3-simplices `(0124),(0134),(0234),(1234)`, 29 unique simplices and face vector `(5,10,10,4)`. Let `C_k(K;R)` have ascending orientations, `B_{sigma,eta}` the signed boundary matrix (lower simplex sigma, coface eta), and `c_sigma∈R` a chain amplitude. Work in the unit Euclidean chain metric and formal dimensionless continuous parameter `u`. A closed conservative carrier law is `c'=(d-d^T)c`; no physical energy/mass unit is assigned. Define nonnegative support `s_sigma=c_sigma²`.

For each `sigma`, let `n_3(sigma)=#{tau maximal tetra: sigma⊂tau}` and `w_{sigma,tau}=1/n_3(sigma)` when contained, 0 otherwise. Define **cell-owned circulating support** `S_tau=Σ_sigma w_{sigma,tau} s_sigma`. Q177–Q179 fix this allocation and current algebra under the stated complex. Do not identify `S_tau` with a physical particle.

## Theorem A — exact cell allocation and signed current

Every simplex here lies in at least one maximal cell, and `Σ_tau w_{sigma,tau}=1`. Therefore `Σ_tau S_tau=Σ_sigma c_sigma²`. Define the **outward lower→upper** incidence current `J_{sigma→eta}:= -2 B_{sigma,eta} c_sigma c_eta`. This sign choice matches Q179's written form. Then

```
d S_tau/du = Σ_(sigma ⊂ eta)
             [w_(eta,tau) - w_(sigma,tau)] J_(sigma→eta).
```

This follows by differentiating `c_sigma²`, pairing the two incidence endpoints, and collecting weights. The integral cell sum of the right-hand side vanishes identically, since both weights individually partition unity. It is **exact accounting**, not a selection theorem.

## Theorem B — the minimal typed one-event transfer family

Introduce a new retained nonnegative **bookkeeping stock** `r_tau≥0` for each tetrahedron. At a declared event on simplex sigma choose an **additional constitutive** transfer `δ_sigma` satisfying `0≤δ_sigma≤s_sigma`. Define a post-event amplitude with `c_sigma'^2=s_sigma−δ_sigma` (its sign convention must also be specified), leave other amplitudes unchanged, and assign

```
r_tau' = r_tau + w_(sigma,tau) δ_sigma,
S_tau' = S_tau - w_(sigma,tau) δ_sigma .
```

Then **exactly and cell by cell** `S_tau'+r_tau'=S_tau+r_tau`, and total `Σ_tau(S_tau+r_tau)` is conserved. The upper bound ensures nonnegative circulating and retained stocks. A transport-boundary term could be added only with an explicitly signed boundary receipt, not invisibly.

This theorem holds for **every** admissible transfer δ, including δ=0. Neither the Q170–Q179 conservation identities nor the equality of ownership shares chooses δ or whether reverse transfer is allowed. For a relabel-covariant candidate, δ must transform consistently under the signed S4 action; the tested single-face preparation is not an S4-invariant initial state.

## Exact discriminating witness: null versus capture

Choose the shared face `sigma=(0,1,4)` and a coface `eta=(0,1,2,4)`. Initially take `c_sigma=c_eta=1`, every other amplitude 0 and all `r_tau=0`. The face has `n_3=2` and weights `1/2` to the two incident tetrahedra.

- Continuous conservative current: `J_(sigma→eta)=-2` in the declared orientation; exact derivatives of cell-owned support are `(-1,+1,0,0)` for maximal cells in their listed order. The direct derivative calculation and Q179 weighted-current calculation agree for every cell; the total derivative is zero.
- Null event, **δ=0**: circulating total 2, retained total 0.
- Capture event, **δ=1**: set the face amplitude to 0 and transfer one support unit into retained shares `r_(0124)=1/2`, `r_(0134)=1/2`. Circulating total becomes 1, retained total becomes 1 and combined total remains 2.

**NO-GO / under conservation-only hypotheses:** Both event outcomes satisfy the exact same source-derived support accounting. A conservation receipt alone cannot force capture, select a threshold, or prove retained-stock persistence. Reverse release `δ<0` is not within the one-way contract; forbidding reverse release is an **additional assumption**. The surviving coface amplitude generates fresh face flow under continued conservative evolution, so capturing once does not freeze the carrier or select a stable spatial cluster.

## Verification, exposure and disposition

Execute `python3 experiments/parity-dynamics-gauge-20261103/retention_receipt_v05.py` (stdlib, exact fractions). Stored output: `retention_receipt_v05.results.json`. Locally executed: PASS, 29-simplex ownership partition, direct versus current derivative, two exact event branches, cell-level nonnegative receipt. No empirical target/physical coefficient was inserted. The two tested event choices were constructed **after exposure to the conservation requirement**, as countermodels; not preregistered physical predictions. No physical clock, particle charge or mass calibration exists.

**Theorem status:** EXACT for the source-defined Q177–Q179 ownership/current identities and conditional transfer-receipt family. CANDIDATE for any chosen δ>0 constitutive event; OPEN for event initiation, decay/persistence, source reservoir, intercell competition and observed physical correspondence. Do not relabel the bookkeeping stock `r_tau` as physical mass or assume the event-parameter index is physical time. Independent non-constructor review NOT_RUN.

**Next discriminant:** Supply a *source-native* admissibility/constitutive gate `δ_sigma= G(c,transport,closure,history)` and an explicit reverse/release or environment coupling law; prove conservation, nonnegative stock, locality, and a quantified persistent advantage over δ=0, including a falsifiable independent readout. Any arbitrary gate must be labeled HYPOTHESIS/FIT, not derived.
