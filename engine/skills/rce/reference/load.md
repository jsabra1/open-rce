# Load

## Standard load (`/rce load`, and automatically at the start of a chat that needs context)

Read from `<owner>/<hub>`:
1. `AGENTS.md`
2. `manifest.yaml`
3. `me/about.md`, `me/preferences.md`, the newest month file in `me/updates/` and any entry files in `me/updates/` not yet folded
4. If the chat belongs to a project: `projects/<name>/context.md` plus any newer files in `context-updates/` (they win), then the newest decisions (month file and unfolded entries in `decisions/`, or `decisions.md` if there is none yet), then the last 7 days of `log/YYYY-MM/` (daily files and unfolded entries).

Entry files are the newest saves (`capture.md`, "Write-once saves"). Read them by listing the folder; they sort by time.

Modules and add-ons: read `MODULE.md` for each module that is on and whose trigger matches this chat (`modules.md`). Add-on repos load only on their own command (`addons.md`).

In `docs/` folders, read the `.md` cards next to files; open a PDF, image or other binary only when the task needs it (`files.md`).
Load everything else only when the task needs it: `docs/`, `chats/`, `memory/`, `me/health.md`, `me/wealth.md`, `me/relationships.md`.

### Which project is this chat?

1. A Claude.ai project chat: match the project name against `name` in `manifest.yaml`.
2. The user names a project: use it.
3. Otherwise: no project. Route each save with the rules in `capture.md`.

## Deep pull (`/rce load deep`)

For agents that need the full picture. Read in this order:
1. `AGENTS.md`, `manifest.yaml`
2. All of `me/`, including `me/updates/` (`/rce load deep public` skips the always-private files, `config.md`)
3. Every project: `project.md`, `context.md`, all of `decisions/` and `decisions.md`, all of `log/` (daily and monthly files)
4. Every project's `docs/` and `frameworks/`
5. `memory/`, including `memory/updates/`
6. `inbox-unsorted/` and open handoff packets in `handoffs/`
7. Modules that are on: their `MODULE.md` and the last 30 days of their data, except private modules when the user ran `/rce load deep public`
8. Transcripts: list each `chats/` folder (file names carry date and title). Open a full chat only when the user names it.

Stop before your context window is full. Then report in one block:

```
RCE deep load: <n> projects · <n> files · ~<n>K tokens · skipped: <what and why>
```
