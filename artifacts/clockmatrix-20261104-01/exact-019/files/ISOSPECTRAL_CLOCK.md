# Equal-frequency packets at different speeds v0.1

**EXACT / CONDITIONAL.** The native scalar dispersion admits different group speeds at equal frequency. Two narrowband localized preparations can have exactly the same frequency law and different centroid speeds. The fixed Laplacian clock coupling gives the same global internal phase for both.

## Carrier and exact witnesses

Discovery parent f18643626689388efb81c36618beb6b24be7ff32. Retain [Fixed Laplacian coupling v0.1](LAPLACIAN_CLOCK.md), including λ=1/128 and the unit-metric scalar incidence lane. Use the infinite periodic lattice, positive-frequency scalar propagation, and the fixed conditional distance convention G=Id/2−11ᵀ/8 from [BCC observation and causality](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/Docs/UD%20BCC%20observation%20clock%20and%20causality%20audit.md), Dimensionless clock and distance. Speeds are in these lattice distance units per dimensionless native time.

Write t(k)=ω²=2Σ_d(1−cos(k·d)) over the seven nonzero binary triples. Group velocity is ∇ω. Take k_A=(a,0,0), cos a=−93/125, and k_D=(b,b,b), cos b=3/5, with both angles in (0,π). At A, t=8(1−cos a). At D, the binomial identity gives t=16−4(1+cos b)²(2cos b−1). Both equal 1744/125. Their velocity vectors are respectively (4,2,2) sin(a)/ω and (1,1,1)(384/125)/ω. Hence their squared G-speeds are 16/125 and 3456/13625. The difference is exact in the declared metric. These central modes alone are plane waves.

## Matched localized preparation

Use local charts (t,y,z)→(x,y,z) and (t,y,z)→(x,x+y,x+z), solving x by the specified t on each branch. Both ∂t/∂x are positive at their centers, so the inverse function theorem supplies both charts on a common neighborhood. Push the same normalized compact smooth-enough density in (t,y,z) through both charts. Use the nonnegative square root of the resulting k-space densities as the two initial spectral amplitudes, with zero spectral phase and identical internal register. The change-of-variables factor in the squared amplitude is |∂t/∂x|. For sufficiently small supports, the amplitudes are square-integrable and differentiable with square-integrable derivative, giving localized finite-second-moment states. Continuity preserves distinct centroid speeds as supports shrink around the exact witnesses.

For the decoupled positive-frequency branch the centroid velocity is the mean of ∇ω, by the Fourier position operator i∂k. For the coupled branch it is also the total vertex-stock centroid velocity: the two circular components have equal stock and their opposite λ∇t additions cancel. Speed here is the G-norm of this mean vector. The global internal contrast with baseline removed is the expectation of exp(2iλts), hence exactly identical for the two preparations at every s. Phase equality applies where contrast is nonzero. This distinguishes frequency detuning from any nonconstant universal rate law of centroid speed that predicts different readings for these speeds. It does not rule out other transport–clock interactions.

## Numerical replay

Use product density proportional to (1−p²)^4(1−u²)^4(1−v²)^4 on [−1,1]³, t=1744/125+p/20, y=u/100 and z=v/100. Use Gauss–Legendre orders 8 and 16 per dimension and solve chart coordinates by bisection. This integrates the spectral representation directly, without a finite spatial grid or a moving window. Both orders agree at the shown precision. Order 16 gives centroid speeds 0.35776934 and 0.50363698, and squared-frequency reconstruction error below 9×10⁻¹⁵. At s=12 the shared internal phase residual is 327/250 rad and contrast is approximately 0.99999600. The phase value follows exactly for the prescribed symmetric t density because the centered characteristic function is real and positive at this time. No coupling coefficient or distance metric was fitted to this result. A spatially restricted detector and a clock interaction with independent sensitivity to speed remain open. Physical promotion 0. Independent review NOT_RUN.

Replay with NumPy and `python3 experiments/clock-matrix-question/isospectral_clock.py`.
