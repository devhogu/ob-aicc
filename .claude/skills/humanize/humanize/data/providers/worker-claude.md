## Workers (Claude Code)

Each document is edited by its own fresh `humanize-editor` sub-agent: latest Opus at high reasoning, defined in `.claude/agents/humanize-editor.md`. Do not edit the documents yourself, and do not use another provider's agents.

For each document that `start` lists as "needs a worker", one at a time (the tool already finished the others: untouchable documents, protected documents with nothing to edit, and duplicates):

1. `humanize task --run <run-id> --doc <doc> --provider claude` prints its instruction.
2. Launch the Agent tool with `subagent_type: humanize-editor` and that instruction as the prompt, in the foreground. Wait for it to finish before starting the next document.

If the `humanize-editor` agent type is not available, stop and tell the user to reinstall humanize; do not fall back to a different model.
