from evennia import CmdSet
from evennia import utils
from commands.command import Command
from ..objects import Object
from ..characters import Character
from world.quests import Quest


class Ball(Object):
    "Implements a ball that a player can kick around."

    def at_object_creation(self):
        self.cmdset.add_default(CmdSetKick, permanent=True)


class CmdKick(Command):
    """
    Kick an object.

    Usage:
        kick <obj>

    Kick an object. Please do not kick other people.
    """
    key = "kick"
    locks = "cmd:all()"

    def func(self):
        """Kick the object"""

        location = self.caller.location
        caller = self.caller

        if self.args:
            obj = self.caller.search(self.args.strip())
        else:
            caller.msg("What do you want to kick?")
            return

        if utils.inherits_from(obj, Character):
            caller.msg("Don't kick other people!")
            return
        elif obj != self.obj:
            caller.msg("You can't kick that.")
            return

        location.msg_contents(text="{char} kicks the ball.", from_obj=caller,
                              exclude=caller, mapping={"char": self.caller})
        self.caller.msg("You kick the ball.")
        self.caller.location.msg_contents(text="The ball rolls around.",
                                          from_obj=self.caller)


class CmdSetKick(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdKick())


class TestQuest(Quest):

    @property
    def name(self):
        return "Test"

    @property
    def description(self):
        return ("Merely a test of your skills. This message is unreasonably "
                + "long; someone might want to do something about that. :)")

    def send(self, event):
        pass
