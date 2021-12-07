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
        Supported options: config. edit config. Edits Mineshaft's configuration. Please note that on MacOS and Linux it requires vim to be installed
        """


        if inp == "config":
            if platform.platform().split("-")[0] in ["Linux", "Unix", "Darwin"]:
                os.system("vim ./.mineshaft/mineshaft.conf")
            elif platform.platform().split("-")[0] in ["Windows", "DOS"]:
                os.system("start .mineshaft\\mineshaft.conf")

            else:
                print("Your system is not supported. Sorry")
        
        else:
            print("Please enter a valid edit command. See help edit for more documentation")
    def do_exit(self, inp):
        """Exit the console. Shortcuts: quit, ex, q, x"""
      
        print("Goodbye, have a nice day!")
        
        if __name__ == "__main__":
            sys.exit(print(inp))
        else: 
            return True
    def default(self, inp):
        if inp in ["quit",  "ex",  "q",  "x"]:
            return self.do_exit(inp)
    
    do_EOF = do_exit




def run():
    cmd = Prompt()
        
    cmd.cmdloop()
