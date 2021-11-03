
from pathlib import Path
import os

class ZIMLab:
  """
  Service-class handling interaction with ZIMlab
  """
  # static variables
  PROJECTS_ROOT_URL = "https://zimlab.uni-graz.at/gams/projects"
  PROJECT_TEMPLATES_WWW_URL = "https://zimlab.uni-graz.at/gams/projects/templates/gams-www"

  def __init__(self, gams_local: Path) -> None:
    self.gams_local = gams_local

  @staticmethod
  def clone_project_www(project_abbr: str, clone_loc: str):
    """
    
    """

    if not Path.is_dir(Path(clone_loc)): raise NotADirectoryError(f"Given Path is not a directory. Given path: {clone_loc}") 

    # check if already checked out
    check_projabbr_path = clone_loc + os.sep + project_abbr
    if Path.is_dir(Path(check_projabbr_path)): raise IsADirectoryError(f"Project seems to be already available at: {check_projabbr_path}")

    # Awaited path on zimlab - enforced by convention
    repo_url  = f"{ZIMLab.PROJECTS_ROOT_URL}/{project_abbr}/gams-www" 
    # save to restore
    cur_cwd = os.curdir

    # clone into location in folder like project_abbr
    os.chdir(clone_loc)
    cmd = f"git clone {repo_url} {project_abbr}"
    os.system(cmd)

    # restore cwd
    os.chdir(cur_cwd)