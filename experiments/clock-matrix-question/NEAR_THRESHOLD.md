# Gain and growth near the first transverse threshold v0.1

**EXACT / CONDITIONAL.** In the fixed prepared eta=1 linear transverse model, let delta=|mu−mu_*| for mu in [31/5,621/100]. Below the threshold the supremum of the Euclidean gain sampled at half-returns lies between (47/10)/sqrt(delta) and (51/10)/sqrt(delta). The continuous-time supremum lies between (47/10)/sqrt(delta) and 41/sqrt(delta). Above the threshold the maximal growth exponent per unit native time lies between sqrt(delta)/4 and (27/100)sqrt(delta).

## Scope and evidence

Integrated base d65c8a27637d3bd73cc855e8fb1173b7e98ce6af, prior discovery head e762e5f559bceb65f63929cfc72e9c8bce10ab62, task clock-matrix-question-20261104 and session clockmatrix-20261104-01 under held claim 72863501bd80db6aae1fd9b68467de48e92cb42c. The prepared plane, ascending Euclidean basis, eta=1 coefficients, transverse projector, and initial phase zero are inherited from [STABILITY_BOUNDARY.md](STABILITY_BOUNDARY.md). Mu=lambda I and rho=mu/(2+mu) are dimensionless. Native time s has phase theta=(2+mu)s. The previous certificate gives 77511/12500<mu_*<62009/10000, three identical critical planes, and two other types of noncritical planes. Independent review and physical calibration remain OPEN. Physical promotion is zero.

The rational envelope constants were selected after inspecting the earlier quarter-orbit enclosure. They are sufficient bounds with slack. The replay verifies them over the whole window using the prior outward-rounded Taylor integrator, eight-node Bernstein interpolation, and its uniform function and derivative remainders. Model coefficients are fixed.

## Quarter-orbit margins

For each reduced plane H=[[a,b],[c,d]] is the fundamental map over [0,pi/2] in phase. Reversibility gives the half-return

    U = (2ad-1)Id + V,
    V = [[0,B],[C,0]], B=2bd, C=2ac,
    det H = ad-bc = 1.

On the critical plane the replay verifies b in (−83/50,−33/20), d in (−18/125,−143/1000), and da/drho in (11/20,14/25). Over the same window d rho/d mu is between 1/34 and 1/33. Since a(mu_*)=0, the mean value theorem gives k_lo delta <= |ad| <= k_hi delta, where k_lo=1573/680000 and k_hi=84/34375. Also 47/100<B<12/25 and |C|<B, so ||V||₂=B. These margins apply to all three identical critical planes.

## Gain below and at onset

Put q=ad>0 below the threshold and phi=2 asin sqrt(q). Then V²=−sin²(phi) Id, and the exact powers are

    U^n = (−1)^n [cos(n phi) Id − sin(n phi) V/sin(phi)].

For any n>=0 their norms are at most 1+B min(n,1/sin(phi)). Taking n nearest to pi/(2 phi) yields |sin(n phi)|>=cos(phi/2)=sqrt(1−q). Acting on the second unit vector at that sample gives norm at least B/(2sqrt(q)). Thus the sampled supremum is between B/(2sqrt(q)) and 1+B/(2sqrt(q(1−q))). Substituting the verified margins and delta<1/100 gives the stated (47/10,51/10) constants. The other reduced planes have sampled gain <5 by the same upper formula using their verified entry boxes and ||V||₂=max(|B|,|C|). The full normal splitting is orthogonal, so its operator norm is the maximum of the block norms.

Within a half-period the Euclidean logarithmic norm on the critical plane is rho(1+sin²(theta))/2. Its integral is 3 pi rho/4<2, giving intra-period gain <8. On each other plane the logarithmic norm is at most 3rho/2, from the diagonal difference and off-diagonal entry of the symmetric Hessian in its 2D basis. Its integral is <4, giving gain <64. Combining with the sampled bounds yields the continuous-time bound 41/sqrt(delta).

A near-peak sample occurs on the scale delta^(-1/2). More precisely, the choice of n above obeys |n−pi/(2phi)|<=1/2. If k_* = −d(mu_*) a_mu(mu_*)>0 and B_*=B(mu_*), then the limit of sqrt(delta) times the sampled gain supremum is B_*/(2sqrt(k_*)). At threshold U=−Id+V with V²=0, so U^n=(−1)^n(Id−nV). The limiting slope of ||U^n||₂/n is B_* in (47/100,12/25).

## Growth above onset

For q=−ad>0 the half-return multipliers are −exp(±ell), with

    ell = arcosh(1+2q) = 2 asinh sqrt(q).
    gamma = (2+mu) ell/pi.

Here ell is the expanding log modulus per half-return and gamma is its Lyapunov exponent in native time, attained on an expanding Floquet direction. Periodic intra-period evolution and the stable noncritical blocks preserve that maximal exponent. The scalar inequality x/sqrt(1+x²)<=asinh(x)<=x for x>=0 follows by integrating its derivative. With the same rational margins this gives (12/125)sqrt(delta)<=ell<=(1/10)sqrt(delta). The native rate conversion yields sqrt(delta)/4<=gamma<=(27/100)sqrt(delta). The limits of ell/sqrt(delta) and gamma/sqrt(delta) at onset from above are 2sqrt(k_*) and 2(2+mu_*)sqrt(k_*)/pi, respectively.

The theorem concerns linear transverse perturbations from the prepared orbit. Nonlinear saturation and operational error budgets near the threshold remain OPEN. Replay with python3 experiments/clock-matrix-question/near_threshold.py.
