import os


class Block:
    def __init__(
        self,
        id,
        image,
        resistance=2,
        name="Block",
        unbreakable=False,
        falls=False,
        breaktime=10,  # seconds
    ):
        self.id = id
        self.image = os.path.join(image)
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


