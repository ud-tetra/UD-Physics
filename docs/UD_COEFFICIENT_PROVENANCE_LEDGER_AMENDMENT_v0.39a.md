# Coefficient provenance ledger amendment v0.39a

**Scope:** Q171–Q173. **Evidence:** EXACT, internal incidence algebra. **Physical Promotion = 0.**

This append-only amendment records the [source-custodian decision](https://github.com/ud-tetra/UD-Physics/issues/338#issuecomment-7107945798) and [independent review](https://github.com/ud-tetra/UD-Physics/issues/338#issuecomment-7105791451). The [frozen v0.39 source](https://github.com/ud-tetra/UD-Physics/blob/421f4d533e998efc9aa57b2cf926e7a9f596bf0e/sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md) is retained byte-for-byte (Git blob 70d5e1c9c6bd29b397e7f646b74c39aa7fdaf228).

## Typed convention and row readings

Keep the Q169 ascending-oriented boundary block \(D_k^{\mathrm{Q169}}\colon C_k\to C_{k-1}\) and generator \(A=D-D^{\mathsf T}\). In the amended current expressions use the typed coefficient alias \(B_k^{\mathrm{flow}}=-D_k^{\mathrm{Q169}}\) for \(k=1,2,3\). A current's reference direction is lower to higher degree. Its value is signed.

- **Q171.** For a face \(f\) incident on tetrahedron \(\tau\), \(J_{23}(f,\tau)=2(B_3^{\mathrm{flow}})_{f\tau}c_f c_\tau\), and \(\dot S_\tau^{\mathrm{core}}=\sum_f J_{23}(f,\tau)\) for \(S_\tau^{\mathrm{core}}=c_\tau^2\).
- **Q172.** For face stock \(S_f^{\mathrm{iface}}=c_f^2\), \(\dot S_f^{\mathrm{iface}}=\sum_e J_{12}(e,f)-\sum_\tau J_{23}(f,\tau)\), with \(J_{12}(e,f)=2(B_2^{\mathrm{flow}})_{ef}c_e c_f\).
- **Q173.** The existing face gate acts on that same signed current: \(J_{23}^{h}(f,\tau)=h_fJ_{23}(f,\tau)\). In paired stock accounting an enabled gated term enters the tetrahedron and leaves the face with opposite signs.

From Q169, \(A_{\tau f}=-(D_3^{\mathrm{Q169}})_{f\tau}\) and \(A_{f\tau}=(D_3^{\mathrm{Q169}})_{f\tau}\). The two contributions to \(\frac{d}{ds}(c_f^2+c_\tau^2)\) cancel pairwise. For the Q170 cut check, with indicator \(\chi\), this pair contributes \((\chi_\tau-\chi_f)J_{23}\). Internal pairs cancel and boundary contributions retain the signed direction. This is a notation and stock-accounting clarification for Q171–Q173. Gate-selection and physical claims are outside the scope.

## Verification record

The independent review records the incidence and cut checks. [PR #301](https://github.com/ud-tetra/UD-Physics/pull/301) supplied the separate sign-replay verification at head 0607b33025be54c2fe957f2f7d537b673a76127d, as [recorded on issue #338](https://github.com/ud-tetra/UD-Physics/issues/338#issuecomment-7107989961).
