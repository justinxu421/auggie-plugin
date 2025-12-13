---
description: Analyze a file or directory for code quality, complexity, and potential issues
allowed-tools: Read, Bash(find:*), Bash(wc:*), Bash(grep:*)
---

## Context

Current directory structure:
```
!`find . -type f -name "*.py" -o -name "*.js" -o -name "*.ts" | head -20`
```

## Your Task

Analyze the specified file or directory: $ARGUMENTS

Provide a comprehensive analysis including:

### 1. Structure Overview
- File count and types
- Directory organization
- Key entry points

### 2. Code Metrics
- Lines of code
- Function/class count
- Cyclomatic complexity estimate

### 3. Quality Assessment
- Code style consistency
- Documentation coverage
- Test coverage (if applicable)

### 4. Potential Issues
- Code smells
- Security concerns
- Performance considerations

### 5. Recommendations
- Priority improvements
- Refactoring suggestions
- Best practices to adopt

Be specific and actionable in your analysis.

