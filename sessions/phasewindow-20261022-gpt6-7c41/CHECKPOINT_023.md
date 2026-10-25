# Checkpoint 023 — six-channel long-time numerical stability and conditional time envelope

**STATUS: COMPLETE local replay / CONDITIONAL exact interpolation / NUMERICAL forward-adjoint u100 checks / VALIDATED numerical interval enclosure NOT_RUN.**

Task `icosahedral-phasewindow-20261022`, held claim `phasewindow-20261022-gpt6-7c41` on branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Read-only integrated mechanical source `59814ea16e94ac4048dc878ef99d23097ca63b9b` (SHA blob checks). Prior claimed research head `1b630ebd6829a7016d4d4656666a183625020cbb`. PR44 independent, no overlapping edits.

## Executed

- Reproduced u100 six-channel adjoint at rtol `3e-7` and `1e-7` (results files and six 180D output rows frozen).
- Independently integrated selected initial tangent forward to u100 at rtol `1e-5`, `1e-6`, and `1e-7`, with distinct ODE solve orientation but shared sparse Jacobian model; agreement at tightest tested settings about `0.0202%` relative.
- Refined sampled response near u4: higher sampled point u4.04 `6.638579048e-5` (NUMERICAL).
- Computed first-order projected **velocity** gain using six dual velocity seeds, sampled up to u100. Largest recorded sample `6.006680801e-4` at u4.04; no continuous-time maximum proved.
- EXACT/CONDITIONAL rational mesh lemma: node gain ≤1/10000 and all-time derivative gain ≤1/1000 imply g(t) ≤151/10000, leaving residual allowance 99/10000 toward 1/40.
- DOP853 tighter adjoint rtol1e-8 and forward rtol3e-8 exceeded compute limits; deliberately not marked passed.

## Handoff

The exact lemma is ready for future interval/certified IVP validation but **the two numerical premises are not proven**. No universal u100 nonlinear phase-ball bound or positive housing-strut clearance. Repository branch can carry proof/receipt/code/checkpoint while complete executable input/output archive remains local. A repository CI integrity run, if present, does not establish the mathematics.

**Next highest-value action, 99/100:** validated interval six-channel adjoints for all 12 nodes and full-time derivative bound `<1/1000`, then nonlinear residual `<99/10000` plus global housing strut positivity. Do not touch PR44 or mainline.