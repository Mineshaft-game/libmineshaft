from cmd import Cmd
import libmineshaft
import sys
import platform

HISTORYFILE = ".libms_history"

class Prompt(Cmd):
    prompt = " Mineshaft~$ "
    intro = f"libmineshaft [{libmineshaft.__version__}] on [{platform.platform()}].\nHave a nice day coding.\n"
    
    def do_exit(self, inp):
        """Exit the console. Shortcuts: quit, ex, q, x"""
        print("Goodbye, have a nice day!")
        sys.exit()
        
    def default(self, inp):
        if inp in ["quit",  "ex",  "q",  "x"]:
            return self.do_exit(inp)
    
    do_EOF = do_exit

def run():
    while True:
        cmd = Prompt()
        cmd.cmdloop()
