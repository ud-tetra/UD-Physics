# UD Discovery — checkpoint initial-curvature-017

- Task: `icosahedral-phasewindow-20261022`; session: `phasewindow-20261022-gpt6-7c41`; live task claim **held**.
- Isolated branch: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
- Versioned read-only base: main `4aaf0a39d24328e27bc425e333e3612baea888a5`; mechanical imported blobs unchanged.
- **Exact positive result:** every allowed 180D housing phase has initial finite nonlinear *projected acceleration* remainder `<267699/3022662500000<9e-8`, valid uniformly over beta, housing weight and nu ranges under the original enlarged housing phase energy cap.
- **Exact negative result:** a family of static positive-length configurations with total energy `<27/1000` has divergent moving-axis projected acceleration Hessian as one strut tends to zero; passivity/total energy alone cannot bound full-time nonlinear remainder.
- Executed: `python3 exact_initial_bound.py --out exact_initial_bound.json`; `OPENBLAS_NUM_THREADS=1 python3 independent_assembly.py --out assembly.json`; `OPENBLAS_NUM_THREADS=1 python3 singular_energy_obstruction.py --out singular_witness.json`. All PASS.
- Source matched: original full 560-phase force reimplementation from prior 016 immutable archive; frozen case coefficient SHA-256 checked inside `source_case.py`. 238 finite phase checks / 13 four-corner force checks; 5 singular-family samples.
- Evidence modes: EXACT / CONDITIONAL for the inequalities and obstruction, NUMERICAL / DEVELOPMENT for constructor tests. No physical identification and no experimental validation.
- The original full nonlinear `u=100` cell, 120-strut, breathing/ringdown criteria remain OPEN; no Green/remainder certificate was obtained.
- Other owner: PR #44 and `integration-icosahedral-greenbounds-20261022` are untouched.
- Next discriminant (99/100): establish a trajectory-domain positive-length tube and bounded projected propagator plus full-state nonlinear source over every admitted phase; do not extend the initial-time inequality by assumption.