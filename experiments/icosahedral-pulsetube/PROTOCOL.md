# Moving-pulse sensitivity and tube attempt v1.0

Base378ecad7c8d8fc96c4d8abf55cd0ca5330ea5adc. Development after exposure to prior joint-window/nonlinear-domain results. No model, housing energy, parameter window or pass threshold changes.

1. Derive the complete560-state Jacobian, including geometric spring prestress, reciprocal device terms, all mount reactions, moving-axis damping derivatives and housing return forces. Check directional derivatives independently against the original nonlinear ODE before using it.
2. Follow the zero-housing-perturbation alpha=.1 pulse, with180 initial housing position/velocity tangent coordinates normalized to unit energy norm. Retain spatial rigid motion and its kinetic energy. Start with the exposed worst breathing case seed10422-0-boundary2 atnu=.05, and the uniform beta=.05/c_f=0 case atnu=.05.
3. Compute the time-integrated mean-volume derivative Gram and cross term. Solve its energy-ball trust-region minimum, rather than substituting the worst housing-ringdown phase. Measure sampled strut and cell-volume derivative norms. These are first derivatives of the nonlinear flow, not a finite-amplitude certificate.
4. Evaluate the adverse breathing phase and its negative at E_h=E_p/40000, then the adverse phase at quarter energy. Compare the nonlinear trajectory with the first-order prediction and retain second-order residuals. Recompute one variational campaign at tighter tolerances/resolution. No new random search or phase retuning after these choices.
5. Derive an a posteriori nonlinear tube criterion that explicitly includes the full forced Green operator, nonlinear Taylor remainder, numerical reference defect, initial error, readout remainder and positive-length margin. Fill only quantities actually bounded. If those quantities do not close the prescribed finite-energy ball, retain OPEN and identify the missing bound. Never use sampled tangent gains or amplitude scaling as uniform Hessian/flow-error certification.

Numerics: DOP853, initial planned rtol2e-9/atol2e-11 for tangent entries, stricter reference-state weights; output every.1u. Original ODE point checks use2e-11/2e-14 on4001points. Refinement uses5e-10/5e-12 and.05u. Algebra is exact over real variables with Q(sqrt5) reference geometry. Internal continuous time/length/energy are uncalibrated. No modular or prime-factor mechanism is assumed. All work is constructor analysis; no delegated or independent review.

## Diagnostic amendment after normal tangent campaign

The fine repeat also records sampled primary-position operator norms, cell singular values and mean-volume gradient norms, to quantify the allowed nonlinear flow-remainder budget. These diagnostics do not change dynamics or phase optimization. The original executed normal source is captured. The root solver's nearzero-multiplier norm calculation now uses stable BLAS norm to avoid intermediate square overflow; solved phases/results are checked by the existing norm and KKT residual criteria.

## Post-exposure frame diagnostic amendment

The raw primary-position determinant budget failed after the first fine repeat: its linear radius0.03500972 already consumes more than the80% breathing margin. Add one repeat of the same fine tangent ODE with readout-only proper-frame projection diagnostics, and one finite phase chosen as the leading final raw-primary tangent singular vector. These diagnose unobservable frame motion; they do not replace the full mechanical state or retune the adverse phases, coefficients, energy or threshold. The reference/tangent repeat is checked for exact elementwise equality. No uniform aligned nonlinear remainder is inferred.
