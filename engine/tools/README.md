# Tools

## `cc-transcript-backup.py` (Claude Code)

Backs up each Claude Code session to the hub, so a session's words survive even if the chat is compacted or closed before RCE saved them. The plugin runs it on `SessionEnd` and `PreCompact` (`hooks/hooks.json`); nothing to install.

- **What it saves:** the user's messages and Claude's text replies, verbatim, to `inbox-unsorted/chats/claude-code/<start-date>_<session-id>_<title>.md`. Tool calls and tool output are left out. Secrets are masked (`[secret omitted]`) before anything is written.
- **Where:** the hub named in `~/.config/rce/rce.config.yaml` (`owner`, `hub`). No pointer means it does nothing. It writes only if the hub is **private**.
- **How:** its own clone at `~/.cache/rce/<owner>__<hub>` (never your working copy, so it can't push your unrelated commits); one commit with that one file, then a push, using your `gh`/`git` login.
- **The one rewritten file:** each run rewrites that session's file with the whole session so far. It is the only file in the hub that RCE rewrites, and `/rce sort` never touches `inbox-unsorted/chats/`.
- **Off switch:** `transcript_backup: false` in the pointer, or `enabled: false` in the hub's `rce.config.yaml`.
- **Never blocks a session:** errors go to `~/.cache/rce/transcript-backup.log`.
