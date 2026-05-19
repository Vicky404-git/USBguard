import subprocess

def scan_path(path):
    print("\nRunning ClamAV scan...\n")

    subprocess.run([
        "clamscan",
        "-r",
        path
    ])
