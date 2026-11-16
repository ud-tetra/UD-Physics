# One-channel AW5 exterior bulk discriminator

**EXACT_INTERNAL. Physical Promotion = 0.** Use real oriented simplicial chains with unit simplex weights. The [multiface result](https://github.com/ud-tetra/UD-Physics/pull/396) concerns the shared cycle–face sector. Here the input and output are taken in its complementary face subspace.

Orient the filled central tetrahedron and four leaves coherently so each internal face cancels. Let $c$ be the central boundary column, $d_i$ the four leaf boundary columns, and $d=\sum_i d_i$. Then $\|c\|^2=4$, $\langle c,d_i\rangle=-1$, and the leaf columns are mutually orthogonal with norm squared four. The closed exterior shell $e=c+d$ has signed entries only on the twelve exterior faces, $\|e\|^2=12$, and $B_2e=0$ on both carriers. This is the same signed direction as the matched exterior probe already used in the [face-residue replay](https://github.com/ud-tetra/UD-Physics/blob/17ce43794977068a27b8805d4004a89fd9f83b5a/candidates/aw5-hollow-star-intake/residue.py), up to scale. The result below gives its full analytic trace and the first separating derivative.

Use one signed exterior face preparation $q(0)=e$, zero initial bulk $\sigma(0)=0$, and the matched scalar readout $R(s)=\langle e,q(s)\rangle/12$. Use the same preparation and readout on both carriers. A loop-only output through $B_2$ vanishes on this preparation throughout the evolution. Write $D$ for the carrier's top boundary matrix. The invariant face/bulk dynamics are
$$
q'=-D\sigma,\qquad \sigma'=D^\mathsf Tq-\gamma\sigma,\qquad
q''+\gamma q'+DD^\mathsf Tq=0.
$$
Here $\gamma\ge0$ is optional uniform bulk damping, fixed to the same value on both carriers. Define $u_{\lambda,\gamma}$ by $u''+\gamma u'+\lambda u=0$ with $u(0)=1$, $u'(0)=0$.

In the hollow carrier $DD^\mathsf T$ has eigenvalue 4 on the leaf-boundary span. The squared projection of $e$ onto that span is 9, leaving 3 in the stationary face subspace. In the filled carrier the top Gram matrix restricted to the central coordinate and unit symmetric leaf coordinate is
$$
\begin{pmatrix}4&-2\\-2&4\end{pmatrix}.
$$
The top coordinates of $e$ in this basis are $(1,2)$. Applying the boundary map weights the squared top amplitudes by their eigenvalues and gives face weights $3/4$ at $\lambda=2$ and $1/4$ at $\lambda=6$. Therefore
$$
R_{\rm hollow}(s)=\tfrac14+\tfrac34u_{4,\gamma}(s),\qquad
R_{\rm filled}(s)=\tfrac34u_{2,\gamma}(s)+\tfrac14u_{6,\gamma}(s).
$$
At $\gamma=0$ the modal functions are $\cos(\sqrt{\lambda}s)$, including the constant at $\lambda=0$. The spectral moments of orders zero, one, and two agree. The order-three moments are 48 and 60, respectively. The derivatives of the two traces agree through fifth order for every common $\gamma$, while the sixth derivative of hollow minus filled is 12. Thus
$$
R_{\rm hollow}(s)-R_{\rm filled}(s)=s^6/60+O(s^7).
$$
With zero damping, the cosine Taylor remainder after degree seven gives $|\Delta R-s^6/60|\le (192+336)s^8/8! = 11s^8/840$, using the two fourth spectral moments. Consequently $\Delta R\ge s^6/280$ for $0<s\le1$. This supplies one scalar discriminator for the two declared carriers at sufficiently small positive native time. It establishes a trajectory difference, so an arbitrary isolated sample need not distinguish the carriers. The common linear evolution at $\gamma=0$ already suffices. Any nonlinear post-processing of identical $B_2$-only traces would still see identical data.

The relevant face subspace is $\ker B_2$, containing both top boundaries and harmonic representatives. The actual homology is $\ker B_2/\operatorname{im}B_3$. Bench access to a coherent signed exterior face preparation and readout, gain and noise tolerance, timing, and instrument admission remain open. The derivation makes no SI identification.
