## Workers (Codex)

Each document is edited by its own fresh Codex worker on the latest Sol model at high reasoning. Do not edit the documents yourself, and do not use Claude.

1. `humanize worker --provider codex` prints the model to use (the newest Sol in the Codex model list). If it reports an error, stop and tell the user.
2. For each document that `start` lists as "needs a worker", one at a time (the tool already finished the others: untouchable documents, protected documents with nothing to edit, and duplicates), run:
   ```
   humanize dispatch --run <run-id> --doc <doc>
   ```
   It writes the worker's instruction, runs the Codex worker (`codex exec` on that model at high reasoning), and returns when the worker exits, usually after a few minutes. If your shell returns before it exits, keep waiting on that same session; never start it again. The tool enforces the order: a second dispatch for the same document refuses (exit 3), a dispatch for the next document waits until the current worker has exited, and the closing `humanize gate --run` waits for any running worker.
