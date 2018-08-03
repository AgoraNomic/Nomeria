import random
from typeclasses.scripts import Script


class EnvScript(Script):

    def at_script_creation(self):
        self.interval = 75
        self.persistent = True

    def at_repeat(self):
        if self.db.messages is not None:
            message = random.choice(self.db.messages)
            self.obj.msg_contents(text=((message,), {"type": "quiet"}))
