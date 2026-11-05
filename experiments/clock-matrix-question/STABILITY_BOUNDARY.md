# First transverse loss certificate v0.1

**EXACT / CONDITIONAL.** For the fixed prepared eta=1 clock, the first loss of bounded linear transverse evolution occurs at a unique coupling `mu_*` in `(77511/12500, 62009/10000)`. The third reduced system contributes three identical nontrivial Jordan blocks at half-return multiplier −1 at the threshold. Immediately above it, those blocks have distinct real reciprocal multipliers, one with modulus greater than one.

## Scope and provenance

This calculation resumes task clock-matrix-question-20261104 and session clockmatrix-20261104-01 under held claim 72863501bd80db6aae1fd9b68467de48e92cb42c. Its integrated base is 738b9d205fd9f9735a05d4976de70f1519474bff and its prior discovery head is c48a78b8f803fadce8d1b0779a05eb2b6b2fc1e3. It uses the prepared plane, Hessian, J, projector P, and ascending Euclidean simplex conventions in [CERTIFIED_INTERVAL.md](CERTIFIED_INTERVAL.md) and the certified initial interval in [FOURIER_INTERVAL.md](FOURIER_INTERVAL.md). The earlier scan exposed instability at mu=8. An exploratory floating scan suggested the bracket near 6.2 and the block decomposition. The certificate uses exact matrix identities and outward-rounded rational enclosures. No model coefficients are fitted. The claim concerns the 12-dimensional linear transverse space and native phase theta. Physical promotion is zero.

## Exact invariant planes

Write the squared frequency labels of the averaged generator T as a in {19/256,35/64,3/64}. The exact replay constructs the candidate projector as the product of P with (T²+bP)/(b−a) over the other two labels b. Within its image it constructs mutually orthogonal pairs (v,Jv) by rational Gram–Schmidt, using projected coordinate seeds and the indicated Hessian filters in the code. It verifies nonzero equal norms in each pair and intertwines each of J and the three compressed Hessian coefficients with the following two-dimensional blocks. The six pairs exhaust the rank-12 range of P.

| Block | Multiplicity | Bc diagonal | Bs diagonal | Bx off-diagonal |
|---|---:|---|---|---:|
| 1 | 1 | (3/2,1) | (1,3) | 1 |
| 2 | 2 | (0,0) | (1,0) | 0 |
| 3 | 3 | (0,1) | (1,3) | 0 |

All Bx diagonals vanish, and all pairs use J2 = [[0,−1],[1,0]]. The common norm within a pair gives an orthonormal basis after one scalar normalization. Repeated blocks therefore remain independent even when multipliers coincide.

## Trace and crossing criterion

Set rho=mu/(2+mu) and A(theta)=J2[(1−rho)Id+rho B(theta)]. With D=diag(1,−1), the listed blocks obey A(pi−theta)=−D A(theta) D. If H=[[a,b],[c,d]] is the fundamental matrix from theta=0 to pi/2, the half-return over [0,pi] is D H^-1 D H. Trace A=0 implies det H=1. Direct multiplication gives

    U = [[ad+bc, 2bd], [2ac, ad+bc]]
    trace U = 4ad−2 = 2+4bc.

The sign test ad>0 and bc<0 gives −2<trace U<2. A real determinant-one 2×2 map in this open range is diagonalizable over C with conjugate unit multipliers. Its integer powers and the intervening phase evolution are bounded at each fixed parameter.

The verified signs for blocks 1 and 2 hold through mu=621/100. Block 3 is strictly elliptic from 1/64 through 31/5. On the final bracket b<0, c>0 and d<0, while a increases strictly with rho and changes from negative to positive. Thus a=0 has exactly one root in the bracket. At it, U=[[-1,2bd],[0,−1]] with bd>0, so powers grow linearly. Above it through the upper endpoint the trace is below −2 and powers grow exponentially in the expanding direction. Two further outward-rounded evaluations at mu=77511/12500 and 62009/10000 give a<-1/10000000 and a>1/10000000, respectively. The monotonicity certificate therefore tightens the threshold to this open bracket, of width 1/50000. Since the prior certificate covers 0<mu<=1/64, these checks cover every smaller positive parameter. The zero-coupling transverse equation is orthogonal. Boundedness here is pointwise in the parameter. A uniform gain up to the threshold is outside this certificate.

## Validated enclosures

Use x=2 theta/pi for the quarter-orbit segment x in [0,1]. The replay encloses pi by the alternating Machin arctangent series. It encloses cos(pi x) and sin(pi x) at the Taylor centers using degree-80 Maclaurin expansions and the real Taylor bound (16/5)^81/81! < 2^-100. Every interval operation uses integer endpoints on a binary grid of step 2^-100 and rounds outward. The Taylor coefficients of the local fundamental matrix satisfy Y0=Id and (k+1)Y_(k+1)=sum_(j=0)^k A_j Y_(k-j) in the rescaled step variable.

In the complex disk of radius 1/4 about any real x in [0,1], the absolute values of cos(pi x) and sin(pi x) are at most cosh(pi/4)<3/2. The latter follows by bounding the positive cosh series at 4/5 using the successive-term ratio after the quadratic term. In the x coordinate the row-sum norm of the generator is bounded by (pi/2)(17/4)<10, from the three displayed blocks, the mean of Bc and Bs, and the cosine and sine coefficients (Bc−Bs)/2 and Bx/2. Integrating from the center along a complex radial segment bounds the fundamental matrix norm by exp(10/4)<16. Cauchy's estimate therefore bounds the tail beyond degree 28 on a step of length 1/16 by 16(1/4)^29/(1−1/4) for each entry. The replay adds that tail to every local map before multiplying the 16 maps.

For the parameter interpolation, in the real theta coordinate the generator row-sum norm is at most 4 and its rho derivative has norm at most 5, directly from the displayed blocks. The propagator composition bound and the ordered derivative integrals give an entrywise bound on the kth rho derivative divided by k! of exp(2pi)(5pi/2)^k/k!, bounded by 1024(55/7)^k/k!. On each rho cell of width w the eight rational nodes enclose a degree-seven interpolant. Its Bernstein coefficient intervals bound its values by convexity. The interpolation remainder is at most M8 w^8 with Mk the preceding divided derivative bound. On the crossing cell the derivative of that remainder is bounded by 8 M8 w^7 + M9 w^8. Indeed the remainder is the product of eight node differences times a divided difference. Differentiating that divided difference repeats the evaluation argument, and the repeated-node divided difference is bounded by M9. The derivative interpolant is enclosed by the consecutive Bernstein differences times 7/w.

The replay confirms a sign margin greater than 1/100000 on all cells preceding the crossing for block 3 and through the upper bracket for blocks 1 and 2. On the crossing cell it verifies the other three signs, a derivative da/drho greater than 1/2, and opposite endpoint signs for a. Replay with `python3 experiments/clock-matrix-question/stability_boundary.py`. Independent review, nonlinear all-time orbital stability, calibration, and stability at parameters beyond this first crossing bracket remain OPEN.
