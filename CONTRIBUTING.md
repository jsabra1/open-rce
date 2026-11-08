# Contributing

Thanks for helping. Issues and pull requests are welcome.

- **Rules live in `engine/skills/rce/reference/`.** Keep `engine/AGENTS.md` and `engine/skills/rce/SKILL.md` in step with any rule you change.
- **No personal data.** Use placeholders (`<owner>`, `<hub>`, "the user") and neutral examples (`projects/acme`). Never commit a filled-in `rce.config.yaml` or anything from a real hub.
- **Write-once saves.** Changes must keep the write-once rules (`capture.md`): saves create new files, never rewrite history, never restore removed content.
- **Test it.** Try the change against a throwaway private hub in at least one tool, and say which in the pull request.
- **Changelog.** Add a line to `CHANGELOG.md` and bump `version` in `engine/.claude-plugin/plugin.json`.
- **Starter hub.** After changing `engine/skills/rce/assets/hub-template/`, run `scripts/sync-hub-template.sh` so the public template repo `jsabra1/rce-hub-template` matches.

## Releasing

Users on `rules: stable` read the rules from the newest release, so a release is what ships a rule change.

1. On `main`, set the same version in `engine/.claude-plugin/plugin.json` and the `Engine:` line at the top of `engine/skills/rce/SKILL.md`.
2. Move the `Unreleased` entries in `CHANGELOG.md` under the new version and date.
3. Tag and publish: `git tag vX.Y.Z && git push origin vX.Y.Z`, then `gh release create vX.Y.Z --notes-file <the CHANGELOG section>`.
4. If the starter hub changed, run `scripts/sync-hub-template.sh`.
5. Never move or delete a published tag: users may pin it.

Version numbers: MAJOR for breaking changes (commands, file layout, config schema), MINOR for new features, PATCH for fixes and wording.
