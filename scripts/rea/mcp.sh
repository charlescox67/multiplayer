#!/bin/sh
# Launches the REA MCP server (stdio) with engines from scripts/rea/install-deps.sh.
# Without installed deps it still starts; engine-backed tools then report themselves unavailable.
REA_DEPS_DIR="${REA_DEPS_DIR:-/opt/rea}"
if [ -f "$REA_DEPS_DIR/env.sh" ]; then
  . "$REA_DEPS_DIR/env.sh"
  exec "$REA_DEPS_DIR/bin/rea" mcp
fi
exec npx -y rea-agents@6.4.0 mcp
