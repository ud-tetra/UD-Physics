# Is UD looking for time dilation or a matrix? v0.1

**RESULT — Different levels of one research programme.** A matrix can represent relational structure and its evolution. Time dilation is a candidate physical clock-comparison consequence, requiring additional clock, frame and readout laws. A matrix alone supplies no such identification. This analysis is Discovery development; no mainline export or physical promotion.

Base: `ud-tetra/UD-Physics@fbb21d58a7662b737e4a2fb5276fefedc547412b`. Sources are pinned to that revision unless otherwise stated. The word “matrix” is ambiguous: we examine an operator matrix, a metric matrix, and a speculative relational substrate. If the intended word was **metric**, the relevant chain is a justified spacetime metric, a clock/proper-time map, and a measured comparison. No interpretation is silently substituted for the user's wording.

## 1. Source-bound interpretation

The [designated project site](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/), inspected 4 November 2026, identifies Papers I–III 1.1.1 / IV 0.1. Its “central idea,” “architecture,” and “scientific position” distinguish the finite carrier, signed state, Hodge–Dirac evolution and independent physical bridge. The source says that the pre-event source law remains open. This is the present source statement, not an empirical constitutive law.

The [local-generator audit v1.0](../qpb1-local-generators/README.md), §§1–2, works on C0⊕C1⊕C2⊕C3 over R, dimension 15, with unit positive chain metric and ascending orientations. Its three-parameter equivariant skew family already admits rate choices. Thus “we have a matrix” does not mean “we have selected the physical generator.” The [action audit v1.0](../action-normalization-audit/README.md), §§1–3, separates a native parameter, action normalization and physical unit identification. The [clock smoke trial](../clock-map-smoke/README.md) explicitly labels its affine time labels synthetic/FIT.

Typed distinction:

| Object | Mathematical role | Further physical requirement |
| --- | --- | --- |
| Incidence/transport matrix | Relates chain coordinates | State preparation and independently measured channel map |
| Generator A | Determines x'=Ax under a declared parameter | Source-selected couplings and calibrated time/readout |
| Positive chain metric H | Defines norm, adjoints and conserved support | No inference of a Lorentzian spacetime signature |
| Lorentzian metric g, if proposed | Defines a candidate causal/proper-time structure | Derivation or explicit assumption, clock coupling and independent tests |
| Time-dilation ratio | Compares specified physical clocks | Motion/potential/frame law, signal-transfer corrections and systematics |
| “Matrix” as simulated reality | Ontological hypothesis | Distinct predictions; finite matrices alone do not establish it |

## 2. Exact toy clock analysis

Objects: V=R^4, coefficient matrices over Q, metric H=I, two oriented phase planes, autonomous continuous parameter s, all amplitudes finite. Let J=[[0,-1],[1,0]] and A=diag(J,2J). Readout: unwrapped phases of both nonzero active modes. No boundary flow, material coupling or SI clock is assumed.

For alpha>0 constant, A_alpha=alpha A gives x_alpha(s)=exp(alpha A s)x(0)=x_1(alpha s). Every frequency scales by alpha; the ratio omega2/omega1=2 stays fixed. The identity follows from the matrix-exponential power series. With s=t/t0, the physical generator would be A/t0. The transformation (A,t0)→(alpha A,alpha t0) leaves A/t0 unchanged. Thus an unconstrained common scale can reflect a unit/map ambiguity; a physically imposed change of generator relative to a fixed reference is a different experiment.

A basis change y=Sx gives B=SAS^-1 and H_y=S^-T H S^-1. This preserves the same dynamics in new coordinates and the spectrum. It differs from changing the rate. Nonorthogonal S can destroy ordinary skew-transpose appearance while preserving H_y-skewness. The accompanying exact replay checks S=diag(2,1,1,1).

For B=diag(J,3J), the ratio is 3, so B cannot be alpha A with a common scalar. It describes relative mode detuning in this fixed readout/metric model, not one shared clock rescaling. Frozen probes must actually see both modes; a hidden or unexcited mode does not supply a measured ratio.

## 3. Why slowing is insufficient for relativistic identification

**EXACT / conditional readout non-identifiability:** a phase phi(t)=omega0 tau(t), with tau(t)=r t, has exactly the same single-channel output as phi(t)=(r omega0)t. Example: omega0=2 and r=1/2 versus omega=1 and r=1. One phase trace cannot distinguish an assigned lapse from an ordinary retuned oscillator. Multiple clock species and independently specified physical motion/potential tests are needed to challenge conventional detuning, thermal shifts, loading and calibration alternatives. Common mode scaling is compatible with a shared lapse but does not prove it.

**OPEN / candidate bridge:** to investigate physical time dilation, introduce a dimensionless relational rate r and a defined model dphi_a/dt=Omega_a r for multiple clocks, where Omega_a has units rad/s and each calibration is independent. Supply a law for r from UD state/coupling/observer variables before inferring it from the desired output. If r depends on the whole dynamical state, multiplying a generator by it changes the vector field; conservation, observer dependence and clock coupling must be checked anew. Merely writing r as a familiar relativistic factor is target-informed HYPOTHESIS/FIT.

The proper-time symbols and Lorentzian metric, if used, belong to a declared spacetime branch. No positive chain norm is silently renamed a spacetime metric; no source-selected causal cone or relativistic law is derived in this toy calculation. “All processes slow together” also means relative to a declared comparison, not an absolute slowing observable to an isolated observer.

For an external experimental comparison, Bothwell et al., Nature 602, 420–424 (2022), DOI [10.1038/s41586-021-04349-7](https://doi.org/10.1038/s41586-021-04349-7), [primary preprint 2109.12238v1](https://arxiv.org/abs/2109.12238v1), abstract, reports a spatial frequency gradient consistent with gravitational redshift. The abstract and primary metadata were read; raw data and full methods were not audited. This illustrates the physical comparison observable; it supplies no UD map or score.

## 4. Answer and next discriminant

UD's current finite mathematical task is to specify which relationships, generator, state, source and observables are selected. A matrix is one representation of that task. A successful physical theory must additionally predict measured relations, potentially including time dilation. The immediate bench trajectory in this conversation concerns clock calibration and controlled phase/charge dynamics, not a demonstrated relativistic effect. The absent bench return is not a time-dilation dataset request.

**Recommended Discovery target:** define two independently prepared local clock/readout subsystems and an interaction that predicts their relative rates without fitting that rate to the answer. Test common scaling, species-specific detuning and basis/readout changes separately. Motion or gravitational comparison and universality across clock types are later, separately specified gates. Physical promotion remains 0; non-constructor review NOT_RUN.

Reproduce: `python3 experiments/clock-matrix-question/audit.py`. The exact rational controls establish only the stated finite examples; the power-series and eigenvalue-ratio arguments establish the corresponding conditional statements. Journal, receipt and immutable capture are linked in the owning session. No new value of a UD structural or physical coefficient is selected.

## Two-clock continuation

[Two tetrahedral clocks and a declared bridge](TWO_CLOCKS.md) gives exact independently prepared phase planes, unchanged rate ratio 1 and preparation-dependent hybridized modes. Reproduce with `python3 experiments/clock-matrix-question/two_clock.py`. This narrows the candidate coupling, with physical clock interpretation OPEN.

## Common-rate classification

[Common-rate couplings](COMMON_RATE.md) proves the tetrahedral equal-gain criterion, a scoped linear autonomy obstruction, and a reciprocal nonlinear action-product alternative. Replay: `python3 experiments/clock-matrix-question/common_rate.py`. The nonlinear coefficient and its local realization remain OPEN.

## Local reciprocal mediator gate

[Report v0.1](LOCAL_MEDIATOR.md), [replay](local_mediator.py), [results](local_mediator_results.json): passive Gram bound, prepared versus memory dynamics, contact isotropy. Native coefficient and physical maps OPEN.

## Incidence-local quartic classification

[Report v0.1](LOCAL_QUARTIC.md), [exact replay](local_quartic.py), [rank results](local_quartic_results.json): nearest-incidence all-state uniform quartic is zero; collective radial quartic first appears at pair distance4. Native nearest-incidence implementation PARKED under those hypotheses.

## Prepared-plane local interaction

[Report v0.1](PREPARED_PLANE.md), [exact replay](prepared_plane.py), [results](prepared_plane_results.json): positive13-term anisotropic local witness gives Omega=2+lambda I and exact invariance on selectedW. FullsignedS4 blocks this target onW; coefficient error creates transverse leakage. Native selection, stability and physical maps OPEN.

## Transverse stability and finite readout

[Report v0.1](TRANSVERSE_STABILITY.md), [exact certificate](transverse_exact.py), [numerical replay](transverse_stability.py): fixed13-termQ is weakpositive transversely unstable; explicit nonlinear one-cycle phase error<1/1000rad passes given gates. Robust-clock witness PARKED; native selection/maps OPEN.

## Positive local transverse penalties

[Report v0.1](LOCAL_STABILIZATION.md), [exact certificate](stabilization_exact.py), [numerical replay](local_stabilization.py):14positiveincidencepenalties retainOmega andeta1givesexactweaktransverselinearstability. Larger testedcouplings fail;nonlinearstability/nativecoefficientsOPEN.

## Explicit coupling and readout certificate

[Report v0.1](CERTIFIED_INTERVAL.md), [exact replay](certified_interval.py), [results](certified_interval_results.json):mu<=2^-30 gives all-time normal linear gain64; modified-model finite nonlinear phaseerror<1/1000 under stated gates. Conservative interval; physical calibration and nonlinear all-time stability OPEN.

[Fourier/Cayley interval certificate](FOURIER_INTERVAL.md) extends the exact conditional interval through mu=1/64 with linear normal gain at most 8.

[First transverse loss certificate](STABILITY_BOUNDARY.md) gives a unique first linear stability threshold in (77511/12500,62009/10000) for fixed eta=1.

[Near-threshold gain and growth](NEAR_THRESHOLD.md) gives rational bounds on transient gain below onset and exponential growth above it.

[Finite nonlinear preparation margin](NONLINEAR_MARGIN.md) gives an explicit one-unit state and phase error budget below the threshold.

[Direct propagation and split preparation gates](ANISOTROPIC_MARGIN.md) tightens the one-unit phase contract.

[Routing-budget clock test](ROUTING_CLOCK_TEST.md) separates native stock exchange from the proposed motion overhead and rejects the square-root law for the stock-fraction and affine-action readouts tested.

[Periodic clock embedding](PERIODIC_CLOCK.md) gives the exact direct-embedding leakage and independent spatial spread test.

[Directional packet](DIRECTIONAL_PACKET.md) tests scalar transport and a co-moving carrier phase on two periodic grids.

[Separate internal phase null](INTERNAL_PHASE_NULL.md) defines a matched moving/reference comparison and a readout sensitivity control.

[Fixed Laplacian coupling](LAPLACIAN_CLOCK.md) tests spectral detuning against the matched reference and tracks both reference lobes.

[Equal-frequency packet comparison](ISOSPECTRAL_CLOCK.md) compares distinct centroid speeds at fixed spectral loading.

[Edge-class clock](EDGE_CLASS_CLOCK.md) separates local incidence detuning from a speed-only law.

[Incidence transport current](INCIDENCE_CURRENT.md) derives signed stock flux and tests the stationary and matched moving controls.

[Local current clock](LOCAL_CURRENT_CLOCK.md) tests stationary, matched-frequency, and counterpropagating controls for a passive rate rule.

[Tracked current-clock phase](TRACKED_CURRENT_CLOCK.md) integrates the site clocks through packet dispersion and counterflow overlap.
