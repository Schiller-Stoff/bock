
from pathlib import Path

class ZIMLab:
  """
  Service-class handling interaction with ZIMlab
  """
  # static variables
  PROJECTS_ROOT_URL = "https://zimlab.uni-graz.at/dashboard/groups"
  PROJECT_TEMPLATES_WWW_URL = "https://zimlab.uni-graz.at/gams/projects/templates/gams-www"

  def __init__(self, gams_local: Path) -> None:
    self.gams_local = gams_local


  