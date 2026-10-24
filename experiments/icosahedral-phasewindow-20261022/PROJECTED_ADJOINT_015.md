# Full-180 source-matched projected adjoint — checkpoint 015

**RESULT: NUMERICAL / DEVELOPMENT / CONDITIONAL; full nonlinear u100 certificate OPEN.**

Session `phasewindow-20261022-gpt6-7c41`, live held claim `claims/icosahedral-phasewindow-20261022`, parent model from integrated `ud-tetra/UD-Physics`. Verified current main `53460195f74411ce764b24e0ab9d4fd772c4bd6f`; six consequential original mechanical source blob SHAs unchanged. No mainline promotion, modification of PR44 ownership, or physical experiment.

## Defined model, source, and units

Frozen integrated coefficient case `edge-p1-b0.005-cf0.0`, source revision `1e6e0f2abe3fa234919c5a6701547883a807b3e5`, canonical source-coefficient SHA256 `8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd`. Its original 13 primary masses, 12 spoke strengths, 30 edge strengths, 150 gain errors, 30 housing mass weights and c_f=0 are retained. This differs from the synthetic scattered case in checkpoint 013. Passive housing strength nu=.05, beta=.005, alpha(0)=.1. Original expanded housing initial energy E_h=2.430311755526067e-6. All 180 initial housing displacement and velocity phase directions are included, with Euclidean normalized energy B^T G B=I. Reference 3D geometry is over Q(sqrt5), time u, length ell0 and energy internal, physical calibration OPEN.

Full nonlinear reference y_ref(u) follows the unchanged 280-position, 560-phase ODE with 120 current-axis viscous links. The 24-component readout C y is an orthonormal coordinate representation of Z=(I-P0-PV)Y on the rank-8 nonaffine vertex sector times xyz. No rigid mechanical coordinate or kinetic energy is discarded.

## Efficient full-phase derivative method

For J(u)=Df(y_ref(u)), at each target time t*, integrate 24 adjoint columns backward:

```
Lambda'(u)=-J(u)^T Lambda(u),  Lambda(t*)=C^T
G(t*)=Lambda(0)^T B                       # 24x180
epsilon=sqrt(2E_h)
sup_{||a||2<=1} ||epsilon G a||=epsilon*sigma_max(G)
||Z_ref(t*)+epsilon G a|| <= ||Z_ref||+epsilon*sigma_max(G).
```

A separate 24-dimensional scaled trust-region secular equation computes the pointwise exact maximum of the *approximate linearized map*. It is a finite-dimensional numerical optimization, not verified interval integration. The sparse full-state Jacobian includes current-axis damping position derivatives, spring prestress, reciprocal device and housing reactions and all original masses.

## Numerical results (selected instants, not continuous-time supremum)

Twelve target times were u=1,2,3,4,5,6,8,10,20,40,70,100. Seven **post-exposure** near-peak targets u=3.25,3.5,3.75,4,4.25,4.5,4.75 were also inspected. Across these 18 distinct instants the largest conservative baseline-plus-linearized-housing triangle bound is **0.0004356646896 at u=4**, or1.743% of the earlier exact/conditional 1/40 orientation threshold. The pointwise maximized combined first-order value at u=4 is **0.00040492925498**. At u=100 the triangle result is **0.00017286147**, with a tighter-adjoint repeat **0.00017286156**. No uninspected times are enclosed.

At u=4 four independently forward-propagated tangent phase directions agree with the 24-output adjoint to relative 1.88e-8. At u=100 four forward tangent comparisons give max absolute error1.59e-8 and relative6.18e-5, reflecting smaller late-time outputs; this is disclosed numerical error, not a mathematical error enclosure. Independently assembled moving-state force JVP and sparse Jacobian agree within3e-13 at the checked state. Earlier 180-forward-column source-matched attempt had TIMED OUT; replacing its cost is the method's principal practical result.

## Full nonlinear validation — distinctly narrower than phase-ball result

The full u0..100 nonlinear solver was run for the u4 largest singular-vector phase, its negative, and the half-amplitude signs. Across these five trajectories including reference, maximum sampled ||Z||=0.0003805824863; maximum sampled vector Taylor remainder for full phase=1.68264874085e-8, half amplitude=4.20622829205e-9, ratio0.2499766. Minimum sampled positive strut0.4913437; relative E+heat balance worst5.24e-11 and spatial P/L drift <1.4e-14. Separately, the u4 **combined-optimal first-order phase** yields actual finite ||Z(4)||=0.00040492956585 versus linear optimum0.00040492925498, vector error2.376e-9. This selected finite check does NOT imply a uniform nonlinear remainder bound.

## Failure/correction, source exposure and reproduction

An initial pointwise trust-region root solver used an insufficient absolute tolerance relative to an O(1e-9) squared gain, giving a phase norm >1. This numerical solution was rejected. The corrected secular equation normalizes lambda by the largest singular value squared, enforces phase norm1 and checks the quadratic dual gap; the quoted u4 combined optimum is the corrected value.

All time samples, threshold1/40, E_h factor3/2 and source case were development data. The near-peak search was chosen after seeing u4. No genuinely unused validation set or independent physical replication exists. No continuous-time gain enclosure, continuous qualified property box, uniform finite nonlinear R180 remainder, full560 forced Green bound, or u100 nonlinear orientation/coherence theorem is claimed.

**Reproduction**: local immutable `projected-adjoint-015` checkpoint ZIP includes 12 original source files, 33 outputs, 12 saved 24x180 gain matrices, seven local probes, both selected finite-replay traces, SHA256 manifest and mathematical receipt. The archive SHA256 is `8a270616332dd8860fff1ba9e807dcdb94344651a40c1bf9ec0eb59a90911342`. Main sequence: `python adjoint_gain.py --out full --times 1,2,3,4,5,6,8,10,20,40,70,100 --check --adj-rtol 1e-8`; `python finite_validation.py --folder full --tstar 4 --T 100 --samples 401`; `python verify_015.py`; `python combined_phase_validation.py`. Use OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.

**NEXT 98/100**: develop validated continuous-time projected tangent gain together with an all-phase nonlinear remainder in a positive full-state/frame-aware norm for this frozen case; then extend to continuous tolerance box. PR44's separately claimed Green recovery is a parallel dependency.
