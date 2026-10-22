# Recovery checkpoint

The compute workspace disconnected after completed numerical calculations and exact reference-geometry checks, before planned local capture/validation/publication.

Preserved byte-for-byte: reference_primary.npz, reference_primary-fine.npz and compact_operators.npz. These were uploaded as Git blobs before the outage. SHA256 was recomputed from retained byte sequences; both primary-node digests match the previously observed exact certificate digests. The compact dataset contains the full forward Gram/cross/reference-RMS/adverse phase/final tangent/injection, plus normal/fine initial housing readout Grams.

reported_observations.json is an explicit transcription of successful tool outputs. It is not the original raw output file. Original executed code, raw JSON/CSV/logs, the local receipt and planned greenbounds-001 capture remain in the unavailable worktree and are not claimed archived here. Full backward P0 matrices were generated but not retained in this recovery capture. Source inputs are version-anchored, not independently copied in this run; input list is intentionally empty.

The standalone geometry checker and proof are recovery-authored versions. Checker NOT_RUN after reconstruction. Local new-tree validator NOT_RUN. A draft PR may pass repository integrity CI; that does not recover missing source provenance or reproduce scientific calculations.

Remain DRAFT and do not merge yet. The task/session claim stays held. First restore the original worktree, recover/capture original scripts and outputs, rerun geometry checks against these exact NPZ files, validate records and tests, and reconcile recovery records in a new immutable run. If the original runtime cannot return, reproduce from the frozen base under an explicit new source version. Do not silently label reconstructed code as the original executed bytes. After recovery, verify the candidate quintic reference's own geometry and Green operators; do not transfer cubic bounds.

Task integration-icosahedral-greenbounds-20261022; held claim 37591be88775425d9b24f8fd5e3792c62e483684; research branch discovery/integration-icosahedral-greenbounds-20261022/green-a1; base ce89a9cd15439463d9a64d983d91c22ea4368726. The scientific goal remains an actual nonlinear all-phase tube through100; this checkpoint only closes a conditional chart slot and identifies a better numerical reference candidate.
