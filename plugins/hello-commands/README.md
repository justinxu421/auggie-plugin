# Hello Commands Plugin

A collection of example slash commands demonstrating Claude Code plugin command capabilities.

## Installation

```bash
/plugin install hello-commands@auggie-plugin-marketplace
```

## Commands

### `/hello`

A simple greeting command that introduces the AI assistant.

**Usage:**
```
/hello
```

**Features:**
- Warm, friendly greeting
- Brief capability introduction
- Prompts user for how to help

---

### `/summarize-file`

Quickly understand any file's purpose and structure.

**Usage:**
```
/summarize-file path/to/file.js
```

**Features:**
- Reads and analyzes the specified file
- Provides structured summary:
  - Purpose
  - Key components
  - Dependencies
  - Usage patterns

**Allowed Tools:** `Read`

---

### `/quick-review`

Perform a quick code review of recent git changes.

**Usage:**
```
/quick-review
```

**Features:**
- Automatically pulls recent git changes
- Reviews for:
  - Correctness issues
  - Style consistency
  - Simplification opportunities
  - Security concerns
- Provides actionable feedback

**Allowed Tools:** `Bash(git diff:*)`, `Bash(git status:*)`, `Bash(git log:*)`

## Command File Structure

Commands are defined as markdown files with YAML frontmatter:

```markdown
---
description: Brief description shown in command list
allowed-tools: Tool1, Tool2
---

## Context
Dynamic context using !`command` syntax

## Your task
Instructions for the AI
```

## Development

To modify or add commands:

1. Create a new `.md` file in the `commands/` directory
2. Add YAML frontmatter with at least a `description`
3. Write the command instructions in markdown
4. Test with `/your-command-name`

## License

MIT

