#!/usr/bin/env bash
#
# Security Check Hook for Code Guard Plugin
# Checks for dangerous patterns before tool execution.
# PreToolUse hook - exit 2 to block, exit 0 to allow
#

# Read entire JSON from stdin
EVENT_DATA=$(cat)

# Extract fields using jq
TOOL_NAME=$(echo "$EVENT_DATA" | jq -r '.tool_name // ""')
TOOL_INPUT=$(echo "$EVENT_DATA" | jq -r '.tool_input // {}')

# Extract content based on tool type
CONTENT=""
case "$TOOL_NAME" in
  "save-file")
    CONTENT=$(echo "$TOOL_INPUT" | jq -r '.file_content // ""')
    ;;
  "str-replace-editor")
    # Check all new_str_N fields
    CONTENT=$(echo "$TOOL_INPUT" | jq -r '[.new_str_1, .new_str_2, .new_str_3, .new_str_4, .new_str_5] | map(select(. != null)) | join(" ")')
    ;;
  "launch-process")
    CONTENT=$(echo "$TOOL_INPUT" | jq -r '.command // ""')
    ;;
  *)
    # For other tools, try to get any content-like field
    CONTENT=$(echo "$TOOL_INPUT" | jq -r 'to_entries | map(select(.key | test("content|command|code"; "i"))) | .[0].value // ""')
    ;;
esac

# If no content to check, allow
if [[ -z "$CONTENT" ]]; then
  exit 0
fi

# High severity patterns (will block)
HIGH_SEVERITY_PATTERNS=(
  "eval("
  "exec("
  "os.system("
  "pickle.load"
  "rm -rf /"
  "sudo rm"
  ":(){ :|:& };:"
)

# Medium severity patterns (warn only)
MEDIUM_SEVERITY_PATTERNS=(
  "shell=True"
  "dangerouslySetInnerHTML"
  ".innerHTML ="
  "SECRET"
  "password ="
  "API_KEY"
)

WARNINGS=""
BLOCKS=""

# Check high severity patterns
for pattern in "${HIGH_SEVERITY_PATTERNS[@]}"; do
  if echo "$CONTENT" | grep -qi "$pattern"; then
    BLOCKS="${BLOCKS}🚫 Security: '$pattern' detected - potentially dangerous pattern\n"
  fi
done

# Check medium severity patterns
for pattern in "${MEDIUM_SEVERITY_PATTERNS[@]}"; do
  if echo "$CONTENT" | grep -qi "$pattern"; then
    WARNINGS="${WARNINGS}⚠️  Security Warning: '$pattern' detected - review carefully\n"
  fi
done

# Output warnings to stderr (shown to user)
if [[ -n "$WARNINGS" ]]; then
  echo -e "$WARNINGS" >&2
fi

# Block on high severity matches
if [[ -n "$BLOCKS" ]]; then
  echo -e "$BLOCKS" >&2
  exit 2  # Block the tool
fi

exit 0  # Allow to proceed

