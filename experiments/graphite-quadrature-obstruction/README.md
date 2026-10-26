# A parity-compatible graphite quadrature map and its clock obstruction

**EXACT/CONDITIONAL** Gaussian and time-reversal construction; **NUMERICAL** replay of the registered conventional model; native material identification, damping and measured force **OPEN**. Physical promotion 0; independent physics review NOT_RUN.

## Physical question and provenance

The [matched conventional Hessian](../graphite-matched-hessian-reconstruction/README.md) and [registry-defect audit](../graphite-registry-defect-source/README.md) give a conditional, nonuniform bond-variance source. Can an edge variable odd under the [native packet reversal](../graphite-packet-reciprocity/README.md) produce that same stationary even observable? If it can, does this also make the native unit-metric packet dynamics a physical graphite oscillator?

The following construction answers the first question **yes under a new material map**, and the second **no for one scalar clock and the unit incidence generator**. The supplied coefficient ledger v0.39(2), SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, still has zero current seam-pairing source Q22; Q24 is conditional, while Q25/Q26 do not source an edge weight or route law. Q166/Q167/Q170 are internal stock/current identities, not physical dissipation. These rows do not derive the map below.

## Canonical quadrature surrogate

Use the registered $14$ physical site heights $h\in\mathbb R^{14}$ (Å), conjugate momenta $p$, mass $m>0$ per site, and the prior positive conventional $K$ in meV/Å² **per upper atom**. The total conservative harmonic energy and temperature convention are

$$H_0=\frac{14}{2}h^TKh+\frac{1}{2m}p^Tp,\qquad \bar\Theta=\frac{k_BT}{14},\qquad \Omega^2=\frac{14}{m}K.$$

Write $B=B_1:\mathbb R^{21}\to\mathbb R^{14}$ for oriented bond incidence, $L=BB^T$, and $q=B^Th$ (Å). Under physical time reversal $(h,p)\mapsto(h,-p)$, $q$ is even. Define the **new proposed physical surrogate**

$$y_*:=\frac{1}{\sqrt{14m}}B^TK^{-1/2}p\quad(\mathrm{Å}),\qquad y_{\rm candidate}:=y_*/\ell,$$

where $K^{-1/2}$ is its unique positive symmetric root and $\ell>0$ is an **unfixed physical-to-native length**. Both $y_*$ and $y_{\rm candidate}$ are odd under the stated reversal. This map requires the full registered conventional stiffness, its positive square root, canonical momenta, and a length calibration. It is generally nonlocal in site coordinates; neither the ledger nor the native packet generator selects it.

In the Gibbs state of $H_0$, $\operatorname{Cov}(h)=\bar\Theta K^{-1}$, $\operatorname{Cov}(p)=mk_BT I$, and $\operatorname{Cov}(h,p)=0$. Therefore

$$\operatorname{Cov}(q)=\operatorname{Cov}(y_*)=\bar\Theta B^TK^{-1}B,\qquad
\langle y_{{\rm candidate},e}^2\rangle=\frac{\bar\Theta}{\ell^2}(B^TK^{-1}B)_{ee}.$$

Both edge fields lie in the rank-13 gradient subspace $\operatorname{im}B^T\subset\mathbb R^{21}$; its orthogonal cycle kernel has dimension eight. The even-source rule $S(w)=M^T\operatorname{diag}(w)B^T$ thus reproduces the previously calculated *mean* source if its weight is **chosen** as $w_e=\langle y_{{\rm candidate},e}^2\rangle$. This is a constructive parity-compatible *surrogate*, not an explanation of why the UD packet state samples the Gibbs measure or why its force coefficient has any particular value. Any local reciprocal energy $E_{\rm int}=14\lambda(Tu)^TS((y_*/\ell)^2)R_hh$ would have a mean mixed $u,h$ Hessian $\lambda T^TS(w)R_h$ per upper atom at the zero-displacement reference. Here $\lambda$ (meV/Å² per atom), frames $T,R_h$, and stable operating range are additional assumptions. Because $y_*$ depends on $p$, the Hamiltonian changes **both** $\dot h=\partial_pH$ and $\dot p=-\partial_hH$; inserting this force while retaining the old uncoupled packet generator would omit backreaction. At $\lambda=0$ the construction is conservative and produces no irreversible friction.

A simpler site-local odd assignment $y_{\rm local}=aB^Tp$ with identical carbon-site masses has $\langle y_{{\rm local},e}^2\rangle=2a^2mk_BT$ for every bond. Since $B M=0$, its mean source is exactly zero. The $K^{-1/2}$ factor supplies the nonuniformity by importing conventional registry stiffness; it is not a native local selection rule.

The parity-safe map also has an exact conservative **statistical degeneracy**. For $t\in\mathbb R$ in the harmonic Gibbs state,

$$C_{qq}(t)=C_{y_*y_*}(t)=\bar\Theta B^TK^{-1}\cos(\Omega t)B,$$

$$C_{q y_*}(t)=\bar\Theta B^TK^{-1}\sin(\Omega t)B,\quad C_{q y_*}(0)=0.$$

Thus $q$ and $y_*$ have the same zero-mean Gaussian process law when observed **separately** in this closed harmonic model, including autocorrelations of their squares; their cross correlation is odd in time. Equal-time variance or an isolated conservative autocorrelation cannot decide which quadrature a native edge represents. The [replay](replay_quadrature.py) gives a maximum $4.83\times10^{-17}$ Frobenius discrepancy between $C_{qq}$ and $C_{y_*y_*}$ at four normalized times, and reproduces the prior 21 bond-variance range $0.00207043$–$0.00212995$ Å²/meV per $\bar\Theta$. These are same-model checks, not empirical validation.

## Why one native clock fails

For the fixed-mask native full-chain unit-metric generator $\dot x=By$, $\dot y=-B^Tx+B_2z$, $\dot z=-B_2^Ty$ in a dimensionless native clock $s$, gradient edges $y\in\operatorname{im}B^T$ and $z=0$ obey

$$\frac{d^2y}{ds^2}=-B^TBy.$$

If $s=t/\tau$ for **one** physical clock $\tau>0$, this is $\ddot y=-\tau^{-2}B^TBy$. The physical surrogate $y_*$ instead obeys the $K$ oscillator. Equality for every physical momentum preparation requires the necessary matrix identity

$$B^TK=c B^TL,\qquad c=\frac{m}{14\tau^2}.$$

This is an exact conditional intertwining test, not a demand that arbitrary UD models have a unit metric. Even after averaging $K$ over the 21-element bond-transitive graph symmetry, $L$ has nonzero eigenvalues $3-\sqrt2$ (sixfold), $3+\sqrt2$ (sixfold), and $6$; the corresponding $\bar K$ eigenvalues are approximately $303.287$, $2302.477$, and $4250.974$ meV/Å². Their ratios to the $L$ eigenvalues are approximately **191.253, 521.605, and 708.496**, so no single $c$ works. On the actual matched $K$, the best Frobenius scalar $c=564.547$ leaves

$$\min_c\frac{\|B^TK-cB^TL\|_F}{\|B^TK\|_F}=0.187354.$$

The group-averaged model gives $0.187316$ by the same diagnostic. The obstruction is essentially present before the smaller registry defect; the $\pm2.5$ MPa model sweep stays near $0.18735$. Fitting $c$ to the **conventional model** is openly target-exposed and supplies no physical clock. A nonunit native metric, mode-dependent rate, new memory variables or changed physical map could pass this test only with an explicit reciprocal generator and independently specified parameters. This is a scoped failure of the simplest bridge, not an all-UD no-go.

## What damping would change

For an **independently assumed** equilibrium Langevin height bath with $D_h\succeq0$ and fluctuation-dissipation noise,

$$dh=\frac{p}{m}dt,\qquad dp=-14Kh\,dt-\frac{D_h}{m}p\,dt+\sqrt{2k_BT D_h}\,dW_t,$$

the same Gibbs equal-time covariance survives. Yet the autocorrelations have different right derivatives at zero lag:

$$C'_{qq}(0^+)=0,\qquad C'_{y_*y_*}(0^+)=-\frac{\bar\Theta}{m}B^TK^{-1/2}D_hK^{-1/2}B.$$

For the scalar bath $D_h=dI$, this becomes $C'_{y_*y_*}(0^+)=-(d/m)C_{qq}(0)$, versus zero for $q$. The result is a **conditional loss discriminator**, not a determination of $d$ from the UD ledger. It also shows why the static proxy and its previous fixed-$d$ load slope cannot be promoted into a signed friction prediction. A physically measured, registered complex response and contact transfer are needed; under shared baths the conventional-subtracted force can include signed cross terms.

Run `python3 experiments/graphite-quadrature-obstruction/replay_quadrature.py` from repository root. The [receipt](../../candidates/graphite-quadrature-obstruction/mathematical_receipt.json), [numerical result](QUADRATURE_RESULTS.json), and [immutable capture](../../artifacts/graphquad-20261026-01/quadrature-002/manifest.json) record the scope. The highest-value next discriminant is to source or measure the edge-to-material map and the full complex loss/contact response **independently** at a held-out angle and load, then freeze them before testing a signed residual. The [experimental publisher abstract](https://doi.org/10.1103/ly48-b4l2) identifies 21.8°/38.2° as friction peaks; conventional triangular commensurability already gives the complementary angles.
