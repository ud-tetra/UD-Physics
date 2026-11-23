# Q171 directional-current convention amendment — v0.39a (PROPOSED, NOT ACCEPTED)

**Review requested:** Source authority for frozen coefficient ledger `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md` Q171. No historical row or mainline claim is modified. Discovery task `klein-tetra-face-flip-20261103`, PR #301.

## Frozen basis and exact witness

Fix ascending simplex orientations and `B3(f,tau)=(partial_3)_(f,tau)`. Source Q169's native unit-metric generator is `A=D-D^T`, hence
```
A_(f,tau) =  B3(f,tau),    A_(tau,f) = -B3(f,tau).
J_(f<-tau) = +2 B3(f,tau) c_f c_tau.
J_(tau<-f) = -2 B3(f,tau) c_f c_tau.
dot S_tau^core = sum_f J_(tau<-f) = -2 sum_f B3(f,tau)c_f c_tau.
```
These signed currents cancel pairwise and obey Q170 cuts. Literal frozen Q171 prints the **positive** `2 B3 c_f c_tau` as **top stock derivative**. For face 012, tetrahedron 0124, `B3=-1`, `cface=ctop=1`, Q169 top derivative is +2, while literal Q171 expression is -2 using the identical B3.

## Recommended typed amendment

Preserve historical coefficient as oriented **outflow**:
```
Q171.v0.39a PROPOSED (NOT AUTO_LOCKED)
J23_out(f,tau) := +2 B3(f,tau)c_f c_tau     [tetrahedron -> face signed current]
J23_in(tau,f) := -J23_out(f,tau)
dot S_tau^core = sum_f J23_in(tau,f) = -sum_f J23_out(f,tau).
```
The word 'outflow' denotes a directed signed current, not numerical positivity. No new coefficient or physical units.

**Alternative requiring explicit source choice:** If original Q171 intended `B3_Q171=-B3_Q169`, formally declare this typed sign alias and retain its positive derivative formula. Do not silently mix the two conventions.

## Review acceptance gate

A source-authorized custodian should choose the intended interpretation and record an append-only versioned change to the Q171 convention, with dependencies Q166/Q169/Q170/Q173/Q177–Q179 reviewed. Verify all oriented face/top pairs and all 24 signed S4 relabelings. The accepted document should distinguish `J_f<-tau` from `dot S_tau`. An author-created proposal or integrity CI PASS does **not** approve the amendment.

**Scientific scope:** No event selector, no cross-complex physical current, no SI time, no Planck promotion. Related derivation: `CURRENT_INTERFACE_Q170_v1.9.md`; full local exact package v1.9.