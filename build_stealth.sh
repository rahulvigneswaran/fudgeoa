#!/bin/bash
set -e

echo "Installing pyinstaller..."
pip install pyinstaller

echo "Building CoreServicesHelper..."
# --noconsole: Hide terminal window
# --name: Stealthy name
# --onefile: Single executable
# --hidden-import: Explicitly include google.generativeai
pyinstaller --noconsole --onefile --name "CoreServicesHelper" \
    --hidden-import=google.generativeai \
    --hidden-import=google.ai.generativelanguage \
    --hidden-import=setproctitle \
    --exclude-module=matplotlib \
    --exclude-module=numpy \
    --exclude-module=pandas \
    --exclude-module=scipy \
    --exclude-module=PIL \
    --exclude-module=tkinter \
    main.py

echo "Build complete. Executable is in dist/CoreServicesHelper"
