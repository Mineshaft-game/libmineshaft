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

Builds will be under the dist/ directory. 
To upload them to PyPI, install twine. 
```
pip3 install twine
cd dist
twine upload * #Only use this if the dist directory contains only a single build that is not to be overrides
twine upload *x.x.x.* #Replace x with the version numbers
```
Please note, that you will have to have access to the `libmineshaft` project on PyPI to upload it. 


