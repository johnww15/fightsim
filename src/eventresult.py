class EventResult(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.source = None
        self.target = None
        self.ability = None

def create_event_result(timestamp, source, target, ability):
    event_result = EventResult(timestamp)
    event_result.source = source
    event_result.target = target
    event_result.ability = ability
    return event_result

def print_event_result(event_result):
    print(f"At t={event_result.timestamp}, {event_result.source.name} used {event_result.ability.__class__.__name__} on {event_result.target.name}. {event_result.target.name} has {event_result.target.current_health} health left.")
