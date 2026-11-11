# P06-to-quadrupole source and normalization audit v0.2

**RESULT — EXACT / NO-GO under linear full-S4 hypotheses.** The source numerator `Delta_theta=8-1=7` counts nonreference parity states. Its natural seven-coordinate permutation representation can feed at most **two** of the five trace-free response dimensions through an S4-equivariant linear map. A uniform seven-state source maps to zero under **every** such map. Thus this carrier and symmetry cannot turn a uniform `7/192` into a nonzero quadrupole amplitude by division by five. Neither a physical U(1) coupling nor a q-pairing Hamiltonian coefficient follows. Nonuniform source weights, nonlinear maps, extra carriers, and reduced symmetry are different branches.

## Source and typed object contract

Integrated base `ud-tetra/UD-Physics@4aa087681f700ab8cb1177a2d8aa1d0866417da3`. Recovered ledger v0.85, `experiments/action-normalization-audit/sources/ledger_v0.85.json`, SHA-256 `8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec`: P04=`|Theta|=8`, P05=`N1=192`, **P06=`Delta_theta=8-1=7`**, F06/C05=`dim Sym²_0(3)=5`, C06=`7/960` exact internal and frozen as physical coupling/current q-pairing coefficient, Q06=current source-selected q-pairing amplitude zero. The [prior v0.4 critique audit](https://github.com/ud-tetra/UD-Physics/issues/357) distinguishes these. The historical [master manuscript excerpts](../qpb1-impedance-selection/sources/MANUSCRIPT_EXCERPTS.json), `UD@957d443` §§Fine-Structure Coupling/Dressing, explicitly *assume* equal coherence division. No measured alpha, Gibson target, or dressed factor enters this calculation.

Work exactly over `Q` with ordered vertices `0,1,2,3`, standard Euclidean inner product on `Q⁴`, `H={v:sum_i v_i=0}` and orthogonal projector `P_H=I-J/4`. S4 permutes vertices. The five-dimensional *response* `R=Sym²_0(H)` consists of symmetric operators on H with zero H-trace; the metric is `Tr(XY)`. This is an SO(3)-type quadrupole representation on a chosen 3D real/rational carrier, **not** a physical photon/graviton identification. The source `C=Q^{Theta\{000}}` has basis indexed by the seven nonzero three-bit words, with S4 acting via vertex-induced permutations of the three opposite-edge matchings. A count `|Theta\{000}|=7`, an element of C, a response tensor, and a physical coupling are distinct typed objects. The uniform vector `u=sum_theta e_theta` is a specified *additional* choice for mapping the count to a source.

## Representation obstruction and exact construction

The S4 action on `C` factors through S3. Its character on the classes `(identity, transposition, double transposition, 3-cycle, 4-cycle)` is `(7,3,7,1,3)`, hence `C=3·1 + 2·2` as real S4 representations. For `R`, the symmetric-square character `[(chi_H(g)^2+chi_H(g²))/2]-1` is `(5,1,1,-1,-1)`, hence `R=2+3`. Therefore `dim Hom_S4(C,R)=2`; every image lies in the **one** two-dimensional irreducible summand of R, so every such map has rank at most two. The kernel has dimension at least five. R contains no trivial summand, so **every** equivariant linear map kills `u`. This is a proof for linear maps and this declared S4 action, not an assertion about every possible constitutive law.

An explicit rank-two witness uses each unoriented edge `ij` and the trace-free dyad

`M_ij=(e_i-e_j)(e_i-e_j)^T-(2/3)P_H`.

For the three opposite-edge matchings `p`, let `Q_p=sum_{ij in p} M_ij`. Then `sum_p Q_p=0`, and

`Psi(c)=sum_{theta!=000} c_theta sum_p theta_p Q_p`

is S4-equivariant, rank two, with `Psi(u)=0`. The reproducible [exact replay](audit.py) verifies rank, zero image, and all 24×7 covariance cases. This demonstrates that a nonuniform parity-state *distribution* can produce a two-mode response after a chosen linear law; neither the distribution nor the law is selected by the integer seven.

## Separate edge-plus-interior branch

The critique describes the numerator as “six edges plus one interior.” That is **not P06**. For comparison only, take a different seven-coordinate carrier `E=Q^6_edges ⊕ Q_top`, with the edges permuted by S4 and the top coordinate transforming trivially or by orientation sign. The edge representation is `1+2+3`; neither a trivial nor a sign top maps into R. Hence `dim Hom_S4(E,R)=2`. The explicit edge map `Phi(x)=sum_ij x_ij M_ij` is surjective onto R, with kernel exactly the uniform edge vector. Its Gram matrix has exact eigenvalues `(0; 2,2; 4,4,4)` on uniform, opposite-pair constant zero-sum, and opposite-pair antisymmetric sectors respectively. Thus the independent two- and three-mode scales are not fixed by symmetry, while a uniform `6+1` source again maps to zero. This branch cannot silently replace the parity seven in C01/P06.

## Normalization and interpretation

**NO-GO / stated premises:** symmetry and dimensions alone determine neither a physical source vector nor a unique relative coefficient for the two allowed response channels. A trace-normalized quadratic statistic `Tr(Psi(c)²)/5` can be *defined*, but the denominator is a chosen convention and the statistic vanishes at uniform c; `Tr(Psi(c))/5=0` for every trace-free response. Neither equation implies an electromagnetic `alpha=(7/192)/5`. Current ledger Q06's zero q-pairing source is consistent with the uniform-source obstruction, but the ledger's separate source construction was not rederived here; one result is not substituted for the other. Physical promotion remains 0.

**Reopening condition:** source-derived nonuniform parity weights or a new carrier, plus a typed S4-equivariant (or explicitly symmetry-broken) interaction operator, an independent normalization law, and an electrical readout with units. Test a held-out observable after freezing these choices. A changed premise opens a new branch and does not refute this scoped no-go.

## 2026-11-11 source-weight addendum v0.2

**Source scope.** The current ledger v0.85 Q201–Q204 defines pair integrity, pre-gate latent support, and the binary three-component receipt `omega^lat_p=T_p^pair 1[Lambda_p^pair>0]` from C0/C1 and hard-integrity data. Q209 proves covariance of the receipt. Q205/Q208 quarantine its obligation and endpoint interpretation; Q210 blocks an obligation conclusion from the closed carrier. None of Q201–Q210 defines a measure on the seven **parity states** `Theta\{000}`, a linear functional from that measure to the response, or a physical electromagnetic interaction. Q01/Q04/Q06 already report a pairing 2-irrep and source-complete scalar q block, but the current source-selected non-scalar q-pairing amplitude is **zero** (Q06); no nonzero edge-class contrast is admitted there. The supplied historical ledger v0.39(2), SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, F06/C05/C06/Q06 has the same separate gate. The provided `master_action.md` and `coherence_equation.md` files are placeholder reconstruction text; no rule is imported from them.

**EXACT / conditional counterexample.** Grant the *additional, unproved* identification of the Q204 mask `omega` with the three labels of the P06 parity fiber. For each nonzero mask `omega`, define two probability weights on `Theta\{000}`:

`c_delta(theta|omega)=1[theta=omega]`, and

`c_orbit(theta|omega)=1[|theta|=|omega|]/binom(3,|omega|)`.

Both are nonnegative, sum to one, and transform covariantly under every vertex permutation. For the explicit rank-two `Psi` of v0.1, `Psi(c_orbit)=0` because each Hamming orbit sum is invariant and the response has no invariant tensor. For `|omega|=1` or `2`, `Psi(c_delta)` is `Q_p` or `-Q_p` for the unique marked or unmarked pair, with exact squared trace norm `8/3`. At `omega=111`, both images are zero; at `omega=000`, the point mass is outside this seven-state source, so the rule requires an additional boundary convention. The positive normalized family `c_t=t c_delta+(1-t)c_orbit`, `0<=t<=1`, has `Psi(c_t)=t Psi(c_delta)` and squared response norm `(8/3)t²` for all six middle masks. Hence symmetry, nonnegativity, total mass one, and the same source-bound receipt do **not** determine the amplitude or a `1/5` allocation. [weight_gate.py](weight_gate.py) checks seven nonzero masks and `7×24×2=336` exact covariance relations in [weight_gate_results.json](weight_gate_results.json).

**Disposition:** AUTO_FREEZE promotion of this receipt-to-alpha route under the current source set; preserve the Q204 receipt and Q01/Q06 internal results. This nonidentifiability does not disprove a future, separately specified map. Reopen only with a versioned pre-event rule selecting a weight vector or edge contrast, a typed response/interaction operator and normalization, and a physical charge readout with an independent bridge test. No fitted endpoint or alpha value was used; physical promotion 0.
