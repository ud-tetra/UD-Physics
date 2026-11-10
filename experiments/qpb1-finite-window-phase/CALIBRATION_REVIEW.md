# Short-time dynamical-phase calibration: Richardson estimator (phase-003)

**RESULT — EXACT / CONDITIONAL, constructor NUMERICAL.** The missing correction D can be estimated to <0.001 radians *under a new, demanding repeatability and phase-reference metrology budget*, via a time-slope estimate of the same model's complex overlap Z(t). This reduces the prior model's joint phase upper bound from 0.008250275742 to **0.008214198087 radians**. This is **not** a measurement of any physical system, nor external independent mathematical review.

## Typed model and calibration question

The source is the unchanged rank-14 active chain carrier with J-positive complex structure, Euclidean metric H=I and signed oriented tetrahedral sector decomposition. For positive g=(g1,g2,g3) near the *target-exposed* (1,1,3/2), sector weights rk>=0, sum rk=1, and dimensionless native evolution U(s)=exp(sG), define

\[
Z(t)=\langle x,U(t)x\rangle_\mathbb C
=\sum_{k=1}^3r_k e^{i\omega_kt},\quad \omega_k=2g_k>0,\qquad
M=\operatorname{Im}Z'(0)=\sum_k r_k\omega_k,\quad D(T)=TM.
\]

The ordinary four-phase analyzer in the preceding [receiver hypothesis](OPERATIONAL_RECEIVER.md) supplies the complex overlap when its reference is coherent. Here the new question is whether M can be estimated without knowing each g or r individually. Absolute g errors <=1/100 imply max |omega|<=151/50. All times use native continuous units; physical conversion t_physical=tau0*t and phase-gauge realization are OPEN.

## Estimator, exact error and operational constraint

Let S(h)=[Im Z(h)-Im Z(-h)]/(2h)=sum rk*sin(omega_k*h)/h and define

\[
\widehat M_R=\frac{4S(h/2)-S(h)}{3},\qquad h=1/12.
\]

By fixed time-independent skew evolution and Hermitian normalization, Z(-h)=conj(Z(h)), hence **S(h)=Im Z(h)/h**. The physical proposal only needs positive-time preparations at h and h/2; the symmetric negative-time expression is a mathematical identity, not a claim that time reversal is implemented in hardware.

The exact expansion for |z|<=1 gives

\[
\frac{4\,\operatorname{sinc}(z/2)-\operatorname{sinc}(z)}{3}
=1-\frac{z^4}{480}+\frac{z^6}{16128}-\cdots,
\]

whose alternating higher-order terms decrease in magnitude. For every positive frequency with |omega h|<=151/600<1, the *entire continuous gain/weight box* obeys

\[
|\widehat M_R-M|\le\frac{\Omega_{\max}^5h^4}{480}
=\frac{78502725751}{3110400000000000}.
\]

This is the exact truncation certificate, not an empirical curve fit or inference from the sampled checks.

## Explicit missing physical inputs and propagated uncertainties

Assume each complex calibration fringe Z(h),Z(h/2) has absolute error eta_c<=2e-6, including reference offset/drift within the probe acquisition; each measured probe time differs from its setpoint by <=1e-7 native units. Lipschitz continuity of Z(t) gives |delta Z|<=Omega_max|delta t|. The Richardson slope error contributed by these two effects is therefore bounded by 3(eta_c+Omega_max*1e-7)/h.

Between calibration preparation/generator and the main measurement assume the normalized state distance <=5e-6 and absolute gain drift per sector <=5e-6. A projective pure-state trace-distance inequality bounds the 3-sector weight L1 shift by at most twice the state distance; hence the mean-rate mismatch is at most 2*Omega_max*(5e-6)+2*(5e-6). To permit a large *actual* main-window jitter of <=0.01 while estimating D, additionally assume its actual T is measured within 1e-5 native units. Finally assume all readouts share the **same fiber-phase gauge**.

Let T_max=44/7+1/100. Then the complete rational calibration certificate is

\[
\begin{aligned}
|\widehat D-D|&\le T_{\max}\left[
\frac{\Omega_{\max}^5h^4}{480}
+\frac{3(\eta_c+\Omega_{\max}\sigma_{\rm probe})}{h}
+2\Omega_{\max}\zeta_{\rm repeat}+2\nu_{\rm repeat}\right]
+\Omega_{\max}\sigma_{\rm main}\\
&=\frac{699576281715419}{725760000000000000}
\approx0.00096392234584<0.001\ {\rm rad}.
\end{aligned}
\]

Bound contributions in radians: truncation 0.00015890; probe noise and clock 0.00052174; state/gain repeatability 0.00025309; main-time metrology 0.00003020. Replace only the preceding receiver's *assumed* 0.001-radian correction cap with this *derived-from-new-assumptions* 0.000964-radian cap; its other error budgets remain unchanged. New total:
\[
\boxed{|\mathrm{wrap}(\widehat\Phi-\pi)|\le
\frac{534794619424186500609612131837359}{65106126461057096943360000000000000}
\approx0.00821419808694<0.01.}
\]

**Selection record:** h=1/12 and eta_c, probe time metrology, state/gain repeatability and main-window metrology levels were set after exposure to the .001-radian calibration target. No measured instrument performance or physical clock scale was used. This is a *conditional feasibility specification*, not an independently validated success or a source/native-selection derivation.

## Baselines, counterexamples, reproducibility and limitations

Without D calibration the prior +-1% common gain uncertainty changes the raw mean dynamical phase by 4*pi*(.01)=0.1256637 radians at T0=2*pi, dwarfing the .01-radian screen; untracked native window jitter .01 with nominal M=5/2 adds .025 rad. A calibrated time-independent local generator can avoid this if repeated measurements satisfy the new stringent bounds; violating reference-phase stability or repeatability invalidates the guarantee.

The separate [Python constructor](calibration_audit.py) computes exact rational certificates and verifies 125 deterministic gain triples, 10,000 seeded arbitrary nonnegative sector-weight/gain triples and 16 adversarial probe-noise sign cases; finite checks are not the proof of the all-box bound. Reproduce from repository root:

\`python3 experiments/qpb1-finite-window-phase/calibration_audit.py --out /tmp/ud-qpb-calibration.json\`

[Immutable phase-003 input/output/manifest](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-003/manifest.json) records the exact bytes and SHA-256. This audit is by the **same assistant**, not independent non-constructor review, and no actual interferometer, source mechanism, calibrated native time, or independent empirical residual is reported.

**Next discriminant (priority 97/100):** a separately controlled reviewer should verify the sinc remainder and state-preparation metrology bound. More importantly, challenge with a specific coupled receiver/clock model: can positive-time fringe probes achieve 2e-6 complex error while holding shared gauge and preparation/gain drift <=5e-6? A premeasured physical phase residual distinct from an ordinary three-tone interferometer is still OPEN.
