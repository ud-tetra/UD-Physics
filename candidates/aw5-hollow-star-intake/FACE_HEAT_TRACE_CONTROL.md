# AW5 face heat-trace control

**EXACT / CONDITIONAL** for signed incidence and the unit simplex metric. Auxiliary diffusion parameter. Physical Promotion = 0.

The audited factorization is (1−exp(−2t))(1+exp(−4t)). The cavity contrast starts at zero with slope 4 and tends to 1. The replay replaces tetrahedra 0123 and 1234 with 0124, 0134 and 0234. The move preserves the local and exterior boundaries and introduces edge 04. Both filled carriers have b₂=0, so the long-time difference is zero. The flipped count rises from 16 to 18 faces. Per-face normalization gives a finite-time contrast with slope −1/12 at zero. The harmonic count uses the unnormalized trace.

See the [pinned UD addendum and replay](https://github.com/ud-tetra/UD/blob/848aef0f1729f1a39f3939b92e008ffec3a2f02e/captures/2026-11-16T004932Z-codex-aw5-heat-729e4b/AW5_FACE_HEAT_TRACE.md) proposed in [UD PR #519](https://github.com/ud-tetra/UD/pull/519). The heat trace counts harmonics in its long-time limit. A common count permits different finite-time spectra and exterior overlap. AW5 scoped diagnostics remain separate from physical diffusion or a CDT continuum claim.

## Run footer

- **Mission** — Test a topology-preserving control against the cavity heat-trace identity.
- **Done** — Replayed signed incidence, local and exterior boundary preservation, exact face spectra and nullities.
- **Finding** — Hub removal changes the long-time face trace by one. The filled bistellar move changes the finite-time trace and preserves the limiting count.
- **Bridge value** — The controls isolate harmonic count from triangulation-dependent spectral response. The bench gate remains open.

## Next step

1. **Priority 90/100** — Test a boundary-fixed refinement of the hollow star and quantify how the exterior readout residue changes at fixed b₂.
