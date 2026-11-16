# AW5 multiface real quadrature network

**EXACT_INTERNAL. Physical Promotion = 0.**

The [single-face bipyramid readout](https://github.com/ud-tetra/UD-Physics/pull/395) extends to a network of coupled faces. Use the unit simplex inner products and increasing vertex orientation. The hollow 46D carrier has four tetrahedra glued to the faces of the formal hub 0123, without the hub itself. Adding the hub gives the filled 47D carrier. Their simplex counts by degree are $(8,18,16,4)$ and $(8,18,16,5)$. Their signed vertex–edge and edge–face incidence matrices $B_1$ and $B_2$ coincide.

## Closed face network

Let $j$ and $q$ be real edge and face states under $A=B^\mathsf{T}-B$. Define $K=B_2^\mathsf{T}B_2$ and
$$
F=B_2^\mathsf{T}j,\qquad H=Kq.
$$
A vertex gradient changes $F$ by $B_2^\mathsf{T}B_1^\mathsf{T}\chi=0$ and leaves $H$ fixed. The $B_1^\mathsf{T}$ and $B_3$ terms vanish in the two readouts by signed boundary nilpotency. Thus $F'=-H$ and $H'=KF$ on $\operatorname{im}K$. In the unit simplex metric set $G=K^{\dagger/2}H=K^{1/2}q$, where $K^{\dagger/2}$ is the inverse square root on the positive spectrum and zero on the kernel. Then
$$
F'=-K^{1/2}G,\qquad G'=K^{1/2}F .
$$
Individual face coordinates are coupled. In an orthonormal positive spectral basis of $K$ each pair $(F_k,G_k)$ rotates at $\sqrt{\lambda_k}$ and conserves $(F_k^2+G_k^2)/\lambda_k$. Their sum is the squared norm of the projection onto $\operatorname{im}B_2\oplus\operatorname{im}B_2^\mathsf{T}$, in degrees one and two. The normalization is a native state norm. Within a degenerate eigenspace, the total for that eigenspace is basis-independent.

The exact positive cycle-block spectrum is
$$
3\ (\times2),\qquad 5\ (\times3),\qquad
\frac{9-\sqrt{17}}2\ (\times3),\qquad \frac{9+\sqrt{17}}2\ (\times3).
$$
The graph is connected and $\operatorname{rank}B_2=11=18-8+1$, so $\operatorname{im}B_2=\ker B_1$. The real cycle–face sector has dimension 22.

## Exterior completeness and the filled–hollow obstruction

Let $D_E$ contain the twelve columns of $B_2$ for exterior faces, identified here as faces containing a leaf apex. The columns have rank 11, so $D_E^\mathsf{T}$ is injective on the cycle space. The twelve exterior components of each of $F$ and $H$ recover the full 22-dimensional projected state. Explicitly, let $C$ contain any eleven independent exterior boundary columns and $M=C^\mathsf{T}C$. The selected rows of $F$ give $j_{\rm cycle}=CM^{-1}F_C$. The selected rows of $H$ give $B_2q=CM^{-1}H_C$. The coexact face part of $q$ follows uniquely by inverting $B_2$ from $\operatorname{im}B_2^\mathsf{T}$ to $\operatorname{im}B_2$. Equivalently, the exterior loop values and their first native derivatives determine that same projected state.

Both carriers have the same $K$, exterior rows and reduced dynamics. For matched projected preparations the entire multi-face trace is identical at all native times. Adding the hub changes $B_3$, which is filtered out because $KB_3=0$. The result thus supplies complete observation within the cycle–face sector and an exact limit on using that sector to discriminate the two carriers. A complementary readout sensitive to the face kernel of $B_2$ is needed to expose the known harmonic and top-cell differences. No bench calibration or physical promotion is implied.

The exact replay checks signed incidence, common operators, exterior rank, the characteristic polynomial and an integer-valued certificate for the reduced output dynamics on both full multi-grade carriers.
