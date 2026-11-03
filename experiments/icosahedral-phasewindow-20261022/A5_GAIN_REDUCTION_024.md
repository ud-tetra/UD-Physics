# A5 reduced moving-pulse gain and conditional continuous-time gate — 024

**RESULT — EXACT / CONDITIONAL (representation and interpolation identities); NUMERICAL / DEVELOPMENT (full u100 gain screen). Continuous-time validated gates and full nonlinear u100 remain OPEN.**

## Question and source

Investigate whether the original alpha(0)=0.1 symmetric uniform-parameter 3D heart pulse, beta=.005, nu=.05, cf=0, E_h <= 51/20000000, meets the selected g(node)<=1/10000 and v(u)<=1/1000 first-order all-180-phase design gates. The mechanical source is the unchanged six files pinned by Git blobs in SOURCE_LEDGER_024.json at read-only main f0f6b707b77467f28c8e3892384fa0e8b28a4869. The held task and sandbox branch are separately named there. Time u and edge length are normalized, with no physical clock calibration. Source, target thresholds and A5 selection have already been exposed; none is a holdout physical prediction.

## Typed maps and exact symmetry structure

Let q in R^280 be the full mechanical configuration, y=(q,qdot) in R^560 the full tangent state, and a in R^180 an energy-normalized initial housing position/velocity preparation with ||a||<=1. Baseline q_b(u) is the exact symmetric invariant family (unperturbed housing phases), with all struts positive at all future times by checkpoint019's conditional energy theorem. The linear tangent generator is J(u)=Df(q_b(u),qdot_b(u)), the readout is the rank24 non-affine shell projection C: R^560 -> R^24, and C_v is its derivative/velocity extraction. Let B: R^180 -> R^560 be the initial energy-orthonormal injection and eps=sqrt(2Eh). Then L(u)=eps C Phi(u,0)B, D(u)=L'(u)=eps C_v Phi(u,0)B, A(u)=D'(u).

For the proper icosahedral group A5 with 60 operations, the model's reference and constitutive forces commute with its real orthogonal action T(g), including signed auxiliary difference transmissions. The irreducible non-affine output is 3 + 3' + 2(4) + 2(5). For an output unit seed e in a single d-dimensional irreducible copy, define the rank-one matrix coefficient projector on configuration coordinates:

    Q_(rho,e) = (d/60) sum_{g in A5} <e,U_rho(g)e> T_q(g).

Real representation Schur orthogonality shows this is an orthogonal projector onto one multiplicity slice of the isotypic sector. The same slice works for aligned duplicate output copies. Its numerical ranks on R^280 are 17,14,18,22 for rho=3,3',4,5; each tangent evolution is restricted to 2r=34,28,36,44 coordinates (4 reduced forward fundamental matrices). The six seed rows and 2x2 Gram blocks recover the complete 180-input operator norm. This is EXACT as an algebraic reduction under the model symmetries, with numerical projector construction errors, not a native physical law.

The local matrix construction checks idempotence within 3.34e-16, seed embedding within 1.19e-15, and discarded-space leakage of K,C within 7.07e-14 for the five tested times (0,1,4,30,100). These are NUMERICAL implementation checks, not interval proofs.

## Numerical calculation and new peak correction

Each small full-state multiplicity-space fundamental matrix is integrated *forward once* along the source-matched six-scalar moving baseline. At grid h=0.025, assemble the reduced moving Jacobians directly from the original source equations at 4001 coefficient times, interpolate with SciPy cubic splines, solve forward with DOP853 at requested rtol1e-11, and evaluate full phase-ball induced norms g(u)=||L(u)||_2, v(u)=||D(u)||_2, w(u)=||A(u)||_2 at all 4001 times. Exact group reconstructs the norm from six output seed channels; **no sampling of input housing directions** is used in these induced-norm evaluations.

Sampled maximum g(u)=6.674200417854993e-5 at u=4.65; sampled maximum v(u)=0.000608074566464554 at u=4.70; sampled maximum w(u)=0.0061443485181751 at u=4.55. The g peak exceeds the previous post-selected u=4.04 sample (6.638579048e-5). Continuous true maxima are not proved. At u=100, the forward reduced gain is approximately 4.280838880992824e-6, matching the reduced backward adjoint 4.28083887121974e-6 with 9.8e-15 absolute spread for that same spline approximation. Older independent full 560-state selected-phase forward checks from checkpoint023 agreed within the reported 0.0202% relative at u100.

Coefficient interpolation h=0.05 vs 0.025 at shared observation times changes g,v,w maxima entrywise by at most roughly 2.03e-13, 1.19e-12, 1.08e-11, respectively. This numerical grid convergence is NOT a rigorous absolute error bound. The sampled source-assembled Jacobian-versus-spline entrywise defect at h=.025 is roughly 1.97e-6 (K block), 2.13e-8 (C block), also NOT a supremum bound. DOP853 tolerances are requested errors, not validated global enclosure; cubic spline values are not exact source coefficients between grid points.

A correction of the standalone short-T replay script was made BEFORE packaging: output node times are now clipped to the integration end T. An early T=6 smoke test erroneously queried values beyond the integration range (spline extrapolation); its resulting huge values were invalid and discarded. Corrected T=6 test samples valid times and reproduces the u4.65 gain.

## Exact conditional double-interpolation theorem (NOT certified premises)

Mesh t_j=j/40, j=0,...,4000, with nearest-node distance 1/80. Suppose all three *true* inequalities have been rigorously verified:

  (G) all nodes g(t_j)<=1/10000,
  (V) all nodes v(t_j)<=13/20000,
  (W) all continuous times w(u)<=1/100.

By the fundamental theorem of calculus applied to the full operator maps, v(u)<=13/20000+(1/80)*(1/100)=31/40000 (<1/1000). Then g(u)<=1/10000+(1/80)*(31/40000)=351/3200000=0.0001096875. This leaves exactly 79649/3200000=0.0248903125 below the 1/40 flat-cell-exclusion threshold for baseline and nonlinear remainder. The symmetric reference Z is identically zero. All arithmetic is independently checked using Python Fraction in exact_gain_gate.py.

All three numerical sample columns pass the chosen gate values, with max g~0.000066742<.0001, max v~.000608075<.00065, and max sampled w~.00614435<.01. The last condition is an ALL-TIME acceleration sup and is NOT established by sampled w; nor are node gains verified with validated numerical error. This theorem is therefore EXACT / CONDITIONAL; **it is not a validated first-order envelope for the original moving ODE**. A naive fixed-equilibrium log-norm test was tried but had too-large integrated positive growth (and an indefinite potential metric in the 3 sector for small regularizer). It does not provide a usable a posteriori enclosure.

If, additionally, an independently certified uniform nonlinear phase-ball remainder stays below 79649/3200000 and all 120 housing struts remain positive, the prior rank-three flat-cell theorem would guarantee oriented cell positivity through u100 for the uniform symmetric original pulse. That nonlinear/strut premise remains OPEN; breathing and ringdown criteria remain separate.

## Validation still missing and next discriminant

Need (1) validated enclosure of the six-dimensional moving reference through u100; (2) interval or defect-controlled enclosures of coefficient interpolation and four small multiplicity-space fundamental matrices including propagated error; (3) machine-rational/interval evaluation of g,v at all 4001 mesh nodes; (4) a certified continuous w(u) bound <=1/100, not just samples. Then (5) a separate nonlinear/relative housing-position bootstrap; and later (6) material scatter. Preserve earlier failures and PR44's separately held source recovery untouched. No mainline promotion or physical calibration is inferred.
