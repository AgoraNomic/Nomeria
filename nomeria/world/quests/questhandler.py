from evennia import logger


class QuestHandler(object):
    """Controls all quests for one player."""

    def __init__(self, player):
        self.player = player

    def send(self, event):
        """Dispatches an event to each open quest.

        Arguments:
            event - an arbitrary entity communicating information to
                    the quests"""

        for quest in self.player.db.quests:
            try:
                quest.send(event)
            except Exception:
                logger.log_trace()

    def add(self, quest):
        """Registers a quest with the handler if it is unregistered."""
        player = self.player.db

        if callable(quest):
            quest = quest(self.player)

        if quest not in player.closed_quests:
            player.open_quests.add(quest)
