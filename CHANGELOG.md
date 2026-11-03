# Changelog

## 2.3.2 (2026-11-03)

- Plugin icon (`engine/.claude-plugin/icon.png`, 1024 px) for the directory listing.

## 2.3.1 (2026-11-03)

- Publisher is now the `jsabra1` GitHub account (plugin author and marketplace owner).
- The listing page has a "Known limits" section linking the open issues.

## 2.3.0 (2026-11-03)

- New public template repo `jsabra1/rce-hub-template`. Setup creates the hub from it (`gh repo create --template`, or a one-click github.com/new link in Claude.ai), so the connector writes only `rce.config.yaml`. Empty-repo setup still works as a fallback.
- `scripts/sync-hub-template.sh` keeps the template repo matching `engine/skills/rcx/assets/hub-template/`.

## 2.2.1 (2026-11-03)

- Setup explains the GitHub connector's `403` on repo creation (its GitHub App has no repo-creation permission) and gives a prefilled github.com/new link instead of retrying.

## 2.2.0 (2026-11-03)

- The skill is now named `rcx` (folder `engine/skills/rcx/`), so the slash command apps show is `/rcx` and matches the commands. The plugin is still Recursive Context Engine.

## 2.1.0 (2026-11-03)

- Commands are now `/rcx …` (`/rcx setup`, `/rcx load`, `/rcx push`, `/rcx pull <code>`, …), so they can't be confused with other `/rce` skills or commands a tool already knows.

## 2.0.0 (2026-11-03)

- The plugin is now **Recursive Context Engine** (`recursive-context-engine`), ready for Anthropic's plugin directory. It works in Claude.ai, Cowork and Claude Code. Reinstall with `claude plugin install recursive-context-engine@open-rce`; the old `rce@open-rce` is gone. Commands stay `/rce …` (renamed to `/rcx` in 2.1.0).
- `/rce setup` is built in (`reference/setup.md`). `BOOTSTRAP.md` is now for tools without the plugin.
- RCE finds the hub by itself, by searching your repos for `rce.config.yaml`. The pointer file is optional, and the `rce.zip` upload is no longer needed.
- Files: PDFs, images and other binaries are saved as originals with a card beside each one (`reference/files.md`). Tools that can only write text leave a `binary pending` card; `/rce files` finishes them.
- Memory: anything you ask Claude to remember is saved to the hub, so every tool shares it.
- The starter hub and `rce.config.example.yaml` moved into the plugin, under `engine/skills/rce/assets/`.
- `engine/README.md` describes everything the plugin runs, reads and sends.

## 1.1.0 (2026-11-03)

- Removed leftover mentions of restricted repos and `/rce open`; the feature isn't part of open-rce.
- Setup in one prompt: `BOOTSTRAP.md` lets the AI create the private hub and install RCE. `SETUP.md` rewritten around it, with a manual path.
- Settings live in `rce.config.yaml` at the hub root; each tool keeps a two-line pointer (`owner`, `hub`). Claude Code reads it from `~/.config/rce/`.
- `/rce` checks write access from permissions, never by writing a test file.

## 1.0.0 (2026-11-03)

- First public release: the `rce` skill and rules, Claude Code plugin, `AGENTS.md` for other agents, starter hub template, and setup guide.
- All names come from `rce.config.yaml`: owner, hub, user name, timezone, and an optional profile.
