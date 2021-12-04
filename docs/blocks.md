## Creating a custom block


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

## Rendering the block
This information may be important if you are making a rendering engine.


The `libmineshaft.blocks.Block` class contains a function called `Block.blit`. It requires two arguments:



* `solution` - The solution for the graphics you are using: It MUST have a `blit` method, which takes the arguments: `image` which is the image path, and the `rect`angle where it is to be blitted: see below
* `rect` - A tuple that contains the coordinates where the block should be blitted

Please note that a wrapper may will be needed with most external libraries, since libmineshaft was made for Pygame, it is adapted to it. An alternative to this would be overriding the `Block.blit` function (maybe in a wrapper Block class) to have the required blit function.
