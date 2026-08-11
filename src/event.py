from ability import Ability
from character import Character

class Event:
    def __init__(
        self,
        timestamp: float,
        ability: Ability,
        source: Character,
        target: Character,
    ) -> None:
        self.timestamp: float = timestamp
        self.ability: Ability = ability
        self.source: Character = source
        self.target: Character = target
        self.event_type: str | None = None
        self.action: str | None = None