# Validation execution history

Graph build started first. An early manifest-writer invocation was mistakenly attempted while the graph process was still running and failed with missing citation_graph.json. No source or scientific result changed. The manifest writer will be rerun only after successful graph completion. This orchestration failure is preserved rather than counted as validation.

First full pipeline exited1 at static prepare: full-build source inputs changed during graph generation. Packet STATE/PR_BODY writes occurred while graph generation was running. Scientific notes and runner were unchanged. The failed log is preserved; retry freezes all candidate files and writes logs outside the worktree.
