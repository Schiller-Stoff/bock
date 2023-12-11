
# bock

Very basic cli-tool to support local (GAMS4+)[http://gams.uni-graz.at/] project development.

- [Bock on pypi](https://pypi.org/project/bock/)

## Quick Start

```sh

# 1. make sure python3 + pip are installed
pip install bock


# 2. restart shell / wsl etc.
# run bock
bock

```

## Update bock

```sh
# u argument = short for 'upgrade'
pip install bock -U

# alternative
pip install bock --upgrade


```

## Install a specific bock version



```sh
# installs bock at version 0.1.2
pip install bock==0.1.2

```


## Requirements
- python 3.10.0?
- pip installed


## Bock development

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
# on windows!
# launch venv first
# cd into clone
./venv/Scripts/activate.bat

# then increment version in setup.py according to semantic versioning!

# build python wheel
py -m build --wheel

# OPTIONAL: check if description is valid
twine check dist/*

```


# Deployment (on pypi)

- on pypi https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi

- check docu for api token (test out on testpypi)


## Pypi

```sh
# First build files + create pypi account (if not existing)
# username: __token__
# pw: MYTOKEN
twine upload dist/*

# install from pypi
pip install bock


```

## Testpypi


```sh
# test on testpypi
# need to specify testpypi repo
# username: __token__
# pw: MYTOKEN
twine upload dist/* --repository testpypi

# install from testpypi
# needs to be done this way -> deps need to be installed from pypi and not the test instance.
pip install bock --extra-index-url https://test.pypi.org/simple 


```


# Testing

## Manual Deployment

### Installation from TestPypi

```sh

# first update ubuntu stuff
sudo apt-get update && apt-get upgrade 

# install pip first
sudo apt-get python3-pip

# install from testpypi
# needs to be done this way -> deps need to be installed from pypi and not the test instance.
pip install bock --extra-index-url https://test.pypi.org/simple 
# (when on wsl -> restart wsl )

# use bock
bock project setup "templates"


```
