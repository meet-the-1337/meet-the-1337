#!/usr/bin/env python3
"""
Dynamic Gemini-Powered Neural Log Generator for GitHub Profile README.
Uses Google Gemini API to generate daily cyberpunk agent transmissions,
system telemetry, or thought streams and injects them into README.md.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

PROMPT = """
You are the AI neural core of Meet The 1337's riced developer system (CachyOS + Hyprland + Kitty, building autonomous agents, cybersec tools, and brain connectomes).
Generate a single daily log entry formatted as an ultra-cool terminal telemetry log for a GitHub profile README.

Format requirements:
- Exactly 3-4 bullet points or short lines.
- Style: Cyberpunk terminal telemetry, high-intellect hacker vibe, sharp, witty, and deeply technical (referencing AI agents, graph neural nets, Linux kernels, memory optimization, or connectomes).
- Do not use markdown backticks around the whole output, just raw text with terminal symbols like ❯, ⚡, 🧠, 📡.
- Include a 1-sentence "Daily Insight" or "Neural Transmission".
- Timestamp format: YYYY-MM-DD UTC

Example output format:
📡 [2026-09-14 22:00 UTC] ❯ Neural telemetry synced with Hermes Agent core.
🧠 [STATUS] ❯ Optimizing fruitfly connectome neural weights; latency dropped to 1.2ms.
⚡ [TRANSMISSION] ❯ "True optimization isn't writing faster code; it's architecting systems that adapt before execution."
"""

def generate_gemini_log():
    if not GEMINI_API_KEY:
        print("⚠️ GEMINI_API_KEY not found in environment. Generating fallback transmission.")
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        return f"""📡 [{now}] ❯ Neural telemetry active • Hermes Agent kernel online.
🧠 [STATUS] ❯ Fruitfly connectome simulation synchronized across 100k synapses.
⚡ [TRANSMISSION] ❯ "Building autonomous systems that think in graphs and breathe in Linux sockets." """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{
            "parts": [{"text": PROMPT}]
        }],
        "generationConfig": {
            "temperature": 0.85,
            "maxOutputTokens": 250
        }
    }

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
            text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            return text
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        return f"""📡 [{now}] ❯ Local neural link active • Hermes Agent standing by.
🧠 [STATUS] ❯ Temporal GNN graph convolutions converging under peak efficiency.
⚡ [TRANSMISSION] ❯ "Why simulate intelligence when you can build agents to automate reality?" """

def update_readme(content):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    start_tag = "<!-- GEMINI_LOG:START -->"
    end_tag = "<!-- GEMINI_LOG:END -->"

    if start_tag not in readme or end_tag not in readme:
        print("Markers not found in README.md! Check your tags.")
        return False

    before = readme.split(start_tag)[0] + start_tag + "\n"
    after = "\n" + end_tag + readme.split(end_tag)[1]

    formatted_block = f"""```bash
┌─ 🤖 GEMINI AI AGENT • DAILY NEURAL TRANSMISSION ──────────────┐
{chr(10).join('│  ' + line for line in content.splitlines())}
└───────────────────────────────────────────────────────────────┘
```"""

    new_readme = before + formatted_block + after

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

    print("✅ README.md successfully updated with Gemini Neural Log!")
    return True

if __name__ == "__main__":
    print("🤖 Querying Gemini API...")
    log = generate_gemini_log()
    print("Generated Log:\n", log)
    update_readme(log)
