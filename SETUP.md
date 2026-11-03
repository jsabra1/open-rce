# Set up RCE

About 15 minutes. Run every command from the same folder. You need a GitHub account and, for the command-line steps, `git` and the GitHub CLI (`gh auth login` done once).

## 1. Create your private hub

Your hub is a new **private** repo made from `hub-template/`.

```bash
git clone https://github.com/jsabra1/open-rce.git
```

```bash
gh repo create my-rce-hub --private --clone
```

```bash
cp -R open-rce/hub-template/. my-rce-hub/
```

```bash
git -C my-rce-hub add -A && git -C my-rce-hub commit -m "Start RCE hub" && git -C my-rce-hub push -u origin HEAD
```

No command line? On GitHub, create a new private repo, then use **Add file → Upload files** and drag in the contents of `hub-template/`.

Then fill in `me/about.md` and `me/preferences.md` with a few lines each. Everything else fills itself as you work.

## 2. Fill in the config

Copy the example into the skill folder and edit it:

```bash
cp open-rce/rce.config.example.yaml open-rce/engine/skills/rce/rce.config.yaml
```

Set at least:

| Key | Set it to |
|---|---|
| `owner` | Your GitHub username |
| `hub` | Your hub repo name (for example `my-rce-hub`) |
| `user_name` | What the AI should call you |
| `timezone` | For example `UTC` or `America/New_York` |

The config holds no secrets, and `.gitignore` keeps it out of this repo. Restricted repos go in the config by alias only; put their real names in your hub's `AGENTS.md`, section "Private names".

## 3. Install it in each tool

Every tool needs read and write access to your hub. RCE never asks for a token in chat.

### Claude.ai and Cowork

1. Connect GitHub: **Settings → Connectors → GitHub**, and give it access to your hub repo.
2. Zip the skill folder with your filled-in config inside it:
   ```bash
   (cd open-rce/engine/skills && zip -r rce.zip rce)
   ```
3. Upload it: **Settings → Capabilities → Skills → Upload skill**, and pick `rce.zip`. Code execution must be on.

### Claude Code

Install the plugin from your local copy, which holds your config:

```
/plugin marketplace add ./open-rce
```

```
/plugin install rce@open-rce
```

Restart Claude Code. Each session starts with "RCE is ON". Saves use your `gh` login. To update later, `git pull` in `open-rce` and run `/plugin marketplace update open-rce`; your config is untouched.

### ChatGPT

1. Connect GitHub in ChatGPT's connector settings and give it access to your hub.
2. **Try the skill first.** The ChatGPT desktop app sometimes recognizes Anthropic-style skills. Add the same `rce.zip` from the Claude.ai steps (with your config inside), open a new chat and type `/rce`. If you get the status line, you're done.
3. **If it doesn't pick up the skill,** use a Project (or a custom GPT) instead: paste the whole of `engine/AGENTS.md` into the instructions, followed by your config values.

If the connector can only read, RCE still loads your context. Saves come back as `⚠ RCE push failed` bullets you can paste into a Claude chat with `/rce sync`.

### Tools without skills

Paste `engine/AGENTS.md` and your config values into the tool's instructions or first message, and give it GitHub access to your hub if it can take it.

## 4. First run

In any installed tool:

1. Type `/rce`. You should see something like `RCE: ON · saves to my-rce-hub · write access OK`.
2. Share one fact, for example "I prefer short answers with examples."
3. Check that the reply ends with a save line, for example `↻ gh-rce › me › preferences`, and that the bullet appears in your hub under `me/updates/`.

No save line, or `⚠ RCE push failed`? See "Troubleshooting" below.

## 5. Optional

- **A restricted repo.** For context you only want loaded on request (for example coaching notes): create another private repo, add `restricted: [{alias: coach}]` to the config, add a row to the "Private names" table in your hub's `AGENTS.md`, and load it with `/rce open coach`.
- **A public profile.** Create a repo, set `profile` in the config, and edit `public/fields.yaml` in your hub to choose which sections of `me/about.md` may be published. Private files are never copied there.
- **Newer rules from GitHub.** Set `rules_repo` to a repo holding `engine/skills/rce/reference/`, and the skill reads the rules from there instead of its local copy.

## Troubleshooting

| You see | Fix |
|---|---|
| "No rce.config.yaml" | The config isn't inside `engine/skills/rce/`. Redo step 2, then re-zip or reinstall |
| `⚠ RCE push failed: no write access` | Give the tool's GitHub connector write access to the hub repo |
| Saves land in `inbox-unsorted/` | Add the project to `manifest.yaml`, or let RCE register it when you name it, then run `/rce sort` |
| Wrong owner or hub | Fix the config and reinstall the skill in that tool |
