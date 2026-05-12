import argparse
import time
import os
import sys
import pyperclip
from google import genai
from google.genai import types
from dotenv import load_dotenv

import logging
from pathlib import Path
import setproctitle

# Mask process name immediately
setproctitle.setproctitle("com.apple.security.pboxd")

# Configure logging
LOG_DIR = Path.home() / ".clipboard_agent"
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / "agent.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def resolve_api_key(cli_key: str | None) -> str:
    if cli_key:
        logging.info("Using API key from --api-key argument.")
        return cli_key
    load_dotenv(dotenv_path=LOG_DIR / ".env")
    key = os.getenv("GEMINI_API_KEY")
    if key:
        logging.info("Using API key from environment / .env file.")
        return key
    logging.error("No GEMINI_API_KEY found.")
    print("Error: provide API key via --api-key YOUR_KEY or set GEMINI_API_KEY env var.")
    sys.exit(1)

# Constants
TRIGGER_PREFIX = "??"
CMD_NEW = "NEW??"
CMD_FOLLOW = "FOLLOW??"
CMD_MODEL_1 = "MODEL_1??"
CMD_MODEL_2 = "MODEL_2??"

MODEL_1_NAME = "gemini-2.5-flash"
MODEL_2_NAME = "gemini-2.5-pro"

SYSTEM_PROMPT = (
    "You are an expert coding assistant. "
    "Your default language for code examples is Python unless specified otherwise. "
    "Provide concise, correct, and efficient code solutions."
)

class ClipboardAgent:
    def __init__(self, client: genai.Client):
        self.client = client
        self.model_name = MODEL_1_NAME
        self.chat = self._new_chat()
        logging.info(f"Agent initialized with model: {self.model_name}")

    def _new_chat(self, history=None):
        return self.client.chats.create(
            model=self.model_name,
            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
            history=history or [],
        )

    def switch_model(self, model_name):
        if self.model_name == model_name:
            return f"Already using {model_name}"
        logging.info(f"Switching model to {model_name}...")
        history = self.chat.get_history()
        self.model_name = model_name
        self.chat = self._new_chat(history=history)
        return f"Switched to {model_name}"

    def clear_history(self):
        self.chat = self._new_chat()
        logging.info("History cleared.")

    def process_request(self, text):
        content = text[len(TRIGGER_PREFIX):].strip()

        if content.startswith(CMD_NEW):
            prompt = content[len(CMD_NEW):].strip()
            self.clear_history()
            return self._generate(prompt)

        elif content.startswith(CMD_FOLLOW):
            prompt = content[len(CMD_FOLLOW):].strip()
            return self._generate(prompt)

        elif content.startswith(CMD_MODEL_1):
            return self.switch_model(MODEL_1_NAME)

        elif content.startswith(CMD_MODEL_2):
            return self.switch_model(MODEL_2_NAME)

        else:
            self.clear_history()
            return self._generate(content)

    def _generate(self, prompt):
        if not prompt:
            return None
        logging.info(f"Processing: {prompt!r} (history len: {len(self.chat.get_history())})")
        try:
            response = self.chat.send_message(prompt)
            return response.text
        except Exception as e:
            logging.error(f"Error generating content: {e}")
            return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Clipboard LLM Agent")
    parser.add_argument(
        "--api-key", "-k",
        metavar="KEY",
        help="Gemini API key (overrides GEMINI_API_KEY env var)"
    )
    args = parser.parse_args()

    api_key = resolve_api_key(args.api_key)
    client = genai.Client(api_key=api_key)
    logging.info("Starting Clipboard Agent...")

    agent = ClipboardAgent(client)
    logging.info(f"Monitoring clipboard. Trigger: '{TRIGGER_PREFIX}'")
    print(f"Clipboard agent running. Trigger: '{TRIGGER_PREFIX}'. Ctrl+C to stop.")

    last_text = pyperclip.paste()

    while True:
        try:
            current_text = pyperclip.paste()

            if current_text != last_text:
                last_text = current_text

                if current_text.startswith(TRIGGER_PREFIX):
                    logging.info("Trigger detected!")
                    result = agent.process_request(current_text)

                    if result:
                        pyperclip.copy(result)
                        last_text = result
                        logging.info("Clipboard updated.")

            time.sleep(0.5)

        except KeyboardInterrupt:
            logging.info("Stopping monitor.")
            print("\nStopped.")
            break
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
