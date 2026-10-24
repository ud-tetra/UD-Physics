# Independent SI charge/flux anchors versus native tetrahedral LC normalization

**RESULT — EXACT / CONDITIONAL** two-anchor formula, exact noncompactness obstruction, physically indistinguishable native-scale family, and a positive periodic conventional-harmonic counterfamily. **FAILED / OPEN:** No independently source-selected UD action/charge normalization or unique quantum/physical response.

## Mission, sources, typed quantities

Can independently defined charge and superconducting flux-quantum scales select the native UD circuit action reference without identifying the UD phase with a physical Josephson phase *by decree*?

Integrated read-only base \`ud-tetra/UD-Physics@f0f6b707b77467f28c8e3892384fa0e8b28a4869\`, specifically [tetrahedral charge-field model](../qpb1-charge-field/README.md), [quantized-charge source audit](../qpb1-quantized-charge/README.md), [impedance-source audit](../qpb1-impedance-selection/README.md), and [unit preparation](../qpb1-unit-preparation/README.md). Earlier experimental-port draft [PR #177](https://github.com/ud-tetra/UD-Physics/pull/177) at \`0b49de51a83d17a31e81efe44825499756a1be19\` is unmerged/read-only, **not** an integrated task dependency.

External primary metrology sources: [BIPM SI defining constants](https://www.bipm.org/en/measurement-units/si-defining-constants) specifies exact \(h=6.62607015\times10^{-34}\) J s and \(e=1.602176634\times10^{-19}\) C. [NIST Josephson voltage standard](https://www.nist.gov/ctl/rf-technology-division/superconductive-electronics-group/quantum-locking-ranges) explains physical superconducting phase \(\varphi\) with \(2\pi\) phase slips and time-integrated voltage \(\int Vdt=\Phi_0=h/(2e)\) in webers. These values are **externally fixed physical inputs**, not observations or source-selected UD constants; no device-specific charge/flux/energy dataset is introduced.

The native **added** R12 tetrahedral canonical field has edge \(a,p\in\mathbb R^6\), positive Euclidean metric and Hamiltonian \(H_0=\frac12p^\top (u_LP_L+u_TP_T)p+\frac v2\|B_2^\top a\|^2\) with positive *free* \(u_L,u_T,v\). It is not the original native R14 active UD packet carrier. For a transverse mode \(a=\alpha w,p=\beta w\), \(\|w\|=1\), \(H_w=u_T\beta^2/2+2v\alpha^2\), \(\alpha,\beta\in\mathbb R\). Native \(s\) is dimensionless; conditional SI dictionary is \(\Phi=\mathcal A_0\alpha/q_0\) Wb, \(Q=q_0\beta\) C, \(t=\tau_0s\) seconds, \(E=\mathcal A_0H_w/\tau_0\) J. The source does **not** choose \(\mathcal A_0,q_0,\tau_0\).

## Exact comparison of externally sourced anchors

For positive externally CHOSEN integer/rational charge factor \(n\) and native phase-period factor \(m\), postulate \(q_0=ne,\Delta\alpha=2\pi m\) and \(\Delta\Phi=\Phi_0\). Then
\[
\frac{\mathcal A_0}{q_0}\,2\pi m=\frac{h}{2e},
\qquad \boxed{\mathcal A_0/\hbar=n/(2m)},\quad \hbar=h/(2\pi).
\]
The equality is algebraic given the three assumptions. Examples checked exactly:

| Chosen \(q_0\) | Chosen native \(\Delta\alpha\) | Inferred \(\mathcal A_0\) |
|---|---|---|
| \(2e\) | \(2\pi\) | \(\hbar\) |
| \(e\) | \(2\pi\) | \(\hbar/2\) |
| \(2e\) | \(4\pi\) | \(\hbar/2\) |
| \(2e\) | \(\pi\) | \(2\hbar\) |
| \(4e\) | \(2\pi\) | \(2\hbar\) |

**CRITICAL STATUS:** The standard Josephson choice \(q_0=2e,\Delta\alpha=2\pi\) reproduces \(\mathcal A_0=\hbar\) **by importing the physical Cooper-pair charge and phase-period identification**. Neither follows from native noncompact \(a\in\mathbb R^6\), a count of tetrahedral register labels, K4 incidence, a finite Weyl phase, or native loop-action O10/O15. There is no independent derivation of \(\hbar\).

Without a native period chosen separately, even fixing BIPM \(h,e\) and the physical Josephson flux quantum does not constrain the earlier exact internal \(r>0\) orbit:
\[
(U,v,a,\mathcal A_0,\psi)\mapsto
(rU,v/r,ra,\mathcal A_0/r,r\psi),
\]
holding \(q_0,\tau_0,p,f\) fixed. Physical charge \(Q\), flux \(\Phi\), inverse-capacitance/inductance matrices, full linear V/I ports and work all remain unchanged. Five rational rescalings verify the exact identities; their all-positive-real scope follows by algebra. If an **independently defined native** period \(\Delta\alpha=2\pi\) is additionally frozen, the transformed period \(r\Delta\alpha\) fails that premise unless \(r=1\). This removes that coordinate-gauge freedom **only by the new native-period assertion**.

## Conditional Josephson normal-mode dictionary and obstruction

Under the *imposed* \(q_0=2e,\alpha=\varphi,\mathcal A_0=\hbar\), the oscillator energy \(E=(\hbar/\tau_0)(u_T\beta^2/2+2v\alpha^2)\) has standard charging/Josephson small-signal coefficients
\[
\frac{E_C}{\hbar}=\frac{u_T}{8\tau_0},\qquad
\frac{E_J}{\hbar}=\frac{4v}{\tau_0},\qquad
\omega_0^2=\frac{8E_CE_J}{\hbar^2}=\frac{4u_Tv}{\tau_0^2}.
\]
Four exact rational \((u_T,v,\tau_0)\) fixtures verify the equation. These are a **dimensional correspondence** of two quadratic oscillators, not a microscopic device construction.

**Topological/constitutive failure:** A superconducting phase coordinate is a point on a circle \(\varphi\sim\varphi+2\pi\). The native quadratic potential \(V_{\mathrm{nat}}=2v\alpha^2\), \(v>0\), fails this identification:
\[
V_{\mathrm{nat}}(\alpha+2\pi)-V_{\mathrm{nat}}(\alpha)
=8\pi v\alpha+8\pi^2 v\ne0.
\]
Thus the original positive noncompact quadratic model **cannot descend as the same globally defined Hamiltonian on the compact Josephson phase circle**. It can approximate the harmonic dynamics near one minimum; replacing \(2v\alpha^2\) with a periodic Josephson cosine is a **new physical constitutive hypothesis**. Adding periodicity alone does not imply quantum rotor statistics, integer charge \(N\), charge superselection, a readout or a native action constant.

Even with \(q_0=2e,\Delta\alpha=2\pi,\mathcal A_0=\hbar\), and the exact same independently calibrated small-signal curvature \(K>0\), consider the continuous conventional family
\[
V_\lambda(\alpha)
=\frac{K}{1+4\lambda}[(1-\cos\alpha)+\lambda(1-\cos2\alpha)],\quad\lambda\ge0.
\]
All are positive bounded \(2\pi\)-periodic physical potentials with \(V''_\lambda(0)=K\). Yet
\[
\frac{\omega_\lambda(a)}{\omega_0}
=1-\frac{1+16\lambda}{16(1+4\lambda)}a^2+O(a^4).
\]
Five chosen \(\lambda=0,1/16,1/8,1/4,1/2\) give *different exact coefficients* \(-1/16,-1/10,-1/8,-5/32,-3/16\). These are **HYPOTHESIS/FIT development alternatives, not measured junction parameters**. Hence physical charge/flux anchors and the linear oscillator curvature fail to select nonlinear constitutive response. An ordinary superconducting circuit with its measured \(E_C,E_{Jm}\) is the complete conventional null.

## Data, identifiability, falsification, record

There is **no device-specific measured data** in this run. The BIPM defining numerical values have no uncertainty as SI constants; a Josephson device's measured realization, transducer losses, capacitance, charge/phase calibration and clock *would* have uncertainty, not estimated here. No new physical effect is derived or measured. The old target \(\eta_{\mathcal A}=2\), old transmon spectrum and Josephson \(\hbar\) were **known prior to selecting this map**; no held-out predictive success follows.

Reproduce from repository root:
\`python3 experiments/qpb-metrology-anchor/anchor_audit.py --out /tmp/qpb-metrology-anchor-001.json\`

Standard library \`Fraction(Decimal)\` gives exact rational SI h/e/flux algebra and parameter/curvature/rescaling checks. The actually executed command was \`python3 /mnt/data/qpb_metrology_20261024/anchor_audit.py --out /mnt/data/qpb_metrology_20261024/result.json\`, byte-identical to captured source. The immutable [anchor-001 manifest](../../artifacts/qpb-metanchor-20261024-gpt6-a1/anchor-001/manifest.json) retains full input/output hashes. Source SHA-256 \`a74484324edeab1062090a6030c5139b6bc9e29e6fa963332833c48e7f532c38\`, output \`5a7077ef691ebaf8e2d39f2a248ec4d9d8e9c61f516b5eac28bc92fe258e23e0\`. No external non-constructor mathematical review and no physical apparatus experiment. The native action/charge physical-identification role remains **PARKED**; the useful Josephson dictionary is an exact conditional analogue, not mainline physics.

**Reopening gate:** a versioned genuinely native periodic phase/charge primitive and a physical q0/action/readout map chosen *without invoking the physical Josephson target*, followed by an unused-data response beyond the conventional Josephson harmonic/null family. If no such primitive exists, switch physical-bridge families rather than continue adjusting λ to a known Josephson spectrum.
