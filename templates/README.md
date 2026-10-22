# Manual record templates

Copy a template into its final record directory, replace every placeholder, and validate. Session and candidate IDs must match their paths. Run manifests require real SHA-256 digests and captured files. Incomplete run drafts stay under the session until finalized. Never report a computational check as passed merely because a template exists.

For consequential UD calculations, fill mathematical_receipt.json and follow docs/UD_MATHEMATICAL_METHOD_v1.0.md. The additional mathematical_profile/session and mathematical_receipts/candidate fields are optional metadata supported by the templates, not retroactive requirements on historical records or automatically populated/verified fields in the current CLI.
