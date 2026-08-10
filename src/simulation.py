from event import create_event
import heapq

# def start_fight(tank, enemy):
#     print(f"Fight started between {tank.name} and {enemy.name}")
#     message = ''
#     time = 0.0
#     while tank.is_alive() and enemy.is_alive():
#         if time % tank.atk_interval == 0:
#             enemy.current_health -= tank.damage
#             message += f"{tank.name} attacks {enemy.name} for {tank.damage} damage. {enemy.name} has {enemy.current_health} health left."
#             ##message += create_event(time, 'Attack', tank, enemy, '')
#         if time % enemy.atk_interval == 0:
#             tank.current_health -= enemy.damage
#             if message:
#                 message += "\n"
#             message += f"{enemy.name} attacks {tank.name} for {enemy.damage} damage. {tank.name} has {tank.current_health} health left."
#         time += 1.0
#         if message:
#             print(message)
#             message = ''
#     if not tank.is_alive():
#         message += f"{tank.name} has been defeated."
#     if not enemy.is_alive():
#         message += f"{enemy.name} has been defeated."
#     print(message)

def start_fight(tank, enemy):
    events = []
