import os

class Block:
    def __init__(self,
            id, image, 
            resistance=2,
            name="Block",
            unbreakable=False, 
            falls=False,
            breaktime=10 #seconds
            ):
        self.id = id
        self.image = os.path.join(image)
        self.resistance = resistance
        self.name = name
        self.unbreakable = unbreakable
        self.falls = falls
        self.breaktime = breaktime
        

dirt = Block(1,  ["assets",  "images",  "blocks",  "dirt.png"], resistance=0,  name = "Dirt",  falls=False,  breaktime=2)
