
import click
from bock.service.gams_local import GamsLocal
from bock.service.zimlab import ZIMLab

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
  click.echo(f"Initializing project for: {project_abbr}")
  click.echo(f"Found gams-local root at: {str(ctx.obj.gams_local.gamslocal_path)}")
  click.echo(f"Found apache dir at: {str(ctx.obj.gams_local.gamslocal_apache)}")

  # cloning project from zimlab 
  GamsLocal.assert_project_abbr(project_abbr)
  ZIMLab.clone_project_www(project_abbr=project_abbr, clone_loc=str(ctx.obj.gams_local.gamslocal_apache))
  click.echo(f"Succesfully cloned project {project_abbr} from zimlab to: {str(ctx.obj.gams_local.gamslocal_apache)}")
