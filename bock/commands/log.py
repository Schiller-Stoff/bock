
import click
import platform

from click.types import Choice
from bock.service.GamsLocalDocker import GamsLocalDocker
from bock.service.gams_local import GamsLocal
from bock.utils.wsl import WSL

# Base Setup
#
# class definition is needed for external data and basic setup here


class Context:
    def __init__(self):
        self.gams_local = GamsLocal()

# assign defined context to command initialization.


@click.group()
@click.pass_context
def cli(ctx):
    """Accessing logs of local GAMS"""
    ctx.obj = Context()
    pass

#
#
#

# first real command in subcommand


@cli.command()
@click.pass_context
def all(ctx):
    """
    Copies all relevant log files to .../gams-local/gams-logs/

    """
    gams_local = str(ctx.obj.gams_local.gamslocal_path)
    path = GamsLocalDocker.grab_logging(gams_local)

    click.echo("***\n")
    click.echo("\n")
    click.echo("\n")
    click.echo(f"Copied all gams-local logs to: {path}")

@cli.command()
@click.pass_context
def one():
    """
    
    """
    container_name = click.prompt('Please enter a number', show_choices=True, type=click.Choice(
        choices=GamsLocalDocker.DOCKER_CONTAINER, case_sensitive=False))
    click.echo(container_name)
    