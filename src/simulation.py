from event import *
from ability import *
from character import *
from eventresult import *

import heapq

def start_fight(tank, enemy):
    events_heap = []
    t=0.0
    event_id = 0

    # Schedule the first attack events for both characters
    event_id = schedule_event(event_id, events_heap, t, tank.abilities[0], tank, enemy)
    event_id = schedule_event(event_id, events_heap, t, enemy.abilities[0], enemy, tank)

    while tank.is_alive() and enemy.is_alive():

        # Get the next event from the heap
        next_event_time, event_id, next_event = heapq.heappop(events_heap)
        t = next_event_time

        # Process the event
        event_id = process_event(t, event_id, events_heap, next_event)

    if tank.is_alive():
        print(f"{enemy.name} has been defeated.")
    else:
        print(f"{tank.name} has been defeated.")

def schedule_event(event_id, events_heap, timestamp, ability, source, target):
    event = create_event(timestamp, ability, source, target)
    heapq.heappush(events_heap, (timestamp + ability.action_time, event_id, event))
    return event_id + 1

def process_event(timestamp, event_id, events_heap, next_event):
    if next_event.source and next_event.target:
        next_event.target.current_health -= next_event.ability.damage

        result = create_event_result(timestamp, next_event.source, next_event.target, next_event.ability)
        print_event_result(result)

        # Schedule the next attack for the source character
        event_id = schedule_event(event_id, events_heap, timestamp, next_event.source.abilities[0], next_event.source, next_event.target)
    return event_id

tank = Tank()
enemy = Enemy()
enemy.add_ability(AutoAttack(enemy.strength, enemy.dexterity))
tank.add_ability(AutoAttack(tank.strength, tank.dexterity))
start_fight(tank, enemy)
