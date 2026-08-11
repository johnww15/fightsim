from ability import Ability
from character import Character

class Event(object):
    def __init__(self, timestamp: float, ability: Ability, source: Character, target: Character) -> None:
        self.timestamp = timestamp
        self.ability = ability
        self.source = source
        self.target = target
        self.event_type = ''
        self.action = ''