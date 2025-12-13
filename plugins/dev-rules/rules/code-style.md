# Code Style Guidelines

When writing or modifying code, follow these style guidelines:

## General Principles

1. **Clarity over cleverness**: Write code that is easy to understand. Avoid complex one-liners when a few clear lines would be better.

2. **Consistent naming**:
   - Use `camelCase` for JavaScript/TypeScript variables and functions
   - Use `snake_case` for Python variables and functions
   - Use `PascalCase` for classes in all languages
   - Use `SCREAMING_SNAKE_CASE` for constants

3. **Function size**: Keep functions under 50 lines. If a function is longer, consider breaking it into smaller functions.

4. **Comments**:
   - Add comments for "why", not "what"
   - Document public APIs with JSDoc/docstrings
   - Remove commented-out code before committing

## Error Handling

1. **Always handle errors explicitly**: Don't ignore catch blocks
2. **Provide useful error messages**: Include context about what went wrong
3. **Fail fast**: Validate inputs early and return/throw early

## Testing

1. **Write tests for new functionality**: Aim for meaningful coverage
2. **Test edge cases**: Empty inputs, nulls, boundary conditions
3. **Keep tests focused**: One assertion per test when possible

