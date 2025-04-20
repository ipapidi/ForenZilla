import os

# Add more file signatures: (extension: (header, footer/None, use_footer))
SIGNATURES = {
    "jpg": (b"\xff\xd8", b"\xff\xd9", True),
    "png": (b"\x89PNG\r\n\x1a\n", b"IEND", True),
    "pdf": (b"%PDF", b"%%EOF", True),
    "zip": (b"PK\x03\x04", b"PK\x05\x06", True),
    "docx": (b"PK\x03\x04", b"PK\x05\x06", True),
    "doc": (bytes.fromhex("D0CF11E0A1B11AE1"), None, False),
    "xls": (bytes.fromhex("D0CF11E0A1B11AE1"), None, False),
    "rtf": (b"{\\rtf", b"}", True),
    "mp3": (b"ID3", None, False),
    "mp4": (b"\x00\x00\x00", None, False),  # simplified for demo
}

MAX_SIZE = 5 * 1024 * 1024  # 5 MB max carve size

def carve_files(image_path, output_dir="reports/carved"):
    os.makedirs(output_dir, exist_ok=True)
    results = []

    with open(image_path, "rb") as f:
        data = f.read()

    for ext, (header, footer, use_footer) in SIGNATURES.items():
        start = 0
        count = 0
        while True:
            header_index = data.find(header, start)
            if header_index == -1:
                break

            if use_footer and footer:
                footer_index = data.find(footer, header_index + len(header))
                if footer_index == -1:
                    start = header_index + len(header)
                    continue
                end_index = footer_index + len(footer)
            else:
                end_index = header_index + MAX_SIZE

            file_data = data[header_index:end_index]

            carved_file_path = os.path.join(output_dir, f"{ext}_carved_{count}.{ext}")
            with open(carved_file_path, "wb") as out:
                out.write(file_data)

            results.append(f"Recovered: {carved_file_path}")
            count += 1
            start = end_index

    return results if results else ["No files recovered."]
