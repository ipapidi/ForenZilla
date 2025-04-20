import re
import os

def parse_email_header(file_path):
    try:
        if file_path.endswith(".rtf"):
            from striprtf.striprtf import rtf_to_text
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_data = rtf_to_text(f.read())
        else:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_data = f.read()

        output = []

        # Basic metadata
        metadata_fields = ["From", "To", "Subject", "Date", "Reply-To", "Message-ID"]
        for field in metadata_fields:
            match = re.search(rf"{field}:\s*(.+)", raw_data, re.IGNORECASE)
            if match:
                output.append(f"{field}: {match.group(1).strip()}")

        # X-Originating-IP (if present)
        x_ip = re.search(r"X-Originating-IP:\s*\[?([^\]]+)\]?", raw_data, re.IGNORECASE)
        if x_ip:
            output.append(f"Originating IP: {x_ip.group(1).strip()}")

        # Received hops (reverse mail path)
        received = re.findall(r"Received:\s*(.+?);", raw_data, re.IGNORECASE | re.DOTALL)
        if received:
            output.append("\n--- Mail Path Traceback ---")
            for i, hop in enumerate(reversed(received)):
                cleaned = " ".join(hop.split())
                output.append(f"Hop {i+1}: {cleaned}")

        return output if output else ["No recognizable headers found."]
    
    except Exception as e:
        return [f"Error parsing header: {e}"]