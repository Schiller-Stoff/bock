
# gamsFrontCLI

Very basic cli-tool to help setting up a gams-project on gams4+ from perspective of frontend-development.


## Quick Start

### Windows

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


### WSL / Linux

```sh
# cd to clone of repo
cd /to/the/clone

# activate venv (needs virtualenv installed)
source venv/Scripts/activate    # if there is an error (like command not found -> use dos2Unix command on venv/Scripts/activate )

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

# Production / Packaging

- according to official doc here: https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project

- based on windows machines

- packaged as "wheel" (check doc link from before)

```sh
# launch venv first
# cd into clone
./venv/Scripts/activate.bat

# build python wheel
py -m build --wheel

# OPTIONAL: check if description is valid
twine check dist/*

```


# Deployment (on pypi)

- on pypi https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi

- check docu for api token (test out on testpypi)

```sh
# test on testpypi
# need to specify testpypi repo
twine upload dist/* --repository testpypi

# install from testpypi
# needs to be done this way -> deps need to be installed from pypi and not the test instance.
pip install bock --extra-index-url https://test.pypi.org/simple 


```


# Testing

## Manual Deployment

- installing from test-pypi

```sh

# install from testpypi
# needs to be done this way -> deps need to be installed from pypi and not the test instance.
pip install bock --extra-index-url https://test.pypi.org/simple 



```