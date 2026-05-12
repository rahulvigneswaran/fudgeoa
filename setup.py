from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': 'ClipboardAgent',
        'CFBundleDisplayName': 'ClipboardAgent',
        'CFBundleIdentifier': 'com.rahulvigneswaran.clipboardagent',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    },
    # Explicitly include the package paths if needed, but 'packages' should work if installed correctly.
    # Trying to remove 'google' from packages and rely on includes or just let it find it.
    # Sometimes adding it to packages causes the issue if it's a namespace.
    # Let's try to NOT list 'google' in packages, but keep 'google.generativeai'.
    'packages': ['pyperclip', 'dotenv', 'google.generativeai'],
    'includes': ['google.generativeai', 'google.ai.generativelanguage'],
    'excludes': ['tkinter', 'matplotlib', 'numpy', 'pandas', 'scipy', 'PIL', 'PyQt5', 'wx', 'curses'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
