#!/usr/bin/env bash
#
# Log Changes Hook for Code Guard Plugin
# Logs tool usage after execution (PostToolUse hook).
# PostToolUse hooks should always exit 0.
#

LOG_DIR="${HOME}/.augment/logs"
LOG_FILE="${LOG_DIR}/code-guard-changes.log"

# Read entire JSON from stdin
EVENT_DATA=$(cat)

# Extract fields using jq
TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name // "unknown"')
TOOL_INPUT=$(echo "$EVENT_DATA" | jq -r '.tool_input // {}')
TOOL_OUTPUT=$(echo "$EVENT_DATA" | jq -r '.tool_output // ""')
TOOL_ERROR=$(echo "$EVENT_DATA" | jq -r '.tool_error // ""')
CONVERSATION_ID=$(echo "$EVENT_DATA" | jq -r '.conversation_id // ""')
WORKSPACE=$(echo "$EVENT_DATA" | jq -r '.workspace_roots[0] // ""')

# Get timestamp
TIMESTAMP=$(date -Iseconds)

# Determine file path if applicable
FILE_PATH=""
case "$TOOL_NAME" in
  "save-file"|"str-replace-editor"|"view"|"remove-files")
    FILE_PATH=$(echo "$TOOL_INPUT" | jq -r '.path // .file_paths[0] // ""')
    ;;
esac

# Determine success status
SUCCESS="true"
if [[ -n "$TOOL_ERROR" ]]; then
  SUCCESS="false"
fi

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Create log entry as JSON
LOG_ENTRY=$(jq -n \
  --arg ts "$TIMESTAMP" \
  --arg tool "$TOOL_NAME" \
  --arg file "$FILE_PATH" \
  --arg success "$SUCCESS" \
  --arg conv "$CONVERSATION_ID" \
  --arg ws "$WORKSPACE" \
  '{timestamp: $ts, tool: $tool, file: $file, success: ($success == "true"), conversation_id: $conv, workspace: $ws}')

# Append to log file
echo "$LOG_ENTRY" >> "$LOG_FILE" 2>/dev/null

# PostToolUse hooks should always exit 0
exit 0

