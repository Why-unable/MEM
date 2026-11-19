#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS="$ROOT/.tools"
mkdir -p "$TOOLS"

clone_if_missing() {
  local repo="$1"
  local dir="$2"
  if [ -d "$dir/.git" ]; then
    echo "exists: $dir"
  else
    echo "cloning: $repo"
    git clone --depth 1 "https://github.com/$repo.git" "$dir"
  fi
}

clone_if_missing "haowen-xiong/research-nexus" "$TOOLS/research-nexus"
clone_if_missing "Zhgb/scholar-literature-maps" "$TOOLS/scholar-literature-maps"
clone_if_missing "oksure/openalex-research-mcp" "$TOOLS/openalex-research-mcp"

cat <<'EOF'

Scheme A tools are installed under MEM/.tools/.

Next steps:
1. Open MEM/vault in Obsidian.
2. Read MEM/guides/scheme-a-setup.md.
3. Optionally load MEM/skills/mem-research-system/SKILL.md into Codex.
4. Use MEM/scripts/build_research_map.py to rebuild maps after editing papers.json/edges.json.
EOF
