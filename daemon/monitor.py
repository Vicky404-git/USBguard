import pyudev
from rich.console import Console
from rich.panel import Panel

from core.mount import safe_mount

console = Console()

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)

monitor.filter_by(subsystem="block")

console.print(
    "[bold green]USBguard started... waiting for USB devices[/bold green]\n"
)

for device in iter(monitor.poll, None):

    try:
        if device.action == "add":

            if device.device_type == "partition":

                if device.get("ID_BUS") == "usb":

                    devnode = device.device_node
                    size = device.get("ID_FS_SIZE", "Unknown")
                    fs = device.get("ID_FS_TYPE", "Unknown")
                    label = device.get("ID_FS_LABEL", "No Label")

                    console.print(
                        Panel.fit(
                            f"[bold cyan]USB DETECTED[/bold cyan]\n\n"
                            f"Device: {devnode}\n"
                            f"Filesystem: {fs}\n"
                            f"Label: {label}\n"
                            f"Size: {size}",
                            title="USBguard"
                        )
                    )

                    safe_mount(devnode)

    except KeyboardInterrupt:
        console.print("\n[bold red]USBguard stopped[/bold red]")
        break

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
