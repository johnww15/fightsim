from character import Character
from ability import Ability

class EventResult(object):
    def __init__(self, timestamp: float, source: Character, target: Character, ability: Ability) -> None:
        self.timestamp = timestamp
        self.source = source
        self.target = target
        self.ability = ability

def print_event_result(event_result: EventResult) -> None:
    print(f"At t={event_result.timestamp}, {event_result.source.name} used {event_result.ability.__class__.__name__} on {event_result.target.name}. {event_result.target.name} has {event_result.target.current_health} health left.")
