import subprocess
from pathlib import Path
from rich.console import Console

console = Console()

MOUNT_DIR = "/mnt/quarantine"


def safe_mount(device: str):
    Path(MOUNT_DIR).mkdir(parents=True, exist_ok=True)

    cmd = [
        "sudo",
        "mount",
        "-o",
        "ro,nosuid,nodev,noexec",
        device,
        MOUNT_DIR
    ]

    try:
        subprocess.run(cmd, check=True)

        console.print(
            f"[bold green]Mounted safely:[/bold green] "
            f"{device} -> {MOUNT_DIR}"
        )

        return MOUNT_DIR

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Mount failed:[/red] {e}")
        return None


def unmount():
    try:
        subprocess.run(
            ["sudo", "umount", MOUNT_DIR],
            check=True
        )

        console.print(
            f"[bold yellow]Unmounted:[/bold yellow] {MOUNT_DIR}"
        )

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Unmount failed:[/red] {e}")
