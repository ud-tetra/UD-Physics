# Reproduce UD non-affine null curvature 016

Requires Python 3.13, NumPy 2.3.5, SciPy 1.17 (exact versions from constructor environment), optional SymPy. No network access required. `inputs/` preserves six sources and the prior 015 24x180 G NPZ at the exact source bytes used.

From this directory:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python nullcurvature.py --mode screen --out .
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python nullcurvature.py --mode hessian --out .
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python nullcurvature.py --mode verify --out .
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python channel_audit.py --out .
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python cancellation_sector.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python convergence.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python hessian_adjoint.py --probe-only --out .
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python axis_bilinear.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_archive.py
```

The `--mode hessian` reconstruction completed once in the constructor runtime and saved `null_hessian_slice.json`; a later all-stages replay exceeded the runtime budget after successfully completing the 48-phase screen. These are **run histories**, not evidence of model failure. A full 156D eigenspectral Hessian run without `--probe-only` was attempted and timed out; its result is NOT CLAIMED. `audit_archive.py` verifies captured bytes, not dynamical or mathematical truth. The source case SHA-256 is `8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd`.
