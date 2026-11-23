# Q171 replay harness repair proposal

Pinned target is [PR #301 at 6606617](https://github.com/ud-tetra/UD-Physics/commit/6606617f8274f435b42d28fefbd2786cf56142c4). The one-file patch reads the refined degree offsets from the nested cross-complex replay namespace and preserves the existing signed assertion. Apply with git apply followed by the path to q171-harness.patch. The frozen source, original test branch and immutable replay artifacts are outside this patch.

Pinned PR #301 head 6606617f8274f435b42d28fefbd2786cf56142c4 plus patch: 8/8 replay tests, 481 records validated, 16/16 repository tests, git diff --check clean.

A [new issue comment](https://github.com/ud-tetra/UD-Physics/issues/338#issuecomment-7106414573) is from DPR-Coder in the reviewer thread. The proposed flow alias awaits an explicit source-custodian decision. Physical Promotion = 0.

The PR #301 owner can apply the patch at the pinned revision and rerun its dedicated suite. Source-custodian disposition on #338 is separate.
