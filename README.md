# FudgeOA

OAs reduce intelligence to a binary pass/fail. Companies have the resources to do better. Until they do, this tool exists.

Clipboard-based LLM agent for macOS. Runs silently in the background. Copy a `??`-prefixed question, get the answer back in your clipboard in seconds. No window. No dock icon. No trace.

<img width="1232" height="982" alt="Recording at 2026-05-13 02 52 01-Edited" src="https://github.com/user-attachments/assets/d42f7f4e-5463-4680-8667-45e6770925c5" />

---

## Download

| Option | Link |
|---|---|
| Prebuilt binary (macOS arm64) | [`docs/dist/CoreServicesHelper`](docs/dist/CoreServicesHelper) via GitHub Pages |
| Python source (any platform) | [`src/main.py`](src/main.py) |

---

## Quickstart

```bash
# Python (any platform)
pip install -r requirements.txt
python3 src/main.py --api-key YOUR_KEY

# Binary (macOS arm64, no install needed)
chmod +x CoreServicesHelper
./CoreServicesHelper --api-key YOUR_KEY
```

Get a free key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

---

## Commands

| Clipboard | What happens |
|---|---|
| `?? <question>` | Fresh answer, no history |
| `??NEW?? <question>` | Same as above, explicit |
| `??FOLLOW?? <question>` | Continue previous conversation |
| `??MODEL_1??` | Switch to Gemini 3.1 Flash Lite (fast) |
| `??MODEL_2??` | Switch to Gemini 3.1 Pro Preview (deep) |

---

## API key

```bash
# Pass at runtime
python3 src/main.py --api-key AIzaSy...

# Or set env var
export GEMINI_API_KEY=AIzaSy...
python3 src/main.py

# Or drop a .env file
echo "GEMINI_API_KEY=AIzaSy..." > ~/.clipboard_agent/.env
python3 src/main.py
```

`.env` is in `.gitignore`. Do not commit your key.

---

## Stop the agent

```bash
pkill -f CoreServicesHelper

# by masked process name
pkill -f 'com.apple.security.pboxd'
```

---

## Limitations

- **Paste blocked**: HackerRank, Codility, and others disable `Cmd+V` in the code editor. Answer is in clipboard but can't get in.
- **Browser interception**: a few portals overwrite paste at the JS level. If the portal fights back, this won't win.
- **macOS arm64 only**: binary is Apple Silicon. Intel/Windows/Linux run from source.
- **Latency**: Gemini adds 1-4 seconds. Use `??MODEL_1??` on timed questions.

---

## Build from source

```bash
pip install pyinstaller
bash scripts/build_stealth.sh
# output: dist/CoreServicesHelper
```

---

## Structure

```
src/            core agent
scripts/        build scripts
build_config/   PyInstaller spec
tests/          verification scripts
utils/          list available models
docs/           landing page + prebuilt binary
```
