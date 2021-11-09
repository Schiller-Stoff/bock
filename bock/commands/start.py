
import subprocess
import click
import os

from bock.utils.wsl import WSL
from bock.service.gams_local import GamsLocal

# Base Setup
#
# class definition is needed for external data and basic setup here
class Context:
    def __init__(self):
        # self.note = svc_note.Note()
        pass

# will launch command directly
@click.group(invoke_without_command=True) 
@click.pass_context
def cli(ctx):
    """Start local gams as docker environment"""
    
    click.echo("*Starting gams-local now...")

    gams_local_path = str(GamsLocal().gamslocal_path)
    old_cwd = os.curdir

    os.chdir(gams_local_path + os.sep + "gams-docker")
    subprocess.run(["docker-compose", "up", "-d"])

    os.chdir(old_cwd)

    click.echo("*gams-local successfully started.")
# 
#
#