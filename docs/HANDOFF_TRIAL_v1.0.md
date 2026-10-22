# Fresh-runtime writer/reviewer trial v1.0

Purpose: exercise the Discovery bootloader, task ownership, isolated workspaces, artifact capture, and review handoff with two fresh LLM contexts.

## Declared scope

Writer task: handoff-writer-20261022. Session: handoff-writer-20261022-a1. Owns experiments/clock-map-smoke, candidates/clock-map-smoke, and its session/artifact directories.

Reviewer task: handoff-reviewer-20261022. Session: handoff-reviewer-20261022-a1. Owns reviews/runtime-handoff-20261022 and its session/artifact directories. It may audit the baseline while the writer works; the final review waits for a frozen writer commit. No task dependency falsely marks writer output complete during reviewer boot.

Coordinator owns task definitions, shared state, runtime fixes if needed, and integration. Agents do not modify each other's files.

## Synthetic demonstration

Assumed map: t_label_ns = offset_ns + scale_ns_per_tick * n. Labels are synthetic numbers with declared nanosecond units, not measured time. Fit n = 0,1,2 to labels 1,3,5 using exact rational arithmetic. Inspect evaluation points n = 3,4 with disclosed labels 7,9. All points are exposed in this plan; this is development evaluation, not a blinded physical prediction.

Writer supplies code, fixture, exact fitted values, residuals, a constant baseline, candidate assumptions and mapping, source revision, captured run, checks actually executed, boot report, and next action. No native UD clock law is inferred.

Reviewer independently executes the writer artifact using its own session and compares outputs; checks source/units/FIT labeling, integrity, reproduction, session isolation and task ownership; tests competing ownership without taking over another task; reports findings separately. Same-model fresh-context review is not experimental replication.

## Acceptance

1. Both sessions read the declared repository load order and report actual capabilities and exact revisions.
2. Distinct claims/branches/workspaces exist with disjoint owned paths.
3. Writer artifacts reproduce in the reviewer workspace; units, target exposure and assumptions are explicit.
4. A competing writer-task claim is rejected without changing its live owner.
5. Review findings and fixes are recorded; checks pass before integration.
6. PRs integrate without overwriting unrelated work, and claims are released with exact-SHA checks.

Report PASS only for criteria actually executed. Missing capabilities remain NOT_RUN or OPEN. No physical bridge promotion results from this trial.
