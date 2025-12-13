# Project Conventions

These conventions are specific to this project and should be followed for consistency.

## Architecture

### Directory Structure
```
src/
  components/     # UI components
  services/       # Business logic
  utils/          # Shared utilities
  types/          # Type definitions
  hooks/          # Custom hooks (React)
  api/            # API layer
tests/
  unit/           # Unit tests
  integration/    # Integration tests
```

### Module Boundaries
- Components should not directly call APIs
- Services handle business logic
- Utils are pure functions with no side effects

## API Patterns

### Request/Response
- Use consistent response envelope
- Include request ID for tracing
- Standardize error format

### Naming
- REST: plural nouns (`/users`, `/orders`)
- Actions: verbs (`/auth/login`, `/files/upload`)

## State Management

### Local vs Global
- Prefer local state when possible
- Use global state for truly shared data
- Avoid prop drilling more than 2 levels

### Async State
- Track loading, error, and data states
- Handle race conditions
- Implement optimistic updates for UX

## Git Workflow

### Branch Names
- `feature/ABC-123-description`
- `fix/ABC-456-bug-description`
- `chore/update-dependencies`

### Commit Messages
```
type(scope): description

- Detail 1
- Detail 2

Refs: ABC-123
```

### PR Guidelines
- One feature per PR
- Include screenshots for UI changes
- Update documentation
- Add tests for new code

