#!/usr/bin/env python3

import os
import sys

# Add install directory to Python path to import modules
INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, INSTALL_DIR)

from main import main  # Ensure 'main.py' has a callable main() function

if __name__ == "__main__":
    main()
