# Contributing

Thanks for helping. Issues and pull requests are welcome.

- **Rules live in `engine/skills/rce/reference/`.** Keep `engine/AGENTS.md` and `engine/skills/rce/SKILL.md` in step with any rule you change.
- **No personal data.** Use placeholders (`<owner>`, `<hub>`, "the user") and neutral examples (`projects/acme`). Never commit a filled-in `rce.config.yaml` or anything from a real hub.
- **Small, safe saves.** Changes must keep the small-file rules: no rewriting whole history files, no deleting, no restoring removed content.
- **Test it.** Try the change against a throwaway private hub in at least one tool, and say which in the pull request.
- **Changelog.** Add a line to `CHANGELOG.md` and bump `version` in `engine/.claude-plugin/plugin.json`.
