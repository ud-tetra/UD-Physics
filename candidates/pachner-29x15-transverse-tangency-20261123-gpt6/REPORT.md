# Exact 29×15 reverse-image tangency and invariant oscillator — v0.1

**Status: EXACT / CONDITIONAL / NO-GO_SCOPED / OPEN_EVENT_SOURCE. Physical Promotion = 0.**

**Source pins:** UD-Physics main `80525f1296a15f4a87f0efecc491679deec39b9b`, `experiments/four-cell-tetrahedron/README.md` v1.0 blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e`, `experiments/pachner-state-transport/README.md` v0.1 blob `0523255744e43cb3849730eb44d5faed5a505077`. Earlier READ_ONLY specification `UD_Adaptive_Simplicial_Mesh_Dynamics_Spec_v0.1/SPECIFICATION.md`, SHA256 `f383f24911fc952754e2c4d342bceb3906f228499eeb017e8079f81c64605615`, expressly left the all-grade isometry unselected.

## Typed construction

Old (K=[0123]) has graded simplex dimensions ((4,6,4,1)), total 15. New (K'=4*\partial[0123]) has ((5,10,10,4)), total 29. Use ascending simplex bases and the real **unit-coefficient chain metric**, not Whitney masses. Let (D'=⊕_{k=1}^3 B'_k), (A_D=D'-D'^T\) acting on (⊕_k C_k(K';\mathbb R)), formal parameter (s), and zero external source.

Define a specific **candidate** stock isometry (T:\mathbb R^{15}\to\mathbb R^{29}): old vertices, edges and faces map identically to their old shared simplices; old top amplitude (a) maps to the coherently oriented signed four daughters with amplitudes ±a/2 (replacement-index signs ((-1,+1,-1,+1)) in daughter list by omitted vertex). Then (T^TT=I_{15}); (P=TT^T). **This is not the boundary-commuting integral chain subdivision**: the latter sends top amplitude (a) to the signed daughter sum, has top stock gain 4 and is a separate typed operator.

## Exact result

Let (L=(I_{29}-P)A_DT). Independent signed-incidence exact SymPy construction gives

```
rank L = 13
dim ker L = 2
charpoly(L^T L) = z^2 (z-1)^13
||L||_F^2 = 13
||[A_D,P]||_F^2 = 26
```

In old 15-space define (e_t=e_{[0123]}) and (e_f=(-e_{[012]}+e_{[013]}-e_{[023]}+e_{[123]})/2). These are orthonormal, and

[
\ker L = \operatorname{span}\{e_f,e_t\}, \quad
L^TL = I_{15}-e_f e_f^T-e_t e_t^T.
]

In the fine space the full generator exactly satisfies
[
A_D T e_t=T e_f, \qquad A_D T e_f=-T e_t.
]

Hence this exact two-dimensional plane is **dynamically invariant**, rotating with formal angular frequency 1. Every initial coarse (c) outside this plane has nonzero first-order transverse leakage, with

[
\|L c\|^2=\|c\|^2-(e_t^T c)^2-(e_f^T c)^2.
]

For an arbitrary preparation in the 15D reversible image, generic evolution leaves that image; a reverse map retaining only (T^T z) discards nonzero complement stock and information. On this special 2-plane no such loss occurs during the declared full generator evolution.

## Claim boundary

**NO-GO_SCOPED:** the complete 15D image of this **specific** T is not invariant under the unmasked daughter unit-chain Hodge–Dirac generator. **Not** a universal no-go for all possible forward jump maps, weighting choices, masked actuators, extra memory, or Whitney metrics. This calculation does not choose a birth event, build geometry autonomously, prove an indefinitely reversible cycle, or make a physical statement.

**Reproduction:** local exact `python verify.py` PASS. Standalone archive `UD_Reverse_Tangency_29x15_v0.1.zip` SHA256 `74088dc51bf846d07a97070102561eb88659f69f94e47d391f9fab342f6b0e63`, containing signed-incidence constructor, exact assertions, report, and manifest. GitHub CI, independent nonconstructor review and any native-event source test are separate.

**Physical Promotion = 0.**
