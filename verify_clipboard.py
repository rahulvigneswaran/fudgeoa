import time
import pyperclip
import sys

def verify():
    print("Starting verification...")
    
    # Initial state
    trigger_text = "?? Write a python function to add two numbers"
    print(f"Copying trigger text: {trigger_text}")
    pyperclip.copy(trigger_text)
    
    # Wait for processing
    print("Waiting for 10 seconds...")
    time.sleep(10)
    
    # Check result
    result = pyperclip.paste()
    print(f"Current clipboard content: {result}")
    
    if "def add" in result or "return" in result:
        print("SUCCESS: Clipboard updated with code.")
        sys.exit(0)
    elif result == trigger_text:
        print("FAILURE: Clipboard content did not change.")
        sys.exit(1)
    else:
        print("WARNING: Clipboard changed but content is unexpected.")
        print(f"Content: {result}")
        sys.exit(1)

if __name__ == "__main__":
    verify()
