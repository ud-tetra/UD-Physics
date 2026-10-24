# Two exact site-response constraints for the graphite source

**Status: EXACT / CONDITIONAL carrier result; archived KC replay NUMERICAL / DEVELOPMENT; measured graphite source OPEN.** This follows the [passive-port attribution limit](../graphite-port-attribution/README.md). The angle pair was already known; no angle or friction value was fitted here.

## Four-site test

Let `H: R^14 → R^2` be a lateral force versus labeled vertical site-displacement cross-Hessian, in the *direct* output coordinates of the archived seven-cell honeycomb carrier. The proposed pure source is `H=S(w)=Σ_i w_i MᵀP_i B₁ᵀ`. Its two output components are covectors with the declared unit-edge metric and triangular Gram `G`; the site labels are `A0..A6,B0..B6`. These are abstract units until a physical map and material scale are specified. The C₃ site permutation is `A_k→A_(4k mod 7)`, `B_k→B_((4k−1) mod 7)`, while columns transform by `J₂⁻ᵀ=[[0,−1],[1,−1]]`. The fixed sites A0 and B5 have zero columns. Four three-site orbits have representatives A1, A3, B0, B1.

Write their ordered components as

`h=(H_A1^1,H_A1^2,H_A3^1,H_A3^2,H_B0^1,H_B0^2,H_B1^1,H_B1^2)^T`.

**EXACT / CONDITIONAL:** For **every** real orbit-weight vector `w`, the pure source obeys both

`r₁ = H_A1^2 + H_B1^1 = 0`,

`r₂ = H_A1^1 − H_A3^1 + H_B0^1 − H_B0^2 + H_B1^2 = 0`.

The source matrix restricted to the eight representative components has rank six and kernel consisting of uniform weight shifts; the two displayed constraint rows have rank two and annihilate it. Every C₃-equivariant `2×14` map is determined by those eight components, so **within that symmetry class**, both constraints are also sufficient for belonging to the six-dimensional source span. This sufficiency tests a parameterization, not its physical origin or its bath law. The exact verifier constructs all eight symmetry-allowed basis maps and checks the carrier's full 14-site covariance.

The constraints do not depend on `w`, an overall nonzero coupling scale, or bath damping. They provide a source-level falsification gate before a friction calculation. They do depend on correct atom labeling, lateral basis registration, and the assumed physical identification of the carrier's site variables with vertical atomic or phonon coordinates. Adding other source terms or a conventional background changes the tested model.

## What to measure

In a site-resolved atomistic calculation, displace each of A1, A3, B0, B1 by a calibrated vertical increment and measure both lateral force derivatives. Register the C₃ labeling from geometry/covariance **before** evaluating `r`. If the proposed source is an *additional* coupling, apply the constraints to `H_add=H_measured−H_conventional`, with the conventional map fixed using disjoint calibration data; applying them to the total Hessian tests only a pure-source model. Cross-check the remaining ten columns against the declared C₃ transformation and the fixed-site zeros.

For a frozen eight-vector estimate `h` with covariance `Σ` in the direct basis, set `L=[[0,1,0,0,0,0,1,0],[1,0,−1,0,1,−1,0,1]]`. The tested residual and covariance are `r=Lh`, `V=LΣLᵀ`. With a predeclared Gaussian error model, invertible `V`, fixed registration and no test-data fitting, `rᵀV⁻¹r` has a reference `χ²` law with two degrees of freedom under the pure-source null. Registration, baseline uncertainty and shared numerical errors belong in `Σ` (or a more appropriate simulation/empirical error model); no such covariance is available here, so no significance or confidence level is claimed. If direct components happened to have equal independent variance `σ²`, then `V=diag(2,5)σ²`, but that is an illustrative assumption, not a graphite error estimate.

## Archived material-model replay

The verifier reuses the five archived, C₃-aligned KC cross-Hessians from [MATERIAL_PROJECTION_RESULTS.json](../../artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures/2026-10-22T224639Z-codex-graphite-material-projection-fcd6e90e-4531aa0e-8487-4d43-b0dd-cfe246d1b6b4/MATERIAL_PROJECTION_RESULTS.json). It applies the **previously selected** site offset 2 and the archived geometric map `x_cart=F u_direct` (bond length 1.42 Å, coincidence basis and primitive swap), so `H_direct=FᵀH_cart`. At cutoff 16 Å and central-difference step 10⁻⁴ Å it gives `r≈(−4.947113,−2.487050)` in meV/Å per upper atom. Across the five previously archived cutoff/step checks, the first component ranges from −4.947141 to −4.947113 and the second from −2.487064 to −2.487050. These are sensitivities to **these five computational choices**, not statistical uncertainty bounds. The old full-map normalized span residual was about 0.155176. This replay shows that the specified KC reconstruction does not satisfy the *pure* source constraints; it supplies neither an experimental refutation of a separate UD addition nor a kinetic-friction measurement.

Run `python3 experiments/graphite-source-constraints/verify_constraints.py`; [captured result](../../artifacts/graphsrc-20261023-48d0f1fd/exact-001/files/graphite-source-result.json) and [receipt](../../candidates/graphite-source-constraints/mathematical_receipt.json) preserve the exact algebra and the selected numerical replay. A future signed paired-angle force/load prediction still needs an independently restricted physical coupling, material stiffness/loss, conventional PES/contact baseline, and unused force data. Mainline physical promotion remains zero.
