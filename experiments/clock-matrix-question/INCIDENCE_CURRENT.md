# Transport current from incidence continuity v0.1

**EXACT / CONDITIONAL.** The displacement-weighted Q170 stock current per unit total scalar-lane stock equals the group velocity on a positive-frequency mode. It vanishes bond by bond on both prior zero-speed controls. For the matched localized packets its spatial sum distinguishes the two transport speeds.

## Native current and added position readout

Discovery parent 11a5448d070c867ebc644f55646ff75a065b14ef. Retain [Equal-frequency packets v0.1](ISOSPECTRAL_CLOCK.md) and the controls of [Edge-class incidence clock v0.1](EDGE_CLASS_CLOCK.md). Historical coefficient ledger v0.39(2), Q166/Q169/Q170, supplies signed incidence products, the skew generator, and the control-volume stock balance. For the scalar lane take u'=Bp and p'=−B* u, with the unit metric and B's oriented edge column −1 at tail and +1 at head. The complex representation is two real quadratures with summed squared stock. Use native dimensionless time and either periodic boundaries or the infinite lattice with finite-first-moment states and summable current.

For a vertex v incident on edge e the outgoing current is F(v→e)=−2Re(conj(u_v) B_ve p_e). Its contribution to vertex stock is −F and to edge stock is +F. Internal currents cancel on a control volume. For each directed translation edge from r to r+d, assign the edge stock to r+d/2 and the vertex stock to its lattice site. These positions are an explicit readout choice. The displacement-weighted contribution from the two incidence bonds on that edge is

    d Re[(conj(u_r)+conj(u_{r+d})) p_e].

Sum over the edges and divide by conserved N=Σ|u|²+Σ|p|². On the infinite lattice this is the time derivative of the normalized stock centroid. On a periodic torus the same sum uses the local displacement lift across the seam and is an oriented flux readout, not a derivative of a wrapped centroid. Norms below use the already declared G=Id/2−11ᵀ/8; there is no physical distance or clock calibration.

## Exact mode reduction and controls

For u_{r+d}=exp(i k·d)u_r and ω>0, the positive-frequency quadrature is p_e=−i(exp(i k·d)−1)u_r/ω. The expression above is 2d|u_r|² sin(k·d)/ω. The edge and vertex stock per mode are equal because Σ_d|exp(i k·d)−1|²=ω². Thus the normalized current vector is Σ_d d sin(k·d)/ω=∇_kω. This equality derives the observable from incidence stock flow before comparing it to dispersion. For a scalar packet, Parseval makes the global current the stock-weighted mean of this vector. Reversal changes its sign.

At k=(π,0,0) and k=(π,π,π), ω=4 and every edge phase is ±1. Each edge quadrature is purely imaginary relative to the real vertex phasors, so all 14 oriented incidence currents per cell vanish for each control. This differs from the longer-edge stock loading, which split the clocks on the same controls. A superposition can have zero net current while its components carry opposing currents. The norm of the summed current and a local current intensity are different observables.

## Replay and scope

The NumPy replay builds the currents from the complex incidence products and independently compares them to the differentiated symbol at both quadrature orders of the existing matched-packet construction. The maximum component difference is below 4×10⁻¹⁶. The G-norms of the mean current are approximately 0.35776934 and 0.50363698, with opposite vectors under reversal. The pi controls also use exact sign characters and integer division by the power-of-two ω. The proof gives the exact relations. The packet values are numerical quadrature.

Reproduce with `python3 experiments/clock-matrix-question/incidence_current.py`. The observable passes the declared transport checks. A local rule for coupling it to the internal rotation remains open. Inserting the norm of this global sum by hand would assume the functional dependence and would respond differently to a counterpropagating superposition than to separated local currents. Physical promotion 0. Independent review NOT_RUN.
