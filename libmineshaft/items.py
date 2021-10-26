import os


class Item:
    def __init__(id, name, texture):
        self.id = id
        self.name = name
        self.texture = os.path.join(texture)
