# Non-affine 3D dynamics audit — executed protocol

The original question is whether the full original alpha=.1 passive mechanical pulse, with the allowed 180-dimensional housing-phase energy ball and continuous qualified material box, maintains `||Z(u)||F<=1/40` through u=100. The previous exact cell-orientation theorem makes this a *sufficient* geometric condition, but no assertion of necessity for coherence/ringdown is made.

## Baselines and candidate selection

- Unmodified mechanical terms reimplemented from byte-pinned 3D primary, multiport, damping, finite housing and mount-loss source at main `a4ae75dd55cd2b691c811c4d6eeae1367fcba015` (see `SOURCE_LEDGER.json`).
- Exact construction: one exterior vertex moves by `(1/25,0,0)`; static alpha0 is **zero** and auxiliary/housing storage is minimized separately. This targets and refutes only *energy-sublevel* inheritance of the bound.
- Four development pulse preparations: uniform properties with no extra housing motion; uniform with one seeded Gaussian housing phase; one seeded ±5% material, ±1% port transmission, ±10% housing-weight, beta=.005, cf=0 case with seeded Gaussian housing phase; the same scattered case with the phase maximizing *linearized u=0 non-affine acceleration*. All have heart alpha0=.1 and nu=.05; phase energy when nonzero equals 1.5 times the original E_p/40000, as authorized in the preceding phase-window study.
- The scattered coefficient vector is reproducibly generated with NumPy default_rng(10422) and is **not** the repository's previously published `seed10422-0-boundary2` case, despite its similar property ranges. It is a constructor development sample, not a truly independent validation sample.
- The initial-gain phase uses SVD of a 36×180 matrix. Its linearization is at the reference state and represents the exact derivative at u=0 of the acceleration with respect to energy-normalized housing phases; due to the changing current strut directions, finite amplitudes can differ. Maximizing acceleration at u=0 does not maximize u=100 displacement.

## Numerical integrations

From `/mnt/data/ud_nonaffine_dynamics_011/`, run:

```bash
python3 exact_witness.py
python3 verify_audit.py
python3 nonaffine_audit.py --out full100 --until 100 --samples 1001 --cases uniform-none,uniform-random,adverse-random,adverse-initial-gain --rtol 2e-9 --atol 2e-11
python3 nonaffine_audit.py --out refined100 --until 100 --samples 2001 --cases adverse-random,adverse-initial-gain --rtol 3e-11 --atol 3e-13
```

Requires Python 3.13, NumPy 2.3, SciPy 1.17, SymPy 1.14 for exact separate check. The inherited model uses length units ell0=1, dimensionless time u and uncalibrated mass/energy constants.

Each readout trace contains sampled time, non-affine Frobenius norm and minimum of all 120 strut lengths. The reported `max_nonaffine_fro` is the *maximum over output samples*, not a validated continuum maximum. DOP853 error tolerance/refinement checks do not prove continuous-time or all-initial-phase bounds. Heat accumulator is mechanical energy loss integrated from zero; energy+heat conservation and total force/torque identities are checked.

Original data exposure and assumptions must be retained. There are no fitted physical units or experimental comparisons; the research branch is hypothetical. Full u=100 all-phase closure remains OPEN. PR #44 has independent ownership of Green-bound recovery and is untouched.
