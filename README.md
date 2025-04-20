<p align="center">
  <img src="assets/forenzilla_icon.png" width="150" alt="ForenZilla Logo">
</p>

<h1 align="center">ForenZilla</h1>
<p align="center">A modular digital forensics toolkit with a clean GUI for fast evidence triage and analysis.</p>

---

## Disclaimer

This tool is intended for educational and lawful forensic investigations only.  
**Do not use ForenZilla on systems you do not own or have explicit authorization to analyze.**  

> Use caution and work with copies of original evidence to maintain forensic integrity.

---

## Features

<table>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>File Hasher</td>
    <td>Generates MD5 and SHA256 hashes for verifying file integrity</td>
  </tr>
  <tr>
    <td>Browser History</td>
    <td>Extracts visit logs from Chrome SQLite databases</td>
  </tr>
  <tr>
    <td>LNK Parser</td>
    <td>Reads metadata from Windows shortcut (.lnk) files</td>
  </tr>
  <tr>
    <td>PCAP Analyzer</td>
    <td>Processes .pcap and .pcapng files to detect Wi-Fi frames and deauth packets</td>
  </tr>
  <tr>
    <td>EXIF Extractor</td>
    <td>Extracts image metadata, including GPS coordinates and camera info</td>
  </tr>
  <tr>
    <td>File Carver</td>
    <td>Finds embedded files inside raw data using known magic signatures</td>
  </tr>
  <tr>
    <td>Email Header Analyzer</td>
    <td>Parses metadata from .eml, .txt, and .rtf email headers</td>
  </tr>
  <tr>
    <td>Log Viewer</td>
    <td>Opens and reads the tool’s action log with timestamps</td>
  </tr>
</table>

---

## Installation

### Option 1: Clone with Git (recommended)

```bash
git clone https://github.com/ipapidi/ForenZilla.git
cd ForenZilla
chmod +x install.sh
./install.sh
```

### Option 2: Download Manually

1. [Download the ZIP](https://github.com/ipapidi/ForenZilla/archive/refs/heads/main.zip)  
2. Extract the contents  
3. Open a terminal in the extracted folder and run:

```bash
chmod +x install.sh
./install.sh
```
---

## Python Package Setup

> You **must** install the following packages before running ForenZilla:

### Linux (Kali, Mint, Ubuntu):

```bash
sudo apt install tshark xdg-utils -y
pip3 install pyqt5 pylnk3 pandas pyshark striprtf olefile Pillow pefile --break-system-packages
mkdir -p logs && touch logs/actions.log
```

### MacOS:

> You **must** install [Homebrew](https://brew.sh), then:

```bash
brew install tshark
pip3 install pyqt5 pylnk3 pandas pyshark striprtf olefile Pillow pefile
mkdir -p logs && touch logs/actions.log
```

---

## Folder Overview

<table>
  <tr>
    <th>File/Folder</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>main.py</code></td>
    <td>Main PyQt5 GUI codebase</td>
  </tr>
  <tr>
    <td><code>modules/</code></td>
    <td>All functional modules (hashing, carving, parsing, etc)</td>
  </tr>
  <tr>
    <td><code>logs/</code></td>
    <td>Auto-generated action log with timestamps</td>
  </tr>
  <tr>
    <td><code>reports/</code></td>
    <td>Reserved for exports or future report functionality</td>
  </tr>
  <tr>
    <td><code>assets/forenzilla_icon.png</code></td>
    <td>App icon used in GUI and launcher</td>
  </tr>
  <tr>
    <td><code>logs/</code> folder</td>
    <td>Must be manually created: <code>mkdir -p logs && touch logs/actions.log</code></td>
  </tr>

  <tr>
    <td><code>forenzilla_launcher.py</code></td>
    <td>Entry point for `.desktop` launch integration</td>
  </tr>
  <tr>
    <td><code>install.sh</code></td>
    <td>Installer for local deployment and desktop shortcut</td>
  </tr>
</table>

---

## System Requirements

<table>
  <tr>
    <th>Component</th>
    <th>Requirement</th>
  </tr>
  <tr>
    <td>Python</td>
    <td>Python 3.8 or later</td>
  </tr>
  <tr>
    <td>OS</td>
    <td>macOS or Linux (Debian-based recommended)</td>
  </tr>
  <tr>
    <td>GUI</td>
    <td>PyQt5</td>
  </tr>
  <tr>
    <td>Log File Opener (Linux)</td>
    <td><code>xdg-utils</code> (for opening logs via GUI)<br><em>Install with:</em><br><code>sudo apt install xdg-utils</code></td>
  </tr>
</table>

---

## License

MIT License — See the [LICENSE](LICENSE) file for full legal info.

---

## Author

**Ioli Papidi**  
GitHub: [@ipapidi](https://github.com/ipapidi)
