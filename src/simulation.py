from event import create_event
import heapq

# def start_fight(tank, enemy):
#     print(f"Fight started between {tank.Name} and {enemy.Name}")
#     message = ''
#     time = 0.0
#     while tank.is_alive() and enemy.is_alive():
#         if time % tank.AtkInterval == 0:
#             enemy.CurrentHealth -= tank.Damage
#             message += f"{tank.Name} attacks {enemy.Name} for {tank.Damage} damage. {enemy.Name} has {enemy.CurrentHealth} health left."
#             ##message += create_event(time, 'Attack', tank, enemy, '')
#         if time % enemy.AtkInterval == 0:
#             tank.CurrentHealth -= enemy.Damage
#             if message:
#                 message += "\n"
#             message += f"{enemy.Name} attacks {tank.Name} for {enemy.Damage} damage. {tank.Name} has {tank.CurrentHealth} health left."
#         time += 1.0
#         if message:
#             print(message)
#             message = ''
#     if not tank.is_alive():
#         message += f"{tank.Name} has been defeated."
#     if not enemy.is_alive():
#         message += f"{enemy.Name} has been defeated."
#     print(message)

def start_fight(tank, enemy):
    events = []
