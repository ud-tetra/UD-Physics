# Phase-006: constrained tetrahedral multiport discriminant and classical equivalence

**RESULT — EXACT / CONDITIONAL:** The previously classified signed-\(S_4\), Euclidean skew-incidence model predicts a fixed four-face sign pattern and exact zero top-cell-to-edge/vertex transfers. Under one declared face–cell bond perturbation an edge transfer appears at order \(t^2\). **FAILED UNIQUE ATTRIBUTION:** A conventional classical skew network with the same 15-port matrix reproduces all transfers identically. These are model-intervention checks, **not** uniquely UD physical predictions.

## Inputs, objects and provenance

Read-only source: [integrated local-generator classification](../qpb1-local-generators/README.md), original base \`41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb\`. Additional source: [phase-005 null comparison](REFERENCE_NULL_PROTOCOL.md), owning branch at \`d8e4b3cf9bbc90075d5757e01c8f660bfcd29057\`. Phase-001 through phase-005 immutable runs remain unchanged.

Let \(C=\bigoplus_{k=0}^3C_k(\Delta^3;\mathbb R)\cong\mathbb R^{15}\), with simplex orientations ascending, real positive metric \(H=I\), ordinary continuous native parameter \(t\), and no physical units. For \(D_k:C_k\to C_{k-1}\) (embedded as 15-by-15 blocks), \(K_k=D_k-D_k^\top\). The imported linear conservative generator is \(G=\sum_{k=1}^3g_kK_k\), with real gains; the positive-energy subfamily requires \(g_k>0\). Here the face index \(j\) is the opposite face obtained by deleting vertex \(j\) from top simplex \(c=[0,1,2,3]\). The \(S_4\) action includes the signs arising from reorienting simplices; that choice matters.

## Source-derived transfer law

The exact imported identities \(K_iK_j=0\) for \(i\ne j\) and \(K_k^3=-4K_k\) yield the full matrix propagator for any real \(t\):
\[
U(t)=e^{tG}=I+\sum_{k=1}^3\left[\frac{\sin(2g_kt)}2K_k+
(\cos(2g_kt)-1)P_k\right],\qquad P_k=-\frac{K_k^2}{4}.
\]
For an initial top cell basis state \(e_c\), \(P_3e_c=e_c\) and \(K_3e_c=\sum_{j=0}^3(-1)^je_{f_j}\); the other \(K_k\) annihilate it. Hence
\[
U(t)e_c=\cos(2g_3t)e_c+\frac{\sin(2g_3t)}2
(e_{123}-e_{023}+e_{013}-e_{012}).
\]
Therefore **EXACT** for this carrier and law: four signed face amplitudes are \((+,-,+,-)\) at a common modulus; every top-cell-to-edge and top-cell-to-vertex amplitude is zero for all \(t\); and the entire top-cell transfer is independent of \(g_1,g_2\). The four-face amplitude signs/ratios are meaningful only if physical port orientation and phase conventions can be operationally fixed. At \(\sin(2g_3t)=0\), the ratio is undefined because all face amplitudes vanish. This is not a physical locality or causal-speed theorem.

## Controlled single-bond alteration: different model, different implications

Choose the opposite face \(f_0=[1,2,3]\) and explicitly add one skew bond \(B_{f_0,c}=+1,\ B_{c,f_0}=-1\), all other entries zero:
\[
G_\varepsilon=G+\varepsilon B.
\]
This is **HYPOTHESIS / intervention**, not a permitted member of the original signed-\(S_4\) generator family: full tetrahedral symmetry is broken, \(K_2B\) need not vanish, and generally \([G_\varepsilon,J]\ne0\). The previous \(J\)-geometric-phase formula therefore cannot be blindly reused.

For any such \(\varepsilon\), from \(e^{tG_\varepsilon}=I+tG_\varepsilon+(t^2/2)G_\varepsilon^2+\cdots\), the leading edge–cell amplitude is
\[
\boxed{(U_\varepsilon(t))_{e,c}
=\frac{t^2}{2}\,\varepsilon g_2(D_2)_{e,f_0}+O(t^3).}
\]
For edges \(e=[1,2],[1,3],[2,3]\), the exact coefficients per unit \(\varepsilon\) at \(g_2=1\) are respectively \(+1/2,-1/2,+1/2\); other edge coefficients vanish to this order. The initial face derivatives become \((g_3+\varepsilon,-g_3,g_3,-g_3)\). A one-bond source perturbation therefore tests whether the symmetry/closed-boundary assumptions are appropriate; it is **not** a prediction from the unmodified source law.

## Conventional nulls and identifiability limit

The earlier **scalar** three-tone baseline \(Z(t)=\sum r_k e^{2ig_kt}\) cannot identify 15 independent register ports or specify their signed readout weights without additional choices. An enriched conventional **15-port** conservative linear network can choose the very same real skew generator \(G\), initial state, physical port mapping, and readout. Its propagator \(e^{tG}\) then agrees on **every** amplitude and controlled gain change, including the defect if the same \(B\) is supplied. Thus port specificity supplies an interpretable *restricted-model* discriminant (and possibly reduces free parameter choices versus unrestricted port fits), but has **zero unique physical attribution** against an incidence-matched classical null. Do not mislabel the restricted scalar null's lack of spatial prediction as evidence against conventional physics.

## Reproducibility and evidence

Run from the repo root:

\`python3 experiments/qpb1-finite-window-phase/multiport_audit.py --out /tmp/qpb-phase006.json\`

A standard-library exact-\(\mathbb Q\) constructor checks the \(15\times15\) incidence matrices, all 24 signed \(S_4\) actions, all cross-operator zeros, three rational gain triples, 13 Taylor orders each (39 checked matrix powers), and four rational single-bond defect strengths. A separate verbose local exact-arithmetic implementation was also exercised in the same construction context and agrees; **not** independent mathematical or empirical replication. Script, output and SHA-256 digests are captured in immutable [phase-006 run](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-006/manifest.json).

**Target exposure / model selection:** The top-cell port intervention and one-bond defect were deliberately chosen after observing the failure of the scalar three-tone bridge in phase-005. No empirical data were fitted. Three unconstrained positive gains, unknown time unit and entire physical source/port mapping remain OPEN. No independent prediction is established.

**Next highest-value discriminant:** identify a source-selected constitutive or perturbation law, with physical port calibration and an unused dataset, that produces a signed/spectral residual *not* achievable by a matched classical incidence network. Otherwise park unique-UD attribution for this finite-dimensional linear family. Priority 99/100.
