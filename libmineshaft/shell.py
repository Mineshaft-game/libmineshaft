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
