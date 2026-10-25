# Matched stationary graphite Hessian and bond-variance proxy

**Status:** NUMERICAL/CONDITIONAL reconstruction of one conventional KC-plus-plate model; HYPOTHESIS for the physical bond-to-native-edge map; OPEN kinetic friction and UD attribution. Physical promotion 0, independent physics review NOT_RUN.

## Result

The [reconstruction](reconstruct.py) obtains a full registered $14\times14$ vertical stiffness $K$ and $2\times14$ mixed stiffness $C$ at **one and the same** stationary state. It uses the archived grid-selected Cartesian translation (rather than re-reading the unavailable original Mendeley grid ZIP), the upper/lower geometry and $16$ Å fixed pair roster in the archived model, and the published KC parameters of Minkin *et al.*, [PRB 108, 085411 (2023)](https://doi.org/10.1103/PhysRevB.108.085411), SI Table S1. The source archive is [arXiv:2308.06302](https://arxiv.org/abs/2308.06302), SHA-256 `adea7468f311c648a0d25abf4f5eecacd8eebe1b6fc7761ffcea7d073b2f460b`. The archived reference translation and comparison data are retained in this repository; the original public Mendeley dataset is [10.17632/svnpzbjc3t.1](https://doi.org/10.17632/svnpzbjc3t.1). No code from that dataset is executed.

The full numerical arrays, aligned atom indices, pressure rows and checks are in [MATCHED_HESSIAN_RESULTS.json](MATCHED_HESSIAN_RESULTS.json). They reproduce the archived stationary eigenvalues to maximum relative error $1.79\times10^{-10}$ and the static softening and unit-isotropic-loss tensor to $1.45\times10^{-8}$ or better. The $C_3$ relative defects of $K$ and $C$ are $4.37\times10^{-10}$ and $7.05\times10^{-8}$. All 4,106 fixed pairs remain in the roster at the optimum. Changing Hessian steps from $(10^{-4},10^{-3})$ Å to $(3\times10^{-4},3\times10^{-3})$ Å changes the largest relative site variance by $9.56\times10^{-6}$. These are constructor comparisons to the same model, not independent empirical validation.

**Thermal normalization:** The reported $K$ is the Hessian of energy $\bar E$ *per mean upper atom*. For total energy $E_{\rm tot}=14\bar E$, the classical harmonic covariance is

$$\Sigma_h=\frac{k_BT}{14}K^{-1}=\bar\Theta K^{-1},\qquad \bar\Theta:=k_BT/14.$$

Thus the saved covariance and variances are coefficients **per $\bar\Theta$**, in Å²/meV. Multiplying directly by $k_BT$ would overstate them fourteenfold. The 14 registered site coefficients range from $0.00857605$ to $0.00892120$ Å²/meV, a $3.94\%$ span relative to their mean. This Gaussian local-Hessian model does not test finite-temperature anharmonicity or contact mechanics.

## Declared proxy and load derivative

The separate [proxy replay](analyze_proxy.py) verifies that the registered upper-layer nearest-neighbor bonds coincide combinatorially with the 21 bonds of the seven-cell UD honeycomb carrier. It then **assumes** a physical proxy $q_e=h_{B(e)}-h_{A(e)}$, and assigns

$$w_e/\bar\Theta=(B_1^TK^{-1}B_1)_{ee},\qquad
S_0=M^T\operatorname{diag}(w/\bar\Theta)B_1^T.$$

This is an illustrative map, not a derivation of a native packet edge variable from graphite heights. The exact carrier identity $B_1M=0$ makes uniform weights cancel. The reconstructed bond coefficients range from $0.00207043$ to $0.00212995$ Å²/meV, with coefficient of variation $0.939\%$; the $C_3$ orbit spread is below $3.2\times10^{-12}$ Å²/meV. The [proxy results](BOND_PROXY_RESULTS.json) give a rank-two $S_0$. A single scalar fit of its Cartesian image to the **conventional** $C$ leaves $42.88\%$ relative Frobenius residual. This fit is target-exposed and cannot identify an additive UD coupling.

For a still stronger **conditional** model, set $C_{\rm port}(P)=\beta\bar\Theta S_0(P)$ and independently assume a height Rayleigh matrix $D_h=dI$ with pressure-independent $\beta,d,T$. Then

$$\Gamma_{\rm port}=\beta^2d\bar\Theta^2 S_0K^{-2}S_0^T,\quad
\left.\frac{\Delta\ln[\operatorname{tr}(\Gamma_{\rm port})/2]}{\Delta P}\right|_{-2.5}^{+2.5}
\simeq 6.74813\times10^{-4}\ {\rm MPa}^{-1}.$$

The same conventional-model pressure sweep gives $8.06051\times10^{-4}\ {\rm MPa}^{-1}$ for its scalar drag per unit isotropic Rayleigh coefficient. Alternate Hessian steps change the conditional port slope to $6.74816\times10^{-4}\ {\rm MPa}^{-1}$. The pressure sweep is around a model reference load, not experimental pressure-resolved friction. Unknown $\beta(P),d(P),T(P)$ change the slope, and shared-bath cross terms can change the sign of a baseline-subtracted residual. Neither this proxy nor the fitted conventional projection predicts measured remaining friction.

## Reproduce and next measurement

From repository root, run `python3 experiments/graphite-matched-hessian-reconstruction/reconstruct.py > /tmp/matched.json` and `python3 experiments/graphite-matched-hessian-reconstruction/analyze_proxy.py` (the latter reads the committed result). The [receipt](../../candidates/graphite-matched-hessian-reconstruction/mathematical_receipt.json) and [capture](../../artifacts/graphmatched-20261025-01/matched-001/manifest.json) preserve input and output hashes.

Next independently determine whether the native even edge state actually measures a bond-height covariance or another registered material observable; measure a matched complex loss matrix and contact transfer; then freeze $\beta,D_h$ and forecast a signed residual on held-out angle, direction, speed and pressure traces. The conventional lattice geometry already gives $\cos\theta=13/14$ and its $60^\circ$ complement, and this one-index reconstruction does not select seven over 13 or 19.
