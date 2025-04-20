#!/bin/bash

echo "[*] Installing ForenZilla locally..."

# Step 1: Upgrade pip + install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Step 2: Set install paths
INSTALL_DIR="$HOME/.local/share/ForenZilla"
DESKTOP_DIR="$HOME/.local/share/applications"
DESKTOP_FILE="$DESKTOP_DIR/forenzilla.desktop"
ICON_PATH="$INSTALL_DIR/assets/forenzilla-icon.png"

# Step 3: Create folders
mkdir -p "$INSTALL_DIR"
mkdir -p "$DESKTOP_DIR"

# Step 4: Copy files (ignore .git and venv)
rsync -av --exclude='install.sh' --exclude='.git' --exclude='venv' . "$INSTALL_DIR"

# Step 5: Create launcher Python file
cat > "$INSTALL_DIR/forenzilla_launcher.py" << EOF
#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, "$INSTALL_DIR")
from main import main

if __name__ == "__main__":
    main()
EOF

chmod +x "$INSTALL_DIR/forenzilla_launcher.py"

# Step 6: Create .desktop shortcut
cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Name=ForenZilla
Exec=python3 $INSTALL_DIR/forenzilla_launcher.py
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Utility;Security;Forensics;
EOF

chmod +x "$DESKTOP_FILE"

echo "[✓] Installed to $INSTALL_DIR"
echo "[✓] Desktop launcher created at $DESKTOP_FILE"
echo "→ You may need to log out/in or run: update-desktop-database"
