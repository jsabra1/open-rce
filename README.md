# open-rce: Recursive Context Engine

RCE gives every AI tool you use the same memory. Your context (who you are, your projects, decisions, logs) lives in **one private GitHub repo that you own**, the hub. Claude, ChatGPT and other agents load from it at the start of a chat and save to it as you work, so a new chat in any tool picks up where the last one left off.

- **You own the data.** It is plain Markdown in your own private repo. No database, no server, no account with us.
- **Any tool.** A skill for Claude.ai, Cowork and Claude Code; a plain `AGENTS.md` for everything else.
- **Small, safe saves.** Daily log files, monthly decision files and a short `context.md` per project. Nothing is overwritten or deleted.
- **Handoffs.** `/rce push` turns a chat into a packet with a 4-digit code; `/rce pull <code>` continues it in another tool.

## How it fits together

```
  Claude.ai / Cowork      Claude Code         ChatGPT / other agents
   (rce skill)          (rce plugin)          (AGENTS.md pasted in)
        \                    |                        /
         \                   |                       /
          +--------- reads rce.config.yaml ---------+
                             |
                 GitHub connector or gh / git
                             |
                  your private hub repo
       me/   projects/<name>/   memory/   inbox-unsorted/   handoffs/
```

1. The **engine** (`engine/`) holds the rules: when to save, where each item goes, the commands.
2. The **config** (`rce.config.yaml`) tells the engine whose hub to use. No secrets in it; access comes from each tool's GitHub connector.
3. The **hub** (made from `hub-template/`) holds your context. It stays private.

## What's in this repo

| Path | What it is |
|---|---|
| `engine/` | The `rce` skill, its rule files, the Claude Code plugin and `AGENTS.md` |
| `hub-template/` | An empty starter hub to copy into your own private repo |
| `rce.config.example.yaml` | The config to copy and fill in |
| `SETUP.md` | Step-by-step setup for each tool |

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

Follow [SETUP.md](SETUP.md). It takes about 15 minutes.

## License

MIT. See [LICENSE](LICENSE).
