import setproctitle
import time
import os

print(f"Original PID: {os.getpid()}")
print("Setting title to 'com.apple.security.pboxd'...")
setproctitle.setproctitle("com.apple.security.pboxd")
print("Title set. Sleeping for 30 seconds. Check 'ps' now.")
time.sleep(30)
