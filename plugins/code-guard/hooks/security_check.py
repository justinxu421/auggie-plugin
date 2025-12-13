#!/usr/bin/env python3
"""
Security Check Hook for Code Guard Plugin
Checks for dangerous patterns before file edits are applied.
"""

import json
import sys

# Dangerous patterns to check for
DANGEROUS_PATTERNS = [
    {
        "pattern": "eval(",
        "message": "⚠️ Security Warning: eval() can execute arbitrary code. Consider safer alternatives.",
        "severity": "high"
    },
    {
        "pattern": "exec(",
        "message": "⚠️ Security Warning: exec() can execute arbitrary code. Use with extreme caution.",
        "severity": "high"
    },
    {
        "pattern": "os.system(",
        "message": "⚠️ Security Warning: os.system() is vulnerable to command injection. Use subprocess with shell=False.",
        "severity": "high"
    },
    {
        "pattern": "shell=True",
        "message": "⚠️ Security Warning: shell=True in subprocess can lead to command injection.",
        "severity": "medium"
    },
    {
        "pattern": "dangerouslySetInnerHTML",
        "message": "⚠️ Security Warning: dangerouslySetInnerHTML can lead to XSS. Sanitize content first.",
        "severity": "medium"
    },
    {
        "pattern": ".innerHTML =",
        "message": "⚠️ Security Warning: innerHTML can lead to XSS. Consider using textContent or sanitizing.",
        "severity": "medium"
    },
    {
        "pattern": "pickle.load",
        "message": "⚠️ Security Warning: pickle can execute arbitrary code. Use JSON for untrusted data.",
        "severity": "high"
    },
    {
        "pattern": "SECRET",
        "message": "⚠️ Security Warning: Possible hardcoded secret detected. Use environment variables.",
        "severity": "medium"
    },
    {
        "pattern": "password =",
        "message": "⚠️ Security Warning: Possible hardcoded password. Use environment variables or secrets manager.",
        "severity": "medium"
    }
]


def extract_content(tool_name, tool_input):
    """Extract content to check from tool input."""
    if tool_name == "Write":
        return tool_input.get("content", "")
    elif tool_name == "Edit":
        return tool_input.get("new_string", "")
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        return " ".join(edit.get("new_string", "") for edit in edits)
    return ""


def check_patterns(content):
    """Check content for dangerous patterns."""
    warnings = []
    for pattern_info in DANGEROUS_PATTERNS:
        if pattern_info["pattern"].lower() in content.lower():
            warnings.append(pattern_info)
    return warnings


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)  # Allow to proceed if can't parse

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name not in ["Edit", "Write", "MultiEdit"]:
        sys.exit(0)

    content = extract_content(tool_name, tool_input)
    warnings = check_patterns(content)

    if warnings:
        high_severity = [w for w in warnings if w["severity"] == "high"]
        
        print("\n".join(w["message"] for w in warnings), file=sys.stderr)
        
        # Block on high severity, warn on others
        if high_severity:
            sys.exit(2)  # Block the tool
    
    sys.exit(0)  # Allow to proceed


if __name__ == "__main__":
    main()

