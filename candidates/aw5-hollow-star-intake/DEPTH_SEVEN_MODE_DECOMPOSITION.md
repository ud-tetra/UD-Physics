# AW5 depth-seven fixed-window spectral decomposition

**EXACT** Hodge-channel and terminal-symmetry identities. **INTERVAL-VERIFIED** selected poles and their individual window contributions. **NUMERICAL** whole-window sector estimates. **Physical Promotion = 0.** Uniform depth seven, unit simplex weights, fixed signed exterior and two-face reference probes, undamped dynamics, and the frozen 256 native midpoints over T=32. No fit or measured data.

## Hodge and terminal channels

On degree two, −A²=L₂=B₂ᵀB₂+B₃B₃ᵀ. Its harmonic space, im B₂ᵀ, and im B₃ are orthogonal invariant summands. The collocated face response is qᵀcos(t√L₂)q. The original signed exterior surface is a closed 2-chain, B₂q=0, so the target has zero edge-channel weight. Its harmonic residue is 64/2315. The fixed two-face reference has zero harmonic residue at equal leaf depths.

In coherent top-cell orientations, H=B₃ᵀB₃ for a leaf equals 4I−W, where W is the adjacency across shared triangular faces. The im B₃ response weights are obtained from the dual Gram spectral measure of u=B₃ᵀq, with a factor 1/λ at each positive dual eigenvalue λ. Each terminal corresponds to the unique top cell incident to one original boundary face. For depth ≥1 those terminal cells are distinct.

The symmetry of the four boundary faces gives the dual port resolvent Z(z)=Z_c(z)P_c+Z_t(z)(I−P_c), with P_c=J/4. Here c is the constant-terminal sector and t is the zero-sum differential sector. The two channels describe the transformation of the boundary projections under permutation. Spatial localization of a lifted eigenvector is an additional question.

In coherent boundary signs, the target loads three equal exterior terminals per leaf, with zero load at the cavity terminal. After summing over four leaves, its squared terminal weights are 3/4 in c and 1/4 in t. The reference drives one terminal in each of two distinct leaves, with opposite coherent signs. Its squared weights are 1/4 in c and 3/4 in t. The top-cell contribution to target minus reference is therefore one half the constant-sector response minus one half the differential-sector response. That difference holds as an identity in time.

## Two-scalar recursive dual transfer

Let a and c be the differential and constant eigenvalues of the terminal Schur operator H_d(z) on zI+H. Thus Z_t=1/a and Z_c=1/c. At the first split the top dual graph is K₄, giving (a,c)=(z+5,z+1). Write b=(c−a)/4 for its J coefficient. In the next four-child gluing, x_ij is child i’s port on the shared face with j and y_i is its exterior port. Let S_i be the sum of child i’s four ports. The inner port equations are a x_ij + b S_i − x_ji=0. Eliminating the paired ports and resolving the sums S in the constant and zero-sum subspaces gives

    c_next = a + b(a−1)/(a−1+3b),
    a_next = a + b(a²−1)/(a²−1+b(3a−1)).

These functions agree with the matrix reduction wherever the displayed denominators are nonzero and extend as rational functions across removable singularities. The replay directly checks the scalar recursion against full dual networks through depth three. Deep calculations use only the two scalar functions for the top-cell sector and the previous grade-aware boundary resolvent for the total.

Write ℓ(z) for a or c. When ℓ(−ω²)=0 is simple, the dual pole residue is 1/ℓ′(−ω²). The corresponding face spectral mass is 1/[ω²ℓ′(−ω²)]. Multiplying that mass by the discrete cosine mean sin(32ω)/[512 sin(ω/16)] and by the signed contrast coefficient ±1/2 gives the individual window contribution. The replay brackets each listed root with outward interval arithmetic. It checks the internal denominators, endpoint signs, derivative sign and widths of the induced mass and contribution intervals. The displayed numbers are interval midpoints rounded for readability.

| Isolated accessible mode | Native angular frequency | Face mass in its unit terminal sector | Signed mean contrast |
| --- | ---: | ---: | ---: |
| Constant-terminal A | 0.00649912141 | 0.168209538 | +0.083499794 |
| Constant-terminal B | 0.02998150689 | 0.079651085 | +0.033991000 |
| Differential-terminal A | 0.01284180648 | 0.062626228 | −0.030439222 |

This isolates three modes with significant finite-window contributions. The two positive modes together contribute about 0.117491. Their timescale is long relative to the 32-unit window. The calculations do not enumerate all poles or classify the spatial geometry of their eigenvectors.

## Whole-window sector accounting

For a terminal scalar inverse Z(z), the Laplace transform of the corresponding face-sector trace is [Z(0)−Z(s²)]/s. The replay uses the same midpoint Fourier weights at cutoff 16384 to estimate its mean. It obtains the edge-reference mean by subtracting the independently computed harmonic and top-cell terms from the total transfer. The target edge term is also checked against the exact boundary closure. These Fourier sector values are numerical diagnostics. The separately certified whole-contrast interval and noisy acquisition bounds are in the [adaptive certificate](ADAPTIVE_DTN_DEPTH_SEVEN.md).

| Contribution to target minus fixed reference | Mean estimate |
| --- | ---: |
| Harmonic | +0.027645788337 |
| Constant-terminal top-cell | +0.129377589874 |
| Differential-terminal top-cell | −0.074086017915 |
| Edge-channel difference | +0.001797636339 |
| Total | +0.084734996635 |

The net top-cell transient is about +0.055292. The isolated constant-terminal pair supplies about 0.117491 of the constant-terminal net +0.129378. Other modal contributions and the differential sector account for the cancellation that produces the smaller observed contrast. All frequencies and rates here are native. The 32-unit window has a laboratory millisecond meaning only under a calibrated emulator map.

Replay: `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 depth_seven_modes.py` from this candidate directory, with NumPy, SymPy and mpmath. Next discriminant: lift the identified eigenvectors through the terminal recursion and report their norm distribution by refinement level and cell orbit.
