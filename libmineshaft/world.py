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
import sqlite3
import os

class World:
    def __init__(self, saves_dir=os.path.join(".mineshaft","saves"),   name="World", gamemode=0):
        """The currently-useless world class"""
        self.db_connection = sqlite3.connect(os.path.join(saves_dir,  name))
        self.database = self.db_connection.cursor()
        self.gamemode = gamemode
        self.name = name
    def save(self):
        self.db_connection.commit()
