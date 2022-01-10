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


from cmd import Cmd
import libmineshaft
import sys
import platform
import os

HISTORYFILE = ".libms_history"


class Prompt(Cmd):
    prompt = " Mineshaft~$ "
    intro = f"libmineshaft [{libmineshaft.__version__}] on [{platform.platform()}].\nHave a nice day coding.\n"

    def do_edit(self, inp):
        """
        Supported options: config. edit config. Edits Mineshaft's configuration. Deprecated as nowdays Mineshaft uses Pickle configuration instead of .conf or .ini files
        """

        if inp == "config":
          print("Editing config is deprecated as config now is in pickle format")
        else:
            print(
                "Please enter a valid edit command. See help edit for more documentation"
            )

    def do_exit(self, inp):
        """Exit the console. Shortcuts: quit, ex, q, x"""

        print("Goodbye, have a nice day!")

        if __name__ == "__main__":
            sys.exit(print(inp))
        else:
            return True

    def default(self, inp):
        if inp in ["quit", "ex", "q", "x"]:
            return self.do_exit(inp)

    do_EOF = do_exit


def run():
    cmd = Prompt()

    cmd.cmdloop()
