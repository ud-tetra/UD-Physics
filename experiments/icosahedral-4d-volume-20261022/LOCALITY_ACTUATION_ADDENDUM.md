# Locality-001 actuation scope addendum (no changes to immutable captured run)

**STATUS: EXACT / CONDITIONAL clarification.** This addendum supplements the captured `locality-001` data and does not modify the source code, output, manifest or SHA-256 hashes.

The positive result is an **internal** locality/reciprocity/symmetry counterexample: ordinary Euclidean 3D pairwise springs, 24 free vertices and no preset guides yield an invariant two-coordinate linear sector whose matrices `K_3,M_3` equal the specified 4D apex model's `K_4,M_4`.

The 4D apex coordinate `z` is one physical point's fourth-direction displacement. The fitted 3D coordinate `z` is a **collective** inner-shell scale, `b=b0-gamma(z-eta)`, of 12 separate free vertices. To drive precisely the isolated two-mode sector, a force conjugate to `z` corresponds to a symmetry-matched force distributed across all inner vertices. This is not equivalent to asserting a single ordinary 3D point actuator.

With reference `|X_i|=rho`, a positive force `F` applied to one inner vertex along its outward radial unit vector produces generalized `z` force `F_z=-gamma*rho*F` in the invariant projection, while it also excites nontrivial internal modes. The magnitude needed for unit projected generalized force is `1/(gamma*rho)=5.25731112119` in the chosen normalization; a uniform set of 12 radial forces instead needs per-site magnitude `1/(12gamma*rho)=0.438109260099`. The sign is chosen opposite outward direction to make `F_z>0`.

The **linear scalar shell-volume** response to calibrated local radial forcing can still agree at the level of the invariant-sector projection, because the full model's symmetric and differential modes decouple at first order. However, local point motion, other mode populations, and the necessary actuator geometry are different, so the construction does not establish a single-port hardware equivalence or a physical realization of the 4D apex.

The earlier exact nonlinear guided-linkage 3D analogue stays a distinct control: its exact two-coordinate equivalence uses explicit guided/transmission constraints, and no claim is made that it is a free local pairwise network.

**NEXT:** Define a comparable physical force-port/actuation budget and evaluate single-site local drives plus nonuniform readouts in both complete systems without refitting. Under these stricter premises, the existence or absence of a discriminator is OPEN.
