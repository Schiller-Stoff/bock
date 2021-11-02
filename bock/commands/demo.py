
import click

from bock.utils.wsl import WSL

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
    """Demo command template for building bock commands"""
    ctx.obj = Context()
    pass

# 
#
#

# first real command in subcommand
@cli.command()
@click.pass_context
def testme(ctx):
  """ Test out bock funtionality"""
  click.echo("This is a test!, Ubuntu LTS 20 being used? ")
  click.echo(WSL.check_for_ubuntu20_lts())