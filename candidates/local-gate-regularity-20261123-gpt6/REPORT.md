# Pairwise normalized gate: zero-state regularity and typed swap audit v0.1

**EXACT / CONDITIONAL / NO-GO_SCOPED. Physical Promotion = 0.**

## Source and history
Pinned base UD-Physics main `80525f1296a15f4a87f0efecc491679deec39b9b`. Native-event restrictions: `experiments/pachner-local-jump-current/README.md` blob `047db9ebafb0192fcf7bc72bf43506a3dee2c2ec`. Related state-local nonlinear family is **development draft** PR #482, `candidates/nonlinear-incidence-robustness-20261123-gpt6/REPORT.md` blob `efc0d03bf400d54dbb9f9d133943dbcd2e9dd40e`. The **specific pairwise ratio gate** is sourced to user-supplied original scratch analysis, not a frozen native law.

## Exact definition and results
For real x,y and assumed real lambda, define `g(x,y)=1+lambda*(x^2-y^2)/(x^2+y^2)` on nonzero pairs and `g(0,0)=1`.

1. **NO-GO_SCOPED (continuous coefficient):** Along the x-axis, g tends to `1+lambda`; along the y-axis, it tends to `1-lambda`. For lambda !=0 no continuous extension at zero exists. More generally a nonconstant degree-zero homogeneous coefficient has no continuous extension at origin.
2. **EXACT / CONDITIONAL exchange:** `g(x,y)-g(y,x)=2lambda*(x^2-y^2)/(x^2+y^2)`. Thus it is not symmetric as an *unsigned scalar on exchangeable endpoints*. If the ports are typed or have an orientation-sensitive signed transformation, check covariance under the actual sourced action instead; a bare coordinate interchange reverses the 2D skew J and is not itself a symmetry test for oriented incidence.
3. **EXACT (two-coordinate skew control):** For `z=(x,y)`, `J=[[0,1],[-1,0]]`, formal evolution `z'=g(z)Jz`, the unit quadratic stock `x²+y²` is conserved. Although g is discontinuous at origin, `F(z)=g(z)Jz` has a continuous extension `F(0)=0` since `|g|<=1+|lambda|` and `|F(z)|<=(1+|lambda|)||z||`. For lambda !=0 the resulting F does not have a common linear derivative at zero.
4. **OPEN gate regularity on larger carriers:** If g is used on a separate incidence block with nonzero other coordinates at x=y=0, the full RHS may be discontinuous. A specific full-carrier lift and local well-posedness proof are necessary.
5. **Optional nonnegativity:** `|lambda|<=1` suffices for nonnegative coefficients at all nonzero pairs, but this is a chosen bound, not a sourced constitutive selection.

## Implications
Passing pointwise skew and pre-event locality does not derive the coefficient, symmetry invariance, stability, selection rule, or autonomous 29→85 birth. A bounded denominator regularization introduces a scale; any choice requires disclosed provenance. A symmetric smooth coefficient would have to be specified and sourced separately. No 13a²→4a² endpoint trajectory, no physical correspondence. Physical Promotion = 0.

## Verification
Local independent symbolic replay `python verify.py` PASS. Locally assembled ZIP: `UD_Local_Gate_Covariance_Audit_v0.1.zip`, SHA-256 `bf0738660e95a4ff7d1a649eedaee6f5c472741dc9a6214347fea43c2f890b70`. The GitHub miniature script is a reproduction aid; CI and non-constructor review pending.
