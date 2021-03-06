"""
Module containing NHL game objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from .list import List
from .team import Team
from .venue import Venue

@dataclass(frozen=True)
class Game(Flyweight):
    """
    NHL game object.

    This is the detailed docstring.
    """

    __slots__ = ["id", "home", "away", "venue", "players", "events"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal game ID"""

    home: Team
    """Team: Game home"""

    away: Team
    """Team: Game away"""

    venue: Venue
    """Venue: """

    players: List
    """List: """

    events: List
    """List: """

    @classmethod
    def _key(cls, id, *args, **kwargs):
        return id

    @classmethod
    def has_key(cls, id):
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        return super().from_key(id)

    def __repr__(self):
        # return "<nhl.Game: {}, {} ({}) at ({}) {}, {}, ID {}>".format(self.gameinfo.description, self.away.team.abbreviation, self.gameinfo.score[1], self.gameinfo.score[0], self.home.team.abbreviation, self.gameinfo.date, self.gameinfo.id)
        return "<nhl.Game: {} at {}, ID {}>".format(self.away.abbreviation, self.home.abbreviation, self.id)
