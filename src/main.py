from character import Tank, Enemy
from ability import AutoAttack
from event import create_event
from simulation import start_fight

print("-----Simulator run-----")

## Test 1
tank = Tank()
enemy = Enemy()
enemy.add_ability(AutoAttack(enemy.Strength, enemy.Dexterity))
tank.add_ability(AutoAttack(tank.Strength, tank.Dexterity))
start_fight(Tank(), Enemy())

print("-----Simulator end-----")