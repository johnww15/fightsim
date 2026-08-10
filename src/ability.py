class Ability(object):
    def __init__(self):
        self.name = ''
        self.base_damage = 0
        self.cooldown = 0.0
        self.cast_time = 0.0
        self.mana_cost = 0

class AutoAttack(Ability):
    def __init__(self, strength, dexterity):
        super().__init__()
        self.name = 'Auto Attack'
        self.damage_coefficient = 10.0
        self.damage = self.calculate_damage(strength)
        self.atk_interval = self.calculate_attack_interval(dexterity)

    def calculate_damage(self, strength):
        return (strength * self.damage_coefficient)

    def calculate_attack_interval(self, dexterity):
        base_interval = 3.0  # Base attack interval in seconds
        dexterity_factor = 0.1  # Each point of dexterity reduces the interval by 10%
        interval_reduction = dexterity * dexterity_factor
        attack_interval = max(base_interval - interval_reduction, 0.1)  # Ensure a minimum interval of 0.1 seconds
        return attack_interval