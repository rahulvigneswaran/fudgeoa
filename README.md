# FudgeOA

> *A voice of rebellion. Online Assessments reduce intelligence to a binary pass/fail. Companies have the talent and resources to do better. Until they do — this tool exists.*

Clipboard-based LLM agent for macOS. Runs invisibly in the background. Copy a `??`-prefixed question → answer appears in your clipboard within seconds.

---

## How it works

1. Copy any text prefixed with `??` to your clipboard
2. The agent detects the trigger, sends it to Gemini, and pastes the answer back
3. Paste the answer wherever you need it

No window. No dock icon. No visible process (masked as a system service).

---

## Quickstart

```bash
# Install dependencies
pip install -r requirements.txt

# Run
python3 src/main.py --api-key YOUR_GEMINI_KEY
```

Get a free API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

---

## Commands

| Clipboard content | Behaviour |
|---|---|
| `?? <question>` | Fresh answer, no history |
| `??NEW?? <question>` | Explicitly new conversation |
| `??FOLLOW?? <question>` | Continue previous conversation |
| `??MODEL_1??` | Switch to Gemini 2.5 Flash (fast) |
| `??MODEL_2??` | Switch to Gemini 2.5 Pro (deep) |

---

## API key options

```bash
# Option 1 — pass at runtime (recommended)
python3 src/main.py --api-key AIzaSy...

# Option 2 — environment variable
export GEMINI_API_KEY=AIzaSy...
python3 src/main.py

# Option 3 — .env file
echo "GEMINI_API_KEY=AIzaSy..." > ~/.clipboard_agent/.env
python3 src/main.py
```

**Never commit your API key.** `.env` is in `.gitignore`.

---

## Kill the agent

```bash
pkill -f CoreServicesHelper
# or by masked process name
pkill -f 'com.apple.security.pboxd'
```

---

## Build a standalone binary

```bash
pip install pyinstaller
bash scripts/build_stealth.sh
# → dist/CoreServicesHelper  (~36 MB, no Python required)
```

Or using py2app:
```bash
pip install py2app
bash scripts/build_app.sh
```

The compiled binary should be distributed via [GitHub Releases](https://github.com/rahulvigneswaran/fudgeoa/releases), not committed to this repo.

---

## Project structure

```
fudgeoa/
├── src/
│   └── main.py              # core clipboard agent
├── scripts/
│   ├── build_stealth.sh     # PyInstaller build (recommended)
│   └── build_app.sh         # py2app build
├── build_config/
│   └── CoreServicesHelper.spec  # PyInstaller spec
├── tests/
│   ├── verify_clipboard.py
│   ├── verify_advanced.py
│   └── test_stealth.py
├── utils/
│   └── list_models.py       # lists available Gemini models
├── docs/
│   └── index.html           # landing page (GitHub Pages)
├── requirements.txt
└── setup.py                 # py2app config
```

---

## Limitations

- **Paste blocked** — some portals (HackerRank, Codility custom editors) disable `Cmd+V` inside the code editor. Answer lands in clipboard but can't get in.
- **Browser clipboard interception** — a small number of portals overwrite paste content at the JS level.
- **macOS arm64 only** — compiled binary targets Apple Silicon. Intel/Windows/Linux must run from source.
- **Network latency** — Gemini adds 1–4 seconds. On timed-per-question OAs, use `??MODEL_1??` (Flash) for speed.

---

## Requirements

- Python 3.11+
- macOS (arm64 for prebuilt binary)
- [google-genai](https://pypi.org/project/google-genai/) — Gemini SDK
