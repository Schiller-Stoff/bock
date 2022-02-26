
import click

from bock.utils.wsl import WSL
from bock.service.GamsLocalFileService import GamsLocalFileService
from bock.service.GamsLocalDocker import GamsLocalDocker

import webbrowser

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
    """Opens basic gams links on your machine's default browser"""

    fcrepo_rest = "https://localhost/fcrepo/rest"
    fc_object_getRDF = "https://localhost/MY_PID/sdef:Object/getRDF"
    g4_doku = "https://gedra.uni-graz.at/g4doku/"
    tutorials = "https://glossa.uni-graz.at/context:training"

    webbrowser.open(fcrepo_rest)
    webbrowser.open(fc_object_getRDF)
    webbrowser.open(g4_doku)
    webbrowser.open(tutorials)
    
