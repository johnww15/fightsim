class Event(object):
    def __init__(self):
        self.Timestamp = 0.0
        self.EventType = ''
        self.Source = None
        self.Target = None
        self.Action = ''

def create_event(timestamp, event_type, source, target, action):
    event = Event()
    event.Timestamp = timestamp
    event.EventType = event_type
    event.Source = source
    event.Target = target
    event.Action = action
