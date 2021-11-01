
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

  # check if wsl is the execution environment of the script  
  if WSL.in_wsl(): 
    click.echo("WSL is the executing environment!")
    # do further stuff here
    # default_root = ctx.obj.gams_local.get_gamslocal_root()
    # print(str(default_root))

  else:
    click.echo("**NOT SUPPORTED: Running bock outside WSL.**")
    # check if wsl would be available  
    if WSL.win_wsl_available():
      click.echo("WSL seems to be installed. Type 'wsl' in your cmd to start and start bock from there!")
      pass
    else:
      click.echo("WSL not installed!")
    return
  
