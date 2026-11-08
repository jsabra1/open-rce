# Changelog

## Unreleased (3.0.0, branch v3-migration)

- A1 One engine, config: everything personal lives in the hub's `rce.config.yaml`. New keys: `schema_version` (3), `enabled` (pause every tool), `rules` (bundled, stable, latest or a tag), `chat_patterns`, `modules`, `addons`. New `reference/config.md` documents every key, its default and how to upgrade an older config. A config without `schema_version` keeps working; every new key defaults to today's behavior.
- A5 Hub discovery: only a pointer, the user's instructions or a search of the user's own repos name the hub, never built-in memory or past chats. Before the first read or write the hub is checked (private, config names match; otherwise stop and ask). `schema_version` is read every chat; older configs keep working on defaults and get one upgrade offer. The `/rcx` status line shows the engine and version (`open-rce 3.0.0-dev`) and the hub, so a stale engine or wrong hub shows at once.
- A4 One read/write layer: new `reference/io.md` is the only place that says how to reach GitHub: the route per tool (shell, connector, commit route for voice, none), reading rules, the voice-mode commit route (new files only), writing rules (one commit per save, permissions check, conflicts, private check) and what to do when a write fails (a new inbox file before giving up). `SKILL.md`, `AGENTS.md`, `capture.md` and `files.md` point to it. The fallback now saves to a new inbox file when writing works, instead of dropping to bullets.
- A3 Write-once saves: every save creates new entry files (`YYYY-MM-DD_HHMMSS_<chat-slug>.md`) and never edits a file, so saves work the same in voice and two chats can't overwrite each other. Log, decisions, context updates, `me/` and `memory/` updates and inbox items each get an entry file; new projects and keywords too, so routine saves never touch `manifest.yaml`. `/rcx sort` gains a Fold step that merges entries dated before today into the daily, monthly and `context.md` files and removes them in the same commit. Loading reads folded files plus unfolded entries. Hubs from before keep working: their files count as already folded.

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
