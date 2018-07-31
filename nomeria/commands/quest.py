from evennia.utils.evtable import EvTable
from commands.command import Command


class CmdQuests(Command):
    """Display quests."""

    key = "quests"
    locks = "cmd:all()"

    def init_parser(self):
        self.parser.add_argument("type", choices=("open", "closed", "all"),
                                 help="What quests do you want to see?")

    def func(self):
        def name(item):
            return item.name

        open_quests = sorted(self.caller.db.open_quests, key=name)
        open_quests = filter(open_quests, lambda quest: not quest.hidden)

        closed_quests = sorted(self.caller.db.closed_quests, key=name)

        if self.opts.type == "open":
            table = EvTable("Name", "Description")
            for quest in open_quests:
                table.add_row(quest.name, quest.description)

        elif self.opts.type == "closed":
            table = EvTable("Name", "Description")
            for quest in closed_quests:
                table.add_row(quest.name, quest.description)

        elif self.opts.type == "all":
            table = EvTable("Name", "Description", "Status")
            for quest in open_quests:
                table.add_row(quest.name, quest.description, "Open")
            for quest in closed_quests:
                table.add_row(quest.name, quest.description, "Closed")

        table.reformat(width=72)
        if len(table.get()) <= 3:
            self.caller.msg("You have no quests meeting that description.")
        else:
            self.caller.msg(table)
