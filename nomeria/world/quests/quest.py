from abc import ABCMeta, abstractmethod, abstractproperty
import evennia
from evennia.utils import lazy_property


class Quest(object, metaclass=ABCMeta):
    def __init__(self, player):
        self._player_ref = player.dbref

    @lazy_property
    def player(self):
        evennia.search_object(self._player_ref)

    @abstractmethod
    def send(self, event):
        """
        Deals with an event.

        Arguments:
        event -- an arbitrary entity communicating information to the quest
        """
        pass

    @abstractproperty
    def name(self):
        """A short name for the quest."""
        pass

    @abstractproperty
    def description(self):
        """A longer quest description."""
        pass

    hidden = False

    def __eq__(self, other):
        return type(self) == type(other) and self.player == other.player

    def __hash__(self):
        return hash(type(self)) + hash(self.player) + 3

    def __repr__(self):
        return type(self).__name__
