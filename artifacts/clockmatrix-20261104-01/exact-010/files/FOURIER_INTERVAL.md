# Fourier and Cayley stability certificate v0.1

**EXACT / CONDITIONAL.** The fixed eta=1 modified clock has all-time linear transverse gain at most 8 for every 0 < mu = lambda I <= 1/64 at reference phase zero. The prior finite nonlinear phase-error contract holds over the same enlarged interval.

## Source and scope

Calculation base 9d934337c0a9f7a6341b20cf116c8b6cd31c79eb, prior discovery head 1de2e0299a813a4362ce38cb2c13d469822a7d1c, held claim 72863501bd80db6aae1fd9b68467de48e92cb42c. Resume of clockmatrix-20261104-01 using Git compute and connector publication. The model, unit Euclidean metric, ascending simplex basis, transverse projector P, native clock s and inverse-designed eta=1 penalty are fixed by [CERTIFIED_INTERVAL.md](CERTIFIED_INTERVAL.md) §§1–2 and [LOCAL_STABILIZATION.md](LOCAL_STABILIZATION.md). The endpoint 1/64 was exposed by the previous numerical scan. This calculation uses exact rational matrix checks and analytic inequalities. Physical calibration and coefficient selection remain OPEN.

## Fourier coefficients and return remainder

Work on N, the range of P, where J² = -Id. The interaction equation is Y' = rho C(theta) Y with C(theta) = exp(-theta J) J(B(theta)-Id) exp(theta J), rho = mu/(2+mu). Its fundamental matrix starts at Id and M = Y(pi) is minus the transverse half-return. The model Hessian is Bc cos²(theta) + Bs sin²(theta) + Bx cos(theta)sin(theta), compressed to N. For any compressed D the conjugate exp(-theta J) JD exp(theta J) has constant, cosine-2 and sine-2 coefficients (JD+DJ)/2, (JD-DJ)/2 and (D+JDJ)/2. Multiplication gives

    C(theta) = T + sum_{k=2,4} [A_k cos(k theta) + B_k sin(k theta)].

Use G0 from the prior certificate, with the negative-signature group projector Pi and K=-JT. The replay proves Id/20 < G0 < 5Id/4 with shifted LDL checks, including the identity extension off N. In the G0-induced operator norm, the replay bounds (T,A2,B2,A4,B4) by (3/4,7/8,49/64,9/32,9/64). Their sum is below 3. Every norm check is a positive-definiteness test of cap² G0 - Aᵀ G0 A.

Put h=pi rho and X=M-Id. The first Dyson term is hT. For the second Dyson coefficient D2, integration over the ordered triangle gives

    D2 - (pi T)^2/2 = pi Z,
    Z = sum_{k=2,4} ([T,B_k] - [A_k,B_k]/2)/k.

Indeed the left side is half the integral of [C(t),C(u)] over 0<=u<=t<=pi. Unequal harmonics integrate to zero by orthogonality, the mean and sine terms give [T,B_k]/k after division by pi, and the matched cosine and sine give -[A_k,B_k]/(2k). The replay gives ||Z||_G0 < 1/2.

For a=3h the Dyson tails after orders 1 and 2 are bounded by r2=a²/(2(1-a/3)) and r3=a³/(6(1-a/4)), by the successive-term ratio bounds. Use the exact scaled Cayley generator L=(2/h)(M-Id)(M+Id)^-1. For x=3h/4+r2, ||X||_G0<=x, and its Cayley series differs from (X-X²/2)/h by at most x³/(4h(1-x/2)). Therefore

    ||L-T||_G0 <= rho/2 + r3/h + (3h/2+r2)r2/(2h) + x³/(4h(1-x/2)).

Each term after cancellation of h is increasing in h and rho. Substituting rho<=1/129 and h<=(22/7)/129 gives e=1/100 as a strict bound. This controls the actual return uniformly down to rho approaching zero.

## Invariant metric and gain

Let S=G0^(1/2) on N and put hats on similarity transforms by S. Then T̂ is skew and R̂0=S(Id-2Pi)S^-1 is an orthogonal involution. The paired circles of radius 1/5 centered at ±i sqrt(35/64) are at least 1/5 from the spectrum of T̂. The other positive frequencies lie below 3/10 and sqrt(35/64)>7/10. The Neumann resolvent bound and the two contour integrals give ||P̂i_rho-P̂i|| <= 2e/(1/5-e)=2/19. Here Pi_rho selects both perturbed groups inside the circles. The same bound along the straight perturbation path preserves rank.

The symplectic Cayley identity gives K_rho=-JL symmetric. On N, SJS = T̂ R̂0 has least singular value equal to the smallest frequency, which exceeds 1/5. Thus ||S^-1 J S^-1||<5 and ||S^-1(K_rho-K)S^-1||<=5e. The signed-pair projector is self-adjoint for K_rho by the signed contour symmetry and LᵀK_rho=-K_rho L. It commutes with L, so G_rho=K_rho(Id-2Pi_rho) is symmetric and invariant for L. Relative to G0 its error from identity is at most

    5e(1+2(2/19)) + 2(2/19) = 103/380 < 1.

Hence the Cayley inverse and the half-return preserve this positive metric. The Euclidean squared gain of any integer half-return power is bounded by 25(1+103/380)/(1-103/380). Within the half-period the earlier Euclidean interaction bound ||C||<=5 gives gain <=8/7, since 5h<1/8. Their combined squared gain is below 64. The bound applies for all real s, using invertibility and periodicity, at the declared initial phase.

## Finite nonlinear readout and checks

The modified Hamiltonian and Hessian bound 18||x||² from [CERTIFIED_INTERVAL.md](CERTIFIED_INTERVAL.md) §5 still apply. With I=1, lambda=mu, initial state error <=1/4096 and both energies <=33/16, the reference energy 2+mu/2 remains below the cap. Through s=1/(128mu) the same Gronwall and phase margins give error <1/1000 rad and reference phase separation 1/128 rad from the zero-coupling null. At mu=1/64 the horizon is 1/2 native time units. The all-time gain theorem concerns the linear transverse equation. The nonlinear result is restricted to this finite readout. Independent review remains OPEN and physical promotion is 0.

Replay with python3 experiments/clock-matrix-question/fourier_interval.py. The small extraction of model_matrices in certified_interval.py preserves the existing matrices() return and the earlier certificate result. The earlier capture remains immutable. The earlier norm-only bound was insufficient to reach this endpoint. No boundary of the full stability region is established.
