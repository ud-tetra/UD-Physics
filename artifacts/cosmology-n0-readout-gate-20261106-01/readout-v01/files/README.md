# N0 finite native-pattern and image-topology gate v0.1

Session `cosmology-n0-readout-gate-20261106-01`; base `9db0edba13db7af9999fcfd1b9d45d3c8d65cdb5`. **EXACT conditional finite controls / SOURCE_BLOCKED physical readout.** Physical promotion 0. No astronomical maps or catalog rows ingested.

## Typed input and proposed readout

Native carrier `C_*(Δ³;Q)=Q^15` with four vertex, six edge, four face and one cell register; source Q165 uses quadratic support and Q169 the signed incidence generator `A=D−Dᵀ` on a fixed complex. These do not supply a spatial pixel embedding. For the illustrative state `q=(1,1,0,0;0^11)`, take the four vertex amplitudes only. An **assumed** layout `P:Q^4→Q^(2×2)` maps vertices to pixels. The image filtration is `I_u(x)=1[Pq(x)≥u]`, with foreground 4-neighbor and background 8-neighbor adjacency, zero exterior, and readout `(β0,β1)` equal to connected foreground components and bounded background holes. This is a precise image observable, **not** an accepted UD observable or a dynamical pattern prediction. Amplitude is not Hα intensity.

## Exact controls

| State/readout choice | Threshold | `(β0,β1)` | Status |
| --- | --- | --- | --- |
| Same native `q`, adjacent active vertices in 2×2 layout | `1/2` | `(1,0)` | EXACT conditional |
| Same `q`, diagonal active vertices in alternate layout | `1/2` | `(2,0)` | EXACT conditional |
| 3×3 ring binary image | `1/2` | `(1,1)` | EXACT image topology |
| 3×3 ring averaged to one pixel, value `8/9` | `1/2` | `(1,0)` | EXACT coarse-graining hole loss |
| Same averaged pixel | `9/10` | `(0,0)` | EXACT threshold dependence |

The source generator and state are identical in the first two rows; only `P` changes. Thus native carrier topology and Q165/Q169 alone do not select image connectivity. Averaging can erase a hole, while a changed threshold can erase the component. The ring is an **image control**, not claimed as a native K4 state. These examples disprove unconditional readout invariance; they do not prove that every future native pattern map fails.

**Dynamical scope:** `q` is an initial state on one fixed carrier; no evolution of an assembled nebula, source/sink, coupling to gas/radiation, boundary preparation, or growth preference is asserted. Source Q169 linear skew flow preserves quadratic support, which by itself neither fixes `P` nor preserves `(β0,β1)` after thresholding. A test of persistence would require a source-selected time evolution on an assembled carrier and a frozen readout at each parameter value.

## N0 stop decision

**SOURCE_BLOCKED:** no accepted source currently selects the embedding `P`, the physical emission readout, PSF/coarse-graining operator, or threshold/segmentation rule. The exact controls show that this freedom changes the proposed observable. N0 therefore stops before downloading or scoring PHANGS maps. A shape coincidence cannot be called UD growth, nebular morphology, or a physical bridge.

**Reopening:** supply a versioned assembled-carrier spatial pattern with initial/boundary data and generator; a native scalar readout equivariant under carrier relabeling; a declared map to projected emission and instrument PSF with units/uncertainty; fixed filtration and morphology nulls. First verify stability across source-permitted layouts and observational resolutions, then freeze a target-blind comparison. The PHANGS-MUSE DR1.1 catalog and Hα maps described in [Cosmological Branch v0.2](../../docs/COSMOLOGY_BRANCH_v0.2.md) remain observational context only.

Run `python3 experiments/cosmology-nebular-entry/n0_readout_exact.py`. Exact integer/fraction assertions cover the two layout choices, hole loss and threshold dependence. The result is independent of a physical Hα calibration.
