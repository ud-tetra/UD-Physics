# Phase-009 — Constitutive coefficient selection: positive-energy degeneracy

**RESULT — EXACT / CONDITIONAL nonidentifiability; FIT reference origin; FAILED unique physical attribution.** The original signed-S4/J tetrahedral symmetry, conservative Hamiltonian dynamics, positive quartic energy, unmodified zero-amplitude linearization, and the old phase-target gain triple do not independently select the nonlinear constitutive coefficients. This is a scoped constructive counterexample, not a theorem excluding every future UD source law. **Disposition:** park UNIQUE PHYSICAL ATTRIBUTION of this 15-register phase-family while preserving its exact mathematical records.

## Source and mathematical domain

Verified live branch parent: 1f6717a8a6fdbe004aae6fda8ae278e3d4498d4a. Integrated read-only source: experiments/qpb1-local-generators/README.md at 41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb, sections 1–4. Earlier exact J-compatible constitutive model: experiments/qpb1-finite-window-phase/PHASE_COMPATIBLE_CONSTITUTIVE.md at 1f6717a8a6fdbe004aae6fda8ae278e3d4498d4a. Additional read-only source selection audits were consulted at main revision 5fd737fda4dadd6f1cc3d9c3c6c086473b7f72bb: experiments/qpb1-source-reservoir/README.md, experiments/qpb1-unit-preparation/README.md, experiments/qpb1-charge-field/README.md and experiments/qpb1-impedance-selection/README.md. None of these specific sources provides a source-selected nonlinear energy coefficient or physical reference unit. The source audit is bounded, not exhaustive across every UD historical record.

Native carrier C is the real 15-register oriented tetrahedral chain with unit positive metric, signed S4 representation, K_k=D_k-D_k^T, orthogonal P_k=-K_k²/4, J=A/2 and A=sum K_k. Coefficient domain Q for the finite exact constructors and R for the parameter family; complex phase interpretation is a separate conditional map. Define *raw* sector support s_k=x^T P_k x >=0. For unit-norm preparations ||x||=1 only, s_k equals the normalized fraction r_k, with sum r_k=1. Physical time, physical energy, register ports and state-preparation amplitude are OPEN.

## Positive quartic family and exact effective generators

For any real symmetric 3-by-3 matrix L, postulate
\[
 H_L(x)=\frac12\|x\|^2+\frac14s(x)^T L\,s(x),\qquad
 s_k(x)=x^T P_kx .
\]
Since the sector projectors are orthogonal and commute with A, the constant-Poisson Hamiltonian flow is
\[
 \dot x=A\nabla H_L(x)
 =\sum_{i=1}^3\left[1+\sum_{j=1}^3 L_{ij}s_j\right]K_i x.
\]
All s_i and ||x||² remain constant on any trajectory. The full signed S4 and continuous J symmetry are retained. Every L gives exactly the original A as the Jacobian at x=0; L positive semidefinite guarantees nonnegative quartic energy and coercive H_L. These conditions do not require the three effective angular frequencies to be positive for arbitrary unbounded amplitudes: **positive energy and positive modal orientation are different questions**.

The real vector space Sym(3) has six parameters. At any fixed nonzero sector vector r with all three coordinates nonzero, the linear map L -> Lr from Sym(3) to R³ has rank three, shown by varying the diagonal entries independently. Consequently three directions remain unidentifiable even from the *complete three-rate* measurement at a single preparation, before imposing positivity. The following positive-semidefinite family proves that degeneracy survives positivity.

## An explicit exact positive-semidefinite nonidentifiability ray

Let r0=(1/4,1/4,1/2), the earlier EXPOSED reference support, and v=(1,-1,0) with v·r0=0. Set
\[
 L(t)=\operatorname{diag}(0,0,1)+t\,vv^T,\qquad t\ge0.
\]
Then for every real vector s,
\[
s^T L(t)s=s_3^2+t(s_1-s_2)^2\ge0,
\quad L(t)r_0=(0,0,1/2),
\quad g(r_0)=(1,1,3/2).
\]
Thus an entire nonnegative ray of distinct positive-energy nonlinear Hamiltonians yields exactly the same old reference gain triple, the same source linearization, S4, J, and conserved sector stocks. This is exact for *all real t>=0*, not an inference from finite fixtures.

The normalized first preparation can be written x0=(e_01+e_0123)/sqrt(2), yielding the above r0. A second, independently named toy preparation x1=(e_0-e_1+e_0123)/sqrt(3) gives r1=(2/3,0,1/3). The modeled gains are
\[
g(r_1)=(1+2t/3,\ 1-2t/3,\ 4/3).
\]
For t=0 the result is (1,1,4/3); for t=1/2 it is (4/3,2/3,4/3). Both laws are positive semidefinite in quartic energy; the latter also retains positive rates on all normalized sector-fraction preparations (t<1 is sufficient for positive modal rates for all such preparations). The exact code includes t=1,2 as additional PSD *stress* examples that do not necessarily retain positive rates for every normalized preparation.

These alternate-preparation differences are **conditional model-selection consequences**, not independent physical predictions: the entire experiment family and the second preparation were explored after exposure to the nominal target. Without freezing L using an independently sourced law, a successful comparison merely fits a selected nonlinear model.

## Stronger locality and classical controls

If impose the stronger premise that the quartic energy couples only the existing top-cell/four-face hidden star, restrict to L=t E33. Its coefficient t is still free for every t>=0. Selecting t=1 using the exposed hidden gain 3/2 at r3=1/2 is FIT, not a native selection theorem. Allowing the full PSD family permits coupling additional sectors and hence retains even more parameter freedom. Locality definitions (incidence-supported differential operator, star-supported constitutive energy, strictly pairwise endpoint law) are not interchangeable; the source records do not identify a physical interaction range.

A conventional classical nonlinear Hamiltonian with *the same Poisson tensor A and Hamiltonian H_L* reproduces all modeled trajectories and observables. The null is exactly matched, with the same six-parameter freedom; there is no incremental UD prediction in the present mathematical law. This does not rule out future physically constrained material/null families, which need source-derived, independently measured restrictions.

## Reproducibility, limits, and disposition

Run from repository root:
\`python3 experiments/qpb1-finite-window-phase/phase009_compact.py --out /tmp/ud-qpb-phase009.json\`.

This compact exact Q calculation pins its sector definitions to the phase-008 audited original 15-register projectors. It certifies the rank-three reference map, positive-semidefinite null ray, five rational t fixtures, 320 signed/nonnegative quadratic-form checks, and two exact preparation gain responses. The larger independent-in-the-same-context 15x15 constructor prototype also checked 24 signed permutations, J commutation, energy conservation, and projector/evolution identities; it is a same-constructor crosscheck, not external scientific review. The [phase-009 immutable capture](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-009/manifest.json) holds executed code and exact output with SHA-256 and versioned source commit.

No physical dataset, uncertainty model, measured clock, port calibration, nonlinear coupling value, non-constructor review, or independent empirical replication exists. **No new mainline physical status.** Only the unique physical-attribution aspect of the phase-compatible quartic candidate is PARKED; the exact finite-dimensional mathematics remains valid under its hypotheses. Reopening condition: a versioned independently motivated constitutive law/parameter and a held-out signed response tested against a realistic parameter-budgeted classical Hamiltonian with physical port/time mapping.

**Next highest-value move, priority 98/100:** seek such a source/measurement outside this fixed 15D constitutive family; do not continue calibrating more t values against the previously exposed reference.
