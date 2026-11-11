# UD-Physics Discovery handoff v0.8 — multiport phase and retention obstruction

**Task:** parity-dynamics-gauge-20261103, session pdyg-20261103-01, claim `refs/heads/claims/parity-dynamics-gauge-20261103` HELD at `d0950c1c5376a31b483908c819123914ae59c404`. Isolated `discovery/parity-dynamics-gauge-20261103/pdyg-20261103-01`, PR #284 draft. Original task base `2207611450df9106adccaf8189a50734fef5a46b`, main seen at `d4b10ea6abeab50d5e1b74e8735fb98955c6e017`. Reconcile moving main before integration. No claim release, merge, or mainline promotion.

## Source-specific result

- Source: `experiments/qpb1-source-reservoir/README.md` v1.1 §§1–2. Matched real 15D filled K4 packet + real 2D reservoir; top-cell embedding, unit Euclidean modal metric, native dimensionless u. Under declared common S4 sign representation, a real 2×2 source port M is allowed. Complex-rotation compatibility **additionally** restricts M=aI+bj.
- In co-rotating mode coordinates r'=M y, y'=-Mᵀ r, total N=||r||²+||y||² conserved. For fixed complex-compatible M=aI+bj, write M=gR with g=sqrt(a²+b²), R∈SO2, ybar=R y. This reduces exactly to scalar reciprocal coupling and preserves rotated D_R=det(r,R y). Old D can change without gaining a new independent physical channel.
- Exact rational test a=3/5,b=4/5 with r=(1,0), y=(0,1): N=2,D_R=3/5, reservoir floor >=9/50, exact orbit minimum 1/5. No full capture.
- Drop complex compatibility (changed-hypothesis candidate): any M remains S4 equivariant under assumed matched signs but singular values are unselected. Co-rotating M diag(1,2) never swaps both independent source components simultaneously; diag(1,3) swaps all empty-target source at *chosen* native u=π/2, but reverses thereafter. A constant anisotropic M in this co-rotating chart entails an added time-varying source-frame coupling, not the original unmodified QPB1 constant port.
- Any fixed source-frame real M in the full matched G_M matrix gives a skew-adjoint generator, which preserves all full-state distances. Thus autonomous full-state attraction absent without changed (nonlinear/open) assumptions.

## Provenance and boundary

QPB1 real 17D port and Q170–Q179 cell-owned support on separate real 29D 1→4 complex remain distinct types with no source-derived interchange map. No source-selected gain ratio, controller, or source/sink renewal rule; no physical clock, energy, particle mass, or Standard Model prediction. This is an exact *negative* result against naive multichannel promotion, not a no-go for all possible future ports.

## Replay

```bash
python3 experiments/parity-dynamics-gauge-20261103/multiport_v08.py
python3 -m unittest discover -s experiments/parity-dynamics-gauge-20261103 -p 'test_multiport_v08.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Commit files:
- `experiments/parity-dynamics-gauge-20261103/NONSCALAR_PORT_PHASE_AUDIT_v0.8.md`
- `experiments/parity-dynamics-gauge-20261103/multiport_v08.py`, `multiport_v08.results.json`, `test_multiport_v08.py`
- `candidates/parity-dynamics-gauge-20261103/mathematical_receipt_multiport_v0.8.json`
- Session journal/record/candidate and this handoff.

Local constructor calculation PASS on exact rational algebra (phase-gauge proof and four rational source-phase fixtures); alternative local four tests PASS. Source independent mathematical review NOT_RUN; CI integrity is tracked to exact head, not considered independent proof.

**Next discriminant:** identify source-bound *non-equivalent* additional transport or nonreciprocal environmental law that changes phase-area after all admissible reservoir-frame transformations, with source/stock, local conservation and controller receipts; test arbitrary phases and null controls. If source cannot supply it, park candidate rather than promote. Physical promotion remains 0.
