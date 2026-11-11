# QPB1 sampled admission and parity closure v0.4

EXACT / CONDITIONAL. Source: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3 and `experiments/qpb1-native-events/EVENT_CONTRACT.md`. Physical promotion 0.

The filled-tetrahedron source-native unit-metric flow has x'=Ax, A=d-d^T, J=A/2, q=Ex, p=EJx; q'=2p and p'=-2q. Here x is real 15D, q and p are real six-vectors, and the continuous parameter u is dimensionless.

At the explicitly chosen sampling u=pi/4, F=I+A/2+A²/4 has F^4=I, and (q,p) maps to (p,-q). Admit configurations where every q and p coordinate is nonzero at the sampling epoch. This domain is preserved under repeated F, but not necessarily under all intermediate continuous times. Record sign bits and opposite-edge pair XORs theta_q and theta_p. Exact update: (theta_q,theta_p) maps to (theta_p,theta_q).

All 4096 ordered six-plus-six sign states occur, and their 64 paired parity states each have 64 sign antecedents. The reported theta_q sequence alternates theta_q,theta_p; 64 separate two-tick histories prove a minimal 64-state deterministic observer for the whole admitted domain. Three-bit theta_q alone is nonautonomous.

The signed S4 edge action induces a well-defined affine action on parity labels. The swap law commutes with that action. Exactly 24 times 4096 permutation-state checks passed locally.

This is **finite information readout, not irreversible material retention**. For positive lambda, x and lambda*x have the same signs but different native squared norms. A sign-only collapse to a fixed representative cannot conserve norm for both without a compensating reservoir. No source-selected reservoir, energy budget, clock calibration, physical mass, or full UD binary admission rule is established.

Script: `retention_gate_v04.py`. Results: `retention_gate_v04.results.json`. Constructor verification only; external review NOT_RUN. Next: derive native source/sink or noninjective state map with explicit energy/stock receipt before interpreting symbolic persistence as physical retention.

## Source-native support-current dependency (ledger v0.39)

The independently imported coefficient ledger at `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md`, objects Q169–Q179, provides signed simplex-current accounting, not an already-selected irreversible gate. In particular Q170 defines control-volume support `S_mu(R)=Σ_{sigma∈R} c_sigma²` with incidence-boundary inflow/outflow; Q171–Q173 define top-cell and face reservoir currents; Q177–Q179 give equal-share cell support `S_mu,tau=Σ_{sigma⊂tau}c_sigma²/n3(sigma)` and its exact current evolution. Q178 explicitly leaves environment/dissipation/renewal semantics open, while Q179 leaves source/sink terms open. G05 marks action weighting as source-blocked pending those open-system receipts. Consequently these receipts support an exact future material-retention **accounting interface** but do not derive a gate transition, irreversible attraction, physical time, or a specific nonzero retention threshold. This source check rules out treating the sign-readout projection itself as conserved material burden.
