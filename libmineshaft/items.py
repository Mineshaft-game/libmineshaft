import os


class Item:
    def __init__(self, id, name, texture):
        '''
        The base class for every item. id is the item ID, name is the name,and the texture is a list which is the path to the texture afterwards joined with os.path.join for cross-platform compaptibility
        '''
        self.id = id
        self.name = name
        self.texture = os.path.join(texture)

class DurabilityItem(Item):
    def __init__(self, id, name, texture, durability):
        '''
        This version of the Item class has an additional property called durability.
        When used,durability decreases.
        '''
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
        '''
        This version of the Item class has the attack() method to attack a victim (mob,player,etc.)
        It needs a property of damage, which should be a float.
        '''
        self.id = id
        self.name = name
        self.texture = os.path.join(texture)
        self.durability = durability
        self.damage = damage

    def attack(self, victim):
        '''
        Attacks the specified victim.
        The victim should have the self.health property.
        '''
        victim.health -= damage
        self.use_durability()
