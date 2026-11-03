# Changelog

## 1.1.0 (2026-11-03)

- Setup in one prompt: `BOOTSTRAP.md` lets the AI create the private hub and install RCE. `SETUP.md` rewritten around it, with a manual path.
- Settings live in `rce.config.yaml` at the hub root; each tool keeps a two-line pointer (`owner`, `hub`). Claude Code reads it from `~/.config/rce/`.
- `/rce` checks write access from permissions, never by writing a test file.

## 1.0.0 (2026-11-06)

- First public release: the `rce` skill and rules, Claude Code plugin, `AGENTS.md` for other agents, starter hub template, and setup guide.
- All names come from `rce.config.yaml`: owner, hub, user name, timezone, optional profile and restricted repos.
