# typeclasses/

This directory holds the modules for overloading all the typeclasses
representing the game entities and many systems of the game. Other
server functionality not covered here is usually modified by the
modules in `server/conf/`.

Contains all typeclasses. The built in modules (accounts, channels,
characters, exits, objects, rooms, and scripts) should only contain
the base typeclasses for each of those things, and any similarly broad
utilities. The docstrings for the built in classes should not be removed.

The sub-packages `./local` and `./misc` contain those typeclasses
limited to specific rooms or areas and those of more general application
respectively. Feel free to add sub-packages within them as necessary,
and add new sub-packages within this package when it makes sense. Other
than the built in modules, hierarchies should generally be categorized
by use, not by type.
