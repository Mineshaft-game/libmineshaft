# Creating a custom block


Copy and paste this code into your block index file.
Feel free to change any names, they are not required: you can change anything which is not already defined.

```python
from libmineshaft.blocks import Block

class CustomBlock(Block):
    id = <insert a non-occupied ID in the block index>
    image = ["assets", "images", "blocks", "custom.png"] # The path as a list, since it will be joined by os.path.join later
    resistance = 10 #blast resistance
    name = "Custom Block"
    falls = False #Does not fall when a block below is broken
    breaktime = 10 # Breaking time in seconds
```


After that, add the block into your block index dictionary, by any means and let the rendering engine do the magic.
