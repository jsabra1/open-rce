# Config (`rce.config.yaml`)

Everything personal lives in the hub's `rce.config.yaml`, never in the rules. The rules name keys (`<owner>`, `<hub>`, `user_name`); the config fills them in. A key that is missing takes the default below.

## Keys

| Key | Default | Meaning | Used by |
|---|---|---|---|
| `schema_version` | `1` if missing | Config format. Current: `3` | Step 0, upgrades below |
| `owner` | none (required) | GitHub account that owns the hub | Everything |
| `hub` | none (required) | The private hub repo | Everything |
| `user_name` | `the user` | What to call the user | Every save |
| `timezone` | `UTC` | Timezone for every date, time and file name | Every save |
| `enabled` | `true` | `false` pauses RCE in every tool: load nothing, save nothing, and say once `RCE: paused in rce.config.yaml` | Step 0 |
| `rules` | `bundled`; `latest` if `rules_repo` is set (the pre-3 behavior). Setup writes `stable` | `stable`: the newest release of `rules_repo` (recommended: fixes arrive without a reinstall). `latest`: its `main` branch. A tag such as `v3.0.0`: that release only. `bundled`: the copy shipped with the plugin. Unreadable `rules_repo` falls back to bundled for that chat | Step 1 |
| `rules_repo` | empty; setup writes `jsabra1/open-rce` | Public repo holding the rules. Needed for anything but `bundled` | Step 1 |
| `profile` | empty | Optional generated public profile repo | `capture.md` |
| `private_files` | the four below | Files and folders never copied into `<profile>` or any public output | Hard rules, `capture.md` |
| `writing_rules` | empty | House style for everything written to the hub | Every save |
| `chat_patterns` | empty | Title prefixes of recurring chats; those chats save a transcript checkpoint every session | `capture.md` |
| `modules` | empty | Optional modules turned on, by folder name under `modules/` | `load.md` |
| `addons` | empty | Add-on repos (below) | `load.md`, `capture.md` |
| `transcript_split_chars` | `500000` | Split long transcripts into parts of this size | `sync.md` |

Default `private_files`: `me/health.md`, `me/wealth.md`, `me/relationships.md`, `me/updates/`. A user's list replaces the defaults; it never adds to them silently.

## Add-on repos

An add-on is a private repo outside the hub for a bigger piece of context. It is off unless listed:

| Field | Default | Meaning |
|---|---|---|
| `name` | none (required) | Short name, used in save lines |
| `repo` | none (required) | Repo name; owner is `owner` unless written `owner/repo` |
| `command` | `name` | `/rce <command>` loads it. Must not clash with a built-in command; setup refuses a clash |
| `instructions` | `AGENTS.md` | The add-on's own rules, read first and followed while it is loaded |
| `saves_to` | `log/` | Saves from a chat that loaded the add-on go here, inside the add-on |
| `load_deep` | `false` | `true` lets `/rce load deep` include it |

An add-on loads only on its command. If the tool cannot read the add-on repo, say so and stop: never fall back to the hub, and never save add-on content into the hub.

## Upgrades

Read `schema_version` first. Never rewrite the user's config without their yes; propose the change and show the new lines.

| From | To | Change |
|---|---|---|
| missing or `1` | `3` | Add `schema_version: 3`. Every new key takes its default, so behavior does not change. If `rules_repo` is set, write `rules: latest` explicitly, since that is what it did before. Offer to add the new keys with their defaults, commented, so the user can see them |
| `2` | `3` | Same as above (`2` was never released) |

A config with a `schema_version` newer than these rules know: use the keys you understand, ignore the rest, and say once `RCE: config is newer than these rules; update the plugin`.
