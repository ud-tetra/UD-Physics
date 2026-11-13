# Direct propagation and split preparation gates v0.1

**EXACT / CONDITIONAL.** For the fixed prepared eta=1 clock, action I=1 and phase zero, take 31/5 <= mu <= 77511/12500. Through one native time unit, either preparation gate below guarantees lifted phase error strictly below 1/300000 rad.

| Gate | Initial tangent norm cap | Initial normal norm cap | Full state error upper bound |
|---|---:|---:|---:|
| Isotropic sufficient gate | 1/3200000 | 1/3200000 | 1/200000 |
| Split gate | 1/8000000 | 1/120000 | 1/22000 |

A Euclidean initial norm cap of 1/3200000 implies both isotropic component caps. This increases the previous sufficient Euclidean preparation radius fivefold at the same phase tolerance and horizon. The split gate permits a larger normal error when tangent preparation is more accurate. Its full state error allowance is larger.

## Source and conventions

Integrated base 234f54471c32cc9ad4873cd8042103fa19795909, discovery parent 84c59f35f58405c06820d5697c74674305aeedbc, task clock-matrix-question-20261104, session clockmatrix-20261104-01 and held claim 72863501bd80db6aae1fd9b68467de48e92cb42c. Retain the ascending Euclidean V=W plus N, J=A/2, Hamiltonian and phase projection from [NONLINEAR_MARGIN.md](NONLINEAR_MARGIN.md). Native time is s and reference phase is theta=(2+mu)s. No changes to the Hamiltonian. The endpoint is below the open first-loss bracket from [STABILITY_BOUNDARY.md](STABILITY_BOUNDARY.md).

## Direct two-time normal bounds

Use the exact three 2D blocks and outward-rounded Taylor integrator in the first-loss certificate. At rho0=31/41, propagate each block to 85 grid nodes theta_j=j*pi/32, j=0,...,84. To reuse the certified quarter-period tables, negate every sine and cosine coefficient on odd quarter-period translates. This follows from the angle shift by pi in the trigonometric coefficients, whose argument is 2 theta. The analytic Taylor tail bound is unchanged on all translates because the real center changes and the complex disk radius and coefficient bounds remain the same.

For each block the exact replay verifies ||U_j|| <43/10 and ||U_i U_j^-1|| <11/2 for all j<=i, by outward entry boxes and an upper Frobenius norm. Trace zero gives determinant one, allowing the inverse entries to be enclosed by the 2D adjugate. The grid reaches 21pi/8, beyond every phase in the one-unit observation window. These finite checks use rational arithmetic on 100-bit dyadic intervals, with no floating comparison.

The Euclidean logarithmic norm in both time directions is bounded by 3rho/2<6/5. Indeed the symmetric part of each traceless generator has norm at most half the magnitude of the diagonal Hessian difference plus the magnitude of the off-diagonal Hessian entry, times rho. Use floor grid nodes for both times and bound each endpoint factor by exp((6/5)pi/32)<8/7. This gives reference normal gains A0=(43/10)(8/7) from phase zero and K0=(11/2)(8/7)^2 between any two times in the grid horizon.

For rho in the full target interval the coefficient perturbation has norm at most 5|rho-rho0|, by the symmetric Hessian row bound. Variation of constants against the reference flow and scalar Gronwall multiply each bound by at most exp(K0*5|rho-rho0|*21pi/8). The rational replay bounds the exponent by 1/100, so the factor is below 100/99. The resulting normal bounds are 5 from zero and 8 between arbitrary ordered times. The proof uses the fixed phase variable before setting theta=(2+mu)s for each parameter. Orthogonality of the exact block decomposition transfers the bounds to N.

## Separate nonlinear error transfer

Write e=x-z, w=P_W e and n=P_N e. Up to first exit from a radius R<=1/1000, the prior Hessian polarization gives ||r||<=160||e||² in e'=DF(z)e+r. Projection bounds each component of the remainder by 160R². The reducing tangent block has initial gain below 14 and integrated forcing gain at most 1+mu<8 on s in [0,1], by integrating the shear envelope 1+2mu(s-u). The normal block has initial gain at most 5 and integrated forcing gain at most 8. Consequently

    ||w(s)|| <= 14 ||w(0)|| + 1280 R²,
    ||n(s)|| <=  5 ||n(0)|| + 1280 R².

For each row of the table, the sum of squares of these two upper bounds is strictly below R² using the indicated state radius. The tube closes by continuity. The phase readout uses W alone, so its disk deviation is bounded by ||w(s)||/sqrt(2). The rational replay verifies (3/4)||w(s)|| < t-t³/6 at t=1/300000, using the upper bound above. The projected readout stays nonzero and its continuously lifted phase satisfies the strict tolerance.

The grid caps were selected after inspecting the first reference-grid calculation. The gate sizes are sufficient design choices, with no coefficient fitting. Replay with python3 experiments/clock-matrix-question/anisotropic_margin.py. Independent review, detector error, coefficient drift, physical calibration and all-time nonlinear stability remain OPEN. Physical promotion is zero.
