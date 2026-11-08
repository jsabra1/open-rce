# RCE in any assistant

RCE is plain Markdown rules plus a private GitHub repo. Any assistant that can read and write files in a GitHub repo can run it in full: load, save, handoffs, sync, sort. The Claude plugin is one way in; for every other assistant the rules start at [`engine/AGENTS.md`](engine/AGENTS.md), which points to the same rule files the plugin uses.

**What an assistant needs:** a GitHub connection that can **write** to your hub (a connector, an integration, or a terminal with `gh`/`git`). Read-only connections load your context but can't save. Check any assistant with `/rce doctor` (or "rce doctor"); it reports what works.

## Setup per assistant

| Assistant | How RCE gets in | GitHub access | Checked by us |
|---|---|---|---|
| Claude Code | The plugin (`claude plugin install recursive-context-engine@open-rce`) | `gh auth login` | Yes |
| Claude.ai, Cowork | The plugin (Customize → Plugins) | GitHub connector (Settings → Connectors) | Yes |
| Claude.ai voice | The plugin; voice mode is built in | Same connector; reads go through commits | Yes |
| ChatGPT | The paste block below, in custom instructions, a Project's instructions or a custom GPT | Its GitHub connector; confirm it can write | Not yet |
| Gemini | The paste block in a Gem's instructions | A GitHub extension or integration that can write, if your plan has one | Not yet |
| Grok | The paste block in custom instructions | A GitHub connection that can write, if available | Not yet |
| GitHub Copilot (chat, agent) | The paste block in your Copilot instructions | Native GitHub access to repos you allow | Not yet |
| Cursor, Codex CLI, other coding agents | The paste block in the agent's rules or `AGENTS.md` | A terminal with `gh` or `git` | Not yet |

"Not yet" means the rules are written for it but nobody has run `/rce doctor` there. Please open an issue with the result.

## The paste block

```
RCE is on. My hub is <owner>/<hub> (private, on GitHub).
At the start of each chat, read engine/AGENTS.md from jsabra1/open-rce
(newest release, v3.0.0 or later) and follow it, using rce.config.yaml at the root of my hub.
Commands work with or without the slash: "rce push" is "/rce push".
```

Replace `<owner>/<hub>` with yours. If the assistant can't read public GitHub files, paste the content of `engine/AGENTS.md` instead and update it when RCE releases.

## Commands without slash commands

Assistants without slash commands understand the same commands typed as plain text ("rce sync", "rce pull 4821") or spoken. Nothing else changes.
