# UD C06 incidence interaction v0.3

**EXACT** for unit-weight edge cancellation on the filled tetrahedron and its failure on AW5. **NO-GO** for unique flag or midpoint readout selection from the edge form alone. **CONDITIONAL** for the five-seat normalization. **Physical Promotion = 0.**

## 1. Exact edge form

Use increasing vertex order to orient simplices, real coefficients, the unit simplex inner product in each grade, and the native time parameter. Write \(B_k:C_k\to C_{k-1}\), \(B=\sum_k B_k\) on the graded space, and \(A=B^\mathsf T-B\). Since \(B^2=0\), the edge block of \(A^\mathsf T A\) is \(\Delta_1=B_1^\mathsf T B_1+B_2B_2^\mathsf T\).

For edges \(e,e'\) meeting at \(v\) and contained in \(f\), the \(v,f\) entry of \(B_1B_2=0\) gives \([v:e][e:f]+[v:e'][e':f]=0\), since exactly two edges of \(f\) meet at \(v\). Multiplying by \([v:e'][e:f]\) shows \([v:e][v:e']+[e:f][e':f]=0\). Disjoint edges contribute zero in both channels. Every wedge in the filled tetrahedron has a triangle, and each edge has two incident vertices and two incident faces. Thus
\[
\Delta_1=4I_6,\qquad \|A j\|^2=4\|j\|^2\quad (j\in C_1).
\]
This is an exact cancellation of edge interference in the full energy. The individual curl and divergence summands have opposite nonzero coefficients on adjacent edge pairs.

## 2. Flag lift and nonuniqueness

Let \(S:\mathbb R^6\to\mathbb R^{12}\) duplicate each edge amplitude into its two edge–face flags. Then \(S^\mathsf T S=2I_6\) and \(P=SS^\mathsf T/2\) is the orthogonal projector onto \(\operatorname{im}S\). A flag metric \(M\) represents the edge form when \(S^\mathsf T M S=4I_6\). On \(J=Sj\) this gives \(\mathcal E_1=2\|J\|^2\). The Euclidean flag metric \(I_{12}\) works with an external factor two, or one can absorb the factor into \(M_0=2I_{12}\). The canonical compression by the pseudoinverse of \(S\) gives \(2P\), which acts as \(2I\) on the sampled subspace.

Define signed face summation \(F\) by \((FJ)_f=\sum_{e\subset f}[e:f]J_{(e,f)}\), so \(FS=B_2^\mathsf T\), and set \(K=F(I-P)\). For every \(\lambda>0\), the positive-definite metric
\[
M_\lambda=2I_{12}+\lambda K^\mathsf T K
\]
has exactly the same pullback as \(M_0\), since \(KS=0\). For distinct edges \(e,e'\) in a common face \(f\), its \(((e,f),(e',f))\) entry is \(\lambda[e:f][e':f]/4\). Each column of \(K\) has a contribution of half the incidence sign in its own face and minus half the sign of the duplicate flag in the other face. The column pair overlaps only at \(f\). The construction is equivariant under vertex relabeling with the induced orientation signs. Thus even a positive, equivariant flag metric can exhibit within-face interference while reproducing the exact edge form. The coherent face-only energy \(F^\mathsf T F\) has a different pullback, \(B_2B_2^\mathsf T\).

The edge identity gives incoherent summation as an exact representation of the native energy on duplicated samples. Lifting that representation to independent flag amplitudes requires a constitutive restriction or readout prescription. The midpoint-axis gains are separate from this edge restriction.

## 3. Conditional shear response

Use the Euclidean Frobenius inner product on real symmetric trace-free \(3\times3\) tensors \(Q\), and evaluate each direction by \(n^\mathsf T Qn\). In coordinates where the tetrahedral vertices are alternate cube corners, the six unoriented edge directions are \((e_i\pm e_j)/\sqrt2\), and the three opposite-edge midpoint directions are the coordinate axes. Write \(Q=Q_E+Q_{T_2}\) with the diagonal and off-diagonal parts. The six-edge sum of squares is
\[
\sum_{\rm edges}(n^\mathsf TQn)^2
  =\tfrac12\|Q_E\|_F^2+\|Q_{T_2}\|_F^2.
\]
The three-axis sum is \(\|Q_E\|_F^2\). Two flags per edge with gain \(g\) per amplitude square, plus one midpoint per axis with gain \(m\), therefore give sector eigenvalues \(g+m\) and \(2g\). Declaring \(m=g=1\) in this normalization yields \(2I_5\) and trace share \(1/5\) per orthonormal component. The full native edge-energy normalization would correspond to \(g=2\) for the same input map. An isotropic response at that normalization would require \(m=2\). The incidence calculation supplies the duplicate count, while equal relative gain and the allocation of the conditional \(7/192\) defect fraction remain separate hypotheses. The target \(7/960\) and equal-response condition were known before this audit. No empirical fit entered the proof.

## 4. AW5 extension

The 47D filled and 46D hollow stars have the same 8 vertices, 18 edges and 16 faces. Removing the hub changes only \(B_3\), so their \(\Delta_1\) are identical. For any simple simplicial complex, each adjacent edge pair lies in at most one triangle. A filled wedge cancels as above. A wedge with no triangle retains \([v:e][v:e']\) from the vertex channel. The AW5 vertex degrees are six at each hub vertex and three at each outer apex. There are \(4\binom62+4\binom32=72\) unordered wedges and \(3\cdot16=48\) filled wedges. The remaining **24** give **48** nonzero off-diagonal matrix entries, each of magnitude one.

Each of the six hub edges belongs to four faces and has diagonal entry six. Each of the twelve apex-to-hub edges belongs to two faces and has diagonal entry four. For \(e=01\), \(e'=05\), where apex 5 belongs to the leaf opposite vertex 1, triangle \(015\) is absent. Both edges start at vertex 0 in the chosen orientation, so \((\Delta_1)_{01,05}=+1\). This is an incidence-level obstruction to extending the scalar edge form to the glued carriers.

## Verification and provenance

The accompanying integer replay builds the signed boundaries independently, checks the two pullbacks and a nonzero within-face metric entry, checks the conditional shear response by a rational Gram calculation, and counts filled and unfilled wedges. It uses the filled simplex convention of the prior AW5 exact work and the incidence and readout setup in the supplied C06 audit. The audit extends the same scalar identity previously used in the structural-exclusivity draft to its flag-lift and AW5 scope. Verification is a constructor replay.

**Claim boundary footer:** Physical Promotion = 0. Native interaction and defect-to-response allocation remain open.
