# Checkpoint 024 — Reduced A5 forward fundamental and conditional gate

- Research session: phasewindow-20261022-gpt6-7c41; live claim: claims/icosahedral-phasewindow-20261022 held.
- Isolated branch: discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41; previous head e9eff380c1e3c129d042e5d40c7790c6930fd4a3.
- Read-only main tested: f0f6b707b77467f28c8e3892384fa0e8b28a4869; six original mechanical blobs unchanged from imported source.
- COMPLETED: exact algebraic A5 slice derivation; numerical four-slice constructor at times0,1,4,30,100; reduced forward fundamental through u100; 4001-point numerical g/v/w scan, two coefficient-grid convergence tests, off-grid spline defect samples, independent reduced backward-adjoint u100 check, exact rational conditional double interpolation checker.
- CORRECTION: prior post-selected g(4.04) sample was not the highest sampled time; new u4.65 sampled g=6.674200417854993e-5. Short-horizon output extrapolation in new script was found and corrected before checkpoint assembly.
- FAILED: unreduced full matrix reassembly inside tight reduced adjoint at u100 timed out; common static Lyapunov norm attempt did not yield a usable global enclosure.
- OPEN: validated original source ODE nodal and continuum gain inequalities, interpolation/ODE error enclosures, nonlinear u100 phase-ball response and all-strut lengths; robustness to coefficient scatter, calibrated physical time/energy, hardware and UD primitive linkage.
- CAPTURE: local ZIP with source, code, data and SHA-256 run manifest. Only requested owned-path repository source/report/receipt should be imported; do not claim complete GitHub raw CSV capture unless it is actually uploaded.
- Next step priority 99/100: error-certified reduced fundamental / baseline integration with enclosures for proposed g,v,w gates; then nonlinear housing-relative bootstrap. PR44 remains separately held; no mainline writeback.
