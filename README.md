[![Documentation Status](https://readthedocs.org/projects/libmineshaft/badge/?version=latest)](https://libmineshaft.readthedocs.io/en/latest/?badge=latest) [![Join the chat at https://gitter.im/Mineshaft-game/libmineshaft](https://badges.gitter.im/Mineshaft-game/libmineshaft.svg)](https://gitter.im/Mineshaft-game/libmineshaft?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/libmineshaft?color=yellow&label=PyPI%20downloads&logo=python&logoColor=white)
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=Mineshaft-game_libmineshaft)](https://sonarcloud.io/summary/new_code?id=Mineshaft-game_libmineshaft)

# libmineshaft
[![libmineshaft](https://raw.githubusercontent.com/Mineshaft-game/libmineshaft/main/logo.png)](#)
This library is created to replace the resources folder in the original Mineshaft.


## Documentation
at the current moment, there is no documentation

## Installation
Run the command below to install the lastest version:


```
pip3 install --user libmineshaft # install
pip3 install --user --upgrade libmineshaft # update to lastest version
pip3 uninstall libmineshaft # uninstall
```
If you are on Windows, you will want to install the `windows-curses` module through pip. 

## Building from source 
If you are developing libmineshaft, then you may will want to built libmineshaft from source.Run the commands below to create wheels and source distributions for libmineshaft.

```
python3 setup.py sdist
pip3 install wheel
python3 setup.py bdist_wheel
```

Builds will be under the dist/ directory
