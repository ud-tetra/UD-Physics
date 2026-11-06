# Cosmological Branch — scope and first gate v0.1

2026-11-06. UD-Physics Discovery charter. Session `cosmology-galactic-entry-20261106-01`; integrated base `45020742a9332445888b39847cb1e2e2903a3f23`. Development status; physical promotion 0. No mainline UD result is amended.

## Purpose and scope

Investigate astronomical and cosmological phenomena through explicit UD dynamics and independently testable physical maps. The name **Cosmological Branch** is an umbrella. Nearby disk-galaxy dynamics is an astrophysical entry experiment; it does not itself derive cosmic expansion, FRW dynamics, dark energy, or a global spacetime metric.

Separate four layers in every proposal: (1) native UD carrier and evolution; (2) mathematical observable; (3) calibrated map with physical units; (4) astronomical measurement and conventional null. A relation at layer 4 cannot be reverse-engineered into layer 1 and called native. Prior historical coefficients, including C02 `185/192` and conditional Q119 `4/3` in the supplied ledger v0.39(2), have no authorized galaxy acceleration interpretation. The current source layer and any amendment must be verified before use.

## Target selection

| Frontier | Available observation | Missing UD dependency | Entry verdict |
| --- | --- | --- | --- |
| Rotationally supported disk galaxies | SPARC has 175 nearby late-type galaxies, 3.6 μm photometry, H I/Hα rotation curves and Newtonian baryonic mass-model downloads [S1,S2]. | Native matter/source profile, radial force/metric map, physical length and time units, equilibrium/readout. | **First target:** one scalar radial acceleration profile; clear units and baselines. |
| Stellar types and color–magnitude populations | Gaia DR3 astrometry, photometry, spectra and stellar classifications [S3]. | Energy generation, radiative transport, opacity, hydrostatic stellar evolution, population selection. | Later: a joint stellar-dynamics/thermodynamics program. |
| Ionized nebulae | PHANGS-MUSE DR1.1 gives 30,790 reliable nebulae in 19 galaxies with emission lines and environments [S4]. | Ionization, chemistry, radiation, gas hydrodynamics, dust and feedback. | Later: morphology or spectroscopy after a material/radiative bridge. |

These rankings are judgments about dependencies and discriminating information, not evidence of UD fit or quantified closure.

## Work lanes

1. **G0 — typed source and units.** Select a versioned UD carrier, state, generator, conserved quantities, boundary conditions, matter/burden source and mathematical radial readout. Supply an explicit map to length and time or keep the branch OPEN_GATED. Verify source provenance and avoid a target-selected acceleration scale.
2. **G1 — equilibrium response.** Derive a radial acceleration or circular-speed profile from G0 without looking at target velocity points. Test sign, dimensionality, finite core/outer limit, mass scaling, symmetry, conservation and noncircular/pressure-support assumptions. If no force/metric law exists, report that obstruction and stop physical scoring.
3. **G2 — measurement protocol.** Freeze galaxy quality cuts, inclinations/distances, gas and stellar mass-model conventions, nuisance parameters, uncertainty/covariance, null models, held-out split and acceptance rule before the held-out velocities are exposed. SPARC's published radial-acceleration relation is already known at the relationship level; do not call a fit to its public points target-blind.
4. **G3 — held-out comparison.** Compare a fixed UD predictor with baryons-only Newtonian and established dark-matter or empirical acceleration baselines using the same data and nuisance treatment. Report posterior/predictive residuals, complexity, failures and uncertainty. Only a separate bridge test can promote a specific correspondence.

The candidate folders `stellar-populations/`, `nebular-dynamics/`, and `expansion-history/` are reserved conceptual lanes, not claims of completed work. Begin them only when their source dependencies become concrete.

## Sources and exposure

- **S1:** Lelli, McGaugh & Schombert, *SPARC: Mass Models for 175 Disk Galaxies*, AJ 152, 157 (2016), DOI 10.3847/0004-6256/152/6/157; author database https://astroweb.case.edu/SPARC/ . Sample and mass-model description read 2026-11-06. No raw velocity table ingested in this session.
- **S2:** McGaugh, Lelli & Schombert, *Radial Acceleration Relation in Rotationally Supported Galaxies*, PRL 117, 201101 (2016), DOI 10.1103/PhysRevLett.117.201101; author PDF https://astroweb.case.edu/ssm/papers/PhysRevLett_117_201101.pdf . The published relation and its use of `g_obs=V²/R` are known to this session; future fits to it are exploratory.
- **S3:** ESA/DPAC, *Gaia DR3 Documentation* release 1.3 (2023), https://gea.esac.esa.int/archive/documentation/GDR3/ .
- **S4:** ESO, *PHANGS-MUSE Nebula Catalog* DR1.1 (2025), https://www.eso.org/qi/catalog/show/436 .
- **UD source:** `ud-tetra/UD-Physics@4502074`, `state/CURRENT.md` and mathematical method v1.0; supplied historical `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, C02/Q119. These provide governance and historical context, not a native galaxy force law.

Independent astronomical review NOT_RUN. All physical promotion remains 0.
