
import click
import platform

# Base Setup
#
# class definition is needed for external data and basic setup here
class Context:
    def __init__(self):
        # self.note = svc_note.Note()
        pass

# assign defined context to command initialization.
@click.group()
@click.pass_context
def cli(ctx):
    """General info about your system (wsl etc.)"""
    ctx.obj = Context()
    pass

# 
#
#

# first real command in subcommand
@cli.command()
@click.pass_context
def system(ctx):
  """
  Provides 
  """
  click.echo(f"Running system: {platform.system()}")
  click.echo(f"OS-release: {platform.release()}")
  click.echo(f"Uname: {platform.uname()}")
  click.echo(f"Machine type: {platform.machine()}")
  click.echo(f"Network-node: {platform.node()}")
  click.echo(f"Uing python version: {platform.python_version()}")