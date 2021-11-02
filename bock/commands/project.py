
import click
from click.termui import prompt
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
@click.argument('project_abbr')
def setup(ctx, project_abbr):
  """ 
    Setup a gams4+ project for your local gams.\n
    :param project_abbr ZIM/GAMS project abbreviation as used in zimlab and auth.
  """
  click.echo("NICE")
  click.echo(project_abbr)
  default_root = ctx.obj.gams_local.win_get_gamslocal_root()
  print("This is the root: ",str(default_root))
