---
title: "MCP connections: Claude Code and your tools"
summary: What MCP is, what you can do with it, how to connect a server without secrets in the repository, where the setting is stored, and why you should connect only what is approved.
category: Claude Code
level: advanced
minutes: 6
order: 57
tags: claude code, mcp, connections, integrations, jira, database
source: Подключите Claude Code к инструментам через MCP (документация на русском)
source_en: Connect Claude Code to tools via MCP
source_url: https://code.claude.com/docs/ru/mcp
source_hash: 0f9e75b7f06c
---

After this guide you will be able to connect an approved outside system (a tracker, a database, documentation) to Claude Code with minimal rights, understand where the setting is stored and who will see it, and keep access keys out of the repository.

MCP (Model Context Protocol) is an open standard for connecting Claude to outside systems: a task tracker, a database, monitoring, design tools, email. Instead of copying data into the conversation, Claude goes to the system itself through a connected MCP server.

## What it gives you {#what}

- Implement a task straight from the tracker (Jira or GitHub, for example).
- Look at errors and metrics in the monitoring system.
- Query a database, preferably a test one, with no customer data, and read-only.
- Build a layout from a mockup in the design system.

All of this only if the connection is approved in your organization.

## How to connect {#add}

```bash
# a remote server over HTTP is the recommended way
claude mcp add --transport http name https://server-address/mcp

# a local server that runs on your machine
claude mcp add --transport stdio name -- server-start-command

claude mcp list          # what is connected
claude mcp remove name   # disconnect
```

In a session, the `/mcp` command shows the state of the connections and helps you sign in.

## Where the setting is stored {#scope}

| Scope | For whom | Where |
| --- | --- | --- |
| local (default) | only you, in this project | your personal settings |
| project | the whole project team | the `.mcp.json` file in the repository |
| user | you, in all projects | your personal settings |

The `--scope` flag sets the scope, for example `--scope project`.

`.mcp.json` is kept in git, so it must contain no access keys. Take them from environment variables: an entry `${NAME}` is replaced with the variable's value:

```json
{
  "mcpServers": {
    "tracker": {
      "type": "http",
      "url": "https://server-address/mcp",
      "headers": { "Authorization": "Bearer ${TRACKER_TOKEN}" }
    }
  }
}
```

In a normal session, servers from `.mcp.json` need your confirmation before first use. When you run `claude -p` without the `--bare` flag, they connect **without asking**; keep this in mind when you run Claude from scripts in someone else's repository.

## Be careful {#safety}

- Connect only servers that you need and that your organization has approved: a server gets access to your environment.
- A server that reads outside content can bring in a [[prompt-injection|prompt injection]].
- Give minimal rights: read-only for a database, a single project for a tracker.
- Turn off connections you don't use: it is safer, and the context stays cleaner.

If a tool is available as a command line (`gh`, `aws`, `gcloud`), it is often simpler to give Claude that: it uses less context than MCP.

**Try this:** in your repository, run `claude mcp list` to see what is already connected, including from `.mcp.json`. In a session, open `/mcp` and turn off whatever the current task doesn't need.
