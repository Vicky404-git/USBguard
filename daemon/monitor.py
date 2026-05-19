import pyudev

from core.mount import safe_mount, unmount
from core.browser import list_files
from core.analyzer import analyze_files
from core.scanner import scan_path
from ui.tui import show_results, menu
from core.sandbox import nuke_drive


def start_monitor():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)

    monitor.filter_by(subsystem="block")

    print("USBguard started")

    try:
        for device in iter(monitor.poll, None):

            if device.device_type != "partition":
                continue

            if device.action != "add":
                continue

            devnode = device.device_node

            print(f"\nUSB detected: {devnode}")

            sandbox_path = safe_mount(devnode)

            if not sandbox_path:
                continue

            try:
                files = list_files(sandbox_path)

                results = analyze_files(files)

                scan_path(sandbox_path)

                show_results(results)

                menu()

                choice = input("\nChoice: ")

                if choice == "1":
                    for idx, file in enumerate(files):
                        print(f"[{idx}] {file}")

                    selected = input("\nSelect file index: ")
                    try:
                        selected_file = files[int(selected)]
                        from core.opener import open_file
                        open_file(str(selected_file))
                    except Exception as e:
                        print(f"Error: {e}")

                elif choice == "2":
                    print("Exiting USB session")
                    # Unmount happens in the finally block

                elif choice == "3":
                    confirm = input(f"Are you sure you want to format {devnode}? (y/N): ")
                    if confirm.lower() == 'y':
                        nuke_drive(devnode)
                        print("Drive wiped. Exiting session.")
                    else:
                        print("Format aborted.")

            finally:
                unmount()

    except KeyboardInterrupt:
        print("\nUSBguard stopped")
