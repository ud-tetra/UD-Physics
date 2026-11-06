# Klein–K4 twisted 72-simplex boundary and native invariant hull — v0.5 handoff

**Session:** ktff-20261103-01; **task:** klein-tetra-face-flip-20261103. **Live claim** refs/heads/claims/klein-tetra-face-flip-20261103 HELD SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4. Existing isolated branch discovery/klein-tetra-face-flip-20261103/ktff-20261103-01; PR #301 draft. Original base 0eef9a3f77198810b35bee8d3ef578ebc3af403a; main has advanced. No merge, physical/mainline promotion, shared CURRENT changes or claim release.

## Source and topology

Read-only source: experiments/qpb1-local-generators/README.md v1.0 §§1–3, signed 15D K4 chain and source unit generator, plus prior development THREED_KLEIN_PACKET_SEAM_v0.4.md. **Assumed** new Klein K×I seam is a real nonorientable 3D Delta complex with 72 labeled tetrahedra and ordinary incidence f=(18,102,156,72). The new seam is not native K4 topology or an established physical volume. The w1 orientation character is (h,v,x)=(1,0,1) over F2.

## Exact work completed

1. **Integral twisted 72-tet boundary:** lift all simplices to orientable two-sheet cover with f=(36,204,312,144), glue sheets using w1, and use deck-anti-invariant bases. The resulting integral boundary matrices have shapes 18×102, 102×156, 156×72; exact compositions zero. Rational ranks (18,83,72), Betti over Q (0,1,1,0). Integral Smith invariant factors of twisted B1: seventeen ones and one two, yielding H0=Z/2. Integral H1/H2 from 72x matrices not separately SNF-audited; source-topology comparison supports H1=Z,H2=Z.
2. **Simplicial-to-cellular rational comparison:** explicit Phi0=0, Phi3=0, Phi_k=t_k h_k^T/(h_k^T h_k) for k1,2, where h and t are exact harmonic representatives from chosen unit metrics. Source norms (160,84), target norms (2,2); exact chain commutation and induced H1/H2 rational equivalence. Composite into earlier twisted 60D model has ranks (0,1,1,0). IMPORTANT: global, nonlocal, **rational**, NOT an integral geometric barycentric-subdivision collapse, NOT H0 Z2 preservation, not an isometry or flow intertwiner.
3. **Native dynamics invariant closure:** earlier even-S4 packet interval map F had rank3 but native K4 generator A_K pushed it out. Its unique minimal invariant hull H=span(F,A_K F,A_K² F) has rank5, one harmonic plus four active real dimensions. Source unit metric projector commutes with A_K; the even S4 permutation fixes H pointwise. Chosen combined loop U_tw=-R_K(even) acts -I5, and the matched null U0=R_K(even) acts +I5. Native unit inner product comparison C_tw(x)=−||x||² versus C0(x)=+||x||² on H contains no selected phase angle or external numeric scaling, but **requires physical orientation frame/readout coupling**, which remains source OPEN. Even S4 completion and H state admission are not forced by the seam.

## Exact reproducibility

```bash
python3 experiments/klein-tetra-face-flip-20261103/twisted_72_boundary_v05.py
python3 experiments/klein-tetra-face-flip-20261103/rational_comparison_v05.py
python3 experiments/klein-tetra-face-flip-20261103/invariant_hull_v05.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p test_v05.py -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Proof: experiments/klein-tetra-face-flip-20261103/TWISTED_72_AND_INVARIANT_HULL_v0.5.md; scripts and three expected JSON output snapshots; typed receipt candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.5.json. Local equivalent exact SymPy script PASS (72 cells, SNF, map, invariant hull). Four constructor regression tests PASS; independent non-constructor review NOT_RUN. GitHub CI checks repository structural integrity, not theorem or physical correspondence, and is reported per head SHA.

## Gaps and stopping rule

OPEN: a local **integral** simplicial-to-cellular subdivision chain map and homotopy equivalence preserving Z/2 torsion; full 72-cell-to-60D source dynamics intertwining; uniquely selected K4 seam completion and operational orientation reference; empirical unit/time bridge. The 5D invariant hull is a scoped source generator theorem **conditioned on** even S4 map F, not autonomous matter or dynamics on K×I. If the integral geometric subdivision map or physical framed observer cannot be sourced, park this branch as an exact conditional topology/chain candidate; no physical promotion.

**Next recommended:** exact integral local subdivision map (or precise obstruction) preserving H0 torsion, then source/prepare physical framed loop comparison with independent null.
