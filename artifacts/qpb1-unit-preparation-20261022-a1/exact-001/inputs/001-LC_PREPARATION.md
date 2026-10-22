# Ideal LC preparation and map-consistency protocol v0.1

**PROPOSED / NOT EXECUTED / UNSCORED — development, no registry entry.**

Purpose: operationally define a reproducible classical reference preparation and test whether one fixed native-to-oscillator map retains support and action consistently across amplitude interventions. This protocol alone does not test the universal QPB1 action ratio.

## Entry requirements

Identify a named single-mode apparatus and its actual accessible state variables. Supply the mode-reduction argument, equations, loading and parasitic model, loss treatment, preparation isolation, observable map and applicable operating domain. An ideal two-state LC model is an assumption until these are supported. A multi-node Stage0 network cannot silently be replaced by this single-mode carrier.

Freeze C, angular-frequency omega and reference precharge V_ref calibration procedures and full dependency receipts. Choose V_ref without using the candidate action ratio, a desired hbar match or a previous measured ratio. State whether this is an external control convention or an independently sourced physical preparation law. Traceability through SI or quantum standards must be disclosed separately from target dependence. No apparatus, safe operating range or supported uncertainty is supplied by this theoretical protocol.

Define the reference as zero initial current/flux and capacitor charge C*V_ref. Document residual current, switch energy, injected noise, losses and uncertainty. If preparation/control consumes a reference or record, include it in the physical boundary rather than identifying the isolated model with the whole apparatus. Supply non-constructor review before any registry advancement under the source governance proposal; this document claims none.

## Frozen map and controls

Use Phi_ref=V_ref/omega, Phi=Phi_ref*X and Q_ch=-C*omega*Phi_ref*Y. Keep that same map in all preparations. Reference support is1; the planned voltage ratios1/2,1,2,3 give supports1/4,1,4,9 under the ideal map. These ratios are development controls chosen for this protocol, not source-derived UD constants or physical observations.

Read capacitor voltage and inductor current, with orientation, clock and channel calibration recorded. Reconstruct flux/charge and the complete winding history; an endpoint alone cannot recover loop action. Compare the measured canonical closed-loop integral with pi*a*J_ref, where J_ref=C*V_ref^2/omega. Corrected nonclosed/damped histories require a separately justified action estimator; do not silently use the ideal closed-orbit formula.

The ideal prediction is quadratic voltage scaling at fixed C,omega. Failure first challenges the apparatus/model/map within its frozen domain. Agreement validates analogue bookkeeping within its uncertainty; it supplies no unique physical identity. Do not renormalize every preparation to support1 and then treat its unadjusted physical action as the same unit scale.

## Reduction and comparison boundaries

For positive calibration intervals use [C_L*V_L^2/omega_U,C_U*V_U^2/omega_L]. Record covariance, repeatability, drift and model-error coverage. An independent work/energy measurement may cross-check2E_ref/omega only after shared dependencies are disclosed. Energy calculated from the same C,V records is not independent.

Freeze the reduced packet before any hbar comparison. A QPB1 comparison remains inadmissible as an independent physical-unit test until a separate source rule identifies this reference preparation with source A0. If that rule chooses V_ref from the candidate itself, disclose FIT/circularity rather than an independent test. No precision, threshold or acceptance result is asserted here; those await a supported apparatus contract.

## Missing inputs

Named apparatus, measured mode map, raw preparation/readout data, full calibration/uncertainty packet, native-to-physical unit-selection rule and non-constructor review are absent. The symbolic circuit parameters and rational examples in audit.py are synthetic mathematical inputs. Hardware status stays NOT_EXECUTED; empirical status stays UNSCORED.
