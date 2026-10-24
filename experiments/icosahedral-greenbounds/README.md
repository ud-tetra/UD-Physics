# Forced-response and proper-alignment study — recovery draft

**EXACT/CONDITIONAL:** proper3D alignment remainder<0.00065 if centered primary error<=0.032. This leaves0.00035 for projected dynamical/reference error within the0.001 goal. Those actual-flow conditions remain OPEN.

**NUMERICAL:** full560-state forced mean-volume gains, complementary forward/backward readout checks and four smooth source checks completed. The cubic reference's coarse defect HS expression~0.005032 exceeds the approximate~0.001764 breathing margin. A post-exposure quintic diagnostic reduces measured defect norms by1,764–12,843times depending on the channel. This changes the numerical reference, not the mechanical model. No cubic gain or geometry certificate transfers to the new curve.

[Alignment proof](ALIGNMENT_THEOREM.md), [Green identities](GREEN_IDENTITY.md), [numerical protocol](NUMERICAL_PROTOCOL.md), [candidate](../../candidates/icosahedral-greenbounds/candidate.json), [mathematical receipt](../../sessions/icosahedral-greenbounds-20261022-a1/mathematical_receipt.json), [recovery checkpoint](../../sessions/icosahedral-greenbounds-20261022-a1/CHECKPOINT.md), [captured datasets and observations](../../artifacts/icosahedral-greenbounds-20261022-a1/recovery-001/manifest.json).

The runtime disconnected before complete source/raw-output capture. Three exact NPZ byte sequences survived; observations are explicitly transcribed. New-tree local validation and recovery checker are NOT_RUN. This PR must remain draft pending recovery and reproduction. Existing mainline results, original energy budget, threshold, mechanical states and momenta remain unchanged. No physical promotion.

To recheck the retained cubic reference curves in a restored runtime, install NumPy and run from repository root:

    python3 experiments/icosahedral-greenbounds/recheck_geometry.py artifacts/icosahedral-greenbounds-20261022-a1/recovery-001/files/reference_primary.npz artifacts/icosahedral-greenbounds-20261022-a1/recovery-001/files/reference_primary-fine.npz

That reconstructed checker has not been executed yet. The original checks passed before disconnection. Restore/capture original numerical source files from the worktree named in the session record, or reproduce under an explicit new version. Do not claim all scientific results reproduced merely because integrity CI passes.
