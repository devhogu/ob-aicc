---
name: graphify-code
description: Query an existing code-only Graphify graph first, or build and update one only when explicitly requested and after proving the corpus contains code only. Use for code relationships, architecture paths, symbol explanations, or deterministic AST graph work where documents, images, audio, video, and semantic model extraction are out of scope.
---

# Graphify code

Use Graphify as a structural code-navigation capability. This skill never
performs document or media extraction and never invokes an inference provider.

## Query first

1. Check for `graphify-out/graph.json` at the selected project root.
2. If it exists and its recorded corpus is code-only, answer codebase questions
   with `graphify query`, `graphify path`, or `graphify explain` before reading
   broadly or rebuilding.
3. Cite the graph's source locations and distinguish extracted structure from
   inference. Never invent an edge.
4. If the graph's corpus provenance is absent, stale, or includes non-code
   material, report that boundary. Do not represent it as code-only evidence.
5. If no valid graph exists and the user did not authorize construction,
   navigate the smallest relevant source set directly. A query-first policy
   must not make ordinary code investigation depend on creating a graph.

## Build or update only when authorized

A question about code does not authorize a graph build. Build or update only
when the user explicitly asks for it.

Before a build or update:

- resolve the exact project root and stay inside it;
- use Graphify detection to confirm the admitted corpus has one or more code
  files and zero documents, papers, images, video, or audio;
- honor `.gitignore` and `.graphifyignore`;
- stop if non-code inputs remain instead of sending them to semantic extraction;
- do not install tools, request credentials, read provider keys, start watch
  mode, install hooks, or enable automatic rebuilds.

For a confirmed code-only corpus, use the current Graphify structural AST path.
No semantic-extraction agent, Gemini backend, or other model is part of this
capability. Preserve an existing graph unless the requested operation and the
tool's shrink safeguards permit replacement.

## Report

Report the exact root, operation, admitted code-file count, ignored paths,
whether the result was query-only or structurally rebuilt, graph health, and
output paths. State explicitly that the result proves code structure only; it
does not establish documentation intent, runtime behavior, deployment, or live
service reachability.
