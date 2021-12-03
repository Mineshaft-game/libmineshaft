## Embedding a custom shell
A custom shell may be embedded using the `libmineshaft.shell` module. 
```python
import libmineshaft.shell as shell

shell.run() # Run a shell session
```
 Or you could create an object of `Prompt`. It's a `cmd.Cmd` object, so refer to `cmd`'s documentation for more options.
 ```
from libmineshaft.shell import Prompt

p = Prompt()

p.cmdloop()
 
```



At this point you can customize the prompt, e.g. add commands, change welcome message, and more.




## Shell commands 
The shell contains a built-in `help` function:



```
libmineshaft [0.1.5] on [Linux-5.11.0-38-generic-x86_64-with-glibc2.29].
Have a nice day coding.

 Mineshaft~$ help

Documented commands (type help <topic>):
========================================
EOF  exit  help

 Mineshaft~$ 
```

All command documentation may be found there.