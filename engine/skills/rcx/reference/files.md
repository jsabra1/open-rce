# Files (PDFs, images, other binaries)

The hub keeps the original file, not just a description of it. A text version can sit next to it, never in its place.

## Where files go

| What | Path |
|---|---|
| A file for a project | `projects/<name>/docs/<file>` |
| A file about the user | `me/docs/<file>` |
| A file you can't place | `inbox-unsorted/files/<file>` |

- Keep the original name, lowercased, with spaces turned into hyphens and only letters, digits, hyphens, underscores and dots. Prefix the date when the name says nothing about it: `2026-11-03_contract.pdf`.
- Never overwrite a file with the same name. Add `-2`, `-3` before the extension.
- Next to each file, write a short card `<file>.md` (for example `contract.pdf.md`): what it is, where it came from, the date, its size, and a one-line summary. `/rcx load` reads cards, not the files.
- If the user wants the text too (or the file is a document Claude will need to read often), save the extracted text as `<file>.txt` beside it.

## How to write them

Use the first route this session has:

The routes are the ones in `io.md`; binaries need one that can carry bytes:

1. **A shell with `git` or `gh`** (Claude Code, Cowork on your computer): clone the hub (or use an existing clone), copy the file in, then one commit and push:
   ```bash
   git clone --depth 1 https://github.com/<owner>/<hub>.git /tmp/rce-hub
   ```
   ```bash
   cp "<local file>" /tmp/rce-hub/projects/<name>/docs/<file>
   ```
   ```bash
   git -C /tmp/rce-hub add -A && git -C /tmp/rce-hub commit -m "rce: projects/<name>: add <file>" && git -C /tmp/rce-hub push
   ```
2. **A GitHub connector that accepts base64 file content:** write the file base64-encoded, plus its card, in one commit.
3. **Neither** (most chat connectors only write text): write the card only, with the line `Status: binary pending`, and tell the user in one line how to finish: open Claude Code with the file and say `/rcx files`, or upload it at `https://github.com/<owner>/<hub>/upload/main/<folder>`. Never write a placeholder or a text conversion as if it were the file.

## Limits

- GitHub warns above 50 MB and refuses files above 100 MB. Above 50 MB, ask before saving; offer to keep it elsewhere and save a card with the link instead.
- Never save files that hold passwords, keys or tokens. Never copy a file from a path in `private_files` into `<profile>`.

## `/rcx files`

1. Find every card in the hub with `Status: binary pending`.
2. For each, ask the user for the local file (or use one already in this chat), save it with route 1 or 2, and change the card's line to `Status: saved YYYY-MM-DD`. One commit.
3. Report: files saved, files still pending.

## Save line

Use the file type `docs`: `↻ gh-rce › projects/acme › docs`.
