#!/bin/bash
# Installs REA engines (cached in the container image after first run) and exports their env.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

bash "$CLAUDE_PROJECT_DIR/scripts/rea/install-deps.sh"

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  cat "${REA_DEPS_DIR:-/opt/rea}/env.sh" >> "$CLAUDE_ENV_FILE"
fi
