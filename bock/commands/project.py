
import click

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
  click.echo("This is a test!")
