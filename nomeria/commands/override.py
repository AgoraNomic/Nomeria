from evennia.commands.default import general, help


class CmdGet(general.CmdGet):
    aliases = ["grab", "take", "pick up"]


class CmdHelp(help.CmdHelp):
    aliases = ["man", "?"]
