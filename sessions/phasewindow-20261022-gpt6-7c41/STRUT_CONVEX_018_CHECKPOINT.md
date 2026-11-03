# Discovery checkpoint — strut-convex-018

Session `phasewindow-20261022-gpt6-7c41`; task `icosahedral-phasewindow-20261022`, claim held. Read-only model source imported from main `5fd737fda4dadd6f1cc3d9c3c6c086473b7f72bb`, five original mechanical blobs matched previously verified `4aaf0a39d24328e27bc425e333e3612baea888a5`.

**EXACT / CONDITIONAL:** For original heart pulse alpha(0)=1/10 and all 180 housing phases at E_h<=51/20000000, all qualified coefficients, the 120 moving struts remain >1/2500 throughout u<=1019/1000. Every spoke and outer edge stays positive, and all same-time convex interpolations between admitted phase trajectories have spoke lengths >17487/50000 (>1/3), outer edge lengths >22487/50000 (>2/5), struts >1/2500. The 560-phase nonlinear mechanical ODE therefore continues through that horizon.

**EXACT / CONDITIONAL:** For per-path viscous force f(d,w)=eta dd^T w/|d|^2, certified Ddd/Ddw coefficients are 22775/18 and 5/18 to u=1; 45550/9 and 5/9 to u=1.01; 4555000/9 and 50/9 to u=1.019. These are **force** Hessian bounds, not solution-flow Hessian or validated u100 response bounds.

**Executed locally:** Python 3 exact Fraction replay and independent SymPy/mpmath/NumPy constructor checks PASS. Immutable complete local ZIP (2 input scripts, 5 captured outputs, manifest) SHA256 `0c050cfbc54c10d6838c3e8d4b69a68cf4d91b4feea3cda49e4ab246fed65c1c`; unpacked replay reproduced output JSON. The complete executable capture is local only; GitHub contains this checkpoint and the proof but not an entire schema-2 captured run. Do not claim repo CI validates the mathematical proof.

**Limitations:** Oriented cell positivity remains proven only through u=49/50. All-180 nonlinear response, u100 strut continuity, breathing/RMS/mismatch/ringdown, physical mapping and calibration OPEN. Current crude Hessian majorants become very large near u=1.019. No mainline export; PR44 greenbounds claim separately held and untouched.

[Detailed theorem and calculations](../../experiments/icosahedral-phasewindow-20261022/STRUT_CONVEX_TUBE.md).

**Next discriminant, priority 99/100:** A time-dependent projected Green/propagator plus trajectory-domain nonlinear bootstrap; prioritize substantive u100 progress rather than further tiny changes to the finite horizon.
