# Capture (auto-save)

Save whenever the user shares something substantial about themselves or their work: facts, decisions, plans, goals, preferences, project progress.
You judge what is substantial. Skip chit-chat. Do not batch: save in the same turn.
Do not save when the user has typed `/rcx off` in this chat, or the chat is incognito.

## Small files only

Read and write as `io.md` says. GitHub connectors can't append: changing one line means uploading the whole file again. So a save only ever writes small, current files:

| What | File | Rule |
|---|---|---|
| Log entries | `log/YYYY-MM/YYYY-MM-DD.md` | One file per day. Create it if missing |
| Decisions | `decisions/YYYY-MM.md` | One file per month, newest first. Create it if missing |
| New facts about the user | `me/updates/YYYY-MM.md` | One file per month, each bullet tagged `[about]`, `[preferences]`, `[health]`, `[wealth]`, `[relationships]` or `[people: <name>]` |
| Cross-project knowledge | `memory/updates/YYYY-MM.md` | One file per month, each bullet tagged `[<topic>]` |
| Current state of a project | `context.md` | Snapshot, kept under about 4 KB (see below) |

Never rewrite these on a routine save:
- Snapshot files: the existing `me/*.md` and `memory/*.md` files. Only `/rcx sort` changes them.
- `manifest.yaml`, except when a project is registered, renamed or retired, or a keyword is added.
- Reference pages (`project.md`, `frameworks/`, `docs/`, transcripts, handoff packets), unless the user asks to change them. When you do change one, keep every other line exactly as it was, and say in the reply which lines you changed.

Decisions and log entries are written immediately, on the same save. The time-based file only decides where they go.

## Save rules (apply to every save)

1. **Never restore missing content.** If something you saved earlier in this chat is no longer in the hub, the user or another session removed it on purpose. Do not add it back. Mention it in one line.
2. **Conflicts.** If a write is rejected because the file changed since you read it, re-read the file and add only your new lines again. Never drop or change lines you didn't write.
3. **No duplicates.** Before adding, check today's log file and this month's decisions file. Skip anything already there, whoever saved it.
4. **Changed minds.** When the user changes an earlier decision or fact, add a new entry ending `(replaces: <old item> of <date>)`, and update `context.md` to show only the current value. Never edit or delete old dated entries.
5. **Ambiguity never blocks.** If the project or meaning is unclear (for example "ACME"), save under your best guess, mark it `(unsure: <A> or <B>)`, and ask the user in the same reply. Fix the entry when they answer.
6. **Chat names.** Name an inbox file from the chat's first message (a short title). Never ask the user what to call it.
7. **Timezone.** All dates, times and file names in the hub use the `timezone` in `rce.config.yaml` (default UTC). Take the time from a tool (a clock, `date`, or the last commit) rather than estimating it; if you can't, write the date only.
8. **Long pastes.** When the user pastes a long document, log one line describing it. Save the full text to `docs/` only if they ask.
9. **Secrets.** Replace passwords, API keys and tokens with `[secret omitted]` before writing anything.
10. **Test messages.** Anything that starts with "RCE test" goes to `inbox-unsorted/tests/YYYY-MM-DD.md`, never to project files, `me/` or `memory/`.
11. **Remember requests.** When the user asks you to remember something, or you would save it to your own tool's memory, save it to the hub too, so every tool shares it: facts about the user and how they like to work go to `me/updates/YYYY-MM.md`, general knowledge to `memory/updates/YYYY-MM.md`. The hub is the shared memory; a tool's own memory is only a local copy.
12. **Files (PDFs, images, other binaries).** Follow `files.md`. Never save a text conversion in place of the original file.
13. **File headers.** If a file has a YAML header (between `---` lines), wrap every text value in double quotes (`description: "Name: Role"`). An unquoted colon breaks the header on GitHub.

## Where it goes (repo `<hub>`)

Every save is routed automatically, item by item. Nobody sorts by hand.

| Order | Rule | Target |
|---|---|---|
| 1 | The chat is inside a project | `projects/<name>/` |
| 2 | No project, but the item clearly belongs to one project in `manifest.yaml` (matched against its `name`, `description` and `keywords`) | `projects/<name>/` |
| 3 | The item is about the user | `me/updates/YYYY-MM.md`, tagged by topic |
| 4 | Cross-project knowledge or a recurring topic | `memory/updates/YYYY-MM.md`, tagged by topic |
| 5 | You can't place it with confidence | `inbox-unsorted/<Chat Name> Context.md` |

- Read `manifest.yaml` fresh on every save, so projects registered by other chats are matched too.
- One message can produce items for several targets. Route each item on its own, all in one commit.
- Items routed by rules 2 to 4 from a no-project chat end with `(auto-routed from <Chat Name>)`, so they can be traced and moved back.
- The save line lists every target (see "Save line" below): `↻ gh-rce › projects/acme › log, decisions · me › health`.

## Project save (one commit)

1. Log: add to `projects/<name>/log/YYYY-MM/YYYY-MM-DD.md`: `- HH:MM: <what happened, in rich detail>`
2. Decisions: add to the top of `projects/<name>/decisions/YYYY-MM.md`: `- YYYY-MM-DD: <decision>, because <reason>. Rejected: <alternatives>.`
3. If the current state changed, update `context.md`: its `## Summary` section, its `Last updated: YYYY-MM-DD` line, and the current state. Keep it under about 4 KB. If it would grow past that, move the oldest detail word for word into today's log file under `## Moved from context.md`. Never delete anything.

Commit message: `rce: <project>: <short topic>`.

## `me/` and `memory/` save

Add a bullet to this month's updates file: `- YYYY-MM-DD [health]: <fact> (auto-routed from <Chat Name>)`. If a fact replaces an older one, say so in the bullet: `(replaces <old fact>)`.
`/rcx sort` folds updates into the snapshot files (`me/health.md` and so on) when the user asks.
Commit message: `rce: me: <topic>` or `rce: memory: <topic>`. Items for several targets go in one commit: `rce: <first target>: <short topic>`.

## Inbox save (fallback only)

Use only for items rule 5 can't place. Append to `inbox-unsorted/<Chat Name> Context.md` under a `## YYYY-MM-DD` heading, one bullet per item.
Create the file on the first save, named from the chat's first message (rule 6). Reuse it for the rest of the chat.

## Unknown project

If the chat is in a project with no match in `manifest.yaml`:
1. If no existing project name is close to it, register it automatically: create `projects/<name>/` with `project.md`, `context.md`, and today's log file, and add a manifest entry (name, folder, description from the project, `keywords` drawn from the description: aliases, clients, products, people; status `active`). In the same commit, scan `inbox-unsorted/` for items that match the new project, move them into today's log file (or this month's decisions file), tagged `(auto-routed from <Chat Name>)`, and delete inbox files left empty.
2. If an existing name is close (for example "Acme Rebrand" vs "Acme"), ask the user: (a) use the existing project, (b) register as new, (c) skip.
3. The save line says: `↻ gh-rce › projects/<name> › log (new project registered, <n> inbox items moved)`.

## Keywords

When the user mentions a new alias, client, product or person tied to a project, add it to that project's `keywords` in `manifest.yaml` in the same commit.

## Profile changes

If `profile` is set in `rce.config.yaml` and the user's role, interests or project list change, regenerate `<profile>/README.md` using only the sections listed in `<hub>/public/fields.yaml`.

## After saving

End the reply with the save line, nothing after it:

```
↻ gh-rce › projects/acme › decisions
```

- `gh-rce` is the hub on GitHub (`<hub>`).
- Then the folder (`projects/<name>`, `me`, `memory`, `inbox`), then the file type: `log`, `decisions`, `context`, `chats`, `health`, `wealth`, `relationships`, `about`, `preferences`, `people`, `tests`, `docs`.
- Several file types in one folder: comma-separated (`log, decisions`). Several folders: separated by ` · `.
- Example: `↻ gh-rce › projects/acme › log, decisions · me › health`

On failure: `⚠ RCE push failed: <reason>` and the bullets to paste later.
