from ability import *

class Character(object):
    def __init__(self):
        self.name = ''
        self.max_health = 1000
        self.current_health = 1000
        self.strength = 0
        self.dexterity = 0
        self.max_mana = 0
        self.mana = 0
        self.abilities = []

    def add_ability(self, abilities):
        self.abilities.append(abilities)

    def is_alive(self):
        return self.current_health > 0

class Tank(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Tank'
        self.max_health = 1000
        self.current_health = 1000
        self.strength = 10
        self.dexterity = 0

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.max_health = 1000
        self.current_health = 1000
        self.strength = 10
        self.dexterity = 10