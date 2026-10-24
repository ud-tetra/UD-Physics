# Edge reversal gate for a candidate UD graphite source

**EXACT / CONDITIONAL algebra; native route and graphite constitutive law OPEN.** This narrows the [source and damping gate](../graphite-native-source-gate/README.md) without selecting an angle or a material coefficient. The paired 21.8°/38.2° peaks were known before this work. The derivation uses the supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q23–Q26. Q24 is already a conditional candidate, while Q25 and Q26 leave the directed weight and route primitive open. The edge-reversal properties below are **new assumptions** for testing that algebra, not claims imported from the ledger.

## Exchange parity of the candidate

For a physical undirected pair `{i,j}`, Q24 proposes a symmetric coefficient

`c_{ij}=(η_O/2)(w_{ij} Ξ_{ij}+w_{ji} Ξ_{ji})`.

Let `w_±=(w_{ij}±w_{ji})/2` and `Ξ_±=(Ξ_{ij}±Ξ_{ji})/2`, all real and dimensionless for this native algebra. Direct expansion gives

`c_{ij}=η_O(w_+ Ξ_+ + w_- Ξ_-)`.

The mixed parity terms cancel **exactly**. If a route is *assumed* to be signed under edge reversal, `Ξ_+=0`, then a reciprocal edge law `w_-=0` yields `c_{ij}=0`, regardless of a scalar load `P` that preserves reciprocity. A signed route alone cannot activate the Q24 symmetric coefficient. If instead the route is exchange-even, `Ξ_-=0`, reciprocal weights can produce a nonzero `η_O w_+ Ξ_+`. If both weights and route have odd parts, their product survives. These branches are mutually distinct possible completions of Q26. No sign parity for `Ξ` or `w` has been established from a current UD primitive.

**Physical identification is additional:** To treat `c_{ij}` as an element of the graphite cross-Hessian, one must specify an energy/length scale, physical site registration, and the map into `C`. Q24's symbol alone supplies none. If `c_{ij}` instead belongs to another Hamiltonian block, none of the friction conclusions below follows.

## Conditional low-speed prediction and its scope

Consider the narrower *frozen-coefficient material ansatz* at fixed pressure `P`. Assume (i) signed, fixed route values `Ξ_{ji}=-Ξ_{ij}`; (ii) no static orientation bias, so `w_{ij}(0,P)=w_{ji}(0,P)`; (iii) a smooth, reversed-drive covariance `w_{ij}(v,P)=w_{ji}(-v,P)`, where `v` is signed sliding speed along a registered axis; (iv) a physical cross-Hessian map linear in Q24 coefficients, with finite coefficients and no additional constant source; and (v) positive stiffness `K_0(P)`, finite positive semidefinite Rayleigh loss `D_0(P)`, and a valid quasistatic elimination at each speed. Then

`w_-(v,P)=a_1(P)v+a_3(P)v³+…`, `C(v,P)=v C_1(P)+O(v³)`.

In the assumed passive reduction `Γ_add=C K⁻¹ D K⁻¹ Cᵀ`, if `K(v,P)` and `D(v,P)` are smooth with finite zero-speed limits,

`Γ_add(v,P)=v² C_1 K_0⁻¹ D_0 K_0⁻¹ C_1ᵀ+O(v³)`.

Thus the route-only term gives **no nonzero Ohmic coefficient as `v→0`**; under the further velocity-local force prescription `F_add=−Γ_add(v,P)v`, its force begins at order `v³` and dissipated power at order `v⁴`. If `K,D` are even under reversal, the tensor remainder becomes `O(v⁴)` and the force remainder `O(v⁵)`. This is a falsifiable exponent for this narrowly defined bridge, **not** a general UD prediction or a derivation of the observed finite-speed friction. A velocity-dependent coupling can carry memory and additional dynamical terms; those must be derived before applying this quasistatic prescription to a real sliding interface. Static directional bias, an exchange-even route, a nonanalytic `w_-`, an added source, a singular soft mode, or a different force readout can produce different exponents.

For an isotropic one-mode illustrative case with `C(v,P)=v χ(P) C_*`, `K=k(P)>0`, `D=d(P)≥0` and `C_*` fixed, the leading `Γ_add/v²` has logarithmic load derivative (where `χ,d>0`)

`∂_P ln(Γ_add/v²)=2∂_P ln|χ|+∂_P ln d−2∂_P ln k`.

A locally flat finite-speed response requires a cancellation among **independently measured** source, stiffness and loss slopes. Q24 does not fix any of them, so this is a conditional measurement identity, not a numerical slope forecast. Contact area and the conventional graphite PES remain separate inputs. In particular, equal complementary angles or this parity identity does not single out the seven-cell quotient; the [locality](../graphite-locality-selection/README.md) and [registry convolution](../graphite-registry-convolution/README.md) obstructions still apply.

## Target-blind discriminant

For matched contact, pressure and temperature, compute or measure the *directed* route/edge coefficients under `+v` and `−v`, and the complex mode response near zero speed. Determine whether `Ξ` is reversal-odd or even, whether `w_-(0,P)` vanishes, and whether the added force scales as `v` or `v³` after independently frozen conventional subtraction. A resolved linear added force rejects the narrow signed-route, reciprocal-equilibrium, smooth-source, frozen-reduction conjunction. It does not reject other UD source laws. Include the paired-angle traces and `(3,1)`/`(3,2)` controls only after fixing the same source rule for all three.

The [exact rational witness](replay_route_parity.py) checks zero reciprocal signed-route coupling, a nonzero exchange-even branch, odd-weight/odd-route survival, and quadratic passive loss. Its [receipt](../../candidates/graphite-route-parity/mathematical_receipt.json) and [capture](../../artifacts/graphroute-20261024-01/exact-001/manifest.json) preserve the model assumptions. Independent physics review NOT_RUN; physical promotion 0.
