# Multiport tests and development history — v1.0

**RESULT — The readout-selected passive network preserves ideal symmetric breathing and passes9/9 declared finite nonlinear screens.** It assumes reciprocal differential transmissions; hardware implementation remains untested. The initial pole-selected design failed and remains preserved.

## Exact/conditional results

- 150 local comparison branches add150 finite inertial coordinates:190 total configurations/380 phase variables. Every geometric endpoint reaction is included in the port model.
- Exact input-derivative rank32; kernel equals six rigid motions plus alpha and uniform scale. Auxiliary forces vanish exactly for symmetric homothety with zero initial auxiliary state.
- Total energy obeys Eprime=-(gamma/10)||zdot||². Linear and angular spatial momenta are conserved.
- All32 transverse primary coordinates plus150 auxiliaries decay asymptotically in the default symmetric equilibrium linearization, for any positive branch parameters. Collective oscillators remain undamped. This does not establish global nonlinear attraction or exclude finite-amplitude parametric effects.
- The previous all-time positive-length energy certificate |A0|<sqrt(19/680) survives. It is distinct from orientation and coherence.

## Exposed design phases

Phase A chose the best minimum transverse pole decay among27 triples. Its fastest design(mu,kappa,gamma)=(1/5,2,1/2) has minimum decay0.169523, but imperfect collective motion keeps exciting deformation. Phase B was declared afterward in the amendment and selected directly on the complete linearized volume pulse, reusing the same exposed properties. Its27-point grid selected(2,50,5), whose minimum transverse pole decay is0.0825214. Slower worst pole decay can accompany a better volume readout under continued collective excitation.

| Full nonlinear result, u0..100 | Phase A: pole-selected | Phase B: readout-selected |
| --- | ---: | ---: |
| Declared preparations | 9 | 9 |
| Passed80% RMS /5% mismatch /50% shape screen | 0/9 | 9/9 |
| Minimum matched mean-volume RMS retained | 94.684% | 99.764% |
| Maximum hub-relative normalized volume mismatch | 17.366% | 0.5784% |
| Maximum shell-centroid normalized volume mismatch | 5.9255% | 0.5299% |
| Absolute shell-shape RMS remaining, range | 44.87–58.66% | 4.018–7.782% |
| Maximum matched hub-offset RMS remaining | 105.08% | 5.174% |

Nine preparations mean three stored ±5% property realizations at each of A0=.025,.1,.2. These are not nine independent validation datasets. Both phases use exposed development data, with no statistical confidence or continuous-box guarantee. The54 parameter evaluations include one repeated triple;53 triples are distinct. No original failed result was replaced.

Mean-volume retention compares each damped point to its own matched undamped preparation. Some values slightly exceed100% because energy can shift from nonuniform motion into the measured mean signal; this is an observable ratio, not energy amplification. Total energy remains nonincreasing.

The normalized volume mismatch is sqrt(integral||P20 y||²/integral||y||²), y_k=V_k/V_k0-1. Shell-shape RMS removes translation, proper rotation and common scale. Hub-relative cell-volume partition and shell-centroid partition remain separate readouts. The minimum sampled Phase B cell volume is0.90456 of reference; supporting halfspaces pass at sampled output times. A0=.2 exceeds the all-time length certificate, so that preparation has only finite numerical support.

## Transmission-ratio sensitivity

Uniform mechanical properties;A0=.1;one fixed seeded direction of reciprocal ratio errors. Ratio error is applied to both forward difference and returned force, retaining passivity. These are separate tests from the material-disorder campaign; no joint tolerance claim follows.

| Phase B ratio-error range | Mean-volume RMS retained | Hub-relative volume mismatch | Total energy remaining at u100 |
| --- | ---: | ---: | ---: |
| Ideal difference | Analytically unchanged | Analytically zero | Analytically100% |
| Within±0.1% | 99.9973% | 0.0120% | 99.9955% |
| Within±1% | 99.7268% | 0.1197% | 99.5548% |

Exact cancellation is lost with ratio error: on uniform breathing each branch output is -delta*b. Loss is therefore possible even with fully reciprocal/passive components. These two finite probes quantify sensitivity; they do not establish a worst-case error bound.

## Verification

- Integer connectivity, exact Laplacian annihilation and moments for both pair graphs; Q(sqrt5) combined derivative rank32 and explicit independent eight-vector kernel.
- Separate endpoint-force/Jacobian assembly, energy directional derivative, force power, zero net force and zero net torque checks pass. Residuals are preserved in summary.json.
- Three amplitudes per phase reproduce the original analytic collective orbit; maximum Phase B coordinate error3.35e-9. Auxiliary activation is below1e-10 in these symmetric integrations.
- Phase B linear active-auxiliary reduction agrees with the unreduced380-phase equations to1.19e-14; geometric volume derivative agrees with finite differences to1.88e-10.
- Maximum Phase B E+D relative residual1.93e-8 over the nonlinear/symmetric/ratio checks. Maximum P/L drifts2.76e-15 /4.07e-15 in internal units.
- Refining the worst Phase B volume mismatch changes it by3.24e-8, with refined energy-balance residual1.05e-10. Phase A's corresponding mismatch change is1.45e-6.
- Force/velocity impedance retains finite mu,kappa and has strictly positive real part. Its high-frequency response differs from a projected dashpot; phaseA/B curves are preserved.

All are constructor calculations with alternative implementation checks, not independent empirical replication. CI validates repository integrity rather than these physical assumptions.

![Finite nonlinear probes and auxiliary impedance](../../artifacts/icosahedral-multiport-20261022-a1/multiport-001/files/multiport-summary.png)

## Remaining discriminant

Derive a joint tolerance budget for transmission-ratio errors, finite housing/routing mass and parasitic common-port loss, then specify a measurable module test. The150-branch symmetric layout is also a complexity cost; a sparse realization preserving the exact kernel could reduce it, but would need a new response and symmetry audit. No native UD variable law, calibrated time/energy scale, material selection or spacetime identification has been established.
