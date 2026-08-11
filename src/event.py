from ability import *
from character import *

class Event(object):
    def __init__(self):
        self.timestamp = 0.0
        self.ability = None
        self.source = None
        self.target = None
        self.event_type = ''
        self.action = ''


def create_event(timestamp, ability, source, target):
    event = Event()
    event.timestamp = timestamp
    event.ability = ability
    event.source = source
    event.target = target
    return event
