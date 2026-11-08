---
name: "health-checkins"
description: "Daily health check-ins: one short structured entry per day, private"
triggers: ["chat title starts with a prefix in chat_patterns marked health", "the user says check-in, daily check-in or health check-in"]
private: true
saves_to: "modules/health-checkins/"
---

# Health check-ins

A short daily check-in the user can do by text or voice. Everything it saves is private.

## When it runs

When a trigger matches. Recurring check-in chats should also be listed in `chat_patterns`, so their transcript is checkpointed every session.

## The check-in

Ask one question at a time, briefly, and accept short answers. Skip any the user skips:
1. Sleep: hours and quality (1 to 5)
2. Energy and mood (1 to 5 each)
3. Body: symptoms, pain, medication taken
4. Movement and food, in a line
5. Anything else worth noting

Don't give medical advice. If the user mentions something urgent, say plainly that they should contact a doctor or emergency services.

## Saving (write-once)

One new file per check-in: `modules/health-checkins/YYYY-MM/YYYY-MM-DD_HHMMSS_checkin.md`:

```markdown
<!-- rce entry YYYY-MM-DD HH:MM:SS <tz> · <tool> · <chat title> -->
- date: YYYY-MM-DD
- sleep: <hours>, quality <n>/5
- energy: <n>/5 · mood: <n>/5
- body: <text>
- movement and food: <text>
- notes: <text>
```

A second check-in on the same day is a second file; never edit the first. Facts that change the user's overall health picture also get a `[health]` entry in `me/updates/` (`capture.md`).

## Loading

Read the last 7 check-ins only when the user asks about trends or a check-in starts. Never load them into other chats.

Save line: `↻ gh-rce › modules/health-checkins › checkin`.
