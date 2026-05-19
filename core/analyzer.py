SUSPICIOUS_EXTENSIONS = [
    ".exe",
    ".bat",
    ".cmd",
    ".scr",
    ".ps1",
    ".sh",
    ".apk",
]

SUSPICIOUS_NAMES = [
    "autorun.inf",
]

def analyze_files(files):
    results = []

    for file in files:
        risk = 0
        reasons = []

        if file.suffix.lower() in SUSPICIOUS_EXTENSIONS:
            risk += 50
            reasons.append("Executable file")

        if file.name.lower() in SUSPICIOUS_NAMES:
            risk += 30
            reasons.append("Autorun detected")

        if file.name.startswith("."):
            risk += 10
            reasons.append("Hidden file")

        results.append({
            "file": str(file),
            "risk": risk,
            "reasons": reasons
        })

    return results
