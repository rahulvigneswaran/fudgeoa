#!/bin/bash
set -e

echo "Installing pyinstaller..."
pip install pyinstaller

echo "Building CoreServicesHelper..."
pyinstaller --noconsole --onefile --name "CoreServicesHelper" \
    --hidden-import=google.genai \
    --hidden-import=setproctitle \
    --exclude-module=matplotlib \
    --exclude-module=numpy \
    --exclude-module=pandas \
    --exclude-module=scipy \
    --exclude-module=PIL \
    --exclude-module=tkinter \
    src/main.py

echo "Build complete. Executable is in dist/CoreServicesHelper"
