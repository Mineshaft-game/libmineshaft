"""
libmineshaft.block
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This submodule contains the block classes:
Block, NoIDBlock and MultipleStateBlock

~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (C) 2021-2022  Alexey "LEHAtupointow" Pavlov

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA


"""


class Block:
    """
    This is the class that should be used as the parent to every block.
    """

    id = None
    imagecoords = (0, 0)
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

    imagecoords = (0, 0)
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
