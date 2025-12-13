# Code Guard Plugin

Security-focused hooks that warn about potentially dangerous code patterns before they're written.

## Installation

```bash
/plugin install code-guard@auggie-plugin-marketplace
```

## Features

### PreToolUse Security Hook

Automatically checks code being written for dangerous patterns:

| Pattern | Severity | Action |
|---------|----------|--------|
| `eval()` | High | Block |
| `exec()` | High | Block |
| `os.system()` | High | Block |
| `pickle.load` | High | Block |
| `shell=True` | Medium | Warn |
| `dangerouslySetInnerHTML` | Medium | Warn |
| `.innerHTML =` | Medium | Warn |
| Hardcoded secrets | Medium | Warn |

**High severity patterns block the edit and require acknowledgment.**

### PostToolUse Logging Hook

Logs all file changes to `~/.claude/code-guard-changes.log` for audit purposes.

Log format:
```json
{"timestamp": "2024-01-15T10:30:00", "tool": "Write", "file": "src/app.js", "success": true}
```

## How It Works

### Security Check Flow

1. Claude attempts to edit a file (Edit, Write, or MultiEdit)
2. PreToolUse hook intercepts the request
3. Content is scanned for dangerous patterns
4. If high-severity pattern found → Edit blocked with warning
5. If medium-severity pattern found → Warning shown, edit proceeds
6. If no patterns found → Edit proceeds normally

### Hook Configuration

Hooks are defined in `hooks/hooks.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "hooks": [{"type": "command", "command": "python3 ..."}],
        "matcher": "Edit|Write|MultiEdit"
      }
    ]
  }
}
```

## Customization

### Adding New Patterns

Edit `hooks/security_check.py` and add to `DANGEROUS_PATTERNS`:

```python
{
    "pattern": "your_pattern",
    "message": "⚠️ Warning message",
    "severity": "high"  # or "medium"
}
```

### Disabling the Hook

Remove or rename the plugin:
```bash
/plugin uninstall code-guard
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ENABLE_SECURITY_REMINDER` | `1` | Set to `0` to disable security checks |

## Files

```
code-guard/
├── .claude-plugin/
│   └── plugin.json       # Plugin metadata
└── hooks/
    ├── hooks.json        # Hook configuration
    ├── security_check.py # PreToolUse security scanner
    └── log_changes.py    # PostToolUse change logger
```

## License

MIT

