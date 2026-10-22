# Proposed module test — v1.0

**Physical status: UNSCORED / NOT_EXECUTED.** This is a measurable test of the assumed mechanical comparison module and declared housing model. No physical hardware, empirical fit or UD correspondence is claimed. The numerical assembly probes do not substitute for this test.

## Device and calibration

Start with one edge-comparison module:two independently driven axial extension inputs,a reciprocal differential transmission,and the finite series-spring/parallel-inerter-damper branch. Measure both input forces and displacements,relative internal stroke z,and housing displacement. Use independent input excitations and force/displacement calibration. Record device topology,reference terminal directions,signs,component values,travel limits,friction/backlash and uncertainty.

Use power-conjugate coordinates

$$u_c=(y_a+y_b)/2,\quad u_d=y_a-y_b,\qquad f_c=f_a+f_b,\quad f_d=(f_a-f_b)/2.$$

Power is f_c*u_c_dot+f_d*u_d_dot. Do not compare force channels with unmatched factors of2. Forward difference and force return must use the same transmission ratio. A nonreciprocal controller is outside the candidate family.

For physical edge extensions x=ell0*y,the dimensionless force/velocity matrix is Z=Z_phys*ell0²/(E_*t0). Physical angular frequency maps as omega=omega_phys*t0. The corresponding radial module requires the fixed input length normalization R_phys and its reciprocal force conversion; do not silently use edge-extension units for radial strain.

Calibrate the branch independently,not from the desired coherence result. With physical spring stiffness k_b and inertance B_b,nominal dimensionless kappa50 andmu2 imply

$$t_0=\sqrt{25B_b/k_b},\qquad E_*/\ell_0^2=k_b/5.$$

Nominal gamma5 then requires C_b=0.5*sqrt(k_b B_b) for the viscous element. These calibrations define this engineered model's units; they do not derive a UD-native clock or energy scale. Record whether measured component response supports these constants over the full band; frequency-dependent ratios,backlash or nonlinear losses require a revised model.

## Input runs and readouts

1. **Component run:** independently estimate k_b,B_b,C_b and uncertainty;fit the declared spring/inerter/damper response,report residuals and alternate explanations. Keep calibration data separate from the acceptance run.
2. **Ratio and reciprocity:** sweep two independent inputs,estimate delta and its force-return counterpart. Reverse the module's input ordering and excitation signs. Record preload,stroke range and preparation. The candidate assumes |delta|<=.01 and reciprocal return.
3. **Common drive:** y_a=y_b. Estimate Z_cc=f_c/u_c_dot and Z_dc=f_d/u_c_dot from complex sinusoidal phasors.
4. **Differential drive:** y_a=-y_b,so u_d=2y_a. Estimate Z_cd=f_c/u_d_dot and Z_dd=f_d/u_d_dot. Test Z_cd=Z_dc within the declared uncertainty.
5. **Band:** test calibrated omega in[1,4],including endpoints and both unloaded collective frequencies sqrt(8±sqrt37). Choose and record the full frequency list before acceptance data. Convert to hertz as f=omega/(2*pi*t0);no numerical Hz target is available before calibration. Include transient settling and repeated preparations;do not treat one favorable frequency as a band result.
6. **Housing run:** measure total housing/routing mass relative to nominal shell mass. Add the declared flexible midpoint-mount test piece and measure its resonance. Proposed nominal beta<=.05,Omega_h=10;the exact symmetric frequency bound applies for uniform mounts withOmega_h>=10. The joint simulation usedOmega_h exactly10 andmatched mass/stiffness scatter;arbitrary mount-frequency variation is not certified. Physical midpoint pickup and casing modes must be documented rather than assumed equivalent.
7. **Energy check:** record input work and returned work;include identified stored spring/inerter/housing energy. Look for unexplained sources or sinks. A lossless housing contribution is conservative;unexplained housing loss belongs in the common-loss budget or a new constitutive model.

## Model-derived gates and uncertainty

For the bare module,mu2/kappa50/gamma5,|delta|<=.01 and0<=c_f<=.001,exact continuous-band bounds give

| Quantity | Bound in normalized port units |
| --- | ---: |
| Re Z_cc | <=1349/3620000 ≈0.000372652 |
| Re Z_dd | >=39601/74528 ≈0.531357 |
| Re Z_cc / Re Z_dd | <=3141821/4479863125 ≈0.000701321 |
| Cross-impedance ratio, absolute values | <=2/199 ≈0.0100503 |

These are diagonal dissipative impedance and cross-impedance bounds,not tetrahedral volume-mismatch bounds. The matrix model is

$$Z_{\rm port}=Z(s)vv^T+\frac{c_f}{10}\operatorname{diag}(2,1/2),\quad v=(-\delta,1+\delta/2),$$
$$Z(s)=5\frac{2s+5}{2s^2+5s+50}.$$

Use upper uncertainty bounds for upper-limit gates and lower uncertainty bounds for lower-limit gates. Predeclare the uncertainty method/coverage. As a chosen resolution goal,common-loss uncertainty should be no larger than one fifth of its upper-limit gate;otherwise report INCONCLUSIVE. Check passivity from the Hermitian part of the measured matrix and its uncertainty. Finite frequency samples do not prove a band inequality without a validated interpolation/model-error bound.

Estimate c_f from the common real response after accounting for delta² Re Z. A housing mount may add an identified conservative impedance;it must not be subtracted as arbitrary fit freedom. Independent damping or frequency-dependent friction requires an amended physical model. Preserve negative results and calibration residuals.

## Assembly follow-up

The whole-assembly80%breathing-RMS/5%volume-mismatch/50%shape screen remains a separate test using20 cell-volume readouts and the declared preparation alpha=.1,reference points,zero initial velocities. Measure the actual equivalents of alpha,preferred-radius coupling and readout before claiming implementation of the full model. The present20 joint simulations are finite development probes,not a guarantee for every module passing the table.

Save:raw calibrated signals,component/ratio estimates,uncertainty,excitation phases,frequency list,mount geometry and mass,preload/temperature where relevant,model residuals,analysis code and declared decision. Mark unperformed rows NOT_RUN. Current physical acceptance remains UNSCORED.

## Added housing-mode gate

A subsequent exact check found54 undamped internal modes in the conservative midpoint-mount model. They are absent from the declared zero-housing-deviation preparation. Add an independent housing-displacement readout and a housing-only perturbation/ringdown test; volume coherence alone cannot detect this sector. Current model predicts persistent housing oscillation atOmega_h,with cancelling primary reactions. Full mechanical relaxation is therefore a FAILED model property until an explicitly passive mount-loss mechanism is supplied and tested. The bare-module impedance gates remain separately testable. See [mount-mode addendum](MOUNT_MODE_ADDENDUM.md).
