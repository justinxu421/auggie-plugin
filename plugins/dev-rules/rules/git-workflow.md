# Git Workflow Guidelines

Follow these guidelines when working with Git:

## Commit Messages

Use conventional commit format:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc.)
- `refactor`: Code refactoring without feature changes
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples:
```
feat(auth): add password reset functionality
fix(api): handle null response from server
docs(readme): update installation instructions
```

## Branching Strategy

1. **Main branch**: Always deployable, protected
2. **Feature branches**: `feature/description-of-feature`
3. **Bug fix branches**: `fix/description-of-bug`
4. **Hotfix branches**: `hotfix/critical-issue`

## Pull Request Guidelines

1. **Keep PRs focused**: One feature or fix per PR
2. **Write descriptive titles**: Summarize the change
3. **Include context in description**: What, why, and how
4. **Link related issues**: Use "Closes #123" syntax
5. **Request reviews**: Tag appropriate reviewers
6. **Respond to feedback**: Address all comments

## Before Pushing

1. Run tests locally
2. Check for linting errors
3. Review your own changes
4. Ensure commits are clean and logical

