# Import (`/rce import`)

Brings the user's existing context into the hub, so RCE starts with what the user's assistant already knows instead of an empty profile. Setup offers it at the end; the user can run it any time. Every item is shown to the user before it is saved, and saves are write-once (`capture.md`).

## 1. This assistant's built-in memory

1. Write out, as a numbered list, everything this assistant holds about the user in its own memory or profile (for example Claude's memory, ChatGPT's saved memories, custom instructions). One fact per line, with its source (`memory`, `instructions`). If this assistant has no memory, or you can see none, say so and go to step 2.
2. Mark each item's likely target: `me/` (about, preferences, people), a project, or `memory/`. Health, wealth and relationship items are marked private.
3. Ask the user to review: keep, fix or drop each item, or "all good".
4. Save the kept items as entry files, routed as `capture.md` says, tagged `(imported from <assistant> memory)`, in one commit.

Run it again in each assistant the user uses; duplicates are skipped (`capture.md`, rule 3).

## 2. Past chats (optional)

Offer it; don't push. Two ways, depending on the assistant:
- **Past-chat search** (if this assistant can search its own past chats): ask which projects or time span matter, read those chats, and propose items as in step 1. Up to about 20 chats per run.
- **Data export** (Claude and ChatGPT both offer an account export as a zip): tell the user where to request it in their settings. Processing it needs a shell: in Claude Code, unzip it to a temporary folder outside the hub, read the conversations, and propose items as in step 1, in batches of about 50 items. Never commit the export itself; it holds everything, including what the user didn't choose to keep.

Transcripts are not imported by default. If the user wants some, save each chosen chat as a checkpoint (`capture.md`, rule 13) in the matching project's `chats/`.

## Report

`RCE import: <n> items saved (<n> me, <n> projects, <n> memory, <n> private) · <n> dropped · <n> duplicates skipped`
