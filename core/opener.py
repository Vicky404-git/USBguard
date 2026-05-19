import subprocess
from pathlib import Path

SAFE_TEXT = [".txt", ".md", ".log", ".json", ".csv", ".py"]
SAFE_MEDIA = [".png", ".jpg", ".jpeg", ".mp4", ".mp3", ".pdf"]

def open_file(path):
    ext = Path(path).suffix.lower()

    if ext in SAFE_TEXT:
        # bat is inherently safe for text
        subprocess.run(["bat", path])

    elif ext in SAFE_MEDIA:
        # Launch the media in an isolated, network-disabled jail
        print(f"Opening {path} in isolated sandbox...")
        subprocess.run([
            "firejail", 
            "--net=none",               # Block internet access
            "--private",                # Give it a temporary fake home directory
            "--read-only=/mnt/quarantine", 
            "xdg-open", 
            path
        ])
    else:
        print(f"Blocked suspicious file type: {ext}")
