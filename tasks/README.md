# Tasks

Use python3 scripts/discovery.py new-task --id TASK --goal "Question" --path OWNED_PATH to create a scoped task. Commit task definitions before other runtimes rely on them. Dependencies must be complete before a dependent task is claimed.

Active ownership is determined by remote claims/* refs, not a local status file. New task files may be proposed before claims; this does not authorize edits to another task's owned paths. Use unique task IDs and inspect existing claims before selecting an ID.

The initial framework publication is a user-authorized empty-repository bootstrap. It precedes the claim system and is documented in sessions/bootstrap-20261022/ rather than falsely claiming a preexisting lock.
