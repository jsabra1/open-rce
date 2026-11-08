# Capture (auto-save)

Save whenever the user shares something substantial about themselves or their work: facts, decisions, plans, goals, preferences, project progress.
You judge what is substantial. Skip chit-chat. Do not batch: save in the same turn.
Do not save when the user has typed `/rce off` in this chat, or the chat is incognito.

## Write-once saves

Read and write as `io.md` says. Every save creates **new files only**: it never reads a file in order to change it. That works the same with every route, voice included, and two chats can never overwrite each other. `/rce sort` folds the new files into the tidy period files later (`inbox.md`, "Fold").

A save writes one **entry file** per target. Name: `YYYY-MM-DD_HHMMSS_<chat-slug>.md` (time from a tool, in `timezone`; `<chat-slug>` = the chat title in lowercase with hyphens, at most 40 characters).

| What | Entry file (new, per save) | Folded into (by `/rce sort`) |
|---|---|---|
| Log entries | `projects/<name>/log/YYYY-MM/<entry>` | `log/YYYY-MM/YYYY-MM-DD.md` |
| Decisions | `projects/<name>/decisions/YYYY-MM/<entry>` | `decisions/YYYY-MM.md`, newest first |
| Current state of a project | `projects/<name>/context-updates/<entry>` | `context.md` |
| New facts about the user | `me/updates/YYYY-MM/<entry>`, each bullet tagged `[about]`, `[preferences]`, `[health]`, `[wealth]`, `[relationships]` or `[people: <name>]` | `me/updates/YYYY-MM.md`, later the snapshot files |
| Cross-project knowledge | `memory/updates/YYYY-MM/<entry>`, each bullet tagged `[<topic>]` | `memory/updates/YYYY-MM.md`, later `memory/<topic>.md` |
| Items you can't place | `inbox-unsorted/<entry>` | routed by `/rce sort` |

Every entry file starts with one line: `<!-- rce entry YYYY-MM-DD HH:MM:SS <tz> · <tool> · <chat title> -->`, then its bullets.

Never change these on a routine save (only `/rce sort`, or the user asking, changes them):
- The folded period files above, `context.md`, and the snapshot files in `me/` and `memory/`.
- `manifest.yaml`. New projects and keywords are written as entry files and added to the manifest by `/rce sort` (see "Unknown project" and "Keywords").
- Reference pages (`project.md`, `frameworks/`, `docs/`, transcripts, handoff packets), unless the user asks to change them. When you do change one, keep every other line exactly as it was, and say in the reply which lines you changed.

One file is rewritten on purpose: the Claude Code session backup in `inbox-unsorted/chats/claude-code/`, owned by the plugin's hook and changed only by it (`tools/README.md`).

Hubs from before write-once (one daily or monthly file edited in place) keep working: their files count as already folded.

## Save rules (apply to every save)

1. **Never restore missing content.** If something you saved earlier in this chat is no longer in the hub, the user or another session removed it on purpose. Do not add it back. Mention it in one line.
2. **Conflicts.** Write-once saves don't conflict. If an edit the user asked for is rejected because the file changed, re-read it and add only your new lines. Never drop or change lines you didn't write.
3. **No duplicates.** Before saving, check today's entry files and folded log, and this month's decisions (entries and folded file). Skip anything already there, whoever saved it. List the folder to find entries; never guess names.
4. **Changed minds.** When the user changes an earlier decision or fact, add a new entry ending `(replaces: <old item> of <date>)`, plus a context update with the current value; `/rce sort` makes `context.md` show only that. Never edit or delete old dated entries.
5. **Ambiguity never blocks.** If the project or meaning is unclear (for example "ACME"), save under your best guess, mark it `(unsure: <A> or <B>)`, and ask the user in the same reply. When they answer, write a new entry with the right target ending `(replaces: <the unsure entry> of <date>)`; never edit the first.
6. **Chat names.** Name an inbox file from the chat's first message (a short title). Never ask the user what to call it.
7. **Timezone.** All dates, times and file names in the hub use the `timezone` in `rce.config.yaml` (default UTC). Take the time from a tool (a clock, `date`, or the last commit) rather than estimating it; if you can't, write the date only.
8. **Long pastes.** When the user pastes a long document, log one line describing it. Save the full text to `docs/` only if they ask.
9. **Secrets.** Before every write, scan what you are about to write and replace each of these with `[secret omitted]`: passwords and PINs; API keys and tokens (for example strings starting `ghp_`, `github_pat_`, `sk-`, `xox`, `AKIA`, `AIza`); private keys (`-----BEGIN ... PRIVATE KEY-----`); anything after `password`, `passwd`, `secret`, `token` or `api key` followed by `:` or `=`; full card numbers; bank account numbers and IBANs; one-time codes. Keep the surrounding sentence. If you are unsure whether something is a secret, mask it. Mention masks in the reply: `(1 secret omitted)`.
10. **Test messages.** Anything that starts with "RCE test" goes to a new `inbox-unsorted/tests/<entry>`, never to project files, `me/` or `memory/`.
11. **Remember requests.** When the user asks you to remember something, or you would save it to your own tool's memory, save it to the hub too, so every tool shares it: facts about the user and how they like to work go to a `me/updates/YYYY-MM/` entry, general knowledge to a `memory/updates/YYYY-MM/` entry. The hub is the shared memory; a tool's own memory is only a local copy.
12. **Files (PDFs, images, other binaries).** Follow `files.md`. Never save a text conversion in place of the original file.
13. **Rolling transcript checkpoints.** Save the chat's own words as you go, before the tool compacts them. A checkpoint is a new file per saving turn: `chats/<chat-start-date>_<chat-slug>/YYYY-MM-DD_HHMMSS.md` in the chat's project folder (or `inbox-unsorted/chats/`), holding the turns since the last checkpoint, verbatim as far as you can see them, in the transcript format from `sync.md`. Never edit an earlier checkpoint. Write one:
    - at the end of every turn that saves something, with only the turns since the last checkpoint;
    - in any chat, once about 20 turns have passed without one, even if nothing else was saved;
    - always in recurring chats (titles matching `chat_patterns` in the config), at least once per session.
   The first line of each file is `<!-- checkpoint YYYY-MM-DD HH:MM <tz>, turns <first>-<last> -->`; read the newest checkpoint's marker first (list the folder) so no turn is written twice. If earlier turns are no longer visible (compacted), write `[turns before <date> compacted before checkpoint]` and add `(transcript gap)` to the save line. Secrets rule 9 applies. Claude Code also backs up its sessions with the plugin's hook (`tools/README.md`).
14. **File headers.** If a file has a YAML header (between `---` lines), wrap every text value in double quotes (`description: "Name: Role"`). An unquoted colon breaks the header on GitHub.

## Where it goes (repo `<hub>`)

Every save is routed automatically, item by item. Nobody sorts by hand. A module whose trigger matches the chat routes its own items first (`modules.md`); a loaded add-on keeps its items inside the add-on (`addons.md`).

| Order | Rule | Target |
|---|---|---|
| 1 | The chat is inside a project | `projects/<name>/` |
| 2 | No project, but the item clearly belongs to one project in `manifest.yaml` (matched against its `name`, `description` and `keywords`) | `projects/<name>/` |
| 3 | The item is about the user | `me/updates/YYYY-MM/<entry>`, tagged by topic |
| 4 | Cross-project knowledge or a recurring topic | `memory/updates/YYYY-MM/<entry>`, tagged by topic |
| 5 | You can't place it with confidence | `inbox-unsorted/<entry>` |

- Read `manifest.yaml` fresh on every save, and list `projects/`: a folder with a `project.md` but no manifest entry is a project registered by another chat and not yet folded. Match it too.
- One message can produce items for several targets. Route each item on its own, all in one commit.
- Items routed by rules 2 to 4 from a no-project chat end with `(auto-routed from <Chat Name>)`, so they can be traced and moved back.
- The save line lists every target (see "Save line" below): `↻ gh-rce › projects/acme › log, decisions · me › health`.

## Project save (one commit)

New files only, in one commit:
1. Log entry: `projects/<name>/log/YYYY-MM/<entry>` with `- HH:MM: <what happened, in rich detail>`
2. Decisions entry (if any): `projects/<name>/decisions/YYYY-MM/<entry>` with `- YYYY-MM-DD: <decision>, because <reason>. Rejected: <alternatives>.`
3. Context update (if the current state changed): `projects/<name>/context-updates/<entry>` with the new state as bullets, plus `Summary: <one line>` when the summary changes. `/rce sort` applies it to `context.md`.

Commit message: `rce: <project>: <short topic>`.

## `me/` and `memory/` save

A new entry file with one bullet per fact: `- YYYY-MM-DD [health]: <fact> (auto-routed from <Chat Name>)`. If a fact replaces an older one, say so in the bullet: `(replaces <old fact>)`.
`/rce sort` folds entries into the month file, and into the snapshot files (`me/health.md` and so on) when the user asks.
Commit message: `rce: me: <topic>` or `rce: memory: <topic>`. Items for several targets go in one commit: `rce: <first target>: <short topic>`.

## Inbox save (fallback only)

Use only for items rule 5 can't place: a new `inbox-unsorted/<entry>` per save, one bullet per item with its likely target.

## Unknown project

If the chat is in a project with no match in `manifest.yaml`:
1. If no existing project name is close to it, register it automatically: create `projects/<name>/` with `project.md` (name, description, `keywords` drawn from the description: aliases, clients, products, people; status `active`), `context.md` and the first log entry, all new files in one commit. `/rce sort` adds it to `manifest.yaml` and moves matching inbox items into it.
2. If an existing name is close (for example "Acme Rebrand" vs "Acme"), ask the user: (a) use the existing project, (b) register as new, (c) skip.
3. The save line says: `↻ gh-rce › projects/<name> › log (new project registered)`.

## Keywords

When the user mentions a new alias, client, product or person tied to a project, add a line `Keywords: <word>, <word>` to that save's log entry. `/rce sort` adds them to `manifest.yaml`.

## Profile changes

If `profile` is set in `rce.config.yaml` and the user's role, interests or project list change, offer to regenerate the profile and, only with the user's yes, regenerate `<profile>/README.md` using only the sections listed in `<hub>/public/fields.yaml`.

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
