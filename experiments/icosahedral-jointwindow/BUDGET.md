# Candidate computational budget v1.0

This is an engineering FIT inside the declared surrogate. It is **not** a manufactured tolerance specification or a continuous nonlinear uncertainty-box certificate. Definitions/proofs: [README](README.md); evidence: [RESULTS](RESULTS.md).

| Quantity | Declared range/preparation | Evidence scope |
| --- | --- | --- |
| Housing-loss strength nu | [1/25,1/20]=[.04,.05] | Numerical continuous-strength enclosure for50 finite parameter sets,all180 housing initial phase coordinates,using analytic interpolation inequalities |
| Nominal housing mass fraction beta | [1/200,1/20]=[.005,.05] | Qualified design range;parameter cases are finite;smaller positive beta retains a separate limiting analysis |
| Input friction c_f | [0,1/1000] | Zero explicitly included;finite parameter tests |
| Housing mount frequency Omega | 10 | Fixed assumption;independent frequency/stiffness errors excluded |
| Primary m_i,g_i | [.95,1.05] | Finite scattered cases;exact compliance bound holds throughout the continuous g box and for positive masses |
| Primary edge k_e | [19/50,21/50] | Finite scattered cases;exact compliance bound holds throughout the continuous k box |
| Reciprocal gain1+delta | [.99,1.01] | Defined reciprocal force return;finite patterns,not a continuous error-box enclosure |
| Housing weights w_e | [.9,1.1],mean1 | Finite patterns;fixed-primary linear energy bound holds throughout this continuous weight box |
| Initial primary pulse | alpha=1/10,reference points,zero primary/relative velocities | Target-informed engineering preparation;physical alpha implementation OPEN |
| Additional housing energy | E_h<=E_p/40000 | Exact all-phase readout inequality in the linearization;finite nonlinear worst-ringdown phases at equality |
| Time window | u in[0,100],T=100 ringdown gate | Dimensionless;physical t0 uncalibrated |
| Housing ringdown gate | <=1/2 total mechanical energy remaining from housing-only initial states | Full180-dimensional initial phase operator norm,including conserved rigid kinetic energy;finite nonlinear housing-only checks |
| Breathing gate | RMS>=4/5 matching original undamped/nohousing RMS | Linear all-phase sufficient inequality;separate nonlinear endpoint preparations |
| Volume/shape gates | hub mismatch<=1/20;residual absolute shape RMS<=1/2 original | Finite nonlinear endpoint tests only |

There are56 case records but50 distinct coefficient sets. The nonlinear endpoint family has32 records per strength,with exact duplicates reused;do not count aliases as additional independent evidence. Linear and nonlinear baselines/readouts are separate. The worst linear ringdown phase need not be the worst nonlinear volume phase.

The old nu=.02,beta=.005,c_f=0 failure remains valid. The new interval is an explicitly different design choice;the original model/results are preserved. A compact positive mass interval permits an existential uniform local decay rate,while no positive full-assembly rate is uniform as beta tends0 with bounded nu and c_f=0. Neither statement supplies a quantitative nonlinear box guarantee.

All120 massless struts,anchors and routing remain idealized. Use the [existing mount-test plan](../icosahedral-mountloss/MOUNT_TEST.md) only after actual geometry,masses,compliance and viscosity are measured. Physical status: **UNSCORED / NOT_EXECUTED**. Mainline promotion:0.
