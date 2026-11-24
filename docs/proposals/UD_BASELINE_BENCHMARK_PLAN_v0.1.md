# UD Computational Benchmark Contract v0.1 — Proposed

**PROTOCOL ONLY — no measured benchmark run, no physical promotion.**

## Objective
Test whether particular UD discrete operators or data representations provide a measurable computational advantage over conventional finite-element, discrete exterior calculus and finite-volume baselines on identical, well-posed computational problems.

## Frozen starter problems
1. **Single tetrahedron / 1→4 refinement:** exact differential/coboundary nilpotency, Whitney (k=0,1,2,3) field restriction, mass-metric norm preservation. Null: established Whitney FEEC transfer under identical mesh and geometry. Avoid credit for identities already inherent to the null.
2. **Local conservative evolution:** skew-adjoint incidence or Whitney-metric generator with prescribed initial/boundary conditions and analytic matrix exponential or high-precision solution as a reference. Compare discrete-time integrators fairly at matched tolerance. Measure quadratic-stock drift, error versus reference, memory, and runtime.
3. **Static boundary response:** tetrahedral 0/1 incidence Laplacian before/after a fixed interior vertex; compare exact boundary Schur complement (4\to5) under unit edge weights to conventional weighted graph FEM/finite-volume solution. Explicitly flag this as a model result, not observed material behavior.

## Report requirements
Prespecify for each run: mesh coordinates/topology and orientation; state dimension; metric/coefficient conventions; initial/boundary data; unit normalization; tolerance; source revision and executable command; hardware and software environment; baseline and identical inputs; runtime, peak memory, conservation/energy error, convergence with refinement/time step, and any code-generation/rendering advantage. Report null, failures, parameter scans and search freedom. Repeat with at least one non-centroid geometry to test robustness.

## Interpretive restrictions
Exact algebraic agreement is not evidence that UD is more accurate or faster than standard FEEC: it may simply reproduce the baseline mathematics. Computational novelty must come from an explicit improved method, complexity, stability, adaptive state selection, parallel architecture or predictive readout. A comparison without matched tolerances and identical tasks is not a benchmark.

## Gates
- **G0:** reproducible exact small cases and committed scripts.
- **G1:** independently reproduced numerical trajectories and tolerances.
- **G2:** stable performance/generalization over held-out meshes/initial states.
- **G3:** optional physical bridge with calibrated independent observables; never implied by G0–G2.

**Next:** implement test matrix and baseline scripts on an isolated claimed research task. **Current status:** NOT_RUN; protocol source candidate only. Physical Promotion=0.
