from evennia import create_script
from typeclasses.objects import Object
from typeclasses.rooms import Room
from typeclasses.misc.messenger import MessengerScript


class Garden(Room):

    def at_object_creation(self):
        script = create_script(MessengerScript, "Local messenger", obj=self)
        script.db.messages = (["The fountain burbles softly."]
                              + ["The wind blows through the trees and bushes."]
                              + ["Birds chirp from the tree tops above"]
                              + ["Light passes through the fountain, forming a rainbow."]
                              + ["Water splashes outside the fountain."]
                              + ["You feel calm and peaceful."]
                              + ["The fountain shimmers oddly. Is it glowing?"])


class Fountain(Object):
    """
    Implements the town fountain.
    """
    pass
