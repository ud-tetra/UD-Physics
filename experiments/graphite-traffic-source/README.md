# Typed traffic and contractible-route test for the graphite source

**EXACT / CONDITIONAL construction; graphite identification OPEN.** This is a target-blind follow-up to the [Q24 exchange-parity gate](../graphite-route-parity/README.md). It supplies an explicit *development candidate* state/update and tests two common shortcuts: treating bare transition rates as transport weights, and treating a local circulation as a harmonic source. It does **not** claim that the current UD theory selects this stochastic law, a physical clock, or the measured graphite friction.

The supplied *UD coefficient provenance ledger v0.39(2)* (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) marks Q24 conditional and Q25/Q26 open. Its Q170–Q179 conserve or allocate native support, but do not derive these rates. The current [UD local-source selection note](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/docs/UD_Local_Source_Selection_v0.1.md) supplies a separately chosen contact gate and uncalibrated model time; the [positive-stock construction](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/docs/UD_Positive_Stock_Balanced_Recovery_and_Predictive_Switching_v0.1.md) explicitly declares constitutive dissipation and load kinetics. Neither source equates its coefficients with graphite Q24. No microscopic packet-to-route derivation is imported here.

## One complete candidate source process

Let `G` be a finite graph with oriented edges, populations `p_i(s)≥0`, `Σ_i p_i=1`, and nonnegative transition rates `k_ij` per **dimensionless internal time** `s`. A continuous-time master equation defines the update

`dp_i/ds=Σ_j(p_j k_ji−p_i k_ij)`.

It preserves total stock and positivity. Define *directed traffic* `T_ij=p_i k_ij≥0` and net current `J_ij=T_ij−T_ji=−J_ji`. As a **proposed** completion of the ledger's notation, set `w_ij=T_ij` and let `Ξ_ij=σ_ij=−σ_ji`, a fixed unit orientation sign. In Q24's candidate,

`c_ij=(η_O/2)(T_ij σ_ij+T_ji σ_ji)=(η_O σ_ij/2)J_ij`.

This is exchange-even and zero at **edgewise detailed balance** `T_ij=T_ji`. Merely having a stationary distribution `dp/ds=0` does not impose edgewise balance on a graph with cycles. The normalizations `Σp=1` and `|σ|=1` eliminate a trivial source-scale ambiguity; `η_O`, graph choice, the rates, initial/boundary state and the physical energy/length/time map remain unspecified. Using a Markov process adds irreversibility absent from a closed skew Hodge–Dirac carrier. It is a declared open-system hypothesis, not a consequence of native support conservation.

## Rate versus traffic: exact equilibrium counterexample

On a two-vertex edge take `k_01=2`, `k_10=1` per internal time. The unique stationary populations are `(p_0,p_1)=(1/3,2/3)`, so both actual directed traffics equal `2/3` and `J_01=0`. With `η_O=σ_01=1`, the traffic-typed Q24 coefficient is **0**. Substituting the bare rates as `w` instead gives `c_01=(2−1)/2=1/2`, an apparent source at a reversible equilibrium with no transport current. This does not prove Q24 must use traffic for every Hamiltonian interpretation; it shows that **if** Q24 is claimed to read transport current, its `w` cannot silently mean bare rate. Q25's notation collision has observable consequences.

On a three-state ring with clockwise rate `a=2`, reverse rate `b=1`, and uniform `p_i=1/3`, the process is stationary but each oriented edge has `J=(a−b)/3=1/3`, hence `c=1/6` for `η_O=σ=1`. A stationary circulating source is possible in this **externally chosen** Markov model. Its dimensionless steady entropy production is `(a−b)ln(a/b)≥0` per internal time, not a graphite heat rate. No upper-face or moiré size is selected.

As an optional smooth speed-drive model, choose dimensionless `u=v/v_*`, `a(u)=r exp(ζu/2)`, `b(u)=r exp(−ζu/2)`, with `r>0`. For the ring, `c(u)=η_O σ r sinh(ζu/2)/3 = η_O σ r ζ u/6+O(u³)`. This reproduces the previous conditional zero-speed source and, **only if** the independently assumed frozen passive material map applies, its `Γ_add=O(v²)` and `F_add=O(v³)`. Parameters `r,ζ,v_*` are **assumed**, not extracted from the reported angle or load trend. The exponential law is a proposed preparation, not a native update theorem.

## A second obstruction: a face current is not a harmonic winding

On each periodic honeycomb quotient `(m,n)=(2,1),(3,1),(3,2)` with `N=7,13,19`, let `B₁:C₁→C₀`, `B₂:C₂→C₁`, and let the two harmonic edge columns of `M` satisfy `B₁M=0`, `B₂ᵀM=0` in the unit edge metric. A current circulating around any contractible hexagonal face is `J=B₂ f` for a face 2-chain `f`. It is divergence-free but has **exactly zero** harmonic projection:

`B₁J=B₁B₂f=0`, `MᵀJ=MᵀB₂f=0`.

The exact replay constructs one six-edge face at each N and checks both identities. A noncontractible winding current can have nonzero harmonic projection, but a local loop by itself cannot populate the two-dimensional harmonic channel. The Q24 `c_ij` is an **exchange-even edge scalar**, not automatically the signed current `J` or the earlier port weight `W`; the zero projection applies if a proposal identifies its *edge-chain input* with `J=B₂f`. An explicit cross-Hessian map is needed to test any other identification. Even a nonzero harmonic winding would exist at N=7,13,19 under a shared local law; it would not alone explain the seven-cell peak.

## Physical and empirical gate

To develop this candidate further, derive `k_ij` and route `σ` from actual UD packet/contact dynamics, specify how physical sliding drives the rates, and check detailed balance or its breaking under reversal. Then identify the material cross-Hessian, complex damping, conventional PES/contact readout and physical time. Freeze that map across the paired angles and N=13/19 controls before inspecting signed force and load data. A local Markov circulation or its entropy production is not friction without this bridge. Independent physics review NOT_RUN; physical promotion 0.

Run `python3 experiments/graphite-traffic-source/replay_traffic.py`; see the [mathematical receipt](../../candidates/graphite-traffic-source/mathematical_receipt.json) and [immutable capture](../../artifacts/graphtraffic-20261024-01/exact-001/manifest.json).
