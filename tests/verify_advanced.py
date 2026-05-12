import time
import pyperclip
import sys

def verify_advanced():
    print("Starting advanced verification...")
    
    # 1. Test Model Switch to Pro
    print("\n[Test 1] Switching to Model 2 (Pro)...")
    pyperclip.copy("??MODEL_2??")
    time.sleep(5)
    res = pyperclip.paste()
    if "Switched to gemini-2.0-pro" in res:
        print("PASS: Model switch to Pro successful.")
    else:
        print(f"FAIL: Model switch to Pro failed. Got: {res}")

    # 2. Test Switch back to Flash
    print("\n[Test 2] Switching back to Model 1 (Flash)...")
    pyperclip.copy("??MODEL_1??")
    time.sleep(5)
    res = pyperclip.paste()
    if "Switched to gemini-2.0-flash" in res:
        print("PASS: Model switch to Flash successful.")
    else:
        print(f"FAIL: Model switch to Flash failed. Got: {res}")

    # 3. Test New Conversation (on Flash)
    print("\n[Test 3] New Conversation...")
    pyperclip.copy("??NEW?? What is 10 + 10?")
    time.sleep(10)
    res = pyperclip.paste()
    if "20" in res:
        print("PASS: New conversation successful.")
    else:
        print(f"FAIL: New conversation failed. Got: {res}")

    # 4. Test Follow-up
    print("\n[Test 4] Follow-up...")
    pyperclip.copy("??FOLLOW?? Add 5 to it.")
    time.sleep(10)
    res = pyperclip.paste()
    if "25" in res:
        print("PASS: Follow-up successful (Context retained).")
    else:
        print(f"FAIL: Follow-up failed. Got: {res}")

    # 5. Test Reset (Implicit NEW)
    print("\n[Test 5] Implicit NEW (Stateless check)...")
    pyperclip.copy("?? What is the capital of France?")
    time.sleep(10)
    res = pyperclip.paste()
    if "Paris" in res:
        print("PASS: Implicit NEW successful.")
    else:
        print(f"FAIL: Implicit NEW failed. Got: {res}")

if __name__ == "__main__":
    verify_advanced()
