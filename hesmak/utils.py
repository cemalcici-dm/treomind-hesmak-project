import typer

__version__ = "0.1.1"


def version_callback(
    value: bool
):
    if value:
        typer.echo(f"Treomind Hesmak Version: {__version__}")
        raise typer.Exit()
