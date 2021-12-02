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
