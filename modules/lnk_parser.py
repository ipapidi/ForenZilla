import pylnk3
import os

def parse_lnk(file_path):
    if not os.path.exists(file_path):
        return ["Error: File does not exist."]
    
    try:
        lnk = pylnk3.parse(file_path)
        output = []
        output.append(f"Shortcut Path: {file_path}")
        output.append(f"Target Path: {lnk.path}")
        output.append(f"Arguments: {lnk.arguments}")
        output.append(f"Working Dir: {lnk.working_dir}")
        output.append(f"Access Time: {lnk.access_time}")
        output.append(f"Creation Time: {lnk.creation_time}")
        output.append(f"Modification Time: {lnk.modification_time}")
        return output
    except Exception as e:
        return [f"Error parsing .lnk file: {e}"]
