# Modules (`modules.md`)

A module is an optional, self-contained piece of RCE for one recurring use, such as daily health check-ins. Core RCE (capture, load, sync, handoffs, transcripts, sort) never depends on one. Modules are off unless listed under `modules:` in `rce.config.yaml`.

## How a module works

- The plugin ships module templates in `modules/<name>/MODULE.md` next to the skill. The user's own modules may live only in their hub.
- Turning one on: add its name to `modules:` in the config. On its first use, copy `MODULE.md` into the hub at `modules/<name>/MODULE.md` (one commit), so every tool reads the same rules. The hub copy wins over the plugin's.
- At the start of a chat, read `MODULE.md` only for modules that are on and whose trigger matches the chat (its `triggers:` header). Never load a module's data unless its rules say so.
- While a module's trigger matches, its save rules come first; anything it doesn't cover is saved by `capture.md` as usual. Saves stay write-once (`capture.md`).
- A module marked `private: true` is always private (`config.md`, "Privacy defaults").

## `MODULE.md` format

```markdown
---
name: "health-checkins"
description: "Daily health check-ins: one short entry per day"
triggers: ["chat title starts with VC_Health", "user says check-in"]
private: true
saves_to: "modules/health-checkins/"
---

# <Name>

What it does, when it runs, what it asks, and exactly where and how each save is written.
```

## Turning modules off

Remove the name from `modules:`. Its files stay in the hub; nothing is deleted.
