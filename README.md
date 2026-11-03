# open-rce: Recursive Context Engine

RCE is memory management and shared context across AI agents: every AI tool you use gets the same memory. Your context (who you are, your projects, decisions, logs, the things you ask Claude to remember, and files such as PDFs and images) lives in **one private GitHub repo that you own**, the hub. Claude, ChatGPT and other agents load from it at the start of a chat and save to it as you work, so a new chat in any tool picks up where the last one left off.

- **You own the data.** It is plain Markdown in your own private repo. No database, no server, no account with us.
- **Any tool.** One plugin, **Recursive Context Engine**, for Claude.ai, Cowork and Claude Code; a plain `AGENTS.md` for everything else.
- **Claude's memories, in your repo.** When you ask Claude to remember something, it's saved to the hub, so every tool shares it.
- **Files too.** PDFs, images and other binaries are kept as the original file, with a short card beside each one. Tools that can only write text leave a `binary pending` card, and `/rcx files` finishes the upload from Claude Code.
- **Small, safe saves.** Daily log files, monthly decision files and a short `context.md` per project. Nothing is overwritten or deleted.
- **Handoffs.** `/rcx push` turns a chat into a packet with a 4-digit code; `/rcx pull <code>` continues it in another tool.

> **You need a GitHub connector that can write.** RCE saves by writing files to your hub, so every tool needs a GitHub connection with **write** access to it. It doesn't need to create repos: if it can't, the AI asks you to create one empty private repo by hand, which takes a minute.
>
> - **Claude Code with the GitHub CLI (`gh`):** does everything, including creating the hub and saving binary files.
> - **Claude.ai with a GitHub connector:** reads and writes text files, but can't create repos (it returns `403`), so you create the hub repo by hand when the AI asks.
> - **Not confirmed:** ChatGPT's GitHub connector. Some GitHub connectors only read.
> - **If your connector only reads:** RCE still loads your context, but saves don't land. They come back as `⚠ RCE push failed` bullets to paste later, and you create the hub repo by hand on github.com.

## How it fits together

```
  Claude.ai / Cowork      Claude Code         ChatGPT / other agents
     (plugin)             (plugin)            (AGENTS.md pasted in)
        \                    |                        /
         \                   |                       /
          +---- finds the hub: rce.config.yaml -----+
                             |
                 GitHub connector or gh / git
                             |
                  your private hub repo
       me/   projects/<name>/   memory/   inbox-unsorted/   handoffs/
```

1. The **engine** (`engine/`) holds the rules: when to save, where each item goes, the commands.
2. The **config** (`rce.config.yaml` at the root of your hub) holds your settings. Each tool finds the hub by looking for that file in your repos, or from an optional two-line pointer (`owner`, `hub`). No secrets anywhere; access comes from each tool's GitHub connector.
3. The **hub** (made from `engine/skills/rcx/assets/hub-template/`) holds your context. It stays private.

## What's in this repo

| Path | What it is |
|---|---|
| `engine/` | The **Recursive Context Engine** plugin: the `rcx` skill, its rule files, the session hook and `AGENTS.md` |
| `engine/skills/rcx/assets/` | The starter hub and the settings file that `/rcx setup` copies into your hub |
| `SETUP.md` | Install, then `/rcx setup`, plus a manual path |
| `BOOTSTRAP.md` | Setup for tools without the plugin, such as ChatGPT |

## Commands

| Command | What it does |
|---|---|
| `/rcx` | Status: on or off, where this chat saves, last save |
| `/rcx setup` | Create your private hub and connect this tool |
| `/rcx load` / `/rcx load deep` | Load your context / the whole hub |
| `/rcx sync` | Save this whole chat into the hub |
| `/rcx push` / `/rcx pull <code>` | Hand a chat to another chat or tool |
| `/rcx live` | Link two chats until closed |
| `/rcx files` | Finish saving files marked `binary pending` |
| `/rcx sort` | Route leftover inbox items |
| `/rcx off` / `/rcx on` | Pause or resume saving in this chat |

## Get started

1. Connect GitHub in your AI tool, with write access.
2. Install the plugin:
   - **Claude.ai and Cowork:** Customize → Plugins, then add the marketplace `jsabra1/open-rce` and install **Recursive Context Engine**.
   - **Claude Code:** `claude plugin marketplace add jsabra1/open-rce`, then `claude plugin install recursive-context-engine@open-rce`.
3. Type `/rcx setup` in a new chat. Claude creates your private hub; you answer three questions.

**ChatGPT and other tools:** paste this into a new chat instead:

```
Set up RCE for me by following https://github.com/jsabra1/open-rce/blob/main/BOOTSTRAP.md
```

Details and a manual path: [SETUP.md](SETUP.md).

## License

MIT. See [LICENSE](LICENSE).
