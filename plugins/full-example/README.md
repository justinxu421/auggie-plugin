# Full Example Plugin

A comprehensive plugin demonstrating all Augment plugin capabilities in a single package.

## Installation

```bash
/plugin install full-example@auggie-plugin-marketplace
```

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/analyze <path>` | Analyze code quality, complexity, and potential issues |
| `/scaffold <type> <name>` | Scaffold new components following project conventions |

### Hooks

| Hook | Trigger | Description |
|------|---------|-------------|
| PreToolUse | Edit, Write, MultiEdit | Checks for dangerous patterns and common issues |
| PostToolUse | Edit, Write | Logs file changes and notifies user |

**Blocked Patterns:**
- `eval()`, `exec()` - Dangerous code execution
- `__import__` - Dynamic imports

**Warning Patterns:**
- `TODO`, `FIXME`, `HACK` - Incomplete code markers
- `console.log`, `print()` - Debug statements
- `debugger` - Debug breakpoints

### Agents

| Agent | Color | Description |
|-------|-------|-------------|
| `refactor-agent` | yellow | Code refactoring specialist |
| `debug-agent` | red | Bug finding and fixing expert |

### Rules

| Rule | Description |
|------|-------------|
| `coding-standards.md` | General coding best practices |
| `project-conventions.md` | Project-specific conventions |

### MCP Server (context7)

Uses the [Context7 MCP server](https://github.com/upstash/context7-mcp) for documentation lookup.

| Tool | Description |
|------|-------------|
| `resolve-library-id` | Find library IDs for documentation lookup |
| `get-library-docs` | Fetch up-to-date documentation for libraries |

## Directory Structure

```
full-example/
├── .augment-plugin/
│   └── plugin.json         # Plugin metadata
├── .mcp.json               # MCP server configuration
├── hooks/
│   ├── hooks.json          # Hook configuration
│   ├── pre_edit_check.py   # PreToolUse hook
│   └── post_edit_notify.py # PostToolUse hook
├── commands/
│   ├── analyze.md          # Code analysis command
│   └── scaffold.md         # Scaffolding command
├── agents/
│   ├── refactor-agent.md   # Refactoring agent
│   └── debug-agent.md      # Debugging agent
├── rules/
│   ├── coding-standards.md
│   └── project-conventions.md
├── mcp/
│   └── project_server.py   # MCP server implementation
└── README.md
```

## Usage Examples

### Analyze Code
```
/analyze src/
/analyze src/components/Button.tsx
```

### Scaffold Components
```
/scaffold component UserProfile
/scaffold service PaymentProcessor
/scaffold api orders
```

### Use Agents
```
> Use refactor-agent to improve the auth module
> Use debug-agent to fix the login issue
```

### MCP Tools
The MCP server provides tools automatically available to the AI for project analysis.

## License

MIT

