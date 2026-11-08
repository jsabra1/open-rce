# Add-on repos (`addons.md`)

An add-on is a private repo outside the hub for a bigger piece of context: a book, a client archive, a mentor's notes. Each one is listed under `addons:` in `rce.config.yaml` (fields in `config.md`) and loads only on its own command.

## Loading (`/rce <command>`)

1. Find the add-on whose `command` matches. None: say so and list the add-ons there are.
2. Read it the way `io.md` says. If the tool has no access to the repo, say `RCE: no access to add-on <name>; grant <owner>/<repo> to this tool's GitHub connector` and stop. Never fall back to the hub, and never guess its content.
3. Read its `instructions` file (default `AGENTS.md`) first and follow it while the add-on is loaded: it says what to load next and how to behave.
4. Say once: `RCE: add-on <name> loaded`.

`/rce load deep` skips add-ons unless `load_deep: true`. `/rce load deep <name>` includes one.

## Saving

While an add-on is loaded, items about it are saved inside it, write-once, under `saves_to` (default `log/`): a new `YYYY-MM-DD_HHMMSS_<chat-slug>.md` per save. Items about anything else are saved to the hub as usual. Never copy add-on content into the hub, the profile or any public output (`config.md`, "Privacy defaults"). Save line: `↻ gh-rce › addon/<name> › log`.

## Adding one (`/rce addon add <repo>`)

1. Check the repo: it must exist, belong to `owner` (or be written `owner/repo`), and be **private**. Public: stop and say so.
2. Check this tool can read it (`io.md`). If not, tell the user how to grant it and stop.
3. Ask, in one message: a short `name` (default: the repo name), the `command` (default: the name; refuse any built-in command such as `load`, `sync`, `push`, `pull`, `live`, `sort`, `files`, `setup`, `doctor`, `import`, `addon`, `off`, `on`, `retire`), and whether `/rce load deep` may include it (default no).
4. If the repo has no `AGENTS.md`, offer to create a short one saying what it holds and what to load first (new file, one commit, only with a yes).
5. Show the new `addons:` entry and, with a yes, add it to `rce.config.yaml` (one commit, keeping every other line). This is one of the few edits a routine flow makes, so read the config first and change only the `addons:` list.
6. Test it: run `/rce <command>` once and report.

`/rce addon remove <name>`: remove the entry from the config with a yes. The repo is untouched.
