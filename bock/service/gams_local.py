
import os
from pathlib import Path

class GamsLocal:
  def __init__(self) -> None:
      self.home_path = str(Path.home())
      self.default_gamslocal = "gams-local"
      pass

  def verify_rootfolder(self) -> bool:
    """
    Method checks if the default wsl root-folder is correctly setup.
    """
    exp_gamslocal_path = Path( self.home_path + os.sep + self.default_gamslocal )
    return Path.exists(exp_gamslocal_path) and Path.is_dir(exp_gamslocal_path)