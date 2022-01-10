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


from . import shell
from . import __version__ as libms_version
import py_cui
import curses
import sys
import storyscript.__main__


class LibmineshaftCui:
    def __init__(self, master: py_cui.PyCUI):

        self.master = master

        master.add_label(
            f"libmineshaft v[{libms_version}] Selection GUI", 0, 0, column_span=2
        )
        master.add_button("Open the shell", 1, 0, column_span=2, command=self.run_shell)
        master.add_button(
            "Open StoryScript shell",
            2,
            0,
            column_span=2,
            command=self.start_storyscript,
        )
        master.add_button("Quit", 3, 0, column_span=2, command=sys.exit)

    def run_shell(self):
        self.master.stop()
        curses.endwin()
        shell.run()
        self.master.start()

    def start_storyscript(self):
        self.master.stop()
        curses.endwin()
        storyscript.__main__.main()
        self.master.start()


def main():
    root = py_cui.PyCUI(5, 2)

    root.toggle_unicode_borders()
    root.set_title(f"libmineshaft v[{libms_version}] Selection GUI")
    cui = LibmineshaftCui(root)
    root.start()


if __name__ == "__main__":
    main()
