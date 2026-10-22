# Icosahedral ordinary passive damping — v1.0

Status: EXACT/CONDITIONAL model identities; NUMERICAL design envelope. This extends the [free3D model](../icosahedral-free3d/README.md) at source revision c7d832c25b5b822572c1a82e0ef93b583cf1a4f0. It adds a declared mechanical loss law. Native UD constitutive selection, physical calibration and material realization remain OPEN.

## State, strains and loss law

Retain40 configuration coordinates x=(alpha,C,X_1,...,X_12), positive mass matrix M, and the parent potential. In reference-edge units a=1, R²=(5+sqrt5)/8, s_i=|X_i-C|/R-1 and e_ij=|X_i-X_j|-1. The internal scalar alpha changes preferred radius; it is distinct from displacement of C. The shell has30 edges and20 faces. All13 spatial points remain free.

Add independent central axial dashpots with uniform nonnegative coefficients c_s,c_e:

R_loss = (c_s sum_i sdot_i² + c_e sum_edges edot_ij²)/2,

M xddot + grad U + partial R_loss/partial xdot =0.

Spoke loss acts on actual radial strain, not on s_i-alpha and not on a difference of different spokes. Each spatial damper has equal/opposite forces along its present line. This is a geometrically defined passive force model; no new anchors or guides are imposed. It still depends on the parent's assumed internal preferred-radius mechanism.

The mechanical energy balance is exactly E'=-2R_loss<=0. Total spatial linear and angular momenta remain conserved. A dissipated-energy accumulator models bookkeeping for heat; bath degrees of freedom are not resolved. Units: u=t/t0, energies E_*, positions ell0. The physical dashpot coefficient is E_* t0 c_s/R_phys² on a spoke and E_* t0 c_e/a_phys² on an edge; the conversion scales remain unspecified.

## Exact collective cost and soft deformation

For default properties g=1,k=2/5,unit inertias, the invariant homothetic manifold remains C=0, X_i=(1+b)r_i. Its equations are

alpha''+13alpha-12b=0,

b''+(c_s+5c_e/2)b'+3b-alpha=0.

The collective mass is diag(1,12). Here R_loss=(6c_s+15c_e)b'². Thus nonnegative independent ordinary dashpots protect nontrivial common breathing identically only when c_s=c_e=0. This obstruction concerns these loss channels; it does not forbid a separately realized multiport loss mechanism.

With d=c_s+5c_e/2, the collective pole polynomial is r⁴+d r³+16r²+13d r+27. For weak d, the low/high collective amplitude-decay rates are

d*(1+5/sqrt37)/4+O(d²), and d*(1-5/sqrt37)/4+O(d²).

These are small-loss asymptotics, not bounds at arbitrary coefficients. The two collective frequency squares at zero loss remain8±sqrt37.

An exact Q(sqrt5) calculation finds rank(K-lambda_s M)=35 for lambda_s=(5+sqrt5)/20. Appending all12 radial-strain rows and the alpha row leaves rank35. The entire five-dimensional soft eigenspace therefore has zero alpha and zero first-order radial strain. On it Be^T Be=R² M, giving

z''+c_e R² z'+lambda_s z=0.

Radial dashpots cannot damp this family directly at equilibrium. In the underdamped range c_e<2sqrt(lambda_s)/R², its complex modal envelope is exp(-c_e R² u/2). This refers to a modal pole, not an induced energy-norm bound, arbitrary initial displacement envelope or finite-amplitude stability theorem. Weak edge loss damps the low collective mode faster than this soft mode: its coefficient exceeds5/8, whereas the soft coefficient (5+sqrt5)/16 is below1/2. The high collective mode is less strongly damped.

## Certified amplitude domain

For the initial preparation alpha=A0, reference positions, and all velocities zero, E(0)=(1+sum g_i)A0²/2. With every g_i in[19/20,21/20], every k_ij in[19/50,21/50], and any positive masses,

|s_i|<=sqrt(68/5)|A0|,

|e_ij|<=sqrt(680/19)|A0|.

For any nonnegative spoke/edge loss, the strict bound |A0|<sqrt(19/680)≈0.167156 keeps every radial and ordinary edge length positive for all time. This is a length-domain certificate derived from positive energy. It does not certify cell orientation, convexity, small deformation, coherence or suppression of parametric growth. The A0=1/5 probes below exceed this certificate and have only finite numerical support. These bounds also apply to zero loss.

## Numerical envelope and reproducibility

[PROTOCOL.md](PROTOCOL.md) defines target exposure and the selected80% breathing-retention/50% soft-envelope screen. Thresholds, coefficient grid, amplitudes and property probes are engineering choices. No physical observations were fitted. Previously exposed ±5% sample7 is deliberately reused; two new deterministic property points are development probes.

Run:

```bash
OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-damping/analyze.py --out /tmp/icosa-damping
python3 experiments/icosahedral-damping/bounds.py --out /tmp/icosa-damping
python3 experiments/icosahedral-damping/draw.py --source /tmp/icosa-damping --out /tmp/icosa-damping/damping-summary.png
```

The coefficient grid has3 spoke choices {0,1/200,1/50} and121 edge choices j/1000 for j=0..120, for363 points. Its symmetric trajectory uses the exact invariant subsystem, numerically evaluated by eigendecomposition. Full3D tests use DOP853,2001 samples on u0..100, rtol1e-10,atol1e-12; the selected refinement uses4001 samples,rtol2e-12,atol2e-14. Separate checks use an independently assembled strain Jacobian, force power, exact ranks, full3D collective reduction and a matrix exponential.

The nonlinear campaign has36 property/amplitude/loss points:3 property realizations × A0 in{1/40,1/10,1/5} ×4 loss settings. There are12 additional symmetric full3D checks. Damped readouts are normalized against their own matched undamped preparation. Absolute shell-shape RMS removes translation, proper rotation and uniform scale. Moving-hub cell volumes and volumes recentered at the shell-vertex mean are separate readouts. Decaying common signal can increase normalized mismatch even while absolute shape error declines.

See [RESULTS.md](RESULTS.md), the [candidate](../../candidates/icosahedral-damping/candidate.json), [receipt](../../candidates/icosahedral-damping/mathematical_receipt.json), and [immutable run](../../artifacts/icosahedral-damping-20261022-a1/damping-001/manifest.json). The scan is finite; failure of this screen is not a theorem that every passive design or every continuous coefficient fails. Central-damper loss is model-realizable as a force law; no physical prototype or native UD identification was tested.
