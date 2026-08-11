from character import Tank, Enemy
from ability import AutoAttack
from simulation import start_fight

print("-----Simulator run-----")

## Test 1
tank = Tank()
enemy = Enemy()
enemy.add_ability(AutoAttack(enemy.strength, enemy.dexterity))
tank.add_ability(AutoAttack(tank.strength, tank.dexterity))
start_fight(tank, enemy)

print("-----Simulator end-----")