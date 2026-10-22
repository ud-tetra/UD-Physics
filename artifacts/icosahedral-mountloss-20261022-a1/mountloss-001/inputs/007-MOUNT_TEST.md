# Added mount-loss test plan v1.0 — UNSCORED / NOT_EXECUTED

This is a design addendum to the [bare-module protocol](../icosahedral-tolerances/MODULE_TEST.md). No measurement is supplied and no hardware pass is recorded. The exact proof requires the four specified anchors and current-axis, equal-opposite forces; an arbitrary housing mount does not inherit it.

## Calibration and separate objects

Keep physical module spring k_b, inerter coefficient B_b, and viscous coefficient C_b distinct from a spatial housing mass or a new strut coefficient. With the parent's calibration

\[
 t_0=\sqrt{25B_b/k_b},\quad E_*/\ell_0^2=k_b/5,
 \quad E_*t_0/\ell_0^2=\sqrt{k_bB_b},
\]

each new strut requires physical viscosity

\[
 C_h=\eta\sqrt{k_bB_b},\qquad
 \eta=\nu\frac{2\beta}{5R^2},\quad R^2=(5+\sqrt5)/8.
\]

At selected nu=.02 and nominal beta=.05, eta≈0.0004422291; C_h/C_b=2 eta≈0.0008844582 when C_b=(1/2)sqrt(k_b B_b). This small value is a calibration requirement, not evidence of fabrication feasibility. Each strut's reference length is ell0/2 or sqrt3 ell0/2, not its coefficient. Housing masses and stiffnesses must be measured separately. A dimensionless 5% housing mass fraction is not a 5% strut loss.

## Required observations

1. Measure each physical attachment point, free strut length, housing mass and mount stiffness, including uncertainty. Confirm the intended two endpoints and two adjoining-face opposite vertices per housing. Count and weigh all 120 struts, routing fixtures and anchors; the mathematical model excludes their inertia and compliance.
2. Test an individual strut's force/velocity response, off-axis force and hysteresis in both directions. Cover the primary band omega=1..4 and housing resonance near10; a proposed development sweep omega=1..12 maps to angular frequency omega/t0 in SI. Report deviations from positive real, frequency-independent viscosity rather than silently fitting them away.
3. Measure housing and all attachment reactions together. Verify zero resultant and torque within instrument uncertainty and check measured force·relative velocity against dissipated power. Route-induced torques or external grounding require an amended model with those reactions and states.
4. Prepare the saved old four-cycle housing displacement with alpha=0 and nominal zero velocities. Record full housing positions/velocities, primary response, total mechanical energy and heat estimate. Compare the u=100 ringdown fraction with the saved prediction and its calibration uncertainty. A single direction is not a test of all54 hidden modes. The saved worst phase requires controlled displacement **and velocity**; otherwise label that test NOT_EXECUTED.
5. Test a primary pulse only after a physical mechanism and calibrated preparation for internal alpha are defined. Measure mean volume, hub-relative and shell-centroid volume mismatch, absolute shell shape, housing lag, strut lengths and total momenta. Use the inherited80/5/50 development screen as an engineering target; disclose it is target-selected and not a physical law.

Record raw time series, units, calibrations, sensor positions/frames, uncertainties, exclusions, actual initial phase, component tolerances and all failed gates. Retain both original baseline and loaded assembly. Freeze an actual apparatus and acceptance rule before independent validation; simulation-generated values must never populate measured fields. The 20 numerical joint points and nominal worst-sector energy bound do not certify a continuous manufactured tolerance box.
