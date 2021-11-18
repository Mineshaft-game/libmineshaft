import os


class Block:
    def __init__(
        self,
        id,
        image,
        resistance = 2,
        name= "Block",
        unbreakable= False,
        falls = False,
        breaktime = 10,  # seconds
    ):
        """
        The basic block class.
        `id` is the ID of the block, is an `int`.
        `imagepath` is the path of the image as a os.path, e.g `["images", "block.png"]`. However if it is `-1` then it becomes transparent.
        `resistance` is the resistance in `int`. Defaults to `2`.
        `name` is a `str`ing. Defaults to `"Block"`. 
        `unbreakable` is an `bool`, showing off if the block is unbreakable, e.g. Bedrock. Defaults to `False`
        `breaktime` is an `int`, which represents seconds it takes to break this block. Defaults to `10`
        """
        
        self.blit = True
        self.id = id
        if type(image) == str:
            self.imagepath = os.path.join(image)
        elif type(image) == int:
            self.blit = False
            self.imagepath = False
            
        self.resistance = resistance
        self.name = name
        self.unbreakable = unbreakable
        self.falls = falls
        self.breaktime = breaktime


class NoIDBlock(Block):
    def __init__(
        self,
        image,
        resistance=2,
        name="No ID Block",
        unbreakable=False,
        falls=False,
        breaktime=10,
    ):
        self.image = os.path.join(image)
        self.resistance = resistance
        self.name = name
        self.unbreakable = unbreakable
        self.falls = falls
        self.breaktime = breaktime


class MultipleStateBlock(Block):
    def __init__(self, id, blocks):
        if len(self.blocks) > 15:
            raise IndexError(
                "There is too much block IDs.\nMore block ID slots may be added in the future"
            )
        self.id = id
        self.blocks = blocks
        self.default = self.blocks[0]

__all__ = ["MultipleStateBlock",  "Block",  "NoIDBlock"]

