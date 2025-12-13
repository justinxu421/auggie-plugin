#!/usr/bin/env python3
"""
Log Changes Hook for Code Guard Plugin
Logs file changes after edits are applied (PostToolUse hook).
"""

import json
import os
import sys
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.claude/code-guard-changes.log")


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    tool_result = input_data.get("tool_result", {})

    if tool_name not in ["Edit", "Write"]:
        sys.exit(0)

    file_path = tool_input.get("file_path", "unknown")
    timestamp = datetime.now().isoformat()
    
    # Create log entry
    log_entry = {
        "timestamp": timestamp,
        "tool": tool_name,
        "file": file_path,
        "success": tool_result.get("success", True)
    }

    # Ensure log directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    # Append to log file
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except IOError:
        pass  # Silently fail if can't write log

    # PostToolUse hooks should exit 0 to not affect the result
    sys.exit(0)


if __name__ == "__main__":
    main()

