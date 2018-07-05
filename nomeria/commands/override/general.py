from evennia.commands.default.general import CmdGet as OldCmdGet


class CmdGet(OldCmdGet):
    aliases = ["grab", "take", "pick up"]
