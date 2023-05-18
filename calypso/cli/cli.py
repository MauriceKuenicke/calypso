import atexit
import os
from subprocess import Popen

import click
import uvicorn


@click.group()
def cli() -> None:
    """Calypso Command Line Interface Tool."""
    pass  # pragma: no cover


@cli.group()
def run() -> None:
    """Start a Calypso server locally."""
    pass  # pragma: no cover


@run.command("dev")
def start_development_server() -> None:
    """Run a simple server for development."""
    is_windows = os.name == "nt"
    windows_cmds = ["cmd", "/c"]
    default_cmds = ["npm", "run", "dev"]
    cmds = windows_cmds + default_cmds if is_windows else default_cmds

    p = Popen(
        cmds,
        cwd=os.path.join("calypso", "static", "calypso"),
    )
    atexit.register(p.terminate)  # pragma: no cover
    uvicorn.run("calypso.main:app", reload=True)  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    cli()  # pragma: no cover
