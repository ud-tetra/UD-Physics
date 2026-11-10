# Phase-004: statistical shot noise and reference-frame test

**RESULT — EXACT / CONDITIONAL; instrumentation OPEN.**

## Question, objects and provenance

Can the phase-003 complex-probe accuracy \(\eta_c=2\times10^{-6}\) be obtained from independently counted fringes, and can the phase-003 calibration distinguish true geometric phase from measurement-frame drift? This extends [phase-003](CALIBRATION_REVIEW.md) at revision \`7e100fa6504fde634fab08497afeb4467ecae710\`; the imported single-tetrahedron generator is pinned at \`41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb\`. The active Euclidean rank-14 carrier, \(J=+i\), sector overlaps \(Z(t)=\sum r_k e^{i 2g_kt}\), dimensionless native time, and previously chosen 0.001/0.01-radian engineering limits are retained. The statistical photon model and measurement-frame drift are **new hypotheses**, not derived physical UD properties.

## 1. Two-delay four-phase receiver: conservative shot budget

At each of two short-time delays \(h=1/12\) and \(h/2=1/24\), take four analyzer settings \(\beta\in\{0,\pi/2,\pi,3\pi/2\}\) with Bernoulli detection probability
\[
p_\beta=\tfrac12[1+\operatorname{Re}(e^{-i\beta}Z)].
\]
Assume \(m\) independent outcomes per setting and no inter-setting correlation, loss bias, phase-step error or fluctuating state. The standard quadrature reconstruction uses \(\widehat{\Re Z}=\hat p_0-\hat p_\pi\), \(\widehat{\Im Z}=\hat p_{\pi/2}-\hat p_{3\pi/2}\). If each of the eight sample probabilities is accurate to \(\delta=\eta_c/(2\sqrt2)\), both complex errors are \(\le\eta_c\).

Hoeffding's inequality with a union bound therefore gives, for **this specific estimator and assumptions**,
\[
\Pr(\exists t\in\{h/2,h\}:|\widehat Z(t)-Z(t)|>\eta_c)
\le16\exp(-m\eta_c^2/4).
\]
Taking \(m=7{,}400{,}000{,}000{,}000\) gives \(m\eta_c^2/4=37/5\). The bound \(16e^{-37/5}<1/100\) follows **exactly** from \(\sum_{k=0}^{13}(37/5)^k/k!>1600\). Hence **59.2 trillion independently sampled binary events** across eight settings are *sufficient* for \(>99\%\) joint sampling accuracy in this ideal model. This is deliberately conservative, not a fundamental lower bound on photons, a measured instrument rate or a deterministic noise limit.

Illustrative continuous detected rates \(10^8\) and \(10^9\) events/second would mean at least ~164.44 or ~16.44 hours counting, ignoring resets, optical loss, phase switches, dead time and long-time drift. These are hypothetical rate scenarios, not evidence such a UD-linked detector exists. The native-to-physical map \(t_{\rm physical}=\tau_0t\) is OPEN, so a *native-time* preparation or clock requirement cannot yet be translated to hardware.

Conventional support (not a UD bridge): Slussarenko et al., *Nature Photonics* (2017), https://www.nature.com/articles/s41566-017-0011-5, describes shot-noise \(1/\sqrt N\) phase scaling; Pak et al., *Applied Optics* (2021), https://doi.org/10.1364/AO.418495, documents phase-shifter and related systematic error sources. No source establishes the hypothetical UD carrier, apparatus or target accuracy.

## 2. Frame-drift counterexample and identifiability

Distinguish the **native** overlap \(Z(t)\) from the observed optical/reference overlap \(Z_{\rm obs}(t)=e^{i\theta_{\rm ref}(t)}Z(t)\). If \(\theta_{\rm ref}(h)=\theta_{\rm ref}(h/2)=0\) but the external measurement reference acquires an untracked phase \(\theta_{\rm ref}(T)=\Delta\) at the main endpoint, the short-time probes cannot detect it and visibility remains unchanged. The reported corrected holonomy rotates by \(e^{i\Delta}\), independently of probe count. A separately observed reference monitor or common-mode cancellation is necessary to distinguish this instrumental phase from a signal phase.

Phase-003's exact calibration bound \(\kappa=699576281715419/725760000000000000\) leaves a margin \(1/1000-\kappa=26183718284581/725760000000000000\) radians. If an additional *differential reference ramp* accumulates over \(T_{\max}=4407/700\) native time, its magnitude must not exceed
\[
\frac{1/1000-\kappa}{T_{\max}}
=\frac{2014132175737}{351475200000000000}
\approx5.73051\times10^{-6}\ \mathrm{rad/native\ time}.
\]
As an adversarial challenge, an untracked main-only reference step \(\Delta=1/500=0.002\) radians would increase the earlier worst-case *budget* from 0.0082141981 to **0.0102141981** radians, no longer certifying the chosen \(<0.01\) screen. The step violates the earlier shared-frame/error premises, so this **does not contradict** the original conditional theorem; nor does an upper-budget failure prove a particular experiment suffers \(>0.01\) error.

## Baseline, verification, and discriminant

An ordinary three-tone interferometer has the same four-step signal formula and the same phase-frame ambiguity. The receiver therefore adds **no independently distinctive UD prediction** without a physically specified carrier coupling and a held-out residual against such a null model. A high-visibility fringe does not certify geometric phase or common-reference stability.

Run \`python3 experiments/qpb1-finite-window-phase/shot_noise_audit.py --out /tmp/qpb-phase004.json\` from the repository root. It checks exact rational tail and frame-bound identities and numerically evaluates sample sizes and rates. The [immutable phase-004 manifest](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-004/manifest.json) captures source/output bytes. **Same-constructor analysis, independent external review NOT_RUN, experimental instrumentation NOT_EXECUTED.** No mainline export.

**Next discriminant, priority 98/100:** freeze a specific receiver protocol; measure phase-frame drift and correlated counts through an independent reference channel; then test whether its attainable \(\eta_c,\kappa,\tau_0\) jointly meet the preselected phase limits. If not, park the physical bridge and retain the valid conditional mathematics.
