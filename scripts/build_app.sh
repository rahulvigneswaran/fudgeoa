#!/bin/bash
set -e

echo "Installing py2app..."
pip install py2app

echo "Building ClipboardAgent.app..."
python3 setup.py py2app

echo "Build complete. App is in dist/ClipboardAgent.app"
