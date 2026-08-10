from ability import *

class Character(object):
    def __init__(self):
        self.Name = ''
        self.MaxHealth = 1000
        self.CurrentHealth = 1000
        self.Strength = 0
        self.Dexterity = 0
        self.MaxMana = 0
        self.Mana = 0
        self.Abilities = []

    def add_ability(self, abilities):
        self.Abilities.append(abilities)

    def is_alive(self):
        return self.CurrentHealth > 0

class Tank(Character):
    def __init__(self):
        super().__init__()
        self.Name = 'Tank'
        self.MaxHealth = 1000
        self.CurrentHealth = 1000
        self.Strength = 10
        self.Dexterity = 0

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.Name = 'Enemy'
        self.MaxHealth = 1000
        self.CurrentHealth = 1000
        self.Strength = 10
        self.Dexterity = 10