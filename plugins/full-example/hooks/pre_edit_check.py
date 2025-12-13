#!/usr/bin/env python3
"""
Pre-edit hook that checks for common issues before allowing edits.
Demonstrates PreToolUse hook pattern.
"""

import json
import sys
import os

# Patterns to warn about
WARNING_PATTERNS = [
    ("TODO", "Contains TODO - consider addressing before committing"),
    ("FIXME", "Contains FIXME - this should be fixed"),
    ("HACK", "Contains HACK - consider a proper solution"),
    ("console.log", "Contains console.log - remove before production"),
    ("print(", "Contains print statement - use logging instead"),
    ("debugger", "Contains debugger statement - remove before committing"),
]

# Patterns to block
BLOCK_PATTERNS = [
    ("eval(", "eval() is dangerous - use safer alternatives"),
    ("exec(", "exec() is dangerous - use safer alternatives"),
    ("__import__", "Dynamic imports can be dangerous"),
]


def check_content(content: str) -> tuple[list, list]:
    """Check content for warning and blocking patterns."""
    warnings = []
    blocks = []
    
    content_lower = content.lower()
    
    for pattern, message in WARNING_PATTERNS:
        if pattern.lower() in content_lower:
            warnings.append(f"⚠️  {message}")
    
    for pattern, message in BLOCK_PATTERNS:
        if pattern.lower() in content_lower:
            blocks.append(f"🚫 {message}")
    
    return warnings, blocks


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)
    
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    
    # Extract content based on tool type
    content = ""
    if tool_name == "Write":
        content = tool_input.get("content", "")
    elif tool_name == "Edit":
        content = tool_input.get("new_string", "")
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        content = " ".join(e.get("new_string", "") for e in edits)
    
    if not content:
        sys.exit(0)
    
    warnings, blocks = check_content(content)
    
    # Output warnings
    for warning in warnings:
        print(warning, file=sys.stderr)
    
    # Block if dangerous patterns found
    if blocks:
        for block in blocks:
            print(block, file=sys.stderr)
        sys.exit(2)  # Block the edit
    
    sys.exit(0)  # Allow the edit


if __name__ == "__main__":
    main()

