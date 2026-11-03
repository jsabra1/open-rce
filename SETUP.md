# Set up RCE

About 5 minutes. You type one sentence into a chat; the AI creates your private hub and installs RCE.

## Before you start

> **You need a GitHub connector that can write.** RCE saves by writing files to your hub, so every tool needs a GitHub connection with **write** access to it. It doesn't need to create repos: if it can't, the AI asks you to create one empty private repo by hand, which takes a minute.
>
> - **Claude Code with the GitHub CLI (`gh`):** does everything, including creating the hub.
> - **Claude.ai with a GitHub connector:** reads and writes files, but can't create repos (it returns `403`), so you create the hub repo by hand when the AI asks.
> - **Not confirmed:** ChatGPT's GitHub connector. Some GitHub connectors only read.
> - **If your connector only reads:** RCE still loads your context, but saves don't land. They come back as `⚠ RCE push failed` bullets to paste later, and you create the hub repo by hand on github.com.

Connect GitHub first:
- **Claude.ai and Cowork:** Settings → Connectors → add a GitHub connector with write access.
- **Claude Code:** `gh auth login` once.
- **ChatGPT:** connect GitHub in its connector settings.

## 1. Paste the setup prompt

Open a new chat in Claude.ai, Cowork or Claude Code and paste:

```
Set up RCE for me by following https://github.com/jsabra1/open-rce/blob/main/BOOTSTRAP.md
```

The AI will:
1. Check your GitHub access and confirm your username.
2. Ask your name, your timezone and a name for your hub (default `my-rce-hub`).
3. Ask your OK, then create the hub as a **private** repo (in Claude.ai it asks you to create the empty repo on github.com, since the connector can't), and fill it from `hub-template/`, with your settings in `rce.config.yaml`.
4. Install RCE in the tool you're using (see step 2).
5. Run a first test: show the status line and save one fact about you.

## 2. The one thing you may do by hand

| Tool | What happens |
|---|---|
| Claude Code | The AI installs the plugin and writes a small pointer file to `~/.config/rce/`. Start a new session; it opens with "RCE is ON" |
| Claude.ai and Cowork | The AI gives you `rce.zip`. Upload it in **Settings → Capabilities → Skills → Upload skill** (code execution must be on), then open a new chat |
| ChatGPT | The AI first tries the skill (the ChatGPT desktop app sometimes recognizes Anthropic-style skills). If that doesn't work, it gives you three lines to paste into custom instructions or a Project |

**More tools:** paste the same setup prompt in each one. The AI finds your existing hub and only does the install.

## 3. Check it works

1. Type `/rce`. You should see something like `RCE: ON · saves to my-rce-hub · write access OK`.
2. Share one fact, for example "I prefer short answers with examples."
3. The reply should end with a save line, for example `↻ gh-rce › me › preferences`, and the bullet appears in your hub under `me/updates/`.

## Optional

Ask the AI in any RCE chat to do this for you, or edit `rce.config.yaml` in your hub:

- **A public profile:** set `profile`, and choose the allowed sections in `public/fields.yaml`. Private files are never copied there.

## Manual setup (no write-capable connector)

1. On github.com, create a new **private** repo (for example `my-rce-hub`) and upload the contents of `hub-template/` from this repo.
2. Copy `rce.config.example.yaml` into the hub as `rce.config.yaml` and set `owner`, `hub`, `user_name` and `timezone`.
3. Install:
   - **Claude Code:** `claude plugin marketplace add jsabra1/open-rce`, then `claude plugin install rce@open-rce`, then create `~/.config/rce/rce.config.yaml` with two lines: `owner: <you>` and `hub: <hub>`.
   - **Claude.ai:** download `engine/skills/rce/`, add the same two-line `rce.config.yaml` inside it, zip the folder and upload it as above.
   - **Other tools:** paste `engine/AGENTS.md` into the instructions, with your owner and hub.

## Troubleshooting

| You see | Fix |
|---|---|
| "Run the setup prompt" | The tool can't find its pointer file. Paste the setup prompt again; it skips the parts already done |
| `⚠ RCE push failed: no write access` | Give the tool's GitHub connector write access to the hub repo |
| Saves land in `inbox-unsorted/` | Add the project to `manifest.yaml`, or let RCE register it when you name it, then run `/rce sort` |
| Wrong owner or hub | Paste the setup prompt again in that tool and give the right hub name |
