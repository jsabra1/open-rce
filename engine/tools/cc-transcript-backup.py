#!/usr/bin/env python3
"""Back up a Claude Code session transcript to the user's RCE hub.

Runs from the plugin's hooks (SessionEnd and PreCompact). Reads the hook's JSON
on stdin, turns the session's .jsonl transcript into Markdown (the user's
messages and Claude's text replies only; tool calls and tool output are left
out), masks anything that looks like a secret, writes it to
  <hub>/inbox-unsorted/chats/claude-code/<start-date>_<session-id-8>_<title>.md
and commits and pushes only that file. The file is rewritten on each run, so
it always holds the whole session as far as the local transcript has it.

Settings come from the pointer ~/.config/rce/rce.config.yaml:
  owner, hub              required; no pointer means the hook does nothing
  transcript_backup       optional; false turns this hook off
The hub is cloned once to ~/.cache/rce/<owner>__<hub>, a clone only this hook
uses, so a push never carries anything but the backup.
The hub must be private; a public repo is never written to.

Never blocks the session: every error goes to ~/.cache/rce/transcript-backup.log
and the script exits 0.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys

POINTER = os.path.expanduser(os.environ.get("RCE_POINTER", "~/.config/rce/rce.config.yaml"))
CACHE = os.path.expanduser(os.environ.get("RCE_CACHE", "~/.cache/rce"))
LOG = os.path.join(CACHE, "transcript-backup.log")
OUT_DIR = "inbox-unsorted/chats/claude-code"

SECRET = re.compile(
    r"(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}"
    r"|xox[abprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----"
    r"|(?i:(?:password|passwd|api[_ -]?key|secret|token)\s*[:=]\s*\S{6,})"
    r"|\b(?:\d[ -]?){13,19}\b"
    r"|\b[A-Z]{2}\d{2}(?:[ ]?[A-Z0-9]{4}){3,7}\b)"
)


def log(msg):
    os.makedirs(CACHE, exist_ok=True)
    with open(LOG, "a") as f:
        f.write(f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M:%S} {msg}\n")


def read_yaml_keys(path):
    """Top-level 'key: value' pairs only; enough for the pointer and config."""
    keys = {}
    if not os.path.exists(path):
        return keys
    with open(path) as f:
        for line in f:
            m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(?:#.*)?$", line)
            if m:
                keys[m.group(1)] = m.group(2).strip().strip("\"'")
    return keys


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n\n".join(
        b.get("text", "") for b in content or []
        if isinstance(b, dict) and b.get("type") == "text" and b.get("text", "").strip()
    )


def slug(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return "-".join(s.split("-")[:6])[:60] or "session"


def run(*cmd, cwd=None):
    return subprocess.run(list(cmd), cwd=cwd, capture_output=True, text=True, timeout=90)


def hub_clone(owner, hub):
    path = os.path.join(CACHE, f"{owner}__{hub}")
    if not os.path.isdir(os.path.join(path, ".git")):
        os.makedirs(CACHE, exist_ok=True)
        r = run("git", "clone", "-q", "--depth", "50", f"https://github.com/{owner}/{hub}.git", path)
        if r.returncode:
            log(f"clone failed: {r.stderr.strip()}")
            return None
    return path


def is_private(owner, hub):
    r = run("gh", "api", f"repos/{owner}/{hub}", "-q", ".private")
    return r.returncode == 0 and r.stdout.strip() == "true"


def main():
    pointer = read_yaml_keys(POINTER)
    owner, hub = pointer.get("owner"), pointer.get("hub")
    if not owner or not hub:
        return  # RCE not set up in Claude Code: do nothing
    if pointer.get("transcript_backup", "true").lower() == "false":
        return
    hook = json.load(sys.stdin)
    path = hook.get("transcript_path")
    sid = (hook.get("session_id") or "unknown")[:8]
    event = hook.get("hook_event_name", "manual")
    if not path or not os.path.exists(path):
        log(f"{sid} {event}: no transcript at {path}")
        return
    if not is_private(owner, hub):
        log(f"{sid} {event}: {owner}/{hub} is not private or not reachable; nothing written")
        return
    repo = hub_clone(owner, hub)
    if not repo:
        log(f"{sid} {event}: no clone of {owner}/{hub}")
        return
    config = read_yaml_keys(os.path.join(repo, "rce.config.yaml"))
    user = config.get("user_name") or "User"
    if config.get("enabled", "true").lower() == "false":
        log(f"{sid} {event}: RCE paused in rce.config.yaml")
        return

    turns, start, title = [], None, None
    with open(path) as f:
        for line in f:
            try:
                e = json.loads(line)
            except ValueError:
                continue
            if e.get("type") == "summary" and e.get("summary") and not title:
                title = e["summary"]
            if e.get("type") not in ("user", "assistant") or e.get("isMeta"):
                continue
            t = SECRET.sub("[secret omitted]", text_of((e.get("message") or {}).get("content"))).strip()
            if not t or t.startswith("<command-") or t.startswith("<local-command"):
                continue
            ts = (e.get("timestamp") or "")[:16].replace("T", " ")
            start = start or ts[:10]
            if e["type"] == "user" and not title:
                title = t.splitlines()[0][:80]
            who = user if e["type"] == "user" else "Claude"
            turns.append(f"## {who} ({ts} UTC)\n\n{t}\n")
    if not turns:
        log(f"{sid} {event}: no text turns")
        return
    start = start or f"{dt.date.today()}"
    name = f"{start}_{sid}_{slug(title or 'session')}.md"
    body = (
        f"# {title or 'Claude Code session'}\n\n"
        f"**Tool:** Claude Code · **Session:** {hook.get('session_id')} · "
        f"**Started:** {start} UTC · **Saved:** {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC ({event})\n\n"
        f"{user}'s messages and Claude's text replies, verbatim; tool calls and tool output left out. "
        "Secrets masked as [secret omitted].\n\n" + "\n".join(turns)
    )
    body = SECRET.sub("[secret omitted]", body)
    rel = f"{OUT_DIR}/{name}"

    run("git", "pull", "-q", "--rebase", "--autostash", cwd=repo)
    os.makedirs(os.path.join(repo, OUT_DIR), exist_ok=True)
    with open(os.path.join(repo, rel), "w") as f:
        f.write(body)
    run("git", "add", "--", rel, cwd=repo)
    if run("git", "diff", "--cached", "--quiet", "--", rel, cwd=repo).returncode == 0:
        log(f"{sid} {event}: unchanged")
        return
    r = run("git", "commit", "-q", "-m", f"rce: claude-code transcript {sid} ({event})", "--", rel, cwd=repo)
    if r.returncode:
        log(f"{sid} {event}: commit failed: {r.stderr.strip()}")
        return
    p = run("git", "push", "-q", cwd=repo)
    log(f"{sid} {event}: saved {rel} " + ("pushed" if p.returncode == 0 else "push failed: " + p.stderr.strip()))


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:  # never break the session
        try:
            log(f"error: {ex!r}")
        except Exception:
            pass
    sys.exit(0)
