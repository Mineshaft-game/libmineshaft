import os


class Item:
    def __init__(self, id, name, texture):
        self.id = id
        self.name = name
        self.texture = os.path.join(texture)

class DurabilityItem(Item):
    def __init__(self, id, name, texture, durability):
        self.id = id
        self.name = name
        self.texture = os.path.join(texture)
        self.durability = durability

    def use_durability(self):
        '''
        Decreases durability of the item.
        Should be called in use()
        '''
        self.durability -= 1

class CombatItem(DurabilityItem):
    def __init__(self, id, name, texture, durability, damage):
        self.id = id
        self.name = name
        self.texture = os.path.join(texture)
        self.durability = durability
        self.damage = damage

    def attack(self, victim):
        victim.health -= damage
        self.use_durability()
