# G0: disk-galaxy radial acceleration entry contract v0.1

Session `cosmology-galactic-entry-20261106-01`. See [branch charter](../../docs/COSMOLOGY_BRANCH_v0.1.md). Status **OPEN_GATED**; no UD galaxy acceleration prediction or fit was produced.

## Typed target

Observed domain: resolved radial points `R>0` in rotationally supported, nearby disk galaxies. `R` has physical length units and `V_obs` has length/time units. Under circular-equilibrium interpretation, the measured kinematic acceleration is

`g_obs(R)=V_obs(R)^2/R`  [length/time²].

This is a conventional observational identity, **not** a UD derivation. Geometry, inclination, distance, asymmetric drift, beam smearing and noncircular motions enter its measurement model. Stellar and gas contributions are separate baryonic observables; stellar mass-to-light ratio is a nuisance/calibration input, not a native UD coefficient. SPARC provides published mass models; their component conventions and uncertainties must be read from the data documentation before calculating a numerical `g_bar`.

Proposed UD input type: a versioned packet/complex state `q` on a declared assembled carrier `K`, native generator `A_K` or transition law, matter/source field `b`, boundary conditions and conserved stock. Required output type: a radial mathematical observable `F_UD(q,b; r_native)` with an explicit physical map `R=ell_* r_native`, `t_phys=tau_* s` and `g_UD=(ell_*/tau_*²) F_UD`, or a different derived, dimensionally complete map. The symbols `ell_*` and `tau_*` here expose missing calibrations; assigning them to fit SPARC is FIT and cannot be promoted as a native derivation. A kinematic `g_obs` match alone does not identify a gravitational field, a metric or a mass law.

## First theorem/calculation request

Derive a source-selected `F_UD` with domain/codomain, sign, boundary and equilibrium assumptions. Check a finite central limit, large-radius asymptotic behavior, baryonic source scaling, normalization and parameter identifiability. If the source gives only a stock or event count with no force/metric/time map, record **NO-GO under that source set** for a dimensional acceleration claim. Do not tune exponents or scales to the observed radial-acceleration relation and relabel them derived.

## Data and decision gate

S1 SPARC author data https://astroweb.case.edu/SPARC/ contains 175 late-type galaxies and downloadable rotation curves/mass models. S2 published radial-acceleration relation https://astroweb.case.edu/ssm/papers/PhysRevLett_117_201101.pdf uses 153 galaxies and 2693 points for that analysis; this is a previously exposed target at the relationship level. No data rows were read or fitted here. Before confirmatory evaluation, fix a new predictor and a genuinely unused galaxy or independent dataset split, quality cuts, baseline family, uncertainties, nuisance ranges and acceptance criterion. Comparison must include conventional baryons-only and dark-matter/empirical alternatives with equal flexibility accounting. If G0 fails, stop before G2/G3.

**RESULT:** G0 source and unit map are OPEN. The entry target and failure criterion are specified; no acceleration law, galaxy fit, dark-matter alternative, or cosmological expansion result is claimed. Physical promotion 0.
