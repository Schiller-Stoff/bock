
# gamsFrontCLI

Very basic cli-tool to help setting up a gams-project on gams4+ from perspective of frontend-development.


## Quick Start

```sh
# cd to clone of repo
cd /to/the/clone

# install via pip locally
pip install .
# logout / login from wsl afterwards

# launch bock commands
bock [cmd]

# launch demo sub-command (inside commands/demo.py)
bock demo testme


```

## Idols / Sources
- https://github.com/IVIURRAY/yt-eve
- https://www.youtube.com/watch?v=Jr4QDJwwj60&ab_channel=SoftwareEngineerHaydn


## Requirements
- python 3.10.0?
- pip installed


### 1. Install pip (WSL + Ubuntu 20.x LTS)
```sh
# pip wsl ubuntu installation
# update / upgrade ubuntu first
sudo apt update && sudo apt upgrade
# install pip on ubuntu
sudo apt install python3-pip
# then install bock

```

## Install

1. create venv
2. install requirements specified in requirements.txt
3. code along!


### Update bock

```sh
# update bock
py -m pip install --upgrade bock

```

## Aims

1. Simplify
  - setting up the dev assets shpuld be
2. Centralize
  - avoid copying of old code. Make sure to spread best practices / bug fixes etc.
3. Abstract away:
  - knowledge about different repositories and other implementation details.
4. Validate:
  - integrate frontend test possiblity into the tool


## Example cli calls

```sh


```

# Production

- according to official doc here: https://packaging.python.org/tutorials/installing-packages/#installing-requirements

- based on windows machines

```sh
# launch venv first
# cd into clone
./venv/Scripts/activate.bat

# build python wheel
py -m build --wheel

# OPTIONAL: check if description is valid
twine check dist/*



```


# Deyployment