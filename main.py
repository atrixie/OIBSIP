import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import track

from modules.speech import speak, listen
from modules.commands import execute
from modules.utils import get_greeting


console = Console()


console.print(
    Panel.fit(
        "[bold cyan]MAX AI[/bold cyan]\n"
        "[green]Intelligent Voice Assistant[/green]\n"
        "Version 1.0",
        border_style="cyan"
    )
)


services = [

    "Loading Speech Engine",

    "Loading Voice Recognition",

    "Loading Command Center",

    "Loading AI Modules",

    "Loading Skills"

]


for service in track(services, description="Initializing..."):

    time.sleep(0.5)


console.print("\n[bold green]✓ MAX AI Ready[/bold green]\n")


speak(
    f"{get_greeting()} Nikijon. "
    "I am MAX, your intelligent voice assistant. "
    "How can I help you today?"
)


while True:

    command = listen()

    if command == "":

        continue

    if execute(command) is False:

        break


console.print("\n[bold red]MAX AI Offline[/bold red]")