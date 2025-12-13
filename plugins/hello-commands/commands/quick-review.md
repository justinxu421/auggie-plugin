---
description: Quick code review of recent changes
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(git log:*)
---

## Context

- Current git status: !`git status`
- Recent changes: !`git diff HEAD~1`
- Last commit: !`git log -1 --pretty=format:"%h - %s (%an, %ar)"`

## Your task

Perform a quick code review of the recent changes shown above. Focus on:

1. **Correctness**: Are there any obvious bugs or issues?
2. **Style**: Does the code follow common conventions?
3. **Simplicity**: Could anything be simplified?
4. **Security**: Are there any security concerns?

Provide actionable feedback in a friendly, constructive manner. If everything looks good, say so!

