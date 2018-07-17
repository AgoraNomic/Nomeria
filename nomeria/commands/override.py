from evennia.commands.default import general, help


class CmdGet(general.CmdGet):
    """
    Pick something up

    Usage:
      get <obj>

    Picks up an object from your location and puts it in
    your inventory.
    """
    aliases = ["grab", "take", "pick up"]


class CmdHelp(help.CmdHelp):
    """
    View help or a list of topics

    Usage:
      help <topic or command>
      help list
      help all

    This will search for help on commands and other
    topics related to the game.
    """
    aliases = ["man", "?"]
