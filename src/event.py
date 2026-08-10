class Event(object):
    def __init__(self):
        self.timestamp = 0.0
        self.event_type = ''
        self.source = None
        self.target = None
        self.action = ''

def create_event(timestamp, event_type, source, target, action):
    event = Event()
    event.timestamp = timestamp
    event.event_type = event_type
    event.source = source
    event.target = target
    event.action = action
