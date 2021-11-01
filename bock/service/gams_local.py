
import os
from pathlib import Path
from bock.utils.wsl import WSL

class GamsLocal:
  def __init__(self) -> None:
    self.check_wsl_active()
    self.default_gamslocal = "gams-local"
    # self.home_path = str(Path.home())
    # self.gamslocal_path = self.get_gamslocal_root()

  def check_wsl_active(self) -> True:
    """
    Returns True if wsl is the executing context. Otherwise will throw a NotImplementedError
    """
     # check if wsl is the execution environment of the script  
    if WSL.in_wsl(): 
      return True
    else:
      # check if wsl would be available  
      if WSL.win_wsl_available():
        raise NotImplementedError("Running bock ouside wsl is currently not supported, but WSL seems to be installed. Type 'wsl' in your cmd and start bock from there!")
      else:
        raise NotImplementedError("Running bock ouside wsl is currently not supported. WSL seems not to be installed")
  
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