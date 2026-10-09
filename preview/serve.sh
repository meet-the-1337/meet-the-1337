#!/usr/bin/env bash
# Localhost live-preview server for GitHub Profile README

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT=8000

echo -e "\033[1;36m"
echo "  ╔═══════════════════════════════════════════════════════════════╗"
echo "  ║        ⚡ GITHUB PROFILE LIVE RICE PREVIEW SERVER ⚡          ║"
echo "  ╚═══════════════════════════════════════════════════════════════╝"
echo -e "\033[0m"
echo -e "  \033[1;32m➜\033[0m  Preview URL: \033[1;34mhttp://localhost:${PORT}/preview/\033[0m"
echo -e "  \033[1;32m➜\033[0m  Root Dir:    \033[1;30m${DIR}\033[0m"
echo -e "  \033[1;33m➜\033[0m  Hot-Reload:  \033[0;32mACTIVE (Edits in README.md update instantly)\033[0m"
echo ""

cd "$DIR"

# Try opening in default browser
if command -v xdg-open &> /dev/null; then
  (sleep 0.8 && xdg-open "http://localhost:${PORT}/preview/") &
elif command -v open &> /dev/null; then
  (sleep 0.8 && open "http://localhost:${PORT}/preview/") &
fi

# Run python server
python3 -m http.server $PORT
