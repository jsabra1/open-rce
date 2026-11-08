# Catch-up save (`/rce sync`)

For a chat where auto-save didn't run, or when the user wants to be sure everything is saved.

1. Read the chat from the very first message.
2. Work out the target (see `capture.md`): `projects/<name>/` or `inbox-unsorted/`.
3. Save the transcript as a checkpoint (`capture.md`, rule 13): the turns since the last checkpoint of this chat, or the whole chat if there is none, as a new file in `chats/<chat-start-date>_<chat-slug>/`. Split at `transcript_split_chars` into `part-01`, `part-02`. Never edit an earlier checkpoint.
4. Extract every substantial item and save it as new entry files with the write-once rules in `capture.md`: a log entry, a decisions entry, `me/updates/` and `memory/updates/` entries, a context update. Inbox chats get one inbox entry.
5. Skip anything already saved from this chat. Running `/rce sync` twice must add nothing the second time.
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
