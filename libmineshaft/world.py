"""

Copyright (C) 2021-2022 Alexey "LEHAtupointow" Pavlov

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
from pynbt import *
import os
import gzip

class World:
    def __init__(self, saves_dir=os.path.join(".mineshaft","saves"),   name="World", gamemode=0):
        """The currently-useless world class"""
        with gzip.open(os.path.join(saves_dir,  name,  "chunks.dat"),  "rb") as gzipped:
            self.world = NBTFile(gzipped)
        self.gamemode = gamemode
        self.name = name
        self.saves_dir = saves_dir
    def save(self):
        with open(os.path.join(self.saves_dir,  self.name,  "chunks.dat.tempsave.ungzipped"),  "wb") as io:
            self.world.save(io)
        with open(os.path.join(self.saves_dir,  self.name,  "chunks.dat.tempsave.ungzipped"),  "rb") as ungzipped,  gzip.open(os.path.join(self.saves_dir,  self.name,  "chunks.dat"),  "wb") as gzip_out:
            gzip_out.writelines(ungzipped)
