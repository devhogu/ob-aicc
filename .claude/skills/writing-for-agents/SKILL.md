---
name: writing-for-agents
description: Create or improve instructions that guide an assistant, including draft Markdown, skills, AGENTS.md, CLAUDE.md, role prompts, and agent runbooks. Use when changing when an assistant should act, how it selects instructions, or what it may do, regardless of the filename. Not for ordinary user-facing prose or routine status requests.
---

# Writing for agents

Write instructions that help an agent select the right material, take the
right bounded action, and know when the requested outcome is actually reached.
Existing product authority and provider conventions remain primary.

## Method

1. Identify who loads the document, how it is discovered, the requests that
   should trigger it, nearby requests that should not, and the observable
   result it must improve.
2. Put selection language in the discovery surface: state what the capability
   does and concrete conditions for use. Keep procedure in the body. When a
   draft has frontmatter or another discovery description, update it alongside
   the body if the trigger changes; a corrected body cannot prevent the wrong
   capability from being selected in the first place. Do not invent frontmatter
   for a document whose consumer does not use it.
3. Give each shared rule one canonical owner. Point to it conditionally from
   consumers instead of copying the method into every role or skill.
4. Keep always-needed steps, authority, safety, and completion in the entry
   file. Move branch-specific examples or detailed reference material behind a
   pointer that states when to read it. Keep definitions beside their rules.
5. End each material step with evidence that distinguishes done from merely
   attempted. State important prohibitions together with the desired behavior.
6. Test ordinary-language matches and near misses in fresh sessions. Inspect
   the transcript and actual artifact, not only the final answer or discovery
   listing.

Scale this to the edit. A short draft needs a clear trigger, useful instructions,
and a matching/near-miss check, not a new workflow or exhaustive scenario suite.

Read [the evaluation corpus](references/capability-evaluation.md) when changing
the framework's capability descriptions, cross-skill routing, or provider
projection behavior.

## Completion

Return the intended trigger and exclusions, authority boundary, canonical
owner and pointers, completion evidence, evaluation results, and unproven
provider behavior.
