import random
from evennia import TICKER_HANDLER
from ..objects import Object


class Fountain(Object):
    """
    Implements the town fountain.
    """

    def at_object_creation(self):
        TICKER_HANDLER.add(45, self.repeat)

        self.locks.add("get:false()")
        self.db.get_err_msg = "The fountain is anchored to the ground."

    def repeat(self):
        """Called at regular intervals to provide motion."""
        loc = self.location
        if loc:
            rand = random.random()
            if rand < 0.2:
                string = "The fountain burbles softly."
            elif rand < 0.4:
                string = "Light passes through the fountain, forming a rainbow."
            elif rand < 0.5:
                string = "Water splashes outside the fountain."
            elif rand < 0.6:
                string = "You feel calm and peaceful."
            elif rand < 0.65:
                string = "The fountain shimmers oddly. Is it glowing?"
            else:
                return
        loc.msg_contents(string)
