# Live link (`/rcx live`)

Links two or more chats or sessions until closed. Every turn is saved verbatim to `<hub>/handoffs/live/<code>_<Topic>/`.

## Two modes (picked automatically)

| Mode | When | Real time? |
|---|---|---|
| Native | All sides are Claude Code sessions on the same Mac that can message each other (session messaging tools are available, for example SendMessage) | Yes: a message wakes the other session |
| GitHub | Any other pair (Claude.ai, Cowork, ChatGPT, another machine) | No: a side syncs only when the user sends it a message |

Tell the user the mode once when the link opens. In GitHub mode, also say: "Chats can't wake each other. Each side sees new turns when you message it."

## Storage

```
handoffs/live/<code>_<Topic-With-Hyphens>/
  CHANNEL.md      code, topic, status, sides, times, mode
  0001-A.md       entry 1, side A
  0002-B.md       entry 2, side B
```

The code comes from the same pool as handoffs. Status lives only in `CHANNEL.md`.

## Open (`/rcx live`)

1. Pick a code and a short topic.
2. One commit: `CHANNEL.md` (Status: Open, side A = this chat), `0001-A.md` with a short context packet (TL;DR, goal, state, next step, handles).
3. Reply with the join command alone in a code block: `/rcx live 4821`.
4. Remember: code, folder, own side letter, last entry seen.

## Join (`/rcx live <code>`)

1. Find the folder. Closed: say so and offer to read it like a pull.
2. Read `CHANNEL.md` and all entries (more than 10: newest 10 in full, older by title).
3. Take the next free side letter (B, C, ...). Update `CHANNEL.md` and write your first entry in one commit.
4. Native mode: send the other side(s) a message that you joined.
5. Reply `Linked to live link <code> (<topic>)` with a 3-line recap.

## Every turn while linked

1. Before answering: read entries newer than your last seen, not written by your side. Check the status.
2. If there were new entries, say so in one line at the top: `📥 2 new (B: 2): <gist>`.
3. Answer the user.
4. After answering: write the next entry (`0007-B.md`) with the user's message and your reply, both verbatim. If the number is taken, use the next free one.
5. Native mode: also send the other side(s) the gist so they wake.
6. End with one footer line: `🔌 Live <code> · entry 0007 · 📥 2 new`

## Leave and close

- `/rcx live leave`: write a final entry, mark your side `Left` in `CHANNEL.md`, stop syncing.
- `/rcx live off`: set `Status: Closed` with time and side, write a final entry, in one commit. Other sides see it on their next turn, read the final entries once, and stop.

## Entry template (`NNNN-<side>.md`)

```markdown
# Entry <NNNN> · side <A|B> · <YYYY-MM-DD HH:MM <tz>>

## User
<verbatim>

## Reply
<verbatim, without the footer>

## Touched
<files, links, decisions, or "None">
```

Never write secrets into entries: use `[secret omitted]`.
