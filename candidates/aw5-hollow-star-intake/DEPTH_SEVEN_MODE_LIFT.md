# AW5 depth-seven interior mode lift

**EXACT** Schur back-substitution and dual-cycle orthogonality. **NUMERICAL** lifted mode profiles, nodal domains and shell projections. **Physical Promotion = 0.** Uniform depth seven, unit simplex weights and undamped dynamics. Frequencies use native units. The modes are selected by the original exterior probe and the fixed-reference contrast from the [modal decomposition](DEPTH_SEVEN_MODE_DECOMPOSITION.md).

## Recursive lift and independent residual

Use the coherent top-cell Gram matrix $H=B_3^\mathsf{T}B_3=4I-W$ on one leaf, with $W$ the dual adjacency. The four leaves share no faces, so the top-cell operator is the direct sum of four such blocks. The two constant-terminal poles lift to the same scalar profiles on every leaf, with relative copies set by the probe. One leaf suffices to compute the normalized geometry for either pole.

At $z=-\omega^2$, start with equal values $y_i=1$ on the four terminal cells. At each split the child terminal Schur matrix is $aI+bJ$, with $a$ the differential eigenvalue and $b=(c-a)/4$ from constant eigenvalue $c$. Child $i$ has exterior value $y_i$ and three shared ports $x_{ij}$. Write $S_i=y_i+\sum_{j

$$
S_i=\frac{\bar y}{1+3b/(a-1)}
   +\frac{y_i-\bar y}{1+b(3a-1)/(a^2-1)},\qquad
x_{ij}=-\frac{b(aS_i+S_j)}{a^2-1}.
$$

Apply these expressions to each child, down to depth one, where the four terminal values are the four cell coordinates. The interval pole check excludes cleared Schur denominator zeros at the roots. The floating-point replay substitutes the interval midpoint and compares the normalized lift to an independently assembled 16,384-cell dual adjacency. As a second check it recovers the unit constant-terminal face spectral mass from $x$ as $\lvert\sum_{\mathrm{ports}} x_i\rvert^2/(4\omega^2)$.

## Interior geometry

A shell consists of cells at the same shortest dual-graph distance from their nearest terminal cell. There are 64 shells. Let $P_s$ average the amplitudes within each shell. The squared-norm fractions $\|P_sx\|^2/\|x\|^2$ and $\|(I-P_s)x\|^2/\|x\|^2$ sum to one. Their ratio also applies to the time-averaged squared top-cell velocity of a single real mode since the common $\omega^2$ factor cancels. Shell distance and the unit-simplex metric define this particular model diagnostic.

| Mode | Native angular frequency | Shell mean share | Within-shell share | Shell mean to within-shell ratio | Positive / negative connected domains | Eigenvector residual |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 0.00649912141 | 99.9927763% | 0.0072237% | 13,842.3 to 1 | 1 / 0 | 6.3e−14 |
| B | 0.02998150689 | 99.5723822% | 0.4276178% | 232.9 to 1 | 4 / 1 | 5.9e−13 |

Both lifts are invariant under relabeling by the three adjacent transpositions generating $S_4$ in coherent scalar cell coordinates, with zero reported numerical defect. Mode A is a nodeless, nearly uniform collective mode. The global mean accounts for 97.2258% of its squared norm. Mode B is a sign-changing, shell-dominated mode with a single connected negative domain carrying 17.6937% of the squared norm. Its global mean carries only 2.1633%. Its largest orthogonal refinement detail, 90.1723%, is the change from averaging by first-generation cells to averaging by second-generation cells. The [replay](depth-seven-lift-replay.txt) records all seven refinement details. These mode profiles are numerical checks using interval-isolated input frequencies.

There is a separate exact sense of circulation. On internal shared faces the lifted face partner $B_3 x/\omega$ is an oriented difference between dual-neighbor cell amplitudes divided by $\omega$. Its signed sum around every closed dual path telescopes, so its projection onto the internal dual cycle space vanishes. This holds for both modes. Within-shell variation measures deviations from distance-shell means. The exact cycle statement uses a different projection and supplies zero dual-cycle content for both lifted modes. Neither diagnostic uses a physical kinetic-energy calibration.

The previous numerical gap estimate includes the reference edge-channel term. Its accounting is $0.027645788337+0.055291571959+0.001797636339=0.084734996635$, comprising harmonic, net top-cell and edge-channel contrast. The original target's exact edge-channel exclusion follows from $B_2q=0$.

Replay from this candidate directory with `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 lift_depth_seven_modes.py`. Dependencies include NumPy, SciPy, mpmath and SymPy. A subsequent mathematical discriminant is to perturb one leaf or the signed probe before comparing shell and dual-cycle observables.

**Physical Promotion = 0.**
