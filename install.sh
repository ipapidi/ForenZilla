#!/bin/bash

echo "[*] Installing ForenZilla locally..."

# Step 1: Set install paths
INSTALL_DIR="$HOME/.local/share/ForenZilla"
DESKTOP_DIR="$HOME/.local/share/applications"
DESKTOP_FILE="$DESKTOP_DIR/forenzilla.desktop"
ICON_PATH="$INSTALL_DIR/assets/forenzilla_icon.png"

# Step 2: Create required folders
mkdir -p "$INSTALL_DIR"
mkdir -p "$DESKTOP_DIR"
mkdir -p "$INSTALL_DIR/logs"
touch "$INSTALL_DIR/logs/actions.log"

# Step 3: Copy all files except excluded ones
rsync -av --exclude='install.sh' --exclude='.git' --exclude='venv' . "$INSTALL_DIR"

# Step 4: Create launcher Python file
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

# Step 5: Create .desktop shortcut
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

echo ""
echo "[✓] Installed to $INSTALL_DIR"
echo "[✓] Desktop launcher created at $DESKTOP_FILE"
echo "Log folder: $INSTALL_DIR/logs"
echo ""
echo "To launch ForenZilla, search for it in your system menu or run:"
echo "   python3 $INSTALL_DIR/forenzilla_launcher.py"
echo ""
echo "If the launcher doesn't appear immediately, try:"
echo "   update-desktop-database $DESKTOP_DIR"
