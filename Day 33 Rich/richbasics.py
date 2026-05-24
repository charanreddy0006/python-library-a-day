from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

# --- create console ---
console = Console()

# --- styled text ---
console.print("Welcome to Rich Library!", style="bold green")

console.print("Python makes CLI beautiful 🚀", style="bold cyan")

# --- create table ---
table = Table(title="Student Marks")

table.add_column("Name", style="magenta")
table.add_column("Marks", style="green")

table.add_row("Chakri", "95")
table.add_row("Rahul", "88")
table.add_row("Aman", "91")

console.print(table)

# --- progress bar example ---
console.print("\nProcessing Files...\n", style="bold yellow")

for i in track(range(10), description="Loading..."):
    time.sleep(0.3)

console.print("\nTask Completed ✅", style="bold blue")