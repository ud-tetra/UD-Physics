# v0.5.1 manifest byte-count erratum

The initially committed v0.5 `manifest.json` recorded Unicode character lengths (12271/2861), not UTF-8 byte counts. The research bytes and SHA-256 hashes were correct and unchanged. Local `wc -c` gives `REPORT.md=12298` and `replay_portable.py=2918`, and remote Git blob SHA-1 values match the local files. The manifest was corrected in a dedicated commit without altering any science artifact. The original manifest remains available in Git history. Physical promotion 0.
