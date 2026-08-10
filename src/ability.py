class Ability(object):
    def __init__(self):
        self.Name = ''
        self.BaseDamage = 0
        self.Cooldown = 0.0
        self.CastTime = 0.0
        self.ManaCost = 0

class AutoAttack(Ability):
    def __init__(self, strength, dexterity):
        super().__init__()
        self.Name = 'Auto Attack'
        self.damageCoefficient = 10.0
        self.Damage = self.calculate_damage(strength)
        self.AtkInterval = self.calculate_attack_interval(dexterity)

    def calculate_damage(self, strength):
        return (strength * self.damageCoefficient)

    def calculate_attack_interval(self, dexterity):
        base_interval = 3.0  # Base attack interval in seconds
        dexterity_factor = 0.1  # Each point of dexterity reduces the interval by 10%
        interval_reduction = dexterity * dexterity_factor
        attack_interval = max(base_interval - interval_reduction, 0.1)  # Ensure a minimum interval of 0.1 seconds
        return attack_interval