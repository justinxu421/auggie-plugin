# Auggie Plugin Marketplace

An example Claude Code plugin marketplace demonstrating various plugin capabilities including commands, hooks, agents, MCP servers, and rules.

## Installation

Add this marketplace to Claude Code:

```bash
/plugin marketplace add justinxu421/auggie-plugin
```

## Available Plugins

### 1. hello-commands
Example slash commands for greeting users and summarizing files.

**Commands:**
- `/hello` - Say hello and introduce yourself
- `/summarize-file <path>` - Summarize a file's contents and purpose
- `/quick-review` - Quick code review of recent changes

### 2. code-guard
Security-focused hooks that warn about potentially dangerous code patterns.

**Features:**
- Pre-tool hooks that check for dangerous patterns (eval, exec, SQL injection, XSS)
- Post-tool hooks that log file changes
- Blocks high-severity security issues

### 3. task-agent
Autonomous agents for breaking down and managing development tasks.

**Agents:**
- `task-planner` - Breaks down complex features into actionable tasks
- `code-reviewer` - Performs thorough code reviews with structured feedback

### 4. time-server
MCP server providing time and date utilities.

**Tools:**
- `get_current_time` - Get current date and time
- `format_date` - Format a date string
- `add_days` - Add/subtract days from a date
- `days_between` - Calculate days between two dates

### 5. dev-rules
Development best practices and coding standards as rules.

**Rules:**
- Code style guidelines
- Git workflow guidelines
- Security best practices

## Augment Subagents

This repository also includes Augment-compatible subagents in `.augment/agents/`:

| Agent | Description | Color |
|-------|-------------|-------|
| `code-review` | Reviews staged changes for bugs, security, and documentation issues | purple |
| `test-generation` | Generates and runs tests for new or modified code | green |
| `task-planner` | Breaks down complex features into actionable tasks | blue |
| `api-designer` | Designs REST/GraphQL APIs and OpenAPI specs | cyan |

**Usage:**
```
> Use the code-review agent to review my staged changes
> Use the task-planner agent to break down this feature
```

## Plugin Structure

```
.augment/
  agents/                   # Augment-compatible subagents
    code-review.md
    test-generation.md
    task-planner.md
    api-designer.md

.augment-plugin/
  marketplace.json          # Marketplace metadata and plugin listings

plugins/
  hello-commands/           # Command examples
    .claude-plugin/
      plugin.json
    commands/
      hello.md
      summarize-file.md
      quick-review.md

  code-guard/              # Hook examples
    .claude-plugin/
      plugin.json
    hooks/
      hooks.json
      security_check.py
      log_changes.py

  task-agent/              # Agent examples
    .claude-plugin/
      plugin.json
    agents/
      task-planner.md
      code-reviewer.md

  time-server/             # MCP server examples
    .claude-plugin/
      plugin.json
    mcp/
      time_server.py

  dev-rules/               # Rules/skills examples
    .claude-plugin/
      plugin.json
    rules/
      code-style.md
      git-workflow.md
      security-practices.md
```

## License

MIT
