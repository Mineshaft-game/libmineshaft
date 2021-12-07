## Opening the CUI
<details>
<summary>What is a CUI?</summary>
A CUI means Command Line User Interface. It is like a GUI but in a command line.
</details>



-----


To launch the CUI, you have to either run `libmineshaft` or `python3 -m libmineshaft`. An alias for this is `libms-cui`.

![](https://github.com/Mineshaft-game/libmineshaft/raw/main/docs/libms-cui.png) 




## Creating your own CUI object
If you will want to modify the CUI, you can import the `libmineshaft.__main__` module as it is where the CUI's class is located.
```python
from libmineshaft.__main__ import LibmineshaftCui
import py_cui

root = py_cui.PyCUI(5,2)
root.toggle_unicode_borders()
root.set_title("title")

cui = LibmineshaftCui(root)

root.start()

```

For more information, please refer to the py_cui documentation.
