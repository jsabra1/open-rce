# Tools

## `cc-transcript-backup.py` (Claude Code)

Backs up each Claude Code session to the hub, so a session's words survive even if the chat is compacted or closed before RCE saved them. The plugin runs it on `SessionEnd` and `PreCompact` (`hooks/hooks.json`); nothing to install.

- **What it saves:** the user's messages and Claude's text replies, verbatim, to `inbox-unsorted/chats/claude-code/<start-date>_<session-id>_<title>.md`. Tool calls and tool output are left out. Secrets are masked (`[secret omitted]`) before anything is written.
- **Where:** the hub named in `~/.config/rce/rce.config.yaml` (`owner`, `hub`). No pointer means it does nothing. It writes only if the hub is **private**.
- **How:** a clone at `local_path` (pointer key) or, by default, one cached at `~/.cache/rce/<owner>__<hub>`; one commit with that one file, then a push, using your `gh`/`git` login.
- **Off switch:** `transcript_backup: false` in the pointer, or `enabled: false` in the hub's `rce.config.yaml`.
- **Never blocks a session:** errors go to `~/.cache/rce/transcript-backup.log`.
