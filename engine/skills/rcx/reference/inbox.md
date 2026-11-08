# Inbox (`/rcx sort`)

Routing is automatic (see `capture.md`). `inbox-unsorted/` only holds items an agent could not place with confidence, so it should stay small.

`/rcx sort` is optional. Run it to clear leftovers:
1. Fold first (below), then read every `*.md` file in `inbox-unsorted/` except `README.md`.
2. Route each item with the rules in `capture.md`. Move it straight away; no approval step.
3. Items you still can't place stay where they are.
4. Moved items go into new entry files at their target (`capture.md`). Remove them from their inbox file and delete inbox files left empty, in the same commit.
5. Update `context.md` (summary and `Last updated`) for every project whose state changed.

6. Report: items moved (with destinations), items left, files deleted.

Never create repos. Never delete items that weren't moved.

## Fold

Saves write one small entry file each (`capture.md`, "Write-once saves"). Folding merges them into the tidy period files. It runs as part of `/rcx sort`, and Claude Code may run it at the start of a session. It needs a route that can read and update files (`io.md`), so it never runs in voice.

1. Fold only entries dated before today (in `timezone`); today's stay as they are, so live chats never collide with a fold.
2. For each folder, in time order:
   - `log/YYYY-MM/<entry>` files: append their bullets to `log/YYYY-MM/YYYY-MM-DD.md` (create it if missing).
   - `decisions/YYYY-MM/<entry>` files: add their bullets to the top of `decisions/YYYY-MM.md`, newest first.
   - `context-updates/<entry>` files: apply them to `context.md` in order (current state, `## Summary`, `Last updated: YYYY-MM-DD`). Keep it under about 4 KB; older detail moves word for word into that day's log file under `## Moved from context.md`.
   - `me/updates/YYYY-MM/` and `memory/updates/YYYY-MM/` entries: append to `me/updates/YYYY-MM.md` and `memory/updates/YYYY-MM.md`.
   - New projects (a `projects/<name>/project.md` with no manifest entry) and `Keywords:` lines: add them to `manifest.yaml`. Move matching inbox items into the new project.
3. In the same commit, delete the entry files that were folded. Nothing is lost: their text is in the folded file, and the entry files stay in git history. Commit message: `rce fold: <n> entries`.
4. Never fold a file you could not read in full. Never change a bullet's text while folding; copy it exactly.

When the user asks to "fold updates" into snapshots, merge the bullets in `me/updates/YYYY-MM.md` and `memory/updates/YYYY-MM.md` into their snapshot files (`me/health.md`, `memory/<topic>.md`, ...), one commit per month file. Keep the month files as history; mark each folded bullet `(folded YYYY-MM-DD)`.
