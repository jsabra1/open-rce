# Packet template

Copy this structure exactly. Keep every heading. Write "None" when a section is empty.

```markdown
# Handoff_<Topic> <code>

## References
- <every doc, artifact, framework, repo, page mentioned, as links>

**Code:** <code> · **Created:** <YYYY-MM-DD HH:MM <tz>> · **Status:** Open
**Scope:** <full chat | last day (since YYYY-MM-DD HH:MM <tz>)>
**From:** <tool + chat or session name>
**To:** <tool + chat or session name, or "new session">

## 1. TL;DR
Three to five lines: what this is, where it stands, what the receiver does first.

## 2. Goal
What the user is trying to achieve, in their words where possible, and why.

## 3. Background
People with roles, project, prior work this builds on.

## 4. Conversation narrative
Chronological and complete. One bullet per meaningful turn or phase.

## 5. Decisions made
- <decision>, because <reason>. Rejected: <alternatives and why>.

## 6. The user's instructions, verbatim
Quotes that must be kept exactly.

## 7. Current state
- Done:
- In progress (and how far):
- Not started:

## 8. Handles
URLs, IDs, file paths, repo/branch/commit, task IDs, email subjects.

## 9. Next steps
1. <the very next action>

## 10. Open questions for the user
- <question> (blocking / non-blocking)

## 11. Constraints and guardrails
What must not change, what needs the user's approval.

## 12. Rollback
How to undo what the sending session changed.

## 13. Target notes
What the receiving tool needs (repo, connectors, inline file content for tools without file access).

## 14. Gaps
What the sender could not see or verify.

## Log
- <date>: Created by <session>.
```
