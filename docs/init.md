## Getting the metadata
The `libmineshaft.__init__` (this module gets imported when you `import libmineshaft`)  module contains the metadata used for verifying versions, and displaying author/contributor information.

```python
>>> import libmineshaft # Automatically imports libmineshaft.__init__

>>> print(libmineshaft.__version__)
0.1.6rc-1 # this is the version in the current case, it will be different when you try it yourself

>>> print(libmineshaft.__author__)
Double Fractal Game Studios

>>> print(libmineshaft.__credits__)
Double Fractal Game Studios team:
*   Mayu Sakurai
*   Alexey Pavlov

>>>

```

This information may be used for debugging, or external tools that require author names or version number.

