# Coding Standards

Follow these standards when writing or modifying code in this project.

## Naming Conventions

### Variables and Functions
- Use descriptive names that explain purpose
- Prefer `getUserById` over `get` or `fetchUser`
- Boolean variables should be questions: `isActive`, `hasPermission`, `canEdit`

### Constants
- Use SCREAMING_SNAKE_CASE for true constants
- Group related constants in objects or enums

### Files and Directories
- Use kebab-case for file names: `user-service.ts`
- Group by feature, not by type

## Code Organization

### Function Length
- Keep functions under 30 lines
- Single responsibility: one function, one job
- Extract helpers for complex logic

### File Length
- Keep files under 300 lines
- Split large files by responsibility

### Imports
- Group imports: external, internal, relative
- Sort alphabetically within groups
- Remove unused imports

## Error Handling

### Always Handle Errors
```javascript
// BAD
const data = await fetch(url);

// GOOD
try {
  const data = await fetch(url);
} catch (error) {
  logger.error('Failed to fetch:', error);
  throw new FetchError('Unable to retrieve data', { cause: error });
}
```

### Provide Context
- Include what operation failed
- Include relevant IDs or parameters
- Don't expose sensitive data in errors

## Comments

### When to Comment
- Explain WHY, not WHAT
- Document non-obvious business logic
- Note workarounds with ticket references

### When NOT to Comment
- Don't explain obvious code
- Don't leave commented-out code
- Don't write TODOs without tickets

## Testing

### Test Names
- Describe the scenario: `should return null when user not found`
- Follow pattern: `should [expected] when [condition]`

### Test Structure
- Arrange: Set up test data
- Act: Execute the code
- Assert: Verify the result

