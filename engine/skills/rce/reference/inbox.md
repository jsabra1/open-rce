# Inbox (`/rcx sort`)

Routing is automatic (see `capture.md`). `inbox-unsorted/` only holds items an agent could not place with confidence, so it should stay small.

`/rcx sort` is optional. Run it to clear leftovers:
1. Read every `*.md` file in `inbox-unsorted/` except `README.md`.
2. Route each item with the rules in `capture.md`. Move it straight away; no approval step.
3. Items you still can't place stay where they are.
4. Remove moved items from their inbox file. Delete inbox files left empty. One commit.
5. Update `context.md` (summary and `Last updated`) for every project whose state changed.

When the user asks to "fold updates" (or as part of `/rcx sort`), merge the bullets in `me/updates/` and `memory/updates/` into their snapshot files (`me/health.md`, `memory/<topic>.md`, ...), one commit per month file. Keep the updates files as history; mark each folded bullet `(folded YYYY-MM-DD)`.
6. Report: items moved (with destinations), items left, files deleted.

Never create repos. Never delete items that weren't moved.
