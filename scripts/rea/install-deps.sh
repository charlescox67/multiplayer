#!/bin/bash
# Installs the external engines REA (rea-agents) needs for full skill coverage.
# Idempotent: each component is skipped once its marker/binary exists.
# Layout: everything under $REA_DEPS_DIR (default /opt/rea); env exported via $REA_DEPS_DIR/env.sh.
#
# Versions follow REA's documented/CI-verified pins (morluto/rea @ 8fc2043).
# Ghidra and WABT digests were recorded from the first GitHub release download (upstream
# publishes no checksum file reachable here); Node, JADX and Wakaru match upstream digests.
set -euo pipefail

REA_DEPS_DIR="${REA_DEPS_DIR:-/opt/rea}"
DL="$REA_DEPS_DIR/.downloads"
mkdir -p "$REA_DEPS_DIR" "$DL"

REA_AGENTS_VERSION=6.4.0
REA_COMMIT=8fc2043eb8bcedbf34dce064f977e455438635d6
NODE_VERSION=24.18.0
NODE_SHA256=55aa7153f9d88f28d765fcdad5ae6945b5c0f98a36881703817e4c450fa76742
GHIDRA_VERSION=12.1.4
GHIDRA_ZIP=ghidra_12.1.4_PUBLIC_20260921.zip
GHIDRA_SHA256=ddac49f903da9d5bac833e5cc79395098b9c33cfd3279be5f31bd00387d2d4db
JADX_MCP_URL=https://github.com/1013503897/jadx-headless-mcp/releases/download/v0.7.1/jadx-headless-mcp-0.7.1-all.jar
JADX_MCP_SHA256=6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75
WAKARU_URL=https://github.com/pionxzh/wakaru/releases/download/v1.14.0/wakaru-linux-x64.tar.gz
WAKARU_BIN_SHA256=664fa06782a61eda7ed15885134b52525fd565dd77607e642062ceb6cd927c38
WABT_VERSION=1.0.42
WABT_SHA256=84895407a6bbb80e918f33b16b2fb2206021c150b6bc9ff6f761263a745ab131
PWNDBG_COMMIT=55596aa676a2756efb8d67034f31675170eabe48
BINWALK_VERSION=3.1.0
UNBLOB_VERSION=26.6.4
JEFFERSON_VERSION=0.4.8
UBI_READER_VERSION=0.8.16
SASQUATCH_VERSION=4.5.1-6
SASQUATCH_SHA256=efbc92bd27594e01211e1b582f105a463a0017360a0746a93de3f283906ade95

log() { printf '[rea-deps] %s\n' "$*" >&2; }

# fetch URL FILE SHA256: download into $DL once, verify digest every time.
fetch() {
  local url=$1 file=$DL/$2 sha=$3
  if [ ! -f "$file" ] || ! echo "$sha  $file" | sha256sum --check --status; then
    log "downloading $2"
    curl -fsSL --retry 6 --retry-delay 2 --retry-all-errors -C - -o "$file.partial" "$url"
    mv "$file.partial" "$file"
  fi
  echo "$sha  $file" | sha256sum --check --status || { log "SHA-256 mismatch for $2"; exit 1; }
}

SUDO=""
[ "$(id -u)" -ne 0 ] && SUDO="sudo"

# --- System packages: TShark, sigrok, GDB, prlimit, Apktool, binwalk build deps, unblob extractors
APT_PKGS=(tshark sigrok-cli gdb util-linux apktool python3-venv python3-dev pkg-config
  libfontconfig1-dev liblzma-dev libbz2-dev zlib1g-dev libssl-dev
  e2fsprogs erofs-utils lz4 lziprecover lzop p7zip-full partclone unar zstd xz-utils
  android-sdk-libsparse-utils adb)
missing=()
for p in "${APT_PKGS[@]}"; do dpkg -s "$p" >/dev/null 2>&1 || missing+=("$p"); done
if [ ${#missing[@]} -gt 0 ]; then
  log "apt installing: ${missing[*]}"
  echo "wireshark-common wireshark-common/install-setuid boolean false" | $SUDO debconf-set-selections
  $SUDO apt-get update -qq || log "apt-get update reported errors; continuing with available lists"
  DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq --no-install-recommends "${missing[@]}" >/dev/null
fi

# --- Node 24 (REA's SQLite inspection needs >=24.15)
if [ ! -x "$REA_DEPS_DIR/node/bin/node" ]; then
  fetch "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
    "node-v$NODE_VERSION-linux-x64.tar.xz" "$NODE_SHA256"
  rm -rf "$REA_DEPS_DIR/node" && mkdir -p "$REA_DEPS_DIR/node"
  tar -xJf "$DL/node-v$NODE_VERSION-linux-x64.tar.xz" -C "$REA_DEPS_DIR/node" --strip-components=1
  rm -f "$DL/node-v$NODE_VERSION-linux-x64.tar.xz"
fi

# --- Ghidra 12.1.4 (uses the system JDK 21; REA requires a full JDK with javac)
GHIDRA_DIR="$REA_DEPS_DIR/ghidra_${GHIDRA_VERSION}_PUBLIC"
if [ ! -x "$GHIDRA_DIR/support/analyzeHeadless" ]; then
  fetch "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_${GHIDRA_VERSION}_build/$GHIDRA_ZIP" \
    "$GHIDRA_ZIP" "$GHIDRA_SHA256"
  rm -rf "$GHIDRA_DIR"
  unzip -q "$DL/$GHIDRA_ZIP" -d "$REA_DEPS_DIR"
  rm -f "$DL/$GHIDRA_ZIP"
fi

# --- JADX headless MCP jar (Android analysis)
mkdir -p "$REA_DEPS_DIR/jadx"
if [ ! -f "$REA_DEPS_DIR/jadx/jadx-headless-mcp-0.7.1-all.jar" ]; then
  fetch "$JADX_MCP_URL" jadx-headless-mcp-0.7.1-all.jar "$JADX_MCP_SHA256"
  mv "$DL/jadx-headless-mcp-0.7.1-all.jar" "$REA_DEPS_DIR/jadx/"
fi

# --- Wakaru (JavaScript source recovery); digest is of the extracted binary, as in REA CI
if [ ! -x "$REA_DEPS_DIR/wakaru/wakaru" ]; then
  mkdir -p "$REA_DEPS_DIR/wakaru"
  curl -fsSL --retry 6 --retry-delay 2 --retry-all-errors "$WAKARU_URL" | tar -xz -C "$REA_DEPS_DIR/wakaru" wakaru
  echo "$WAKARU_BIN_SHA256  $REA_DEPS_DIR/wakaru/wakaru" | sha256sum --check --status \
    || { rm -f "$REA_DEPS_DIR/wakaru/wakaru"; log "SHA-256 mismatch for wakaru"; exit 1; }
fi

# --- WABT 1.0.42 (WebAssembly inspection)
if [ ! -x "$REA_DEPS_DIR/wabt-$WABT_VERSION/bin/wasm2wat" ]; then
  fetch "https://github.com/WebAssembly/wabt/releases/download/$WABT_VERSION/wabt-$WABT_VERSION-linux-x64.tar.gz" \
    "wabt-$WABT_VERSION-linux-x64.tar.gz" "$WABT_SHA256"
  tar -xzf "$DL/wabt-$WABT_VERSION-linux-x64.tar.gz" -C "$REA_DEPS_DIR"
  rm -f "$DL/wabt-$WABT_VERSION-linux-x64.tar.gz"
fi

# --- pwntools venv (ELF layout + recorded crash decoding)
PWN_VENV="$REA_DEPS_DIR/pwntools-venv"
if ! "$PWN_VENV/bin/python" -c 'import pwn, elftools, unicorn' >/dev/null 2>&1; then
  python3 -m venv "$PWN_VENV"
  "$PWN_VENV/bin/python" -m pip install -q --disable-pip-version-check \
    'pwntools==4.15.0' 'pyelftools==0.33' 'unicorn==2.1.2' 'uv==0.12.0'
fi

# --- pwndbg at REA's pinned commit (optional debugger context for crash cores)
PWNDBG_DIR="$REA_DEPS_DIR/pwndbg"
PWNDBG_VENV="$REA_DEPS_DIR/pwndbg-venv"
if [ ! -f "$PWNDBG_VENV/.rea-$PWNDBG_COMMIT" ]; then
  if [ "$(git -C "$PWNDBG_DIR" rev-parse HEAD 2>/dev/null)" != "$PWNDBG_COMMIT" ]; then
    rm -rf "$PWNDBG_DIR" && git init -q "$PWNDBG_DIR"
    git -C "$PWNDBG_DIR" fetch -q --depth=1 https://github.com/pwndbg/pwndbg.git "$PWNDBG_COMMIT"
    git -C "$PWNDBG_DIR" checkout -q --detach FETCH_HEAD
  fi
  UV_PROJECT_ENVIRONMENT="$PWNDBG_VENV" "$PWN_VENV/bin/uv" sync -q --project "$PWNDBG_DIR" \
    --frozen --no-editable --no-default-groups --python /usr/bin/python3 --no-managed-python
  touch "$PWNDBG_VENV/.rea-$PWNDBG_COMMIT"
fi

# --- Binwalk 3.1.0 (firmware region inspection), built from crates.io
if ! "$REA_DEPS_DIR/binwalk/bin/binwalk" --version 2>/dev/null | grep -q "binwalk $BINWALK_VERSION"; then
  command -v cargo >/dev/null || { log "cargo not found; skipping binwalk"; }
  if command -v cargo >/dev/null; then
    log "building binwalk $BINWALK_VERSION (several minutes)"
    cargo install -q --locked --version "$BINWALK_VERSION" --root "$REA_DEPS_DIR/binwalk" binwalk
  fi
fi

# --- Unblob 26.6.4 (firmware extraction)
UNBLOB_VENV="$REA_DEPS_DIR/unblob-venv"
if ! "$UNBLOB_VENV/bin/unblob" --version 2>/dev/null | grep -qx "$UNBLOB_VERSION" \
  || [ ! -x "$UNBLOB_VENV/bin/jefferson" ] || [ ! -x "$UNBLOB_VENV/bin/ubireader_extract_files" ]; then
  python3 -m venv "$UNBLOB_VENV"
  "$UNBLOB_VENV/bin/python" -m pip install -q --disable-pip-version-check "unblob==$UNBLOB_VERSION" \
    "jefferson==$JEFFERSON_VERSION" "ubi-reader==$UBI_READER_VERSION"
fi
# unblob resolves its extractors from PATH
for b in jefferson ubireader_extract_files ubireader_extract_images; do
  [ -e "/usr/local/bin/$b" ] || $SUDO ln -s "$UNBLOB_VENV/bin/$b" "/usr/local/bin/$b"
done
if ! command -v sasquatch >/dev/null; then
  fetch "https://github.com/onekey-sec/sasquatch/releases/download/sasquatch-v$SASQUATCH_VERSION/sasquatch_1.0_amd64.deb" \
    sasquatch_1.0_amd64.deb "$SASQUATCH_SHA256"
  $SUDO dpkg -i "$DL/sasquatch_1.0_amd64.deb" >/dev/null
  rm -f "$DL/sasquatch_1.0_amd64.deb"
fi

# --- REA built from the same commit as the vendored skill. npm $REA_AGENTS_VERSION lacks tools the
# skill routes to (inspect_wasm_artifact, inspect_sqlite_database, inspect_go_binary,
# inspect_packet_capture, decode_signal_recording).
REA_SRC="$REA_DEPS_DIR/rea-main"
if [ ! -f "$REA_SRC/.rea-built-$REA_COMMIT" ]; then
  log "building rea-agents from $REA_COMMIT"
  rm -rf "$REA_SRC" && git init -q "$REA_SRC"
  git -C "$REA_SRC" fetch -q --depth=1 https://github.com/morluto/rea.git "$REA_COMMIT"
  git -C "$REA_SRC" checkout -q --detach FETCH_HEAD
  (cd "$REA_SRC" && PATH="$REA_DEPS_DIR/node/bin:$PATH" npm ci --no-audit --no-fund --loglevel=error \
    && PATH="$REA_DEPS_DIR/node/bin:$PATH" npm run build >/dev/null)
  touch "$REA_SRC/.rea-built-$REA_COMMIT"
fi

# --- `rea` CLI wrapper on Node 24
mkdir -p "$REA_DEPS_DIR/bin"
cat > "$REA_DEPS_DIR/bin/rea" <<EOF
#!/bin/sh
exec "$REA_DEPS_DIR/node/bin/node" "$REA_SRC/scripts/rea.mjs" "\$@"
EOF
chmod +x "$REA_DEPS_DIR/bin/rea"
"$REA_DEPS_DIR/bin/rea" --help >/dev/null

# --- Environment for the shell (SessionStart hook) and the MCP server (scripts/rea/mcp.sh)
cat > "$REA_DEPS_DIR/env.sh" <<EOF
export PATH="$REA_DEPS_DIR/bin:\$PATH"
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f "$(command -v javac)")")")"
export GHIDRA_INSTALL_DIR="$GHIDRA_DIR"
export REA_BROWSER_EXECUTABLE="$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | tail -1)"
export REA_JADX_MCP_JAR="$REA_DEPS_DIR/jadx/jadx-headless-mcp-0.7.1-all.jar"
export REA_WAKARU_COMMAND="$REA_DEPS_DIR/wakaru/wakaru"
export REA_WABT_BIN_DIRECTORY="$REA_DEPS_DIR/wabt-$WABT_VERSION/bin"
export REA_PWNTOOLS_PYTHON="$PWN_VENV/bin/python"
export REA_PWNDBG_GDB="$(command -v gdb)"
export REA_PWNDBG_GDBINIT="$PWNDBG_DIR/gdbinit.py"
export REA_PWNDBG_VENV_PATH="$PWNDBG_VENV"
export REA_TSHARK_COMMAND="$(command -v tshark)"
export REA_SIGROK_COMMAND="$(command -v sigrok-cli)"
export REA_APKTOOL_COMMAND="$(command -v apktool)"
export REA_ADB_PATH="$(command -v adb)"
export REA_BINWALK_COMMAND="$REA_DEPS_DIR/binwalk/bin/binwalk"
export REA_UNBLOB_COMMAND="$UNBLOB_VENV/bin/unblob"
EOF
log "done; env written to $REA_DEPS_DIR/env.sh"
