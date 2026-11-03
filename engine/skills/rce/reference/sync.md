# Catch-up save (`/rcx sync`)

For a chat where auto-save didn't run, or when the user wants to be sure everything is saved.

1. Read the chat from the very first message.
2. Work out the target (see `capture.md`): `projects/<name>/` or `inbox-unsorted/`.
3. Save the full transcript, verbatim as far as you can see it, to `chats/YYYY-MM-DD_<Title>.md` in that folder. Split at 500K characters into `part-01`, `part-02`. The transcript is written once; later syncs of the same chat replace only this chat's own transcript file.
4. Extract every substantial item and save it with the small-file rules in `capture.md`: log entries to today's `log/YYYY-MM/YYYY-MM-DD.md`, decisions to `decisions/YYYY-MM.md`, facts about the user to `me/updates/YYYY-MM.md`, state changes to `context.md`. Inbox chats get dated bullets only.
5. Skip anything already saved from this chat. Running `/rcx sync` twice must add nothing the second time.
6. Everything in one commit: `rce sync: <target>: <title>`.
7. Reply with what was saved and where, then the save line from `capture.md` (for example `↻ gh-rce › projects/acme › chats, log`).
8. Keep RCE on for the rest of the chat.

If early turns were compacted and are no longer visible, write `[earlier turns not visible to this session]` in the transcript instead of guessing.

## Transcript file

```markdown
# <Title>

**Tool:** <Claude.ai / Cowork / Claude Code / ChatGPT / ...> · **Project:** <name or none> · **Started:** <date <tz>> · **Saved:** <date time <tz>>

## User
<verbatim>

## <Assistant>
<verbatim>

...
```
