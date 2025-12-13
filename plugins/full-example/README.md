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

### MCP Servers

Demonstrates both local (stdio) and remote (HTTP/SSE) MCP servers:

| Server | Type | Description |
|--------|------|-------------|
| `context7` | stdio | Documentation lookup for libraries |
| `fetch` | HTTP | Fetch and convert web content to markdown |
| `sequential-thinking` | HTTP | Structured problem-solving tool |
| `deepwiki` | HTTP | Auto-generated architecture docs for codebases |
| `coingecko` | SSE | Cryptocurrency data platform |
| `semgrep` | SSE | Static analysis for code security |

## Directory Structure

```
full-example/
├── .augment-plugin/
│   └── plugin.json         # Plugin metadata
├── .mcp.json               # MCP server configuration (context7)
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
Multiple MCP servers provide various capabilities:
- **context7**: Library documentation lookup
- **fetch**: Web content retrieval
- **sequential-thinking**: Structured problem solving
- **deepwiki**: Codebase architecture documentation
- **coingecko**: Cryptocurrency data
- **semgrep**: Code security analysis

## License

MIT

