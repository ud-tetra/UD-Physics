# UD Discovery runtime bootloader v1.0

## Copy-paste launch instruction

> Prepare this runtime for UD Discovery in ud-tetra/UD-Physics. Read this bootloader, AGENTS.md, instructions/UD_DISCOVERY_v1.1.md, state/CURRENT.md, docs/CONCURRENCY.md, and docs/ARTIFACTS.md at a verified repository revision. Check the assigned task and live claim refs. Identify read/write/compute capabilities; do not assume shared memory or model identity. Create a unique session, claim the task, and work on an isolated branch/worktree. Report a short BOOT REPORT before substantive work. Then execute the authorized task, record assumptions and target exposure, capture reproducible artifacts, and leave a checkpoint. Hypothetical discovery is permitted; mainline export is separate.

## Load order

1. Verify repository identity, default-branch head, and your branch/working-tree state. Fetch or read current files; never discard uncommitted work to boot.
2. Read AGENTS.md and the canonical Discovery instructions.
3. Read state/CURRENT.md and the assigned task, including dependencies. Inspect relevant open PRs and live refs/heads/claims/*; a stale local task file does not prove availability.
4. Read docs/CONCURRENCY.md, docs/ARTIFACTS.md, and relevant candidate/source records.
5. State the runtime's actual access mode: read-only; connector write; or Git/compute. Record the model only if known, otherwise unknown.
6. Allocate a session ID. Acquire the task claim before substantive edits. Claim acquisition can be performed in a disposable coordination workspace before creating the research branch. If occupied, choose an independent task or remain read-only.
7. Record the exact integrated base revision. Create discovery/<task>/<session> from that revision, in an isolated checkout/worktree. On resume use your existing branch and inspect its changes.
8. Create the running session record and begin the authorized task. Do not upload an entire private conversation.

## BOOT REPORT

- Repository and exact base revision:
- Runtime/model as reported; capabilities:
- Session ID and task:
- Claim ref and claim commit, or READ_ONLY / UNCLAIMED:
- Working branch and owned paths:
- Source/candidate dependencies:
- Evidence mode and known target exposure:
- Next authorized action; blockers:

Never report READY_TO_WRITE if claim acquisition, isolation, or access failed. Analysis may continue as READ_ONLY or UNCLAIMED with no publication.

## Minimal Git runtime sequence

```bash
git fetch origin main
git worktree add -b discovery/TASK/SESSION ../ud-physics-SESSION origin/main
```

Replace TASK and SESSION with your allocated identifiers; do not run literal placeholders. In that worktree:

```bash
python3 scripts/discovery.py bootstrap --session SESSION --runtime "known runtime or unknown" --task TASK --goal "specific authorized question"
python3 scripts/discovery.py claim --session SESSION --task TASK
```

If the claim is occupied, do not edit the research task. Keep only your private boot attempt or move to another task. The bootstrap files document a boot attempt; they do not establish ownership.

## Connector-only runtimes

Read and write repository files through the GitHub connector. Create one branch per session. The atomic claim protocol is described in docs/CONCURRENCY.md. Use templates/session.json and templates/claim.json when Python cannot run. Use expected-head checks for branch updates; reread after a rejected lease. Record computational checks as NOT_RUN until executed by a capable runtime.

## Resume and finish

On resume, reread current integrated state, your checkpoint, and the live claim. Inspect source changes before reusing earlier conclusions. At finish, save the finding, failed alternatives, artifacts, tests, and next step; open a PR. Release the claim after integration or explicit abandonment. A chat response without committed records is not a durable handoff.
