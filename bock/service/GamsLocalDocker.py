

import os
import tempfile
import subprocess
from shutil import copytree

class GamsLocalDocker:
  """
  Encapsulates all methods related to the local docker environment of the local GAMS.
  Like access to docker logging etc.

  """

  DOCKER_CONTAINER = ["activemq", "blazegraph", "cocoon", "fcrepo4", "latex", "nexuscube", "proai", "relight", "skosifier", "toolbox", "triplestore",
                      "apache", "cm4f", "fcgate", "fits", "loris", "postgres", "rdf4j", "rscript", "solr", "treetagger", "verovio"]

  def __init__(self) -> None:
      pass


  @staticmethod
  def grab_logging(location: str) -> str:
    """
    Copies all available gams-local logs to specified location into gams-logs folder.
    :param location target to where logs should be copied. 
    :return path to the logs.
    """

    gams_logspath = location + os.sep + "gams-logs"
    if not os.path.isdir(gams_logspath):
      os.mkdir(gams_logspath)

    with tempfile.TemporaryDirectory() as tmpdirpath:
      
      logs_temp = tmpdirpath + os.sep + "logs"
      os.mkdir(logs_temp)  

      for container in GamsLocalDocker.DOCKER_CONTAINER:
        cmd = f"docker logs {container}"
        ret = subprocess.check_output(cmd, shell=True, text=True).strip().replace("  ", " ")

        f = open( logs_temp + os.sep + f"{container}.log", "a")
        f.write(ret)
        f.close()

        copytree(logs_temp, gams_logspath, dirs_exist_ok=True)
    

    return gams_logspath

      