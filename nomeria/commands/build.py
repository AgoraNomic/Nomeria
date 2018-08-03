from evennia import search_script, create_script
from evennia.utils.eveditor import EvEditor
from commands.command import Command
from typeclasses.misc.env import EnvScript


class CmdEnv(Command):
    """Manage an EnvScript."""

    key = "@env"
    aliases = ["env"]
    locks = "cmd:perm(Builder)"

    def init_parser(self):
        self.parser.add_argument("type", choices=["status", "init", "edit", "rm"],
                                 help="What do you want to do?")
        self.parser.add_argument("-l", "--location", dest="loc",
                                 help="Location of EnvScript")

    def func(self):
        caller = self.caller
        opts = self.opts

        if opts.loc:
            location = caller.search(opts.loc, global_search=True)
            if not location:
                caller.msg("Destination not found.")
                return
        else:
            location = caller.location

        existing = search_script("EnvScript", obj=location)

        if opts.type == "init":
            if len(existing) > 0:
                caller.msg("An EnvScript already exists.")
                return

            script = create_script(EnvScript, obj=location, key="EnvScript")
        elif len(existing) == 1:
            script = existing[0]
        elif len(existing) == 0:
            caller.msg("No script found.")
            return
        else:
            caller.msg("Error: multiple scripts found.")
            return

        if opts.type == "init" or opts.type == "edit":
            def _env_load(caller):
                return "\n".join(script.db.messages)

            def _env_save(caller, buffer):
                script.db.messages = buffer.splitlines()
                caller.msg("Messages saved.")
                return

            caller.msg("Please place one message on each line.")
            EvEditor(caller, loadfunc=_env_load, savefunc=_env_save,
                     key="Save messages: :w")

        if opts.type == "status":
            caller.msg("The script is operational.")

        if opts.type == "rm":
            script.delete()
            caller.msg("Script deleted.")
