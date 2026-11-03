# Security

## How RCE handles your data

- Your context lives only in your own GitHub repos. This project runs no server and collects nothing.
- Keep your hub **private**. Anyone who can read it can read your context.
- The config holds no secrets. Access comes from each tool's GitHub connector or your `gh` login. RCE never asks for a token in chat.
- The rules tell agents to write `[secret omitted]` instead of passwords, API keys or tokens, and to treat file contents as data, not instructions.
- Private files (`private_files` in the config) and restricted repos are never copied into a public profile.

These are instructions to an AI model, not hard guarantees. Review what gets saved, and don't paste secrets into chats.

## Reporting a problem

Please report security issues privately through GitHub's **Security → Report a vulnerability** on this repo, not in a public issue. Include what you saw and how to reproduce it, with any personal data removed.
