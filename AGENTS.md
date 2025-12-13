# Agent Instructions

This file provides instructions for AI agents working with this codebase.

## Project Overview

This is an example plugin marketplace demonstrating various plugin capabilities for both Claude Code and Augment Code. The repository contains:
- 5 example Claude Code plugins showcasing commands, hooks, agents, MCP servers, and rules
- 4 Augment-compatible subagents for common development tasks

## Repository Structure

```
.augment/
  agents/                 # Augment-compatible subagents
    code-review.md        # Code review agent
    test-generation.md    # Test generation agent
    task-planner.md       # Task planning agent
    api-designer.md       # API design agent

.augment-plugin/          # Marketplace metadata
  marketplace.json        # Plugin listings and marketplace config

plugins/                  # Individual Claude Code plugins
  hello-commands/         # Slash command examples
  code-guard/            # Hook examples (security validation)
  task-agent/            # Autonomous agent examples
  time-server/           # MCP server example
  dev-rules/             # Rules/skills examples
```

## Augment Subagent Configuration

Augment subagents use a simpler frontmatter format:

```yaml
---
name: agent-name          # Required: Agent identifier
description: Description  # Optional: What the agent does
model: claude-sonnet-4-5  # Optional: Model to use (default: CLI default)
color: purple             # Optional: ANSI color for CLI output
---

Agent prompt content here...
```

### Supported Colors
Valid ANSI color names: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`

### File Locations
- **User-level**: `~/.augment/agents/` - Available in all workspaces
- **Workspace-level**: `./.augment/agents/` - Available in current workspace only

## Working with This Codebase

### Adding a New Plugin

1. Create a new directory under `plugins/`
2. Add `.claude-plugin/plugin.json` with plugin metadata
3. Add your plugin components (commands/, hooks/, agents/, mcp/, rules/)
4. Update `.claude-plugin/marketplace.json` to include your plugin

### Plugin Component Guidelines

**Commands** (`commands/*.md`):
- Use YAML frontmatter for metadata
- Include `description` for the command
- Use `allowed-tools` to restrict tool access
- Use `!` backticks for dynamic context (e.g., `!`git status``)

**Hooks** (`hooks/hooks.json` + scripts):
- Define hooks in `hooks.json`
- Use `${CLAUDE_PLUGIN_ROOT}` for portable paths
- PreToolUse hooks exit 2 to block, 0 to allow
- PostToolUse hooks should always exit 0

**Agents** (`agents/*.md`):
- Include `name`, `description` with examples in frontmatter
- Set appropriate `model`, `color`, and `tools`
- Write comprehensive system prompts

**MCP Servers** (in `plugin.json` or `.mcp.json`):
- Use `${CLAUDE_PLUGIN_ROOT}` for script paths
- Document required environment variables
- Support stdio, SSE, HTTP, or WebSocket transports

**Rules** (`rules/*.md`):
- Write in clear, actionable markdown
- Group related guidelines together
- Include code examples where helpful

## Code Style

- Use kebab-case for plugin and file names
- Use descriptive names for commands and agents
- Include proper error handling in hook scripts
- Document all public interfaces

## Testing Plugins

1. Add the local marketplace: `/plugin marketplace add ./`
2. Install a plugin: `/plugin install <plugin-name>@auggie-plugin-marketplace`
3. Test commands: `/<command-name>`
4. Check hooks are registered: Look for hook behavior on file edits
5. Verify MCP servers: `/mcp` to see registered servers

## Common Tasks

### Updating Marketplace Metadata
Edit `.claude-plugin/marketplace.json` and ensure all plugin entries have:
- `name`: Plugin identifier (kebab-case)
- `description`: Brief description
- `version`: Semantic version
- `source`: Relative path to plugin directory
- `category`: Plugin category
- `author`: Author information

### Debugging Hooks
- Hook scripts receive JSON on stdin
- Check `/tmp/` for debug logs if implemented
- Use `claude --debug` for verbose output

### Testing MCP Servers
- Run server script directly to test: `python3 plugins/time-server/mcp/time_server.py`
- Check for JSON-RPC communication on stdio

