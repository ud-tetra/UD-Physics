# Joint tolerance study protocol v1.0

Development at source4ddf692. Previous PhaseB(mu,kappa,gamma)=(2,50,5), geometry and3 property points are exposed. Do not retune the device parameters in this study. Targets below are engineering choices, not native UD coefficients or measured hardware properties.

## Defined hardware model

Retain the150 finite difference branches. Add reciprocal ratio errors delta per branch, and parasitic axial viscosity c_f/10 at each of its two input ports. All input ports act on the actual member strains before the transmission; no fixed-ground friction is introduced. Incidence degrees give effective radial and edge viscosities c_s=c_f/2,c_e=4c_f/5. Common breathing damping coefficient is5c_f/2.

Add30 independent3D housing points H_e near edge midpoints M_e=(X_i+X_j)/2. Housing masses m_he have total12beta in the parent's point-mass units. Their potential is sum(k_he/2)||H_e-M_e||², with k_he=(m_he/R²)*Omega_h². The midpoint pickup and isotropic zero-rest vector spring are an ideal attachment model, not an arbitrary real casing. Include endpoint reactions, housing kinetic energy and momentum; do not infer a bound for unmodeled gear,shaft or casing modes. Extra90 spatial coordinates give280 configurations/560 phase variables.

## Proposed budget and calculations

- Ratio errors |delta|<=1/100; beta<=1/20 of the original twelve-shell-point total mass; c_f<=1/1000; uniform mount frequency Omega_h=10. For joint probes allow housing mass weights within±10% of their mean,with exact total mass preserved. Original primary masses/spokes/edge springs range±5%. Initial alpha=.1,reference geometry,zero velocities and auxiliary states. Time windowu0..100.
- Derive the exact reciprocal common/differential2-by2 module impedance, passive balances and continuous-band1<=omega<=4 bounds. Use force/velocity impedance and power-conjugate coordinates. Module bounds do not certify whole-assembly coherence.
- Derive the ideal uniformly loaded three-coordinate collective subsystem and a conservative frequency-downshift bound for its two low modes with Omega_h>=10,beta<=.05. This symmetry-specific bound does not cover arbitrary nonuniform housing placements.
- Joint full560-phase probes:12 boundary cases (3 stored exposed primary-property sets ×4 ratio directions:all+,all-,alternating,seededRademacher). All at beta=.05,c_f=.001 and ratio magnitude.01; four deterministic housing mass patterns span±10% and preserve total mass.
-8 interior cases generated from seed90247: fresh deterministic primary properties within±5%,ratio components within±.01,beta in[.005,.05],c_f in[0,.001],housing-weight variation<=10%,Omega_h10. These are development probes,not independent predictive validation or confidence samples.
-4 challenges using the previously exposed worst primary set: ratio3%;housing mass20%;friction c_f=.02;or mount frequency4. Change only the named budget factor relative to the declared boundary setting. Preserve failures and do not expand the proposed budget silently.
- Screens:mean-volume RMS>=80% of each matching original undamped/no-housing preparation,hub-relative volume mismatch<=5%,absolute shell-shape RMS<=50% of that same baseline. Compute fresh no-housing undamped baselines for the8 new property points; use stored baselines for the3 exposed points. Reference denominators therefore include housing costs. Also report ideal loaded symmetric RMS and frequency shifts separately.
- Verify4 symmetric loaded cases against the reduced3-coordinate equations:beta=.05/Omega10 with c_f0 and.001;beta=.2/Omega10/c_f0;beta=.05/Omega4/c_f0. Check force gradients,power,E+D and total primary+housing P,L. Primary momentum alone can exchange with the housings.
- Refine the largest hub mismatch among the20 in-budget probes with4001 samples and tighter tolerances. Keep sampled orientation/halfspace checks distinct from all-time certificates. Produce a module-test protocol with explicit calibrations,uncertainty and UNSCORED physical acceptance.
