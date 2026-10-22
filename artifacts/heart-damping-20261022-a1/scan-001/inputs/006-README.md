# Passive difference damping and a usable band — v1.0

Evidence: **EXACT/CONDITIONAL**, **NUMERICAL**, **FIT/design**. This is a separately assumed scalar/radial mechanical candidate in UD Discovery. No native damping law or physical correspondence is established.

## 1. Objects, sources and chosen question

Base: `bbf15511970e08330bfece2503a541a902f9f96c`. Continue the [positive-energy radial model](../heart-shell-elastic/README.md) and [imperfection analysis](../heart-shell-robustness/README.md). State $x=(a,q_1,q_2,q_3,q_4)\in\mathbb R^5$, with velocities giving phase space $\mathbb R^{10}$; $a$ is an internal preferred strain, not a displaced point. Actual outer positions are $R_i=(1+q_i)r_i$, on four fixed regular-tetrahedron rays. The heart is at the fixed geometric centre. Angular and shear coordinates are absent.

Use dimensionless continuous parameter $u$; prime means $d/du$. Let $b=\sum_iq_i/4$, $P=I-J/4$, $d=Pq$. The Euclidean projection $P$ has rank 3 and kernel the common outer motion. Positive kinetic metric is $M=\operatorname{diag}(1,m_1,\ldots,m_4)$.

Retain $I_h=K_h=K_s=1,K_t=1/2$, positive spokes $g_i$ and inertias $m_i$. The potential is

$$
U=\frac{a^2}{2}+\frac12\sum_iq_i^2+\frac12\sum_i g_i(q_i-a)^2
 +\frac14\sum_{i<j}(q_i-q_j)^2.
$$

These illustrative coefficients and the following damping channel are assumed, not imported native coefficients. Historical source ledger v0.39, Q139/Q144–145/Q151–152, still leaves physical clock and constitutive selection open. No numerical constant here resolves those questions.

Question: can selective passive damping suppress unequal volume motion while retaining a substantial common response? Known targets include the prior illustrative squared frequencies $1,4,6$ and the exposed imperfection campaign. Choose ±5% parameter tolerance, 5% linear volume-signal leakage and 80% coherent gain retention as **design criteria**, not empirical acceptance levels. Choose $\gamma=1/2$ for the certificate before inspecting its pulse results; compare (1/10,1/4,1/2) in the pulse campaign. No global optimum is claimed.

## 2. Exact passive law and its protected subspace

The complete four-node graph has six edges, degree three, and Laplacian $L_{K_4}=4I-J=4P$. Propose Rayleigh dissipation

$$
\mathcal R=\frac\gamma2\sum_{i<j}(q_i'-q_j')^2=2\gamma\|d'\|^2,
\qquad \gamma\ge0.
$$

The equation is $Mx''+Cx'+Kx=0$, with $C=\operatorname{diag}(0,4\gamma P)\succeq0$, $K$ the Hessian of $U$. It gives the exact balance

$$
E'=x'^T(Mx''+Kx)=-x'^TCx'=-4\gamma\|d'\|^2\le0.
$$

The damper annihilates both heart velocity and common outer velocity; it dissipates only outer differences. This is passivity, not full asymptotic stability: perfectly symmetric collective modes remain undamped. For the symmetric baseline, the collective equations and their squared frequencies $1,6$ are unchanged, while every differential coordinate obeys

$$
d''+4\gamma d'+4d=0,\qquad s_\pm=-2\gamma\pm2\sqrt{\gamma^2-1}.
$$

Thus $\gamma=1/2$ gives differential exponents $-1\pm i\sqrt3$; $\gamma=1$ is critical damping. Disorder couples these subspaces, allowing dissipation of part of a breathing pulse. No claim of exact protection under arbitrary disorder is made.

Positive pins give $U\ge\sum q_i^2/2$. For the declared heart preparation $a(0)=1/10$, other coordinates and velocities zero, $E(0)=(1+\sum g_i)/200\le29/1000<1/2$ for ±20% spokes. Hence $q_i>-1$ for all unforced times, also with damping. This keeps the radial volume readout in its positive geometric domain.

## 3. Harmonic mismatch and the removed differential pole

Use complex phasors $e^{-i\omega u}$, $\lambda=\omega^2>0$. Here the heart amplitude is prescribed to be 1 to define a transfer shape; an actual motion is rescaled small. It is a different experiment from a fixed heart-force drive or the unforced pulse.

Let $\bar g,\bar m$ be arithmetic means, $\delta g=P g$, $\delta m=P m$, and $v=\delta g-\lambda\delta m$. On the three-dimensional contrast space,

$$
H_d d=\delta g-bv,\qquad
H_d=P\operatorname{diag}(3+g_i-\lambda m_i)P\big|_{\operatorname{im}P}
 -i4\gamma\omega I.
$$

The real part is self-adjoint in the Euclidean contrast metric, so

$$
\sigma_{\min}(H_d)\ge 4\gamma\omega>0.
$$

This removes every real-frequency pole of the isolated differential block for positive $\omega,\gamma$. It does not remove every resonance of the full driven system or give an all-frequency gain guarantee.

For balanced signs $s=(1,1,-1,-1)$, $g_i=1+\epsilon s_i,m_i=1+\eta s_i,q_i=b+s_i d$, the mean equation is $(2-\lambda)b+(\epsilon-\lambda\eta)d=1$. Substituting into the contrast equation gives exactly

$$
\frac d b=\frac{\epsilon(1-\lambda)+\lambda\eta}
 {4-\lambda-\epsilon^2+\epsilon\lambda\eta-i4\gamma\omega}.
$$

At the former differential frequency $\lambda=4$, $\epsilon=1/20,\eta=0$, the undamped volume differential/collective amplitude ratio was 20. With $\gamma=1/2$ it is

$$
\frac{|d|}{3|b|}=\frac{20}{\sqrt{2560001}}\approx0.01250.
$$

The ratio uses complex amplitudes; it is not an energy fraction. The damping sign follows the declared negative-exponential convention.

## 4. Continuous-box frequency certificate

Assume independently $g_i,m_i\in[1-\varepsilon,1+\varepsilon]$. Then

$$
\|\delta g\|\le G=2\varepsilon,\quad \|v\|\le V=2\varepsilon(1+\lambda),\quad
\|d\|\le(G+V|b|)/s,\quad s=4\gamma\sqrt\lambda.
$$

The mean equation is $h b+v^Td/4=\bar g$, $h=1+\bar g-\lambda\bar m$. Set $D=|2-\lambda|$. If $D-\varepsilon(1+\lambda)>V^2/(4s)$, the shell block is invertible: eliminating (d) gives Schur complement $h-v^TH_d^{-1}v/4$, whose magnitude cannot vanish under this inequality. Also

$$
|b|\ge b_{\min}=\frac{1-\varepsilon-VG/(4s)}{D+\varepsilon(1+\lambda)+V^2/(4s)}>0,
\qquad \frac{\|d\|}{|b|}\le B=\frac{G/b_{\min}+V}{s}.
$$

Linear fractional child-volume phasors are $y_i=3b-d_i$. Orthogonality gives

$$
L_h=\frac{\|d\|}{\sqrt{36|b|^2+\|d\|^2}}
\le\sqrt{\frac{B^2}{36+B^2}},\qquad
\frac{|b|}{|b_{\mathrm{sym}}|}=D|b|\ge D b_{\min},
\quad b_{\mathrm{sym}}=\frac1{2-\lambda}.
$$

The executable certificate covers each interval by 100 closed rational subintervals. In each, replace (s) by a rational lower bound using integer square root, $V,D_{\max}$ by upper bounds and $D_{\min}$ by a lower bound. All decisive comparisons use `Fraction`: $B^2\le12/133$ implies $L_h\le1/20$, and $D_{\min}b_{\min}\ge4/5$. This is a continuous-frequency, continuous-parameter-box certificate, not a sampled-frequency claim.

For $\varepsilon=1/20,\gamma=1/2$:

| Squared-frequency interval $\lambda$ | Angular frequency in model units | Certified $L_h$ upper bound, rounded up | Certified coherent gain lower bound, rounded down |
| --- | --- | --- | --- |
| ([4/5,6/5]) | $[\sqrt{4/5},\sqrt{6/5}]\approx[0.8944,1.0954]$ | 2.953% | 82.43% |
| ([11/2,13/2]) | $[\sqrt{11/2},\sqrt{13/2}]\approx[2.3452,2.5495]$ | 4.145% | 85.86% |

These are sufficient bands, not maximal bands or a physical prediction. They certify small-signal linear volume shapes under prescribed heart amplitude; they do not certify finite-amplitude nonlinear volume leakage or a force-to-volume gain. Thirty-one sampled frequencies per band and all 256 corner patterns independently check the full complex shell solve: observed maxima $0.6571\%,3.5145\%$, minimum gain retentions $92.3077\%,86.9281\%$, respectively. Those sampled checks are numerical, distinct from the exact certificate.

## 5. Pulse campaign and amplitude cost

Same preparation and parameter corners as the prior campaign: all 16 spoke-sign patterns times 16 inertia-sign patterns for each tolerance; unforced trajectories over $u\in[0,100]$, 4001 samples. Run three damping coefficients: 3072 damped corner trajectories, each compared with its corresponding undamped trajectory. A further 256 seeded interior points at ±5% use $\gamma=1/2$.

Use exact nonlinear geometry $V_i=(V_0/4)\prod_{j\ne i}(1+q_j)$, $V_0=8L^3/3$, and $y_i=V_i/(V_0/4)-1$. Report

$$
L_V=\sqrt{\frac{\int\|Py\|^2du}{\int\|y\|^2du}},\qquad
R_b=\frac{\operatorname{RMS}(\bar y)_{\mathrm{damped}}}{\operatorname{RMS}(\bar y)_{\mathrm{same\ parameters,undamped}}}.
$$

These are signal-amplitude measures; neither is an energy/information fraction. The minima/maxima below can occur at different corners.

| Variation | Prior maximum $L_V$, undamped | Maximum $L_V$, $\gamma=1/2$ | Minimum mean-volume RMS retained | Minimum initial energy remaining at $u=100$ |
| --- | --- | --- | --- | --- |
| ±1% | 1.88% | 0.49% | 99.78% | 98.37% |
| ±5% | 9.35% | 2.36% | 95.08% | 66.40% |
| ±10% | 21.25% | 4.10% | 84.46% | 20.47% |
| ±20% | 40.68% | 5.85% | 68.01% | 2.44% |

Among seeded ±5% interiors: maximum $L_V=1.4721\%$, minimum $R_b=97.6799\%$. No statistical confidence or continuous-box pulse bound follows from these samples. Stronger damping did not monotonically minimize every loss metric; the complete sweep is retained in the CSV.

![Finite pulse comparison](../../artifacts/heart-damping-20261022-a1/scan-001/files/damping-comparison.png)

## 6. Verification and reproduction

`analyze.py` uses NumPy 2.3.5 / SciPy 1.17.0, float64 complex eigensystem propagation of the ten-dimensional first-order generator. Maximum eigenvector condition number: 16.49; every evaluated trajectory is cross-checked at $u=1/4$ against SciPy matrix exponential $maximum discrepancy (4.86\times10^{-16})$. This is a second numerical implementation by the same constructor, not independent empirical replication. Energy monotonicity is checked at every sample; integrated dissipation balance error is at most $8.92\times10^{-7}$ relative to initial energy. Symmetric damped/undamped trajectories differ by at most $8.80\times10^{-15}$.

For each tolerance's worst observed $\gamma=1/2$ leakage pattern, repeat quadrature at 8001 and 16001 samples. Largest difference: $3.50\times10^{-9}$. This supports the displayed precision for those cases; it is not a global numerical error bound. No critical-damping eigensystem is evaluated; the exact analytic result covers it.

From repository root, with NumPy, SciPy and Matplotlib installed:

```bash
OPENBLAS_NUM_THREADS=1 python3 experiments/heart-shell-damping/analyze.py --out /tmp/ud-damping
python3 experiments/heart-shell-damping/draw.py --summary /tmp/ud-damping/summary.json --baseline artifacts/heart-robustness-20261022-a1/scan-001/files/summary.json --out /tmp/ud-damping/damping-comparison.png
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The [run manifest](../../artifacts/heart-damping-20261022-a1/scan-001/manifest.json) captures code, imported implementation, baseline data, this report, receipt and outputs with SHA-256. Reproduce in repository layout because the analysis deliberately imports the preserved preceding implementation. Integrity CI validates records and hashes; it does not run the numerical campaign or certify physics.

## 7. Physical realization constraint and remaining question

The scalar graph damper is **not** automatically an ordinary axial dashpot on each spatial tetrahedron edge. For the regular rays used here,

$$
\widehat{(r_i-r_j)}\cdot(q_i'r_i-q_j'r_j)=\sqrt2L(q_i'+q_j').
$$

Ordinary edge dashpots therefore respond to sums of radial velocities. Six equal dashpots with coefficient (c>0) dissipate (48cL^2b'^2) during common breathing. They cannot realize the assumed difference-only protection in this direct arrangement. The exact ray dot products are checked in the executable certificate.

A passive implementation would need a specified linkage, internal relative coordinate, constraint, or another mechanism selecting radial differences. Its energetic and geometric consistency remains OPEN. The chosen damping is a useful mathematical requirement for such a mechanism.

If $u=t/t_0$, frequencies become $\omega/t_0$; with model energy unit $E_*$, physical generalized inertia and damping coefficients scale as $E_*t_0^2 M$ and $E_*t_0 C$. Neither $t_0$, $E_*$, a material, nor a native UD variable has been selected. The model has no angular/shear robustness guarantee or autonomous energy supply.

Next discriminant: construct or obstruct a passive geometric realization of the difference channel, then test its additional degrees of freedom and force-to-volume response.
