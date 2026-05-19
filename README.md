# USBguard

> A paranoid USB isolation + analysis tool for Linux.  
> Automatically mounts external drives in a restricted environment, scans them, analyzes suspicious files, and lets you safely inspect content before trusting it.

Built for people who plug random USBs into their machine and instantly regret it.

---

## Features

- 🔒 Read-only USB mounting
- 🛡️ `nosuid`, `nodev`, `noexec` protection
- 🦠 ClamAV malware scanning
- ⚠️ Suspicious file analysis
- 📂 Recursive file browser
- 🧪 Sandboxed file opening with Firejail
- 💣 Full USB wipe / FAT32 reformat option
- 👀 Live USB monitoring via `pyudev`
- 🖥️ Rich terminal UI
- ⚡ Lightweight + keyboard-driven

---

# How It Works

When a USB is plugged in:

1. `pyudev` detects the device automatically
2. USB is mounted safely in read-only mode
3. Files are recursively indexed
4. Suspicious files are analyzed
5. ClamAV scan is executed
6. Results are displayed in a TUI interface
7. Files can optionally be opened in a network-isolated Firejail sandbox

---

# Architecture

```text
USBguard
├── daemon/
│   └── monitor.py
│
├── core/
│   ├── analyzer.py
│   ├── browser.py
│   ├── mount.py
│   ├── opener.py
│   ├── sandbox.py
│   └── scanner.py
│
├── ui/
│   └── tui.py
│
├── rules/
│   └── 99-usbguard.rules
│
├── reports/
├── logs/
├── sandbox/
├── main.py
└── pyproject.toml
```

---

# Tech Stack

- Python 3.13
- pyudev
- Rich
- ClamAV
- Firejail
- Linux udev
- FAT32 tools
- subprocess-based system integration

---

# Installation

## Clone

```bash
git clone https://github.com/Vicky404-git/USBguard.git
cd USBguard
```

---

## Install Dependencies

### Debian / Ubuntu

```bash
sudo apt install clamav firejail python3-pip
```

### Arch Linux

```bash
sudo pacman -S clamav firejail python-pip
```

---

## Python Packages

```bash
pip install pyudev rich
```

or using uv:

```bash
uv sync
```

---

# Run

```bash
python main.py
```

---

# Example Workflow

```text
USB detected: /dev/sdb1

Mounted safely:
 /dev/sdb1 -> /mnt/quarantine

Running ClamAV scan...

┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Index ┃ File                  ┃ Risk ┃ Reasons           ┃
┣━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ 0     ┃ autorun.inf           ┃ 30   ┃ Autorun detected  ┃
┃ 1     ┃ payload.exe           ┃ 50   ┃ Executable file   ┃
┗━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━┻━━━━━━━━━━━━━━━━━━━┛

[1] Open file safely
[2] Exit & Unmount
[3] NUKE DRIVE
```

---

# Safe File Opening

Text files are opened using:

```bash
bat
```

Media/PDF files are opened inside a restricted Firejail sandbox:

```bash
firejail --net=none --private
```

Blocked extensions:

- `.exe`
- `.bat`
- `.cmd`
- `.scr`
- `.ps1`
- `.apk`
- `.sh`

---

# Dangerous Mode

USBguard includes an optional drive wipe feature.

Selecting:

```text
[3] NUKE DRIVE
```

Will:

- unmount the drive
- wipe filesystem metadata
- format the device as FAT32

---

# Security Model

USBguard assumes:

- every USB is hostile
- executables should never auto-run
- suspicious files should be isolated
- removable devices deserve sandboxing

Mounted drives are protected using:

```text
ro,nosuid,nodev,noexec
```

This prevents:

- executable payload execution
- device node abuse
- privilege escalation
- accidental modification

---

# Philosophy

Modern operating systems trust USB devices too quickly.

USBguard is built around a simple principle:

> Inspect first. Trust later.

The project is inspired by:

- malware analysis workflows
- forensic isolation systems
- sandbox-first security
- paranoid Linux setups

---

# Roadmap

- [ ] VM-based file opening
- [ ] YARA rule support
- [ ] PDF exploit heuristics
- [ ] SHA256 reputation database
- [ ] Web dashboard
- [ ] AI-assisted malware classification
- [ ] Per-device trust profiles
- [ ] Read-only overlay filesystem
- [ ] Automatic backup before wipe
- [ ] Live notification daemon
- [ ] Device history tracking

---

# Warning

This tool interacts directly with:

- block devices
- mount points
- filesystem formatting
- sandboxed execution

Use carefully.

Especially the nuke option.

---

# License

MIT License

---

# Author

***`Vicky404`***

> Built for terminal addicts who don't trust USB drives.
