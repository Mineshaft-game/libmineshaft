import libmineshaft
import libmineshaft.shell as shell
import platform
import sys

def main():
    print(f"libmineshaft [{libmineshaft.__version__}] on [{platform.platform()}].\nHave a nice day coding.\n\n")
    try: 
        shell.run()
    
    except KeyboardInterrupt:
        sys.exit(print("Goodbye, have a nice day"))

if __name__ == "__main__":
    main()
