# Twenty-cell icosahedral cone — exact audit v1.0

Evidence: **EXACT**, **CONDITIONAL**, **NUMERICAL**. Source base: f70871b7df8465ceea88cbb6e41fa9493dddee6b. This audits the user's proposed regular-icosahedron centre cone and compares it with the [four-cell tetrahedron](../four-cell-tetrahedron/README.md). Static geometry, an explicitly chosen chain evolution, and physical interpretation are separate.

## 1. Audit result and incidence correction

The construction is valid. For a regular icosahedral boundary $S$ and interior centre $v_0$, $K=v_0*S$ is a geometric cone triangulating the solid icosahedron. Every tetrahedron has one exterior equilateral face and three shared interior isosceles faces. All twenty tetrahedra are congruent, with three radial edges $R$ and three base edges $a$; they are not regular tetrahedra.

One supplied incidence is corrected: **an exterior edge belongs to two tetrahedra**, one coned from each of its two incident boundary triangles. It is the exterior face that belongs to one tetrahedron.

| Object | Count | Incidence |
| --- | --- | --- |
| Central vertex | 1 | All 20 cells; 12 radial edges |
| Boundary vertices | 12 | Five boundary triangles and five cells at each |
| Radial edges | 12 | Five cells at each |
| Boundary edges | 30 | Two cells at each |
| Interior faces | 30 | Two cells at each |
| Exterior faces | 20 | One cell at each |
| Tetrahedral cells | 20 | Three internal neighbours and one exterior face each |

Checks: $12(5)+30(2)=20(6)=120$ cell–edge incidences, and $30(2)+20(1)=20(4)=80$ cell–face incidences. The face vector is $(13,42,50,20)$ and $\chi=1$. The ball conclusion follows from coning the verified convex spherical boundary, not from Euler characteristic alone.

The exact construction identifies edges by squared distance $a^2$, enumerates the twenty triangular cliques, and checks with signed $\mathbb Q(\sqrt5)$ inequalities that every such triangle is a supporting face. Thus the coordinate hull and the simplicial complex agree.

## 2. Metric audit and actual local metric tensor

All supplied lengths, areas, volumes and angles agree with the regular-icosahedron realization. With $a>0$ and $\phi=(1+\sqrt5)/2$:

| Quantity | Exact expression |
| --- | --- |
| Radial length | $R=\frac a4\sqrt{10+2\sqrt5}=a\sin(2\pi/5)$ |
| Altitude/inradius | $h=\frac{3+\sqrt5}{4\sqrt3}a$ |
| Midradius/lateral-triangle altitude | $r_{\rm mid}=\phi a/2$ |
| Cell volume | $V_c=(3+\sqrt5)a^3/48$ |
| Base area | $A_{\rm ext}=\sqrt3a^2/4$ |
| Interior face area | $A_{\rm int}=\phi a^2/4$ |
| Total cell area | $A_c=(\sqrt3+3\phi)a^2/4$ |
| Apex face angle | $\arccos(1/\sqrt5)=\arctan(2)$ |
| Base–lateral interior dihedral | $\beta=\arctan(\phi^2)$ |
| Lateral–lateral interior dihedral | $\psi=2\pi/5$ |
| Central solid angle | $\Omega_c=\pi/5$ |

An isolated cell has threefold rotations and three reflection symmetries, giving the stated $C_{3v}$ symmetry.

An explicit metric tensor in the edge-vector basis $(r_a,r_b,r_c)$ at $v_0$ is the positive Gram matrix

$$
G=\frac{a^2}{8}
\begin{pmatrix}
5+\sqrt5&1+\sqrt5&1+\sqrt5\\
1+\sqrt5&5+\sqrt5&1+\sqrt5\\
1+\sqrt5&1+\sqrt5&5+\sqrt5
\end{pmatrix}.
$$

Its eigenvalues are $a^2/2$ (multiplicity 2) and $(7+3\sqrt5)a^2/8=3h^2$ (multiplicity 1); its determinant is $(7+3\sqrt5)a^6/32$. Consequently $\sqrt{\det G}/6=(3+\sqrt5)a^3/48$. This is a Euclidean cell metric, distinct from a metric on the chain register or any spacetime metric.

Exact metric verification uses squared norms/areas, determinants and normal-vector dot products. The dihedral cosines are

$$
\cos\psi=\frac{\sqrt5-1}{4},\qquad
\cos^2\beta=\frac{3-\sqrt5}{6},\qquad
\cos(2\beta)=-\frac{\sqrt5}{3}.
$$

The positive interior branches give $72^\circ$, approximately $69.09484255^\circ$, and approximately $138.18968510^\circ$. The solid-angle formula also follows from spherical excess $3\psi-\pi=\pi/5$.

All four proposed assembly checks pass: five radial dihedrals close to $2\pi$, twenty solid angles sum to $4\pi$, two base–lateral angles recover the exterior-edge dihedral, and twenty cell volumes sum to $5(3+\sqrt5)a^3/12$.

## 3. Three distinct graphs and what fivefold closure means

| Graph | Nodes | Edges | Degrees |
| --- | --- | --- | --- |
| Primal vertex graph | 13 | 42 | Centre 12; outer vertices 6 |
| Internal cell adjacency | 20 | 30 | All 3; dodecahedral graph |
| Cell adjacency with one exterior-region node | 21 | 50 | Exterior 20; cell nodes 4 |

The primal graph is the cone/join of a single vertex with the icosahedral vertex graph. It is not a complete graph on thirteen vertices. The internal cell graph is the polyhedral dual of the icosahedral shell, namely the dodecahedral graph. Adding the exterior region gives the cone over that graph; the exterior-region node is not the geometric centre.

Around each radial edge, its five tetrahedra form an explicit five-cycle in the cell graph. This is a spatial link. A temporal five-state register would require a separately declared update and clock map.

In a piecewise-Euclidean curvature interpretation the interior edge deficit is

$$
\delta_{\rm radial}=2\pi-5(2\pi/5)=0.
$$

Thus this realization has flat Euclidean bulk. The boundary has intrinsic angular deficit $\pi/3$ at each vertex, summing to $4\pi$, and nonzero exterior bending. These statements refer to different geometric locations and curvature notions; the fivefold incidence alone does not generate bulk gravitational curvature.

![Primal cone and cell dual](../../artifacts/icosahedral-cone-20261022-a1/audit-001/files/icosahedral-cone.png)

## 4. Exact chain registers and homotopy

Use ascending vertex labels to orient each simplex and integer boundary maps $B_k:C_k(K;\mathbb Z)\to C_{k-1}(K;\mathbb Z)$. The executable audit checks $B_1B_2=B_2B_3=0$ entry by entry. The contraction sends a simplex not containing $v_0$ to its cone and sends a simplex already containing $v_0$ to zero. Its verified identity is

$$
\partial h+h\partial=I-P_0,
$$

where $P_0$ maps every vertex to $v_0$ and vanishes in positive degrees. This proves integral contractibility and no torsion; ranks over $\mathbb Q$ are $(12,30,20)$, with Betti vector $(1,0,0,0)$.

| Register | Degree dimensions | Total |
| --- | --- | --- |
| Full cone | $(13,42,50,20)$ | $125$ |
| Boundary shell | $(12,30,20)$ | $62$ |
| Relative pair $(K,\partial K)$ | $(1,12,30,20)$ | $63$ |

The total $125=5^3$ and relative count $63=2^6-1$ are exact arithmetic facts about these registers. They do not establish a base-five clock, six qubits, a mod-13 law, or physical dimension. For any such cone with $N$ nonempty boundary simplices, the full and relative counts are $2N+1$ and $N+1$; here $N=62$.

Relative homology is concentrated in degree 3 with one generator, represented by the consistently oriented twenty-cell chain. No parent/relative isomorphism with a single tetrahedron is claimed: their dimensions differ. The decomposition is not a self-similar recursive icosahedral fractal.

## 5. Exact graph spectrum and a conditional dynamics comparison

Let $A_D$ denote the cell-adjacency matrix, $L_D=3I-A_D$, on $\mathbb R^{20}$ with Euclidean metric.

| Eigenvalue of $L_D$ | Multiplicity |
| --- | --- |
| $0$ | 1 |
| $3-\sqrt5$ | 3 |
| $2$ | 5 |
| $3$ | 4 |
| $5$ | 4 |
| $3+\sqrt5$ | 3 |

The exact characteristic polynomial is

$$
\det(tI-L_D)=t(t-2)^5(t-3)^4(t-5)^4(t^2-6t+4)^3.
$$

The audit proves the square-free polynomial with these six distinct roots annihilates $L_D$, then checks exact trace moments through degree 5. Distinct roots and Vandermonde uniqueness fix the multiplicities, independently cross-checked numerically. An analogous exact certificate verifies the icosahedral vertex Laplacian spectrum $0^1,(5-\sqrt5)^3,6^5,(5+\sqrt5)^3$.

If one *chooses* cell diffusion $z'=-\kappa L_Dz$, $\kappa>0$, the mean is conserved, $d\|Pz\|^2/du=-2\kappa z^TL_Dz\le0$, and the slowest contrast rate is $\kappa(3-\sqrt5)$. In the four-cell $K_4$ graph it is $4\kappa$ at the same per-edge rate and same degree three. Thus the icosahedral cone adds distinct spatial contrast sectors and slower global equilibration, rather than automatically improving coherence. Diffusion, damping and oscillatory chain evolution are different optional laws.

## 6. Canonical unit-chain-metric audit

Declare $H=I$ on the direct sum of all chain groups, $\partial=\sum B_k$, real skew generator $A=\partial^T-\partial$, and unit dimensionless evolution rate $c'=Ac$. Then $-A^2=\Delta=\partial\partial^T+\partial^T\partial$. This chain metric is not the geometric $G$ above.

The full 125-dimensional skew characteristic polynomial is

$$
\det(zI-A)=
z(z^2+1)(z^2+13)(z^2+3)^{10}(z^2+4)^8
(z^2+6)^8(z^2+7)^{10}
(z^4+8z^2+11)^6(z^4+12z^2+31)^6.
$$

For the relative 63-dimensional complex it is

$$
z(z^2+12)(z^2+2)^5(z^2+3)^4(z^2+5)^4(z^2+6)^5
(z^4+6z^2+4)^3(z^4+10z^2+20)^3.
$$

Both are certified by exact integer annihilating-polynomial and moment calculations on the corresponding Hodge Laplacians, with numerical eigenvalue discrepancies below $8.0\times10^{-15}$. These are exact statements under the specified metric/generator, not measured physical spectra.

For consistently oriented cells, the top-degree blocks simplify to

$$
\Delta_3^{\rm full}=I+L_D,\qquad \Delta_3^{\rm relative}=L_D.
$$

The extra identity is the contribution from one exterior face per cell. Therefore boundary retention versus quotienting changes even the collective mode.

## 7. Heart seed versus exterior collective cell mode

Let $e_0$ be the unit chain amplitude at the central vertex. Exact iteration gives

$$
A^3e_0=-13Ae_0,\qquad
\dim\operatorname{span}\{e_0,Ae_0,A^2e_0\}=3.
$$

Its minimal polynomial is $z(z^2+13)$. The motion has a static component and frequency $\sqrt{13}$ in model units, and occupies only vertex and radial-edge chain amplitudes. It has no face or cell amplitudes. In particular,

$$
c_{v_0}(u)=\frac1{13}+\frac{12}{13}\cos(\sqrt{13}\,u)
$$

for this unit seed and convention. This centre result is a general cone vertex effect; its occurrence at thirteen vertices does not privilege mod-13 physics.

There is a separate, exact collective sector. Let $Z$ be the sum of the twenty consistently oriented cells and $S=\partial Z$. Internal interfaces cancel, so $S$ consists of the twenty oriented exterior faces and $\|Z\|^2=\|S\|^2=20$. The generator satisfies

$$
AZ=-S,\qquad AS=Z.
$$

Thus the normalized cell/surface pair spans a two-dimensional frequency-one oscillator under this chosen chain law. This is an algebraic cell-to-boundary amplitude cycle, not automatically an expanding physical volume or pressure cycle. It is orthogonal to the invariant heart-seed space, so the declared generator supplies no heart-to-cell transfer.

Moving the geometric centre inside a fixed shell also keeps total polyhedron volume fixed, merely repartitioning cell volumes. A physical breathing interpretation still needs a shell motion and a constitutive/readout law, as in the separately assumed [radial mechanical candidate](../heart-shell-elastic/README.md).

## 8. Verification, provenance and next discriminant

Run from repository root with NumPy and Matplotlib installed:

    OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-cone/analyze.py --out /tmp/ud-icosa
    python3 experiments/icosahedral-cone/draw.py --out /tmp/ud-icosa/icosahedral-cone.png
    python3 scripts/validate.py
    python3 -m unittest discover -s tests -v

The [manifest](../../artifacts/icosahedral-cone-20261022-a1/audit-001/manifest.json) captures executable code, this report, the mathematical receipt, exact simplex/boundary data, results and coordinate-derived illustration. Coordinates are in $\mathbb Q(\sqrt5)$ with edge length one; geometric scaling by $a$ remains explicit. No physical time unit or fitted observation is used.

The supplied historical ledger v0.39, Q139/Q144–145/Q151–152, leaves generator pushforward, breathing identification and constitutive selection open. The supplied CRL-2 amendment v1.0 is a governance proposal, not a mathematical input or automatically adopted registry rule. These records do not identify the newly calculated spectra with physical observables.

All verification is constructor work: exact identities plus numerical cross-checks, not non-constructor peer review or empirical replication. Repository integrity checks certify record consistency and tooling, not physics.

**Recommended next question:** construct a local, symmetry-compatible, energy-consistent coupling from the central mode into the collective cell/surface sector, or prove an obstruction for a stated class of couplings. Compare against the uncoupled generator above, and define the volume readout before calling any response breathing.
