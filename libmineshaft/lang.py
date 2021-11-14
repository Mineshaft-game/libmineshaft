import os
import platform
import libmineshaft
from time import sleep

def respond(response):
    response = response.split(' ')
    if response[0].lower() == 'edit':
        try:
            if response [1].lower() == "config":
                if platform.platform().lower().startswith('linux') or platform.platform().lower().startswith("darwin"):
                    print("Please be sure that you are running this in a command prompt, not a GUI client.")
                    sleep(1)
                    os.system("nano .mineshaft/mineshaft.conf")
                else:
                    print("edit: Cannot edit config; Editing is onlly supported on Linux/Unix and MacOS")
        except:
            print("\nedit help:")
            print("edit - print this unhelpful message")
            print("edit config - edit .mineshaft/mineshaft.conf\n")
            
    elif response[0].lower() == "clone":
        print("This requires git to be installed.")
        sleep(1)
        os.system("git clone http://github.com/Mineshaft-game/Mineshaft")
    
    elif response[0].lower() == "quit":
        raise KeyboardInterrupt
    
    
    elif response[0].lower() == "help":
        print(f"\nLibmineshaft {libmineshaft.__version__} console help:")
        print("help - this really unhelpful message")
        print("edit - edit a mineshaft-related file. (Unix-like only) ")
        print("clone - clone the Mineshaft git repository locally")
        print("quit - quit the console\n")
