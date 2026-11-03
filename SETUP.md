# Set up RCE

About 5 minutes. You install one plugin and type `/rcx setup`; Claude creates your private hub and does the rest.

## Before you start

> **You need a GitHub connector that can write.** RCE saves by writing files to your hub, so every tool needs a GitHub connection with **write** access to it. It doesn't need to create repos: if it can't, the AI asks you to create one empty private repo by hand, which takes a minute.
>
> - **Claude Code with the GitHub CLI (`gh`):** does everything, including creating the hub and saving binary files.
> - **Claude.ai with a GitHub connector:** reads and writes text files, but can't create repos: the GitHub App behind it has no repo-creation permission, and Claude's "Always allow" setting can't add one. It returns `403`, so you create the hub repo by hand when the AI asks (it gives you a prefilled link). PDFs and images are saved as `binary pending` cards; `/rcx files` in Claude Code uploads them later.
> - **Not confirmed:** ChatGPT's GitHub connector. Some GitHub connectors only read.
> - **If your connector only reads:** RCE still loads your context, but saves don't land. They come back as `⚠ RCE push failed` bullets to paste later.

Connect GitHub first:
- **Claude.ai and Cowork:** Settings → Connectors → add a GitHub connector with write access.
- **Claude Code:** `gh auth login` once.
- **ChatGPT:** connect GitHub in its connector settings.

## 1. Install the plugin

| Tool | How |
|---|---|
| Claude.ai and Cowork | **Customize → Plugins**: find **Recursive Context Engine** in the directory (once it's listed), or add the marketplace `jsabra1/open-rce`, then install. It also reaches Claude Code on your account |
| Claude Code | `claude plugin marketplace add jsabra1/open-rce`, then `claude plugin install recursive-context-engine@open-rce`, then start a new session |
| ChatGPT and other tools | No plugin. Paste the prompt below into a new chat instead |

```
Set up RCE for me by following https://github.com/jsabra1/open-rce/blob/main/BOOTSTRAP.md
```

## 2. Type `/rcx setup`

In a new chat, type `/rcx setup`. The AI will:
1. Check your GitHub access and confirm your username.
2. Ask your name, your timezone and a name for your hub (default `my-rce-hub`).
3. Ask your OK, then create the hub as a **private** repo (in Claude.ai it asks you to create the empty repo on github.com, since the connector can't), and fill it from the starter template, with your settings in `rce.config.yaml`.
4. Run a first test: show the status line and save one fact about you.

**More tools:** install the plugin (or paste the prompt) in each one. RCE finds your existing hub by itself.

## 3. Check it works

1. Type `/rcx`. You should see something like `RCE: ON · saves to my-rce-hub · write access OK`.
2. Share one fact, for example "I prefer short answers with examples."
3. The reply should end with a save line, for example `↻ gh-rce › me › preferences`, and the bullet appears in your hub under `me/updates/`.

## Optional

Ask the AI in any RCE chat to do this for you, or edit `rce.config.yaml` in your hub:

- **A public profile:** set `profile`, and choose the allowed sections in `public/fields.yaml`. Private files are never copied there.
- **Skip the hub search:** in Claude.ai, add `My RCE hub is <owner>/<hub>.` to Settings → Profile. Claude Code keeps it in `~/.config/rce/rce.config.yaml`.

## Manual setup (no write-capable connector)

1. On github.com, create a new **private** repo (for example `my-rce-hub`) and upload the contents of `engine/skills/rcx/assets/hub-template/` from this repo.
2. Copy `engine/skills/rcx/assets/rce.config.example.yaml` into the hub as `rce.config.yaml` and set `owner`, `hub`, `user_name` and `timezone`.
3. Install the plugin as in step 1. In tools without plugins, paste `engine/AGENTS.md` into the instructions, with your owner and hub.

## Troubleshooting

| You see | Fix |
|---|---|
| "No hub found" or an offer to run `/rcx setup` | RCE couldn't find a private repo with `rce.config.yaml` at its root. Run `/rcx setup`; it skips the parts already done |
| `⚠ RCE push failed: no write access` | Give the tool's GitHub connector write access to the hub repo |
| A file saved as `binary pending` | Open Claude Code and type `/rcx files`, or upload the file on github.com at the path on the card |
| Saves land in `inbox-unsorted/` | Add the project to `manifest.yaml`, or let RCE register it when you name it, then run `/rcx sort` |
| Wrong hub | Add `My RCE hub is <owner>/<hub>.` to the tool's instructions, or fix `~/.config/rce/rce.config.yaml` in Claude Code |
