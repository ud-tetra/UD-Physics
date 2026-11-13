# Separate internal phase on the directional packet v0.1

**EXACT / CONDITIONAL.** The decoupled transported clock and the stationary-centroid reference have identical internal rates. The moving phase readout cancels the scalar carrier phase pointwise. This supplies a null and a readout control.

## Model and match

Discovery parent 2e94035ea548242a97d01d361b761014d36acc7a. Retain [Directional packet v0.1](DIRECTIONAL_PACKET.md) for the periodic scalar generator and directional preparation. Add a declared two-channel internal register with J=[[0,−1],[1,0]] and Ω=2, matching the isolated [prepared plane](PREPARED_PLANE.md) at λ=0 in its normalized basis. This product register is an added model, with no native coupling claimed.

On the unit-metric periodic scalar chain space tensored with the two real internal coordinates, use the autonomous skew generator A_scalar⊗Id+Id⊗ΩJ. Periodic boundaries, no drive, native dimensionless time s. Norm is conserved. The complex representation encodes real solutions with two propagation quadratures and is used for the analytic vertex readout. Initial state is a scalar launch tensored with (1,0). Moving launch uses the width 9/50 packet. The reference is the normalized coherent sum of that spectrum and its reflection. The lobes are disjoint and ω is even, so both preparations have exactly the same normalized frequency distribution and equal norms. The reference has zero centroid by reflection, with oppositely directed components and a different spatial profile. It is a stationary-centroid reference, not a single spatially immobile pulse.

## Exact null and readout

The two generator terms commute. At any vertex the channel pair is (a,b)=u(r,s)(cos Ωs,sin Ωs), with scalar envelope u. Form the centroid using |a|²+|b|². In any nonnegative observation window with nonzero stock, compute

    C = Σ_r W(r) [|a|²−|b|²+2i Re(a* b)],
    N = Σ_r W(r) [|a|²+|b|²].

Substitution yields C/N=exp(2iΩs). The carrier phase cancels, including any dispersive distortion of u. The readout resolves internal phase modulo π, with a lift fixed by initial phase zero and steps satisfying |Ω Δs|<π/2. This cancellation follows from product preparation and identical scalar propagation in both internal channels. Entangling coupling or unequal channel calibration changes the result. Independent clock rate means separate model coordinates and readout here. The measured rate is fixed by the added generator and cannot establish a speed law.

## Constructor replay

The numerical replay evolves the two circular components at ω±Ω separately on a 97³ torus. It reconstructs the two internal channels, computes the total vertex-stock centroid, and reads C/N through a Gaussian window centered at each measured centroid. It samples 25 times spaced by 1/2 through s=12. The moving branch has nonzero displacement and the reference centroid stays at zero to roundoff. The lifted phase difference stays below 10⁻¹² rad. For an injected moving-branch detuning of +1/32 per native time, the recovered difference at s=12 is 3/8 rad to the same tolerance. Injection is a readout control, not a motion mechanism. The smallest weighted window-stock fraction was approximately 0.00154 across the three runs. The centroid window can sit between the reference lobes. The normalized contrast therefore measures ideal phase alignment and supplies no noise-robustness guarantee. See the JSON for actual residuals and window stock.

Reproduce with `python3 experiments/clock-matrix-question/internal_phase_null.py` and NumPy. There is no physical calibration, external test or non-constructor review. Physical promotion 0.
