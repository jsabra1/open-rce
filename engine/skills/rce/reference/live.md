# Live link (`/rce live`)

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
  CHANNEL.md      code, topic, side A, start time, mode (written once)
  CLOSED.md       present once the channel is closed
  0001-A.md       entry 1, side A
  0002-B.md       entry 2, side B
```

The code comes from the same pool as handoffs. Nothing is ever edited: who joined or left is read from the entries, and `CLOSED.md` marks a closed channel. That keeps live links working in voice and with two sides writing at once.

## Open (`/rce live`)

1. Pick a code and a short topic.
2. One commit: `CHANNEL.md` (side A = this chat), `0001-A.md` with a short context packet (TL;DR, goal, state, next step, handles).
3. Reply with the join command alone in a code block: `/rce live 4821`.
4. Remember: code, folder, own side letter, last entry seen.

## Join (`/rce live <code>`)

1. Find the folder. Closed (it has `CLOSED.md`): say so and offer to read it like a pull.
2. Read `CHANNEL.md` and all entries (more than 10: newest 10 in full, older by title).
3. Take the next free side letter (B, C, ...) and write your first entry, starting `Joined.`, in one commit. `CHANNEL.md` is never edited after the open: who is in the channel is read from the entries.
4. Native mode: send the other side(s) a message that you joined.
5. Reply `Linked to live link <code> (<topic>)` with a 3-line recap.

## Every turn while linked

1. Before answering: read entries newer than your last seen, not written by your side. Check for `CLOSED.md`.
2. If there were new entries, say so in one line at the top: `📥 2 new (B: 2): <gist>`.
3. Answer the user.
4. After answering: write the next entry (`0007-B.md`) with the user's message and your reply, both verbatim. If the number is taken, use the next free one.
5. Native mode: also send the other side(s) the gist so they wake.
6. End with one footer line: `🔌 Live <code> · entry 0007 · 📥 2 new`

## Leave and close

- `/rce live leave`: write a final entry starting `Left.`, stop syncing.
- `/rce live off`: write a final entry starting `Closed.` and a new file `CLOSED.md` (time and side), in one commit. A channel with `CLOSED.md` is closed. Other sides see it on their next turn, read the final entries once, and stop.

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
