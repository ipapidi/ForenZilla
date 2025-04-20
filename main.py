import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QTextEdit
from modules.logger import log_action
from modules.history import extract_history
from modules.lnk_parser import parse_lnk
from modules.pcap_analyzer import analyze_pcap
from modules.exif_parser import extract_exif
from modules.file_carver import carve_files
from modules.email_header_parser import parse_email_header

class ForenZilla(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ForenZilla - Digital Forensics Toolkit")
        self.setGeometry(300, 300, 500, 400)

        self.layout = QVBoxLayout()

        # Section label
        self.label = QLabel("Choose a forensic task:")
        self.layout.addWidget(self.label)

        # Hash file button
        self.btn_hash = QPushButton("Hash a File")
        self.btn_hash.clicked.connect(self.hash_file)
        self.layout.addWidget(self.btn_hash)

        # View log button
        self.btn_view_log = QPushButton("View Action Log")
        self.btn_view_log.clicked.connect(self.open_log_file)
        self.layout.addWidget(self.btn_view_log)

        # Output area
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        # Forensic modules
        self.btn_history = QPushButton("Extract Browser History")
        self.btn_history.clicked.connect(self.extract_browser_history)
        self.layout.addWidget(self.btn_history)

        self.btn_lnk = QPushButton("Parse LNK Shortcut")
        self.btn_lnk.clicked.connect(self.parse_lnk_file)
        self.layout.addWidget(self.btn_lnk)

        self.btn_pcap = QPushButton("Analyze PCAP File")
        self.btn_pcap.clicked.connect(self.analyze_pcap_file)
        self.layout.addWidget(self.btn_pcap)

        self.btn_exif = QPushButton("Extract EXIF from Image")
        self.btn_exif.clicked.connect(self.extract_exif_data)
        self.layout.addWidget(self.btn_exif)

        self.btn_carve = QPushButton("Carve Deleted Files")
        self.btn_carve.clicked.connect(self.carve_deleted_files)
        self.layout.addWidget(self.btn_carve)

        self.btn_email = QPushButton("Analyze Email Header")
        self.btn_email.clicked.connect(self.analyze_email_header)
        self.layout.addWidget(self.btn_email)

        self.setLayout(self.layout)


    def hash_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Hash")
        if file_path:
            import hashlib
            md5 = hashlib.md5()
            sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                data = f.read()
                md5.update(data)
                sha256.update(data)
        
            self.output.append(f"\nFile: {file_path}")
            self.output.append(f"MD5: {md5.hexdigest()}")
            self.output.append(f"SHA256: {sha256.hexdigest()}")

            log_action(f"Hashed File: {file_path} | MD5: {md5.hexdigest()} | SHA256: {sha256.hexdigest()}")

    def open_log_file(self):
        import subprocess
        import platform

        log_path = os.path.join("logs", "actions.log")

        if os.path.exists(log_path):
            system = platform.system()
            try:
                if system == "Darwin":  # macos
                    subprocess.run(["open", log_path])
                elif system == "Linux":
                    subprocess.run(["xdg-open", log_path])
                elif system == "Windows":
                    os.startfile(log_path)
                else:
                    self.output.append(f"Cannot open file on unsupported OS: {system}")
            except Exception as e:
                self.output.append(f"Error opening log file: {e}")
        else:
            self.output.append("Log file not found.")

    def extract_browser_history(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Chrome History SQLite File")
        if file_path:
            results = extract_history(file_path)
            self.output.append("\n--- Browser History ---")
        
            log_action(f"Extracted browser history from {file_path}")
        
            for line in results:
                self.output.append(line)
                log_action(f"[History Entry] {line}")

    def parse_lnk_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select .lnk Shortcut File")
        if file_path:
            results = parse_lnk(file_path)
            self.output.append("\n--- LNK Shortcut Analysis ---")
            for line in results:
                self.output.append(line)
                log_action(f"[LNK] {line}")

    def analyze_pcap_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PCAP or PCAPNG File", filter="PCAP Files (*.pcap *.pcapng)")
        if file_path:
            results = analyze_pcap(file_path)
            self.output.append("\n--- PCAP Analysis ---")
            for line in results:
                self.output.append(line)
                log_action(f"[PCAP] {line}")

    def extract_exif_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select an Image File", filter="Images (*.jpg *.jpeg *.png)")
        if file_path:
            results = extract_exif(file_path)
            self.output.append(f"\n--- EXIF Metadata for {file_path} ---")
            for line in results:
                self.output.append(line)
                log_action(f"[EXIF] {line}")

    def carve_deleted_files(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Disk Image File", filter="Raw Disk (*.dd *.img *.bin)")
        if file_path:
            results = carve_files(file_path)
            self.output.append(f"\n--- File Carving Results for {file_path} ---")
            for line in results:
                self.output.append(line)
                log_action(f"[Carver] {line}")

    def analyze_email_header(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Email Header File", filter="Email Headers (*.eml *.txt)")
        if file_path:
            results = parse_email_header(file_path)
            self.output.append(f"\n--- Email Header Analysis for {file_path} ---")
            for line in results:
                self.output.append(line)
                log_action(f"[Email] {line}")

def main():
    app = QApplication(sys.argv)
    window = ForenZilla()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
