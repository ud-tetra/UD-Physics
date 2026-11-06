# Finite nonlinear preparation margin v0.1

**EXACT / CONDITIONAL.** For the fixed prepared eta=1 Hamiltonian, take I=1, lambda=mu, phase zero and 31/5<=mu<77511/12500. If the initial Euclidean state error in V is at most 1/16000000, it remains at most 1/240000 through one native time unit. The continuously lifted phase error is strictly below 1/300000 rad over the same interval.

## Scope and provenance

Integrated base 234f54471c32cc9ad4873cd8042103fa19795909, stored research parent fca1a8afb36f7037b3917f88d58873823c2ab7f8, task clock-matrix-question-20261104, session clockmatrix-20261104-01 and held claim 72863501bd80db6aae1fd9b68467de48e92cb42c. Use the ascending Euclidean carrier V=h0-perp, J=A/2, prepared plane W and normal space N, and H=||x||²+lambda(Q+R) from [LOCAL_STABILIZATION.md](LOCAL_STABILIZATION.md). The reference z(s)=cos((2+mu)s)v+sin((2+mu)s)h has norm sqrt(2). The nearby trajectory uses the same autonomous Hamiltonian and native time s. Both can be evolved globally by coercivity and conservation of H. No physical time map or apparatus is assigned.

The one-unit horizon, I=1 and the 1/1000 bootstrap radius are sufficient design choices. The coefficient bounds were inherited and the replay checks the resulting rational margins. No empirical fitting enters the calculation. Independent review and physical calibration remain OPEN.

## Two-time linear control

Write d=77511/12500−mu>0, which is a known lower bound on the distance to the first critical coupling. For T>0 choose an integer m>=ceil((2+mu)T/pi). Set

    C = min(51/(10 sqrt(d)), 1+(12/25)m),
    A_T = max(50, 8 C, 1+2mu T),
    K_T = max(500, 64 C, 1+2mu T).

These bound the linear evolution Phi(s,0) and Phi(s,u), respectively, for 0<=u<=s<=T in the full V space. The derivation uses the following facts.

1. W and N reduce the variational equation. Invariance of W makes the symmetric Hessian preserve W along z. The skew J preserves W and its orthogonal complement in V. On W the explicit nonlinear orbit rotates at 2+lambda I. Differentiation gives, after orthogonal rotations, a shear of magnitude 2mu(s−u). This gives the norm bound 1+2mu T.
2. On the critical normal planes the sampled gain through m half-returns is bounded by C using both the peak bound and the finite-return bound from [NEAR_THRESHOLD.md](NEAR_THRESHOLD.md). On the other planes the sampled gain is less than 5.
3. Write U(r) for the phase-zero linear normal evolution within a half-period. The critical-plane logarithmic norm integrates to 3 pi rho/4<2, giving ||U(r)||<8. For the first noncritical plane the diagonal difference has absolute value at most cos²(theta)/2+2sin²(theta), and the off-diagonal term has absolute value |cos(theta)sin(theta)|, before multiplication by rho. Integrating half the diagonal bound plus the off-diagonal bound over [0,pi] gives rho(5pi/8+1)<9/4. The second plane gives rho pi/4<9/4. Thus both have ||U(r)||<10. The inverse has the same Euclidean norm on each plane by determinant one.
4. With theta(s)=n_s pi+r_s, the two-time normal map is U(r_s) U(pi)^(n_s−n_u) U(r_u)^(-1). The integer difference is at most m. This accounts for both endpoint factors in K_T and just one in A_T. The orthogonal splitting gives the maximum across planes and W.

The finite-return alternative in C keeps the certificate bounded at fixed T as d approaches zero. A phase-zero all-time bound alone would not justify replacing K_T by A_T in the forced problem.

## Quadratic remainder and comparison

Write e=x−z and F(x)=J grad H(x). On the tube ||e||<=R0=1/1000,

    e' = DF(z)e + r,
    ||r|| <= lambda(18||z||+6||e||)||e||² < 160||e||².

Indeed the Hessian B(x) of Q+R is homogeneous quadratic and obeys ||B(x)||<=18||x||² by [CERTIFIED_INTERVAL.md](CERTIFIED_INTERVAL.md) §5. Its symmetric bilinear polarization has norm bounded by 18||x||||y||, by the quarter-difference formula on unit vectors and the parallelogram identity. Thus ||B(z+t e)−B(z)||<=18(2t||z||||e||+t²||e||²). Integrating its action on e from t=0 to 1 gives the stated remainder. J has norm one on V, and mu<=621/100 and sqrt(2)<10/7 give the rational constant 160.

For initial error epsilon>0, variation of constants gives

    ||e(s)|| <= A_T epsilon + 160 K_T integral_0^s ||e(u)||² du.

The right side is a scalar majorant y with y'<=160 K_T y² and initial value A_T epsilon. Integrating the reciprocal gives y<=A_T epsilon/(1−160 K_T A_T epsilon s) while the denominator is positive and the solution stays in the tube. Consequently the sufficient preparation gate is

    epsilon <= min(R0/(2 A_T), 1/(640 K_T A_T T)).

It gives ||e(s)||<= (4/3)A_T epsilon <=2R0/3, closing the tube by continuity. The zero-error case is the reference solution by uniqueness. The bounds are finite-time and conservative.

## Concrete one-unit contract

For T=1, m=3 suffices using pi>3 and 2+mu<=821/100. The finite cap gives A_T=50 and K_T=500, since 8(1+(12/25)3)<50, 64(1+(12/25)3)<500 and 1+2mu<50. The preparation gate is 1/16000000 and its state bound is 1/240000. The two-coordinate readout (v^T x/2,h^T x/2) deviates from the unit reference circle by at most ||e||/sqrt(2). The disk tangent bound gives a phase deviation at most arcsin(||e||/sqrt(2)), with the lift chosen near the reference at time zero. No readout zero is reached. The exact inequalities 1/sqrt(2)<3/4 and sin(t)>=t−t³/6 at t=1/300000 certify the strict phase tolerance.

Replay with python3 experiments/clock-matrix-question/nonlinear_margin.py. This is an initial-state error contract. Coefficient drift, detector error, all-time nonlinear stability, and calibration remain OPEN. Physical promotion is zero.
