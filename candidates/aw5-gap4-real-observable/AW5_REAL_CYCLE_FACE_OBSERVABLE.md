# AW5 real cycle–face loop observable

**EXACT_INTERNAL. Physical Promotion = 0.**

Use the oriented filled bipyramid 0123–0124 and unit simplex inner products from the [phase dynamics audit](https://github.com/ud-tetra/UD-Physics/blob/4ace239c3fa5e874ca077087c2a731bc58cb45c6/candidates/aw5-gap4-phase-dynamics/AW5_BIPYRAMID_PHASE_DYNAMICS.md). The real edge space has dimension nine. Let $Z_1=\ker B_1$, $Y_2=\operatorname{im}B_2^\mathsf{T}$, and $x=B_2e_{012}$. The edge–face sector $Z_1\oplus Y_2$ is invariant under $A=B^\mathsf{T}-B$. Write its states as $(j,q)$ and use dimensionless native time $s$.

## Direct loop and face readout

For any real edge cochain $j$, the loop functional $\langle z,j\rangle$ is invariant under $j\mapsto j+B_1^\mathsf{T}\chi$ for every real vertex potential $\chi$ and every cycle $z\in Z_1$. In particular the shared loop reads the real face coboundary $\langle x,j\rangle=(B_2^\mathsf{T}j)_{012}$. Equivalently, the orthogonal representative of an edge cochain modulo vertex gradients is $P_{Z_1}j$. The discarded edge cut sector evolves with vertices, so the cycle–face dynamics and their readout are independent of the choice of edge representative. This is an additive coboundary invariance of the readout and reduced dynamics.

Let $w=B_2^\mathsf{T}x$. Signed incidence gives $B_2w=5x$, $B_3^\mathsf{T}w=0$, $\|x\|^2=3$, and $\|w\|^2=15$. Define the real loop and normalized face quadratures

$$
F=\langle x,j\rangle,\qquad G=\frac{\langle w,q\rangle}{\sqrt5}.
$$

Then

$$
\frac{d}{ds}\begin{pmatrix}F\\G\end{pmatrix}
=\sqrt5\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}F\\G\end{pmatrix}.
$$

The pair distinguishes the two initial quadratures and determines the entire shared-loop trace, $F(s)=F(0)\cos(\sqrt5s)-G(0)\sin(\sqrt5s)$. With $G(0)=0$ it recovers the edge-only result. The gauge-invariant norm

$$
I_{012}=\frac{F^2+G^2}{3}
       =\frac{\langle x,j\rangle^2}{3}
        +\frac{\langle w,q\rangle^2}{15}
$$

is the conserved squared norm of the projection onto the real plane spanned by $(x,0)$ and $(0,w)$. It classifies the time-translation orbits of that plane, including the zero orbit, because a full oscillator period sweeps every angle. Other cycle–face modes can share the same readout. For the shared-face trace the signed period mean is zero and the RMS is $\sqrt{3I_{012}/2}$.

## Relation to compact readout

No angle reduction or amplitude conversion is needed for $(F,G)$ or $I_{012}$. The earlier compact witness has an optional calibrated image $\exp(2\pi i\kappa F)$, with declared conversion $\kappa$. The native pair distinguishes the two real lifts in the compact-descent counterexample from the initial time. For example in the unscaled turns convention $j=0$ and $j=x$ have $F=0$ and $F=3$. The result supplies an exact real observable for Gap 4 under the specified additive symmetry. A physical readout and any autonomous compact transport law remain open.

The constructor replay checks exact incidence, gradient invariance for all vertex basis generators, the two-dimensional output closure in rational coordinates and the quadratic conservation identity.
