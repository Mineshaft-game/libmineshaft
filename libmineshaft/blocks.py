"""
libmineshaft.block
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This submodule contains the block classes:
Block, NoIDBlock and MultipleStateBlock
"""


class Block:
    """
    This is the class that should be used as the parent to every block.
    """

    id = None
    image = None
    resistance = -1
    name = "Block"
    unbreakable = True
    falls = False
    breaktime = -1

    def blit(self, solution, rect):
        """
        This function manages how the rendering engine should display the block, and the character in it.
        It is to be overriden in special blocks, e.g. Air, stairs, etc
        """
        # TODO: Move the character thing to self.logic
        if self.image:
            solution.blit(self.image, rect)


class NoIDBlock(Block):
    """
    This class is the class that should be used as the parent to every block in MultipleStateBlock.blocks.
    """

    image = False
    resistance = -1
    name = "No Id Block"
    unbreakable = True
    falls = False
    breaktime = -1


class MultipleStateBlock(Block):
    """
    This class is the class that should be used as the parent to every block that has multiple states, e.g. furnace lit/unlit, dirt/coarse dirt, etc.
    """

    id = None
    name = "Multiple State Block"
    blocks = None
    currentstate = None

    def blit(self, solution, rect):
        if self.currentstate:
            solution.blit(self.blocks[self.currentstate.image], rect)
        else:
            return None


__all__ = ["MultipleStateBlock", "Block", "NoIDBlock"]
