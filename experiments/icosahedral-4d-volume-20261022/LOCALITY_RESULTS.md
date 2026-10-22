# Locality, reciprocity and rotational symmetry: 3D null for the 4D icosahedral apex

**Session:** `icosa4dvol-20261022-gpt6-c7d2`  
**Task:** `icosahedral-4d-volume-20261022`  
**Verified prior research branch:** `1bc9f2d450bde6deb85f0b05dd31109795ef2b76`  
**Integrated base:** `92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa`  
**Evidence:** EXACT / CONDITIONAL / NUMERICAL / FAILED as unique 4D discriminator.

## Question and scope

Can a local, reciprocal, SO(3)-equivariant 3D mechanical network reproduce the nonzero **linear** 4D apex-to-shell-breathing response with all unconstrained point coordinates free? Preserve the previous **exact nonlinear** 3D guided-linkage equivalence as a separate baseline. No native UD selection rule, spacetime time coordinate, empirical calibration, or physical prototype is asserted.

## Restricted 13-point 3D symmetry obstruction (EXACT / CONDITIONAL)

Let a regular icosahedral shell have symmetric homothetic scale `s` (trivial representation of proper icosahedral rotations) and only one central point with displacement `u in R^3` (standard vector representation). If a smooth potential is invariant under the proper icosahedral group and the equilibrium has full icosahedral symmetry, then its mixed Hessian `d²U/(ds du)` is an invariant covector of that 3D representation. There is no nonzero vector fixed by all proper icosahedral rotations, hence **the mixed Hessian vanishes**. This no-go applies to a centre-only 3D model with no additional scalar inner mode. It is not a universal 3D obstruction.

## Constructive all-pairwise 3D counterexample

Use two concentric icosahedra: 12 outer points `p_i=s X_i`, 12 inner points `q_i=b X_i`, with `|X_i|²=r²=(5+sqrt(5))/8`, outer edge length 1, inner reference radius factor `b0=1/4`, and `b=b0-gamma(z-eta)` with `gamma=1/5`, `eta=sqrt((3-sqrt(5))/8)`. Every vertex moves freely in R³ in the **full network**; `(s,z)` is only its invariant collective sector.

Connect 30 outer-shell edges, 30 inner-shell edges, 12 matching radial spokes, and 60 nearest-neighbour cross braces (both directions per one of 30 icosahedral edges). Each is a finite-length pairwise Hookean spring with local force `k(ell-ell0)*direction`, its own positive stiffness, and zero reference extension. No prescribed guides, nonlocal transmissions, three- or six-body constraints are used. The total potential is a sum of nonnegative pairwise spring energies, invariant under rigid translations and rotations SO(3), and exactly conserves total linear and angular momentum when unforced. The reference shape has icosahedral point symmetry, not full SO(3) configuration symmetry.

At the symmetric sector the complete reduced 3D potential is

`U3=15 ke(s-1)^2 + 15 ki(b-b0)^2 + 6 ks*r²[(s-b)-(1-b0)]² + 30 kc[sqrt(r²(s-b)²+s*b)-sqrt(r²(1-b0)²+b0)]²`.

The 4D target (previous session) is

`U4=6[sqrt(r²*s²+z²)-1]² + 15(s-1)²`, with `K4=[[12 r^4+30, 12 r² eta],[12 r² eta,12 eta²]]` and `M4=diag(12r²,1)`.

For `gamma=1/5, b0=1/4, kc=1/20`, choose positive spoke, outer, inner stiffnesses to solve **exactly** the three independent Hessian entries. The exact expressions and derivation are in `locality_audit.py`; fitted numerical values are in `results.json`. Choose each inner vertex mass `mi=1/(12r² gamma²)` and every outer vertex mass 1. This also matches the 2x2 mass metric. These parameters are **FIT to the previous 4D target**, not native or measured quantities. There are additional free choices (`gamma`, `b0`, `kc`), so the construction is not unique; `kc` has a nontrivial positive interval of admissible values near the selected 1/20.

## Mechanical stability beyond the two-coordinate reduction

There are 24 free 3D nodes = 72 configuration coordinates and 132 pairwise springs. The weighted spring-length Jacobian has **rank 66** and exactly **six rigid zero modes** (NUMERICAL SVD; EXACT structural certificate follows). Each convex triangulated icosahedral shell is infinitesimally rigid (30 independent edge constraints each). After quotienting common rigid motion, relative translation `t` and rotation `omega` remain. The twelve matching radial springs impose `X_i dot t=0` for all `i`, hence `t=0`. An adjacent cross brace imposes a multiple of `(X_i cross X_j) dot omega=0`; three actual adjacent-edge cross products (edges `(0,1)`, `(0,2)`, `(1,2)` in the published ordering) have exact determinant `(7+3 sqrt(5))/32 !=0`, hence `omega=0`. So the two rigid shells have no internal first-order mechanism. All springs are stress free, thus quadratic stiffness is positive modulo rigid motions. This is local equilibrium stability, not global finite-amplitude attraction.

The symmetric two-coordinate sector is dynamically invariant at linear order, with exact `K3=K4`, exact `M3=M4`, and residual below `7e-16` for the numerical embedding. Both normal frequencies are `0.886724725` and `2.007002196`; the entire linear transfer from a symmetric inner radial drive to exterior volume is identical. There are nevertheless **64 further nonrigid modes outside this two-mode sector** in the 3D network (vs 32 in the full 40-coordinate 4D model).

## Nonlinear and nonuniform discriminants (NUMERICAL, model-relative)

The cubic derivative `d³U/dz³` of the selected local pairwise 3D model differs from the 4D model by `-10.04770570446` in unit normalization, despite equality at Hessian order. Under a Gaussian apex/internal generalized force with amplitude +0.08, peak fractional shell-volume change is `3.523392%` in 4D versus `4.121657%` in the local pairwise 3D system (finite example, identical reduced mass and damping). Its maximum pointwise signed fractional-volume trajectory difference over `t in [0,70]` is `2.324292%` (not the peak difference). The earlier **guided** 3D two-coordinate analogue continues to reproduce the 4D nonlinear dynamics at **all orders**; this new difference does not supersede that result.

For a net-force/torque-balanced local shell drive, the total linearized volume amplitude agrees at all tested frequencies due to the matched trivial symmetry sector; a local shell compliance does not. At `omega=0.3`, the frequency-domain local shell compliance magnitude is `0.52721` (4D) versus `1.08710` (3D pairwise), with the same unit-normalized forcing and `C=0.06 M`. The 3D network has additional low-frequency modes around `0.24332` and `0.46328`. These differences are **discriminants among these specified models**, not a universal geometric proof of four dimensions. Additional 3D constitutive choices can alter them.

## Target exposure and interpretation limits

- Target selection: previous 4D equal-edge geometry and its 2x2 `K, M` were exposed before constructing the 3D network. Four positive material values were solved to match them; `gamma=1/5`, `b0=1/4`, `kc=1/20` were additionally chosen; no held-out physical dataset was used.
- Baselines: prior exact guided 3D nonlinear analogue (preserved); restricted 13-point 3D centre-only model (symmetry obstruction); the new 24-node pairwise network (linear equivalence, nonlinear differences).
- All 3D spring forces are pairwise reciprocal and exactly rotation-equivariant. Spring crossings, component volume, manufacturing feasibility, tolerance robustness and higher-mode damping are **not** established.
- No physical metric signature, Lorentzian dynamics, quantum field map, measured energy scale, native UD constitutive selection or causal explanation follows from the result.

## Reproduction and checkpoint

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 locality_audit.py` from this directory with Python + NumPy, SciPy, SymPy. The script writes `results.json`, `pulse_curves.csv` and prints checks for exact symbolic identities, full Jacobian rank, invariance, force/torque conservation, numerical static solves and pulse ODE. Finite values use floating-point 64-bit NumPy, SVD rank threshold `1e-9`, DOP853 relative tolerance `1e-10` and absolute `1e-12`. Constructor self-checks passed. Independent scientific replication/physical experiment not performed.

Checkpoint next: constrain component/node counts and fabrication complexity, test nonuniform shell-drive spectra under a frozen null family, and isolate a physically motivated UD rule that removes added scalar 3D modes. No automatic writeback to mainline.
