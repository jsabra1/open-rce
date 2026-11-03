# Recursive Context Engine

**Memory management and shared context across AI agents.** Recursive Context Engine (RCE) keeps your memory in one private GitHub repo that you own, the hub, so Claude and your other AI tools all load and save the same context. A new chat in any tool picks up where the last one left off.

## What it stores

- **Memories:** facts about you, your preferences, and anything you ask Claude to remember. They're saved to the hub, so they reach every tool, not just one app's memory.
- **Project context:** a short `context.md` per project, a daily log, and a monthly decisions file.
- **Files:** PDFs, images and other binaries, saved as the original file in the project's `docs/` folder with a short card beside each one. When a tool can only write text, RCE writes the card marked `binary pending`, and `/rcx files` in Claude Code finishes the upload later. It never swaps a file for a text copy.
- **Handoffs:** `/rcx push` turns a chat into a packet with a 4-digit code, and `/rcx pull <code>` continues it in another chat or tool.

Everything is plain Markdown in your repo. There's no database, no server, and no account with us.

## Get started

1. Connect GitHub with **write** access: a GitHub connector in Claude.ai or Cowork, or `gh auth login` for Claude Code.
2. Install this plugin.
3. Type `/rcx setup`. Claude asks your name, your timezone and a name for your hub, asks your OK, then creates the hub as a **private** repo and fills it from the starter template. If your connector can't create repos, Claude asks you to create one empty private repo on github.com, which takes a minute.

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

## What it runs, reads and sends

- **GitHub only.** RCE reads and writes your own hub repo through the GitHub connector or the `gh`/`git` login you've already set up in that tool. It sends nothing to any other service and has no telemetry.
- **Your data stays in your repo.** RCE saves what you share in chat (which can include personal facts) to your private hub, and keeps it until you delete it there. It never writes passwords, keys or tokens, and never copies the files listed in `private_files` into a public repo.
- **Repos.** It creates one repo, your private hub, and only after you say yes. It never deletes a repo.
- **Finding your hub.** If no pointer is set, RCE reads your GitHub username and lists your private repos and looks for the one with `rce.config.yaml` at its root.
- **Setup files.** `/rcx setup` copies the starter files from this plugin's `skills/rce/assets/`. If a tool can't read them locally, it reads the same files from the public `jsabra1/open-rce` repo.
- **Optional rules repo.** If you set `rules_repo` in your config, RCE reads its rule files from that GitHub repo instead of the copies in this plugin.
- **Session hook (Claude Code and Cowork).** At session start, a hook prints `hooks/session-start.md`, a short reminder that RCE is on. It runs nothing else and makes no network calls.
- **Local files (Claude Code).** RCE may write `~/.config/rce/rce.config.yaml`, which holds only your GitHub username and hub name. To save a binary, it may clone your hub to a temporary folder and push the file.

## Works with

| App | Support |
|---|---|
| Claude Code | Full: skill, session hook, `gh` and `git` |
| Cowork | Skill and session hook |
| Claude.ai chat | Skill. No hook, so RCE starts when the skill triggers or you type `/rcx`. Binary files are usually saved as `binary pending` cards |
| ChatGPT and other agents | Not through this plugin. Follow `BOOTSTRAP.md` in [jsabra1/open-rce](https://github.com/jsabra1/open-rce) |

## License

MIT. Source, setup guide and issues: [github.com/jsabra1/open-rce](https://github.com/jsabra1/open-rce).
