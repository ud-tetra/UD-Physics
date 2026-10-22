# Joint mechanical tolerance study — v1.0

**RESULT — A proposed joint budget passes the20 declared coherence probes;the added conservative mounts introduce54 undamped housing modes.** Exact module bounds and a measurable test protocol are available. Full mechanical relaxation remains FAILED in the defined hardware model.

Source revision:`4ddf692a11b7d21103799745d75a969f75a14c14`. This extends the [passive multiport model](../icosahedral-multiport/README.md) without retuning its selected(mu,kappa,gamma)=(2,50,5). The [initial protocol](PROTOCOL.md) declares the budget and probes before outcomes. All are Discovery development results;no native constitutive law,empirical experiment or physical promotion is inferred.

## 1. Typed state and nonidealities

The original centre-cone geometry remains13 complex vertices and20 cells. The mechanical model now has43 spatial point masses:13 original points plus30 housing points H_e. Housing masses are not new simplicial vertices. With internal scalar alpha and150 relative auxiliary coordinates,the total is3*43+1+150=280 configurations/560 phase variables;one extra scalar records heat.

Three additions are explicit:

1. Each branch compares d=y_a-(1+delta)y_b and returns the reciprocal force ratios. Ratio errors do not introduce active control.
2. Each of its two input ports has axial parasitic viscosity c_f/10,acting on actual member strain before the transmission. Incidence degrees5 and8 give effective radial/edge viscosities c_s=c_f/2,c_e=4c_f/5. All forces include their endpoint reactions.
3. Every shell edge has a3D housing point attached to its moving midpoint M_e=(X_i+X_j)/2 by an ideal pickup and positive isotropic spring. This is a defined housing-and-mount model,not a bound for arbitrary real casing or routing.

Let m_he be the housing mass in the parent's point-mass units. With total sum m_he=12 beta,

$$T_h=\frac1{2R^2}\sum_e m_{he}|\dot H_e|^2,\qquad U_h=\frac12\sum_e k_{he}|H_e-M_e|^2,$$
$$k_{he}=\frac{m_{he}}{R^2}\Omega_h^2.$$

Mass weights in the joint probes vary within±10% of their mean while preserving total mass. Stiffness scales with mass to keep the sameOmega_h;independent mount-stiffness scatter is outside this study. The pickup and zero-rest vector spring remain ideal attachment assumptions. Gear,casing and rotor modes outside this model are not covered.

For deltaH=H_e-M_e,the potential gives forces -k_he*deltaH on H_e and+k_he*deltaH/2 at each endpoint. Their total force and torque vanish. Added mount forces are not individually ordinary edge-axial forces;the three-point reaction balance is explicit.

The full energy balance is

$$\dot E=-\frac\gamma{10}\|\dot z\|^2-\frac{c_f}{10}\sum_{\text{branch inputs}}\dot y_p^2\le0.$$

E includes parent,relative auxiliary and housing kinetic/potential energies. Total spatial P,L include housings;the primary structure can exchange momentum with them. The old positive-length energy certificate survives because all added storage is nonnegative and initiallyzero. It does not certify coherence or orientation.

## 2. Exact bare-module joint bound

Use power-conjugate coordinates

$$u_c=(y_a+y_b)/2,\quad u_d=y_a-y_b,\qquad f_c=f_a+f_b,\quad f_d=(f_a-f_b)/2.$$

For v=(-delta,1+delta/2),the two-port force/velocity matrix is

$$Z_{\rm port}=Z(s)vv^T+\frac{c_f}{10}\operatorname{diag}(2,1/2),\qquad Z(s)=5\frac{2s+5}{2s^2+5s+50}.$$

It is reciprocal and passive. In particular,

$$Z_{cc}=\delta^2Z+c_f/5,\quad Z_{cd}=Z_{dc}=-\delta(1+\delta/2)Z,$$
$$Z_{dd}=(1+\delta/2)^2Z+c_f/20.$$

Common self-loss from ratio error is quadratic in delta;cross-coupling is first order. Measuring common loss alone cannot bound every unwanted response.

For1<=omega<=4,

$$\operatorname{Re}Z(i\omega)=\frac{1250}{4\omega^4-175\omega^2+2500},\qquad \frac{1250}{2329}\le\operatorname{Re}Z\le\frac{625}{362}.$$

The denominator decreases on this band:with x=omega²,8x-175<0 for x in[1,16]. Thus for |delta|<=1/100 and0<=c_f<=1/1000,exact fraction bounds give

$$\operatorname{Re}Z_{cc}\le\frac{1349}{3620000},\qquad \operatorname{Re}Z_{dd}\ge\frac{39601}{74528},$$
$$\frac{\operatorname{Re}Z_{cc}}{\operatorname{Re}Z_{dd}}\le\frac{3141821}{4479863125}\approx0.000701321,$$
$$\frac{|Z_{cd}|}{|Z_{dd}-c_f/20|}\le\frac2{199}.$$

These are continuous-band **bare-module impedance** bounds. The0.0702% number is a conservative dissipative diagonal ratio,not tetrahedral volume mismatch,probability or a whole-assembly guarantee. Component valuesmu,kappa,gamma are fixed at the declared nominal design;their independent tolerances are not included.

## 3. Symmetric mass-loading frequency bound

For uniform housing masses,ideal ratios and default primary symmetry,let X_i=(1+b)r_i and H_e=(1+c)M_e0. Define

$$\rho=|M_{e0}|^2/R^2=(5+\sqrt5)/10.$$

The exact collective equations are

$$\ddot\alpha+13\alpha-12b=0,$$
$$\ddot b+3b-\alpha+\beta\rho\Omega_h^2(b-c)+\frac52c_f\dot b=0,$$
$$\ddot c+\Omega_h^2(c-b)=0.$$

Ideal differential branches stay unexcited,while housing inertia changes frequencies and input friction dissipates breathing. For c_f0,the two low loaded eigenvalues lie below the parent ones by a Rayleigh trial c=b. Eliminating c belowOmega_h² yields effective added b-inertia beta*rho/(1-lambda/Omega_h²). Since8+sqrt37<15 andrho<3/4,for beta<=1/20 andOmega_h>=10,

$$\sqrt{68/71}\le\omega_{j,\rm loaded}/\omega_{j,\rm parent}\le1,\qquad j=1,2.$$

This bounds the downshift by2.136% for that symmetric conservative subsystem. It is distinct from a signal-retention or nonuniform mass tolerance theorem. At beta=.05,Omega_h10,the computed low-mode downshifts are1.639% and0.179%.

## 4. Joint probes and the housing counterexample

[RESULTS.md](RESULTS.md) records12 boundary,8 interior and4 out-of-budget challenge probes. The proposed preparation-dependent budget is |delta|<=1%,beta<=5%,c_f<=.001,Omega_h10 with the declared primary/housing scatter,A0=.1,u0..100. All20 in-budget probes pass the80%breathing-RMS/5%volume-mismatch/50%shape screen. They are finite development points;there is no continuous whole-assembly box certificate.

A subsequent [mount-mode addendum](MOUNT_MODE_ADDENDUM.md) exposes54 undamped housing modes with cancelling primary reactions. They are unexcited in the declared zero-housing-deviation preparation. A full560-phase counterexample retains housing energy despite positive device/input losses. Therefore this enlarged model does not give full transverse asymptotic relaxation. The previous190-coordinate theorem retains its original scope. A passive mount-loss mechanism and its common-breathing cost are the next required construction.

## 5. Reproduction and module test

```bash
python3 experiments/icosahedral-tolerances/bounds.py --out /tmp/tolerances
OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-tolerances/analyze.py --out /tmp/tolerances
OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-tolerances/mount_modes.py --out /tmp/tolerances
python3 experiments/icosahedral-tolerances/draw.py --source /tmp/tolerances --out /tmp/tolerances/tolerance-summary.png
```

The independent full trajectories use two CPU processes,not LLM delegation. DOP853 uses2001 samples,u0..100,rtol1e-10,atol1e-12;the selected refinement uses4001 samples,rtol2e-12,atol2e-14. The housing-only counterexample usesalpha0,u0..10,1001 samples,rtol2e-12,atol1e-15. Inputs,case arrays,baselines,results,exact bounds and figure are captured.

[MODULE_TEST.md](MODULE_TEST.md) specifies component calibration,power-conjugate drives,reciprocity/impedance gates,housing measurement and uncertainty. Its status isUNSCORED/NOT_EXECUTED. Unitst0,E_*,ell0 remain calibrated engineering choices,not a native UD physical map. A separate housing-only ringdown is now required to detect the unresolved sector.

See the [candidate](../../candidates/icosahedral-tolerances/candidate.json),[receipt](../../candidates/icosahedral-tolerances/mathematical_receipt.json) and[immutable run](../../artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/manifest.json). Historical ledgerQ139,Q144–145,Q151–152 remain read-only provenance for open clock/constitutive maps;their status is not promoted by this construction.
