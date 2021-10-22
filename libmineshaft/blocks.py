import os


class Block:
    def __init__(self,
                 id, image,
                 resistance=2,
                 name="Block",
                 unbreakable=False,
                 falls=False,
                 breaktime=10  # seconds
                 ):
        self.id = id
        self.image = os.path.join(image)
        self.resistance = resistance
        self.name = name
        self.unbreakable = unbreakable
        self.falls = falls
        self.breaktime = breaktime


air = Block(0,  image=False, 
             resistance=-1,  name="Air",  falls = False,  breaktime=-1)
dirt = Block(1,  ["assets",  "images",  "blocks",  "dirt.png"],
             resistance=0,  name="Dirt",  falls=False,  breaktime=2)
stone = Block(2,  ["assets",  "images",  "blocks",  "stone.png"], 
             resistance = 10,  name="Stone",  falls=False,  breaktime=15)
cobblestone = Block(3,  ["assets", "images",  "blocks",  "cobblestone.png"], 
             resistance = 10,  name = "Cobblestone",  falls=False,  breaktime=15)

BLOCKS = {0 : air,  1 : dirt,  2 : stone,  3 : cobblestone}
