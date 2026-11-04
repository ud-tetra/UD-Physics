# Klein × K4 twisted packet-chain handoff v0.3

**Task:** klein-tetra-face-flip-20261103. **Session:** ktff-20261103-01. **Claim:** refs/heads/claims/klein-tetra-face-flip-20261103 at commit 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4, HELD. **Branch:** discovery/klein-tetra-face-flip-20261103/ktff-20261103-01, draft PR #301. Original verified main base 0eef9a3f77198810b35bee8d3ef578ebc3af403a; main later advanced. Rebase/reconcile before integration; no mainline export, shared CURRENT edit or claim release.

## Source and object types

Native K4 factor: experiments/qpb1-local-generators/README.md v1.0 §§1–3, filled tetrahedral C_*(Delta³;Z) with 4+6+4+1=15 chain coordinates; source unit-metric skew generator. New topology factor: previous Discovery Klein 2-face quotient with orientation character from DOUBLE_COVER_AND_TRANSPORT_v0.2.md. Its CW equivalent has one vertex, two edges, one 2-cell and relation h v h^-1 v. This is an imposed nonorientable seam topology, not K4's original S2 shell or a proved glued three-dimensional packet assembly.

## Exact conditional construction

Twisted orientation local coefficient rho(h)=-1,rho(v)=1 gives CW d1=[-2,0], d2=[0,0]^T by Fox differentiation; untwisted trivial rho gives d1=[0,0],d2=[0,2]^T. Both square to zero but have different integral homology: twisted H0=Z/2,H1=Z,H2=Z; untwisted H0=Z,H1=Z+Z/2,H2=0.

Take graded tensor with all 15 K4 packet coordinates using d_total(b_p tensor k_q)=d_CW b tensor k + (-1)^p b tensor d_K k. Exact product chain dimensions (4,14,20,15,6,1), total60; nilpotency holds for both. Over R, boundary ranks twisted (4,9,10,5,1), untwisted (3,10,10,5,1); Betti vectors twisted (0,1,1,0,0,0), untwisted (1,1,0,0,0,0).

Under **chosen** unit Euclidean metric, source-type 60D skew evolution x'=A x, A=d_total-d_total^T conserves native squared norm exactly. Yet both models have exactly the same UNGRADED Laplacian spectrum of -A²: eigenvalues 0 mult2, 4 mult30, 8 mult28; trace344, squared trace2272. The twist is not spectrally identifiable from this readout alone. Independent factor Laplacian computation: CW spectrum 0²+4² in both, K4 0¹+4¹⁴; sum gives identical tensor spectrum.

Orientation loop transport rho_tw(h)=-I15 versus rho_null(h)=+I15, and Klein relator maps I15. Norm-squared readout cannot distinguish these, although reference-framed sign/holonomy path comparisons could. This is a PATH transport statement, not a physical clock or matter-generation mechanism.

## Reproduce

```bash
python3 experiments/klein-tetra-face-flip-20261103/twisted_packet_chain_v03.py
python3 experiments/klein-tetra-face-flip-20261103/spectral_crosscheck_v03.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p test_twisted_packet_v03.py -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Committed: experiments/klein-tetra-face-flip-20261103/{TWISTED_K4_PACKET_CHAIN_v0.3.md,twisted_packet_chain_v03.py,twisted_packet_results_v03.json,spectral_crosscheck_v03.py,test_twisted_packet_v03.py}; candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.3.json; session journal/record and this handoff.

Local exact 60D construction PASS, independent factor-spectrum computation PASS, four local unit checks PASS (two methods, same constructor). Repository CI verifies integrity only; non-constructor mathematical review NOT_RUN. Physical promotion 0.

## Critical no-go and next discrimination

Topological twist is not a new universal physical spectral eigenvalue: exact twisted/untwisted isospectrality under the declared metric. Sign-insensitive stocks see no global loop difference. The next high-information action is to derive a real native *three-dimensional* K4 gluing/seam and an orientation-sensitive operational readout (e.g. relative interferometric path-frame comparison) without inserting a free phase or physical clock. First demonstrate signed chain-map compatibility and conservation on a finite, nonmanifold or manifold packet network; then test a discriminating held-out readout. If sourcing fails, park this construction as an exact mathematical candidate.
