# Security Best Practices

Follow these security guidelines in all code:

## Input Validation

1. **Never trust user input**: Always validate and sanitize
2. **Use allowlists over denylists**: Specify what's allowed, not what's blocked
3. **Validate on the server**: Client-side validation is for UX only

## Authentication & Authorization

1. **Use established libraries**: Don't roll your own crypto
2. **Hash passwords properly**: Use bcrypt, argon2, or similar
3. **Implement proper session management**: Secure cookies, token expiration
4. **Check authorization on every request**: Don't rely on hidden URLs

## Data Protection

1. **Encrypt sensitive data**: At rest and in transit
2. **Use environment variables**: Never hardcode secrets
3. **Minimize data collection**: Only collect what you need
4. **Implement proper access controls**: Principle of least privilege

## Common Vulnerabilities to Avoid

### SQL Injection
```python
# BAD
query = f"SELECT * FROM users WHERE id = {user_id}"

# GOOD
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### XSS (Cross-Site Scripting)
```javascript
// BAD
element.innerHTML = userInput;

// GOOD
element.textContent = userInput;
```

### Command Injection
```python
# BAD
os.system(f"process {filename}")

# GOOD
subprocess.run(["process", filename], shell=False)
```

## Logging & Monitoring

1. **Log security events**: Failed logins, permission changes
2. **Don't log sensitive data**: Passwords, tokens, PII
3. **Monitor for anomalies**: Unusual patterns, high failure rates

