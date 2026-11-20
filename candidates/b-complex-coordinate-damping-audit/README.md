# B-complex damping correction and PB5 shear projection

**EXACT / CONDITIONAL.** The printed four-coordinate B-complex sink leaves 17 lossless real dimensions and 10 asymptotically damped dimensions for every positive damping coefficient. On PB5, the additive interface lossless projector retains only equatorial coefficients of an edge-only preparation. A fully symmetry-equivariant edge encoding can retain at most two of the five symmetric trace-free components. **Physical Promotion = 0.**

## B-complex correction

Use the cells 0134, 0234 and 1234, one coordinate per oriented simplex, increasing vertex orientations, the Euclidean coefficient metric, and \(A_B=\partial-\partial^\mathsf T\). The four printed sinks are the coordinate selector \(R\) of 34, 034, 134 and 0134. For \(\gamma>0\) the generator is \(A_B-\gamma R^\mathsf TR\). The rows of \([R;RA_B;RA_B^2;RA_B^3]\) have rank 10 and are closed under right multiplication by \(A_B\). The cumulative ranks are 4, 8, 9 and 10. The maximal lossless subspace therefore has dimension \(27-10=17\), with exact characteristic polynomial
\[
 z(z^2+2)(z^2+5)^7.
\]
For the damped generator the squared norm derivative is \(-2\gamma\|Rx\|^2\). A purely imaginary eigenvalue in the orthogonal complement would require an \(A_B\)-eigenvector annihilated by \(R\), contradicting the construction. Every eigenvalue on the 10-dimensional complement therefore has strictly negative real part.

This corrects the printed coordinate-mask calculation. The separate A→B relay claim depends on its specified transfer and intertwining residual. The repository baseline uses the same B simplices and keeps the event transfer dependent on its own assumptions. [Historical working notes, pp. 19–20](https://chatgpt.com/library?file_id=libfile_0b03fa1c6524819193bbdef197bb21b4&account_id=personal) · [Pinned repository B geometry](https://github.com/ud-tetra/UD-Physics/blob/03722496f5b00e8f3f01b2400e4015eb65fdebc4/artifacts/pachsym-20261104-01/exact-001/files/README.md)

## The PB5 projector on edge preparations

Use the five cells \([i,i+1,5,6]\), cyclically in \(i\), with the same incidence convention. Let \(S\) select the eleven distinct edges in the five radial triangles \([i,5,6]\). The positive Whitney face masses give the additive sink the same kernel as \(S\). The observable row space closes at \([S;SA]\), with rank 22, leaving a 21-dimensional lossless invariant space \(K\). Its orthogonal projector is \(P_K=U(U^\mathsf TU)^{-1}U^\mathsf T\) for any basis matrix \(U\) of \(K\).

Let \(E\) include the 16 oriented edge coordinates in the 43-dimensional carrier and let \(Q_{\rm eq}\) select the five equatorial edges in that edge space. Every equatorial edge basis vector lies in \(K\) because both \(S\) and \(SA\) annihilate it. Every other edge basis vector lies in \(\operatorname{im}S^\mathsf T\subset K^\perp\). Thus the explicit projected edge encoding for any shear map \(L\) is
\[
P_K E L = E Q_{\rm eq}^\mathsf T Q_{\rm eq} L .
\]
Instantaneous projection and the subsequent evolution on \(K\) are distinct operations. [PB5 interface audit](https://chatgpt.com/library?file_id=libfile_fde3_f-19390516f1bc8191a59d5674402e8c31_6894c086e37481918ca587ea44a8b0bc&account_id=personal)

## Five shear coordinates and two preparations

Supply a unit regular planar pentagon, with equatorial angles \(\theta_i=2\pi i/5\) and poles at equal opposite heights. This chart specifies the test preparations. The incidence metric and positive sink support specify the dynamics. Decompose the Frobenius-normalized symmetric trace-free space into the axisymmetric coordinate \(q_0\) along \(\operatorname{diag}(1,1,-2)/\sqrt6\), the planar spin-two coordinates \((q_c,q_s)\) along \(\operatorname{diag}(1,-1,0)/\sqrt2\) and the symmetric \(xy\) basis matrix, and the two axial shears \(xz,yz\). The spin designation refers to rotation about the axis in this supplied chart.

**Signed equivariant preparation.** Form the vertex potential \(p_i=x_i^\mathsf TQx_i\), and put \(L(Q)_{ij}=p_j-p_i\) on oriented edges. This is a candidate linear preparation. On the surviving equator its cyclically oriented entries are
\[
 \frac{q_c(\cos 2\theta_{i+1}-\cos 2\theta_i)+
 q_s(\sin 2\theta_{i+1}-\sin 2\theta_i)}{\sqrt2}.
\]
The last cyclic edge changes sign in the increasing orientation basis. The projected Gram has gain \(5(5+\sqrt5)/8\) on each planar shear and zero on the other three coordinates, giving exact rank two. The \(xz,yz\) entries vanish for this potential on all supplied vertices. Their absence from this preparation alone would be insufficient evidence of damping.

**Symmetry bound for any linear signed-edge preparation.** For \(D_5\) equatorial rotations and reflections together with pole exchange, \(P_K E\) takes values in the signed equatorial edge module. Pole exchange acts trivially on that module and reverses \(xz,yz\). The unique equatorial vector fixed by all rotations is the oriented cycle, which reverses under reflection. The axisymmetric source coordinate is fixed by both. Equivariance therefore kills \(q_0,xz,yz\). The signed potential example realizes the resulting rank-two upper bound.

**Directional measurement with a supplied cyclic orientation.** The geometric measurement \(n_e^\mathsf TQn_e\) is independent of edge orientation. If its amplitudes are assigned to the chosen signed cycle, the projected entries are
\[
 \frac{q_0}{\sqrt6}
 -\frac{q_c\cos(2\theta_i+2\pi/5)+q_s\sin(2\theta_i+2\pi/5)}{\sqrt2}.
\]
The Gram gains are \(5/6,5/4,5/4,0,0\), with rank three. The supplied cycle excludes reflection equivariance of this signed preparation. No fitted parameters or empirical targets enter either calculation. The existing support-to-shape audit supplies an edge measurement and leaves the reverse preparation law open. [Edge-strain constitutive source audit, §§1–3](https://chatgpt.com/library?file_id=libfile_2ee214edca088191a0456621df881b4a&account_id=personal)

## Same-clock relay transfer

The historical 15-dimensional A→B sector is specified as a zero mode plus a 14-dimensional squared-frequency-five sector. For an intertwiner \(A_{\rm PB5}T=TA_{\rm relay}\) with the same unit clocks, that sector maps into \(\ker(A_{\rm PB5}^2+5I)\), which is zero. Consequently a same-clock intertwiner on the stated historical sector has rank at most one. Geometric transfer with a changed generator, altered clock, or additional port remains a separate construction. The full five-dimensional physical shear identification remains open beyond the stated edge encodings. [Historical working notes, pp. 13 and 19–20](https://chatgpt.com/library?file_id=libfile_0b03fa1c6524819193bbdef197bb21b4&account_id=personal)
