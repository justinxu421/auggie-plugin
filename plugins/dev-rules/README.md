# Dev Rules Plugin

Development best practices and coding standards provided as rules that guide AI behavior.

## Installation

```bash
/plugin install dev-rules@auggie-plugin-marketplace
```

## Rules

### Code Style (`rules/code-style.md`)

Guidelines for writing clean, maintainable code:

- **Clarity over cleverness** - Readable code over complex one-liners
- **Consistent naming** - Language-appropriate conventions
- **Function size** - Keep functions under 50 lines
- **Comments** - Document "why", not "what"
- **Error handling** - Always handle errors explicitly
- **Testing** - Write tests for new functionality

### Git Workflow (`rules/git-workflow.md`)

Guidelines for version control:

- **Conventional commits** - `feat:`, `fix:`, `docs:`, etc.
- **Branch naming** - `feature/`, `fix/`, `hotfix/`
- **PR guidelines** - Focused PRs with good descriptions
- **Pre-push checklist** - Tests, linting, self-review

### Security Practices (`rules/security-practices.md`)

Security guidelines for all code:

- **Input validation** - Never trust user input
- **Authentication** - Use established libraries
- **Data protection** - Encrypt sensitive data
- **Common vulnerabilities** - SQL injection, XSS, command injection examples

## How Rules Work

Rules are markdown files that are automatically included in the AI's context when the plugin is enabled. They guide behavior without requiring explicit commands.

**Example effect:**

Without rules:
```
User: Write a function to query the database
AI: def get_user(id):
      return db.execute(f"SELECT * FROM users WHERE id = {id}")
```

With security-practices rule:
```
User: Write a function to query the database
AI: def get_user(id):
      return db.execute("SELECT * FROM users WHERE id = ?", (id,))
```

## Customization

### Adding New Rules

1. Create a `.md` file in the `rules/` directory
2. Write guidelines in clear, actionable markdown
3. Include code examples where helpful

### Rule Structure

```markdown
# Rule Title

Brief introduction to what this rule covers.

## Section 1

Guidelines with examples:

1. **Guideline name**: Description
2. **Another guideline**: Description

## Section 2

More guidelines...

### Code Examples

```python
# BAD
dangerous_code()

# GOOD  
safe_code()
```
```

## Files

```
dev-rules/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata
└── rules/
    ├── code-style.md    # Code style guidelines
    ├── git-workflow.md  # Git workflow guidelines
    └── security-practices.md  # Security guidelines
```

## License

MIT

