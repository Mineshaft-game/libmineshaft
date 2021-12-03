from . import shell
from . import __version__ as libms_version
import py_cui
import curses
import sys

class LibmineshaftCui:
    def __init__(self, master : py_cui.PyCUI):
        
        self.master = master
        
        master.add_button("Open the shell", 0,  0,  column_span = 2,  command=self.run_shell)
        master.add_button("Quit", 1,  0,  column_span = 2,  command=sys.exit)
        master.add_label("More coming soon", 2,  0,  column_span = 2)
        
    def run_shell(self):
        self.master.stop()
        curses.endwin()
        shell.run()
        self.master.start()


root = py_cui.PyCUI(5, 2)

root.toggle_unicode_borders()
root.set_title(f'libmineshaft v[{libms_version}] Selection GUI')
cui = LibmineshaftCui(root)


if __name__ == "__main__":
    root.start()
