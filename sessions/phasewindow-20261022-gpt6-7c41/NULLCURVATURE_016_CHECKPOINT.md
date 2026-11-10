# CHECKPOINT — nonaffine-nullcurvature-016

STATUS: EXACT local viscous cross-force derivative / NUMERICAL nonlinear nullspace exploration / OPEN uniform nonlinear phase-ball theorem. Separate UD Discovery research sandbox only.

Session: phasewindow-20261022-gpt6-7c41; task: icosahedral-phasewindow-20261022; live claim: HELD (verified); branch: discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41. Read-only integrated main at boot: 0abea764505989dde38fe0906d0d32c53d76b93c. Source-frozen case SHA256 8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd; restored original independent Jacobian/source files byte-for-byte from 015 capture.

COMPLETED: 24×180 sampled u=4 G rank24/null156; 48 normalized ± full nonlinear phases; 24 extra pure-channel ± phases; 36 mixed cancellation ± phases; 10D scalar quadratic slice; amplitude scaling at 1,1/2,1/4; five solver tolerance levels; numerical full-null scalar adjoint gradient/Hessian symmetry probe; exact model-specific local viscous displacement/velocity bilinear force expansion checked by direct full-state initial acceleration.

KEY RESULTS: mixed cancellation sector 24D generates up to5.714001e-9 even output at u4 in declared sample; fitted 10D curvature phase 1.812931e-9, half/full ratio .250000205, quarter/full .062500424; moving-axis bilinear source predicted 2.792356e-9 versus observed2.790464e-9 in initial projected acceleration. No universal nonlinear remainder bound.

FAILED/NOT COMPLETED: full156D Hessian eigenanalysis timed out. A later all-stage replay also timed out during Hessian reconstruction (initial 48-phase replay succeeded); original successful 10D run and follow-up tighter verification remain preserved. No verified continuous-time error, no u100 nonlinear ball proof.

REPRODUCE: From the checkpoint archive root with NumPy/SciPy and optional SymPy, run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python nullcurvature.py --mode screen --out .`; then `--mode hessian` and `--mode verify`; `python channel_audit.py`; `python cancellation_sector.py`; `python convergence.py`; `python hessian_adjoint.py --probe-only --out .`; `python axis_bilinear.py`; then `python audit_archive.py`. Source dependencies are under inputs/, including 015's frozen 24×180 G matrix; exact source bytes are SHA256 manifest records. Integration's `scripts/validate.py` and unittests were NOT_RUN locally (no git checkout).

HIGHEST NEXT: a validated full156D or full180D curvature-envelope operator bound, followed by continuous time and uniform material-parameter coverage. PR44 greenbounds remains owned by another held session; do not write to it. No mainline export.
