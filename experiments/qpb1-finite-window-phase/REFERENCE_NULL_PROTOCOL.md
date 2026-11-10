# Phase-005: independently monitored reference and path-bypass null protocol

**RESULT — EXACT / CONDITIONAL and NUMERICAL synthetic controls.** Common reference drift is removable by a measured reference; a path-matched bypass null can additionally remove matched differential drift. **FAILED physical identification:** an unmatched signal-minus-null phase remains observationally confounded with a new physical phase. A conventional three-frequency interferometer reproduces the UD three-sector overlap exactly. No hardware has been assembled or measured.

## Provenance, typed model and target exposure

Task \`qpb1-finite-window-phase-20261023\`, session \`qpb1-finwindow-20261023-gpt6-b6f2\`; this phase-005 run starts from branch head \`63c4f997b68563460b54af73b04105b3f15ab687\` and inherits the original local-generator and continuous-phase source at integrated \`41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb\`. The active chain state lies in a 14D real Euclidean J-complex carrier with \`H=I\`, oriented ascending simplices, sector projectors Pk, and assumed linear local generator \`G=sum gk Kk\`. The phase model is \`Z(T)=sum rk exp(i 2gkT)\` with nonnegative normalized weights and native dimensionless time; physical clock \`t_phys=tau0*T\` and actual coupling to optical beams are **OPEN**. The earlier \`-1\` nominal geometric phase, selected \`0.01\`-radian target, \`0.001\`-rad receiver error and \`phase-003\` calibration budget were already target-exposed. New null error \`1e-4\`, unmatched drift limit \`5e-4\`, and design thresholds are **FIT / target-informed engineering assumptions**, not measured performance.

## Operational design and estimators

Use three concurrently timestamped phase-stepped readout channels under a nominal shared phase reference \(\theta(T)\):

- **S** (signal through assumed UD-like carrier): \`S=Z(T) exp(i[theta+delta_s])+e_s\`.
- **R** (independent coherent reference monitor): \`R=exp(i theta)+e_r\`.
- **N** (same-path bypass or sham/null traversal, without the modeled evolution): \`N=exp(i[theta+delta_n])+e_n\`.

Phase-step the four analyzer values \(\beta=0,\pi/2,\pi,3\pi/2\), with equalized arm amplitude and explicit detector-bias calibration. From complex channel estimates and the independently estimated dynamical phase \(\widehat D\), compute \(\Phi_R=\arg(S/R)-\widehat D\), \(\Phi_N=\arg(S/N)-\widehat D\), and the diagnostic \(C=\arg(N/R)\). In the noiseless model, \(\Phi_R=\Phi_{\rm native}+\delta_s\) and \(\Phi_N=\Phi_{\rm native}+\delta_s-\delta_n\), while \(C=\delta_n\), modulo \(2\pi\). These are **exact algebraic identities** for nonzero overlap and their declared phase branch, not an observed instrument mechanism.

The null traverse must be designed to share every significant optical/reference disturbance with S *except* the hypothesized native evolution. Swapping the source arm between S and bypass changes geometry and may introduce new differential drift; path matching and phase-reference transfer require **independent engineering verification**. R detects global/common phase; N tests common *path* phase. Calibrate the phase-003 positive-time \(D\) probes separately in the same coherent phase frame; the new main-window null does **not** automatically repair prior short-time calibration drift.

## A controlled experimental sequence (future, NOT EXECUTED)

1. **Freeze and prerecord** hardware layout, native-to-laboratory time map \(\tau_0\), analyzer-step calibration, sign convention, channel gains, acceptance limits, noise model, and a conventional multi-tone null. Do not tune a threshold using the blinded evaluation data.
2. **Sham / no-source run:** bypass the purported UD interaction in S while preserving the three-channel paths. Check that \(C=\arg(N/R)\) accounts for systematic reference motion and that \(\Phi_N\) is null within its independently established uncertainty.
3. **Common-mode injection:** introduce known, independently logged \(\pm0.002\) rad phase shifts upstream of S, R and N; verify \(\Phi_N\) and \(\Phi_R\) are invariant, while the independent reference monitor detects the step.
4. **Matched differential injection:** impose known \(\pm0.002\) rad on both S and N but not R. Verify that \(\Phi_R\) shows the injected bias, \(C\) detects it and \(\Phi_N\) cancels it.
5. **Unmatched differential challenge:** impose \(+0.002\) rad on S alone with \(\delta_n=0\). The correct outcome is **failure of the null cancellation**: \(\Phi_N\) retains a 0.002-rad bias with unchanged visibility. This is a negative control and an identifiability limit, not permission to absorb the deviation as a UD effect.
6. **Randomized, held-out runs:** independently randomize source-on/bypass, injection sign, arm swap, pulse delay, gain preparation and analyzer ordering; keep raw four-step channel statistics, reference timestamps, null residuals, detector counts and flags. Evaluate a model frozen *before* seeing these results.
7. **Discrimination gate:** fit a conventional three-tone model and compare signed held-out residuals under identical noise, state preparation and reference controls. Since the existing UD model yields **exactly the same \(Z(T)\)** for matched frequencies and sector weights, this gate cannot pass without a *new* physically specified UD-specific constitutive or coupling prediction.

## Exact uncertainty composition and statistical scope

Assume the **entire phase-003** dynamical-calibration and main signal-receiver error contract remains valid (in particular its coherent short-time \(D\) measurements), with previous worst-case phase error
\[
B_{\rm prev}=\frac{534794619424186500609612131837359}{65106126461057096943360000000000000}
\approx 0.008214198086935355.
\]
If a separately certified null complex-error magnitude satisfies \(|e_n|\le\eta_n=10^{-4}\) and a separately certified signal-to-null drift mismatch satisfies \(|\delta_s-\delta_n|\le\xi=5\times10^{-4}\) radians, then for an ideal unit-modulus null reference
\[
|\arg(N)-(\theta+\delta_n)|\le\frac{\eta_n}{1-\eta_n}=\frac1{9999},
\]
so the extended conditional bound is
\[
B_{\rm new}=B_{\rm prev}+\frac1{2000}+\frac1{9999}
\approx0.008814208087935455<0.01
\]
radians. This is a **deterministic conditional** budget. A separate ideal IID Bernoulli model gives \(\Pr(\text{one of both monitor errors}>10^{-4})\le16e^{-m(10^{-4})^2/4}\). With \(m=3\times10^9\) events per each of 8 monitor/analyzer settings, this probability is \(<0.01\), since the rational partial Taylor sum through order 11 of \(e^{15/2}\) exceeds 1600. Total **24 billion ideal monitor events** is a *sufficient*, not minimal, sample budget; it does **not** include previously required short-time calibration photon counts or certify a combined end-to-end 99% probability. No UD physical detector or event rate is established.

The all-state phase certificate is conditional on the original phase-003 state preparation radius; the random weight perturbations in the synthetic check were **not** separately certified to lie in that radius. The synthetic tests check the three-channel algebra and noise inequality for those sampled weights, not the original full preparation contract.

## Synthetic tests, counterexamples and baseline

Reproduce: \`python3 experiments/qpb1-finite-window-phase/null_protocol.py --out /tmp/qpb-null.json\`.

The standard-library constructor runs five explicitly labeled scenarios with 1,024 seeded samples each (5,120 total). Gain errors cover \(\pm0.01\), native-window errors \(\pm0.01\), and receiver/noise vectors of 0.001 signal and 0.0001 null modulus. Recorded sampled minimum \(|Z|=0.9931327589489719\). Common-drift correction, matched-bypass cancellation and error envelopes pass; the mismatched \(0.002\)-rad injection persists as designed. Every sampled conventional three-frequency baseline readout matches the UD-model \(Z\) **exactly as a computation**, and analytically it does so for every time and preparation because \(\omega_k=2g_k\) and identical weights produce the same characteristic sum. With identical noise laws, the statistical likelihoods are also identical. This is an **EXACT / CONDITIONAL observational-equivalence obstruction** for this restricted model family, not a no-go theorem against all UD extensions.

See the [immutable phase-005 SHA-256 manifest](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-005/manifest.json) and the owning session receipt. Earlier phase-001 through phase-004 artifacts are unchanged.

## Conventional source evidence and remaining work

Reference subtraction and limits from non-common-mode noise are conventional in heterodyne interferometry: Hechenblaikner, *JOSA A* 30 (2013), 941–947, https://pubmed.ncbi.nlm.nih.gov/23695326/. Phase-step calibration and mechanical drift are documented in Schwider, *Applied Optics* 28 (1989), 3889–3892, https://doi.org/10.1364/AO.28.003889. These sources explain **instrument controls**, not a UD mechanism or attained detector precision.

**Evidence boundary:** EXACT / CONDITIONAL algebra and NUMERICAL same-constructor synthetic checking; measured photon statistics **NOT_EXECUTED**, independently confirmed path-matching **NOT_EXECUTED**, non-constructor mathematical review **NOT_RUN**, physical/native clock selection **OPEN**, mainline promotion **0**. The phase readout remains **observationally equivalent to a conventional multi-tone null** until a genuinely discriminating dynamic/source law is specified.

**Next priority 99/100:** derive one constrained, source-justified UD-specific response, symmetry or scaling residual that is absent from the three-tone null, then freeze it for experimental comparison. A supporting independent workload is a realistic reference drift and monitor-phase error budget on a specified apparatus.
