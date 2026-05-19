from pathlib import Path

def list_files(path):
    files = []

    for file in Path(path).rglob("*"):
        if file.is_file():
            files.append(file)

    return files
