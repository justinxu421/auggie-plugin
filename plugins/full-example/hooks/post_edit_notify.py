#!/usr/bin/env python3
"""
Post-edit hook that logs and notifies about file changes.
Demonstrates PostToolUse hook pattern.
"""

import json
import sys
import os
from datetime import datetime

LOG_DIR = os.path.expanduser("~/.augment/logs")
LOG_FILE = os.path.join(LOG_DIR, "file-changes.log")


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)
    
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    tool_result = input_data.get("tool_result", {})
    
    # Get file path
    file_path = tool_input.get("file_path", tool_input.get("path", "unknown"))
    
    # Create log entry
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "action": tool_name,
        "file": file_path,
        "success": tool_result.get("success", True)
    }
    
    # Ensure log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Append to log
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except IOError:
        pass
    
    # Print notification
    print(f"📝 Modified: {file_path}", file=sys.stderr)
    
    # PostToolUse hooks should always exit 0
    sys.exit(0)


if __name__ == "__main__":
    main()

