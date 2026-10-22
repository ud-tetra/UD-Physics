# Concurrent runtime protocol v1.0

## Ownership and isolation

Each runtime has a unique session ID, research branch, and local worktree/checkout. A GitHub account can host multiple runtimes; account identity is not session ownership. Use discovery/<task>/<session> for work branches. Never edit a shared checkout simultaneously.

Task files describe scope and dependencies. Live claim refs coordinate ownership. A claim is not a security lock; all writers must follow this protocol. GitHub branch rules, if enabled separately, enforce integration policy.

One claim owns one task. Different task owners may work concurrently only when owned paths do not overlap. Existing candidate directories have one task owner. Split overlapping work into proposals under each session's directory and let an integrator reconcile them.

Atomic acquisition covers one task ID, not arbitrary overlapping paths across different task IDs. Define shared work under the same task key; scope review before parallel execution is required. The CLI does not pretend to provide multi-path transactional locks.

## Atomic task claims

The claim ref is refs/heads/claims/<task-id>. Its commit contains claim.json with task, session, creation time, base revision, and owned paths.

Git runtime:
```bash
python3 scripts/discovery.py new-task --id TASK --goal "Question" --path candidates/CANDIDATE
python3 scripts/discovery.py claim --session SESSION --task TASK
```

The claim command creates a claim commit and pushes with an explicit empty expected ref:
`git push --force-with-lease=refs/heads/claims/TASK: origin COMMIT:refs/heads/claims/TASK`.
The empty expectation requires absence. A competing claim fails instead of overwriting an existing ref. This is a narrowly scoped compare-and-swap operation on a coordination ref, not permission to rewrite research branches.

Connector runtime:
1. Read the task and current integrated base commit.
2. Create a Git tree containing claim.json, then a commit with that base commit as parent.
3. Create the new branch claims/<task-id> at that commit with the create-branch operation. A preexisting ref means failure; never update or force an existing claim ref to acquire it.
4. Save the returned claim SHA in your session record. Recheck the live ref if a request times out; do not assume success.
5. Create a separate discovery work branch from the verified integrated base, not from the claim commit.

Claims have no automatic expiry. A timestamp is diagnostic, not permission to take over. Ask the task owner/custodian to resolve an abandoned claim; record any reassignment and use the exact prior claim SHA as a lease. The CLI intentionally does not implement automatic takeover.

## Release

`python3 scripts/discovery.py release --session SESSION --task TASK` deletes only the claim recorded in that session, after verifying the remote SHA. A changed claim rejects release. Record completion/integration before release. Connector runtimes lacking conditional ref deletion leave release pending for a Git-capable integrator; do not pretend a local status frees a live ref.

## Integration

Use one focused PR per task. Integrators claim integration-<scope> and serialize changes to shared state, instructions, schemas, tooling, and candidate summaries. Rebase or merge current main into the work branch, rerun checks, and resolve conflicts explicitly. Never overwrite a newer default-branch head from a stale API snapshot.

Prefer separate session directories and new immutable run directories to shared logs. Do not hand-edit a global generated index. CURRENT.md is a milestone summary, not a realtime lock table.

Review labels: constructor self-check, separate-context LLM review, non-constructor review, and independent empirical replication are distinct. Two sessions using the same model do not establish independent experimental evidence.

## Access modes and fallback

Read-only agents can inspect, calculate privately, and propose patches, but cannot claim write ownership. Connector agents can coordinate with refs and publish text; Git/compute agents can also run capture and checks. If a server rule blocks claim refs, record the blocker and use isolated proposals until an administrator enables an appropriate namespace. Never weaken a protection rule to make a claim succeed.
