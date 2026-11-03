# open-rce: Recursive Context Engine

RCE gives every AI tool you use the same memory. Your context (who you are, your projects, decisions, logs) lives in **one private GitHub repo that you own**, the hub. Claude, ChatGPT and other agents load from it at the start of a chat and save to it as you work, so a new chat in any tool picks up where the last one left off.

- **You own the data.** It is plain Markdown in your own private repo. No database, no server, no account with us.
- **Any tool.** A skill for Claude.ai, Cowork and Claude Code; a plain `AGENTS.md` for everything else.
- **Small, safe saves.** Daily log files, monthly decision files and a short `context.md` per project. Nothing is overwritten or deleted.
- **Handoffs.** `/rce push` turns a chat into a packet with a 4-digit code; `/rce pull <code>` continues it in another tool.

> **You need a GitHub connector that can write.** RCE saves by writing files to your hub, so every tool needs a GitHub connection with **write** access to it (and permission to create a repo, if the AI sets up the hub for you).
>
> - **Tested and working:** a GitHub MCP connector with write access in Claude.ai, and the GitHub CLI (`gh`) in Claude Code.
> - **Not confirmed:** whether Claude.ai's built-in GitHub integration, or ChatGPT's GitHub connector, can write. Some GitHub connectors only read.
> - **If your connector only reads:** RCE still loads your context, but saves don't land. They come back as `⚠ RCE push failed` bullets to paste later, and you create the hub repo by hand on github.com.

## How it fits together

```
  Claude.ai / Cowork      Claude Code         ChatGPT / other agents
   (rce skill)          (rce plugin)          (AGENTS.md pasted in)
        \                    |                        /
         \                   |                       /
          +------ pointer: owner + hub name --------+
                             |
                 GitHub connector or gh / git
                             |
                  your private hub repo
       me/   projects/<name>/   memory/   inbox-unsorted/   handoffs/
```

1. The **engine** (`engine/`) holds the rules: when to save, where each item goes, the commands.
2. The **config** (`rce.config.yaml` at the root of your hub) holds your settings. Each tool keeps a two-line pointer (`owner`, `hub`) to find it. No secrets anywhere; access comes from each tool's GitHub connector.
3. The **hub** (made from `hub-template/`) holds your context. It stays private.

## What's in this repo

| Path | What it is |
|---|---|
| `engine/` | The `rce` skill, its rule files, the Claude Code plugin and `AGENTS.md` |
| `hub-template/` | An empty starter hub to copy into your own private repo |
| `rce.config.example.yaml` | The settings file the setup copies into your hub |
| `SETUP.md` | Setup in one prompt, plus a manual path |
| `BOOTSTRAP.md` | The setup steps the AI follows |

## Commands

| Command | What it does |
|---|---|
| `/rce` | Status: on or off, where this chat saves, last save |
| `/rce load` / `/rce load deep` | Load your context / the whole hub |
| `/rce sync` | Save this whole chat into the hub |
| `/rce push` / `/rce pull <code>` | Hand a chat to another chat or tool |
| `/rce live` | Link two chats until closed |
| `/rce sort` | Route leftover inbox items |
| `/rce off` / `/rce on` | Pause or resume saving in this chat |
| `/rce open <alias>` | Load a restricted repo from your config |

## Get started

Connect GitHub in your AI tool (with write access), then paste this into a new chat:

```
Set up RCE for me by following https://github.com/jsabra1/open-rce/blob/main/BOOTSTRAP.md
```

The AI creates your private hub and installs RCE; you answer three questions. Details and a manual path: [SETUP.md](SETUP.md).

## License

MIT. See [LICENSE](LICENSE).
