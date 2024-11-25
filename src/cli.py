"""Console script for facebook_friend_tracker."""
import facebook_friend_tracker

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for facebook_friend_tracker."""
    console.print("Replace this message by putting your code into "
               "facebook_friend_tracker.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
