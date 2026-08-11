from event import Event
from eventresult import EventResult
from ability import Ability, AutoAttack
from character import Character, Enemy, Tank
from eventresult import print_event_result

import heapq

class Simulation(object):
    def __init__(self, event_queue: list[tuple[float, int, Event]] = [], current_time: float = 0.0, event_id: int = 0) -> None:
        self.event_queue = event_queue
        self.current_time = current_time
        self.event_id = event_id

    def update_queue(self, event: Event) -> None:
        heapq.heappush(self.event_queue, (event.timestamp, self.event_id, event))
        self.event_id += 1

    def update_time(self, timestamp: float) -> None:
        self.current_time = timestamp

def start_fight(tank: Character, enemy: Character) -> None:
    simulation = Simulation()

    # Schedule the first attack events for both characters
    schedule_event(simulation, tank.abilities[0], tank, enemy)
    schedule_event(simulation, enemy.abilities[0], enemy, tank)

    while tank.is_alive() and enemy.is_alive():

        # Get the next event from the heap
        next_event_time, _, next_event = heapq.heappop(simulation.event_queue)

        # Process the event
        process_event(next_event_time, simulation, next_event)

    if tank.is_alive():
        print(f"{enemy.name} has been defeated.")
    else:
        print(f"{tank.name} has been defeated.")

def schedule_event(simulation: Simulation, ability: Ability, source: Character, target: Character) -> None:
    event = Event(simulation.current_time + ability.action_time, ability, source, target)
    simulation.update_queue(event)

def process_event(timestamp: float, simulation: Simulation, next_event: Event) -> None:
    if next_event.source and next_event.target:
        next_event.target.current_health -= next_event.ability.damage

        # Create an EventResult for damage dealt and print the event result. To be revised when more event types are added.
        result = EventResult(timestamp, next_event.source, next_event.target, next_event.ability)
        print_event_result(result)

        # Update the simulation time to the timestamp of the processed event
        simulation.update_time(timestamp)

        # Schedule the next attack for the source character
        schedule_event(simulation, next_event.source.abilities[0], next_event.source, next_event.target)

tank = Tank()
enemy = Enemy()
enemy_attack = AutoAttack(enemy.strength, enemy.dexterity)
tank_attack = AutoAttack(tank.strength, tank.dexterity)
enemy.add_ability(enemy_attack)
tank.add_ability(tank_attack)
start_fight(tank, enemy)
