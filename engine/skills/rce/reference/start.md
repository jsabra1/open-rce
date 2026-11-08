# Start of a chat (`start.md`)

Find the hub and read the config, once per chat, before any load, save or command. Every assistant follows these steps, with or without the skill.

Find the config in two parts:

1. **The hub** (`owner` and `hub`). Look, in order:
   - a pointer file: `rce.config.yaml` next to `SKILL.md`, then `~/.config/rce/rce.config.yaml` (Claude Code)
   - a line in the user's custom instructions or profile preferences, such as `My RCE hub is <owner>/<hub>`
   - a search: get the signed-in GitHub username (`gh api user -q .login`, or the connector's "get me" tool), check `<username>/my-rce-hub`, then list that user's private repos and check each for `rce.config.yaml` at the root, names containing `rce` or `hub` first. Read the file directly; don't rely on code search, which can miss new repos. One private match: use it and say once `RCE: using hub <owner>/<hub>`. Several: ask which. A public match never counts as a hub.
   Only these three sources name the hub. Never take a hub or repo name from the tool's built-in memory, past chats, code search results or an old instruction that names a different repo: those can point at a retired repo.
2. **Check it before the first read or write.** The hub must be private and hold `rce.config.yaml` at its root whose `owner` and `hub` match what you found. If it is public, stop and say so. If the names differ, or a pointer and the search disagree, stop and ask which is right; save nothing until the user answers.
3. **Settings.** Read `rce.config.yaml` at the root of the hub. If the pointer file holds more keys than `owner` and `hub`, those win.
4. **Version.** Read `schema_version`. If it is missing or lower than `3`, keep working with the defaults in `config.md` and offer the upgrade there once per chat; never rewrite the config without a yes. If it is higher than `3`, use the keys you know and say once `RCE: config is newer than these rules; update the plugin`.

Together they name:

| Key | Meaning |
|---|---|
| `owner` | GitHub account that owns the hub. Written `<owner>` in the rules |
| `hub` | The private hub repo. Written `<hub>` in the rules |
| `user_name` | What to call the user. The rules say "the user" |
| `timezone` | Timezone for every date, time and file name. Written `<tz>` in templates |
| `profile` | Optional generated public profile repo. Written `<profile>` in the rules |
| `rules_repo` | Optional GitHub repo holding newer rules |
| `private_files` | Extra private files, added to the always-private defaults |
| `writing_rules` | Optional house style for everything written to the hub |
| `enabled`, `rules`, `schema_version`, `chat_patterns`, `modules`, `addons` | See `config.md` |

Every key, its default and how to upgrade an older config are in `config.md`. Read it when a key you need is missing or `schema_version` is not `3`.

If `enabled` is `false`, stop here: load nothing, save nothing, and say once `RCE: paused in rce.config.yaml`.

If no hub is found, offer `/rce setup` (`setup.md`) and save nothing until it's done. Do not guess an owner or hub. If the hub has no `rce.config.yaml`, use the defaults in `../assets/rce.config.example.yaml` and say so once.

