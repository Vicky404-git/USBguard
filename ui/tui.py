from rich.console import Console
from rich.table import Table

console = Console()

def show_results(results):
    table = Table(title="USB Analysis")
    table.add_column("Index")
    table.add_column("File")
    table.add_column("Risk")
    table.add_column("Reasons")

    for idx, item in enumerate(results):
        table.add_row(
            str(idx),
            item["file"],
            str(item["risk"]),
            ", ".join(item["reasons"])
        )
    console.print(table)

def menu():
    console.print("\n[1] Open file safely")
    console.print("[2] Exit & Unmount")
    console.print("[3] [bold red]NUKE DRIVE (Format FAT32)[/bold red]")
