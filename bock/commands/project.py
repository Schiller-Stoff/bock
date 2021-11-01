
import click
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
    """Commands related to gams-projects. """
    ctx.obj = Context()
    pass

# 
#
#

# first real command in subcommand
@cli.command()
@click.pass_context
def setup(ctx):
  """ Setup a gams4+ project for your local gams."""

  click.echo("NICE")
  # default_root = ctx.obj.gams_local.get_gamslocal_root()
  # print(str(default_root))
