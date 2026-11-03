# Session handoff v0.6 — source-bound admission/release controller test

**STATUS:** EXACT/CONDITIONAL reciprocal port; exact NONUNIQUENESS of retention selection; no autonomous physical selector. Task `parity-dynamics-gauge-20261103`; session `pdyg-20261103-01`; claim HELD at SHA `d0950c1c5376a31b483908c819123914ae59c404`; isolated `discovery/parity-dynamics-gauge-20261103/pdyg-20261103-01`; PR #284 DRAFT. Resume main revision `7c26ef783b0dccac998eb61c3dcb15c52d2cf746`, original task base `2207611450df9106adccaf8189a50734fef5a46b`. Main advancement requires rebase before integration; no mainline export or state/CURRENT edit.

## Source
- `experiments/qpb1-source-reservoir/README.md` **v1.1 §§1–5**: reversible matched 15D packet + two-mode source, skew generator, source/packet support reciprocity, exact swap, release, externally prescribed gate-off; g and controller not sourced.
- `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md` Q170–Q179 and G05: exact **distinct** 29D subdivided-tetrahedron support-current accounting, but constitutive gate and physical action open.
- Prior local v0.4 sampled sign parity is an observer; v0.5 one-event cell capture is a **conditional bookkeeping model**. Neither establishes a cross-carrier map to the 17D matched port.

## Experiment/derivation
Under source-unit joint metric, native dimensionless u, g=1 selected trial, empty addressed target r0=0 and source y0=(1,0), target and source support are sin²u and cos²u. At u=pi, three lawful branches give target stock 0 (g=0 null), 0 (g=1 constant reciprocal release), or 1 (g=1 until pi/2 then g=0). The off command is a new controller assumption. The signed current j=sin 2u vanishes at both empty and full endpoints; zero-current alone cannot select. Initial target r0=±y0 changes occupancy at pi/4 between 2 and 0. Constant finite-dimensional skew-adjoint flow preserves full-state Euclidean distances and cannot have an open attracting basin; this no-go is **not** about arbitrary nonlinear/open dynamics.

## Reproduce
```bash
python3 experiments/parity-dynamics-gauge-20261103/reciprocal_gate_v06.py
python3 -m unittest discover -s experiments/parity-dynamics-gauge-20261103 -p 'test_reciprocal_gate_v06.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Committed: `NATIVE_ADMISSION_RELEASE_v0.6.md`, `reciprocal_gate_v06.py`, `reciprocal_gate_v06.results.json`, `test_reciprocal_gate_v06.py`, and `candidates/parity-dynamics-gauge-20261103/mathematical_receipt_reciprocal_v0.6.json`. Exact local constructor script PASS; alternative four tests PASS. GitHub Discovery integrity CI to be checked on newest SHA. Non-constructor mathematical review NOT_RUN.

## Decision
**SOURCE_BOUND:** reciprocal transfer is a workable exact internal mechanism. **NO-GO / scoped:** no unique retention selector or attracting final state from fixed skew conservation/locality/S4 alone. **OPEN:** autonomously derived gate switch, environmental reset and feedback, microscopic 29D-to-17D interface, parameter choice, physical clock/units/measurement. Do not call externally switched target a dynamically selected particle.

## Next discriminant
Recover a concrete source-defined *autonomous* gate or feedback `g=g(c,y,closure,history)` and signed controller/source receipt; test initial phase, null/no-source, reversible-release and nonzero perturbation families without retrofitted selection. An added latch or nonlinear feedback remains a candidate unless primitive dynamics force it. No claim release or merge performed.
