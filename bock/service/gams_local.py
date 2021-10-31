
import os
from pathlib import Path

class GamsLocal:
  def __init__(self) -> None:
      self.default_gamslocal = "gams-locale"
      self.home_path = str(Path.home())
      self.gamslocal_path = self.get_gamslocal_root()

  def verify_rootfolder(self, exp_gamslocal_path: Path) -> bool:
    """
    Method checks if the default wsl root-folder is correctly setup.
    """
    return Path.exists(exp_gamslocal_path) and Path.is_dir(exp_gamslocal_path)

  def get_gamslocal_root(self) -> Path:
    """
    Retrieves Path representation of gams-local folder.
    """
    exp_gamslocal_path = Path( self.home_path + os.sep + self.default_gamslocal )
    is_default = self.verify_rootfolder(exp_gamslocal_path=exp_gamslocal_path)
    if not is_default:
      raise NotADirectoryError("gams-local dir not available at user home!")
    
    return exp_gamslocal_path