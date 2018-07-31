# commands/

This folder holds modules for implementing one's own commands and
command sets. All the modules' classes are essentially empty and just
imports the default implementations from Evennia; so adding anything
to them will start overloading the defaults.

Any non-trivial functionality should be implemented using the [unixcommand]
syntax, as that allows for much more powerful commands than the default
MuxCommand class supports.

[unixcommand]: https://github.com/evennia/evennia/blob/master/evennia/contrib/unixcommand.py
