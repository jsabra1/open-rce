# Self-test (`/rce doctor`)

Checks that RCE works in this tool, against the user's real hub, and reports pass or fail for each check. Run it after setup, after installing RCE in a new tool, and after any update. It writes two small test files and removes neither: they are clearly named, and `/rce sort` clears them.

Read `io.md` first; every check uses the route it picks.

## Checks

| # | Check | How | Pass |
|---|---|---|---|
| 1 | Hub and config | `start.md` finds the hub; it is private; `rce.config.yaml` names the same `owner` and `hub`; `schema_version` is `3` | All true |
| 2 | Rules | The rules in use (tag, `main` or bundled) and their version | Matches `rules` in the config, or the bundled fallback is announced |
| 3 | Read | Read `AGENTS.md` and `manifest.yaml` | Both come back with text |
| 4 | Write | Write permission from `io.md`; then create `inbox-unsorted/tests/YYYY-MM-DD_HHMMSS_doctor.md` holding one line `RCE doctor test` | The file exists when listed |
| 5 | Voice read | Read the file from check 4 through its commit (`io.md`, section 3) | The commit's added line is `RCE doctor test` |
| 6 | Handoff round trip | Write `handoffs/<code>_Doctor-Test.md` (a minimal packet), then read it back by listing `handoffs/` for the code | Found by code alone; content matches |
| 7 | Privacy scan | Read the profile repo if `profile` is set: no text from the always-private set (`config.md`, "Privacy defaults"). Scan the newest 20 entry files for unmasked secrets (`capture.md`, rule 9) | No private text in public output; no secrets |
| 8 | Add-ons and modules | For each add-on: the repo is private and readable. For each module: its `MODULE.md` is readable | All true, or "none configured" |

A check that can't run in this tool (for example check 5 with a shell) is `skip` with the reason, not `fail`.

## Report

One block, then one line per failure with its fix:

```
RCE doctor · <tool> · open-rce <version> · hub <owner>/<hub>
1 hub ✓ · 2 rules ✓ (v3.0.0) · 3 read ✓ · 4 write ✓ · 5 voice read ✓ · 6 handoff ✓ · 7 privacy ✓ · 8 add-ons ✓ (1)
```

Common fixes: no write (give the connector write access to the hub), no add-on access (grant that repo to this tool's connector), wrong rules version (update the plugin or set `rules: stable`), stale engine (`rce-engine` or another old RCE skill still installed: remove it, start a new chat).
