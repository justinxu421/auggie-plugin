# Task Agent Plugin

Autonomous agents for breaking down and managing development tasks.

## Installation

```bash
/plugin install task-agent@auggie-plugin-marketplace
```

## Agents

### Task Planner

Breaks down complex features into actionable, well-organized tasks.

**Triggers when you say:**
- "Break down this task..."
- "Plan a feature for..."
- "Create a task list for..."
- "Help me organize this work..."

**Example:**
```
User: I need to add user authentication to my app
Claude: I'll use the task-planner agent to break this down into manageable steps.
```

**Output includes:**
- Overview of the entire effort
- Prerequisites and setup needed
- Numbered task list with details per task:
  - Description
  - Files involved
  - Dependencies
  - Estimated complexity
  - Acceptance criteria
- Risks and considerations
- Estimated timeline

**Tools:** `Read`, `Bash(find:*)`, `Bash(grep:*)`

---

### Code Reviewer

Performs thorough, structured code reviews with actionable feedback.

**Triggers when you say:**
- "Review my code..."
- "Check my changes..."
- "Review this PR..."
- "Look at my implementation..."

**Example:**
```
User: Can you review the changes I just made?
Claude: I'll use the code-reviewer agent to analyze your recent changes.
```

**Review categories:**
- 🐛 Bugs and Errors
- 🔒 Security
- 📖 Readability
- ⚡ Performance
- 🧪 Testability

**Output includes:**
- Issues found with location, severity, and recommendations
- Overall assessment (Approve / Request Changes / Needs Discussion)
- Key strengths
- Priority items to address

**Tools:** `Read`, `Bash(git diff:*)`, `Bash(git log:*)`, `Bash(git status:*)`

## Agent File Structure

Agents are markdown files with YAML frontmatter:

```markdown
---
name: agent-identifier
description: Use this agent when... <example>...</example>
model: inherit
color: blue
tools: ["Tool1", "Tool2"]
---

System prompt instructions...
```

### Configuration Options

| Field | Description |
|-------|-------------|
| `name` | Unique identifier (kebab-case) |
| `description` | Trigger conditions with examples |
| `model` | `inherit`, `sonnet`, `haiku`, or `opus` |
| `color` | Terminal color for agent output |
| `tools` | Allowed tools (omit for full access) |

### Colors

- `blue`/`cyan` - Analysis, review
- `green` - Generation, creation
- `yellow` - Validation, caution
- `red` - Security, critical
- `magenta` - Transformation, creative

## Development

To create a new agent:

1. Create `.md` file in `agents/` directory
2. Add YAML frontmatter with configuration
3. Write comprehensive system prompt
4. Include 2-4 trigger examples
5. Test by describing scenarios that should trigger it

## License

MIT

