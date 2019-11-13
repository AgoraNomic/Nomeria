"""
Commands

Commands describe the input the account can do to the game.

"""
from evennia import Command as BaseCommand
from evennia.contrib.unixcommand import UnixCommand as BaseUnixCommand


class Command(BaseCommand):
    """
    This is the root of the nomeria command hierachy; built-in
    commands work using the MuxCommand syntax, which is seperate.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - init_parse(): This initalizes the argparse parser for the
            command.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass


class UnixCommand(BaseUnixCommand):
    """
    This is the root of the nomeria command hierachy; built-in
    commands work using the MuxCommand syntax, which is seperate.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - init_parse(): This initalizes the argparse parser for the
            command.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass
