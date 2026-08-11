class Ability:
    def __init__(
            self,
            name: str | None = None
    ) -> None:
        self.name: str | None = name
        self.base_damage: float = 0.0
        self.cooldown: float = 0.0
        self.cast_time: float = 0.0
        self.mana_cost: int = 0
        self.damage: float = 0.0
        self.action_time: float = 0.0

class AutoAttack(Ability):
    def __init__(self, strength: int, dexterity: int) -> None:
        super().__init__('Auto Attack')
        self.damage_coefficient = 10.0
        self.damage = self.calculate_damage(strength)
        self.action_time = self.calculate_attack_interval(dexterity)
        self.event_pattern = [{
                                "event_type": "ATTACK",
                                "timing": "END",
                                "action": "DEAL_DAMAGE"
                            }]

    def calculate_damage(self, strength: int) -> float:
        return (strength * self.damage_coefficient)

    def calculate_attack_interval(self, dexterity:int) -> float:
        base_interval = 3.0  # Base attack interval in seconds
        dexterity_factor = 0.1  # Each point of dexterity reduces the interval by 10%
        interval_reduction = dexterity * dexterity_factor
        attack_interval = max(base_interval - interval_reduction, 0.1)  # Ensure a minimum interval of 0.1 seconds
        return attack_interval

class ShieldCrash(Ability):
    def __init__(self, strength: int) -> None:
        super().__init__('Shield Crash')
        self.damage_coefficient = 20.0
        self.damage = self.calculate_damage(strength)
        self.action_time = 2.0
        self.mana_cost = 50
        self.event_pattern = [{
                                "event_type": "ATTACK",
                                "timing": "END",
                                "action": "DEAL_DAMAGE"
                            }]

    def calculate_damage(self, strength: int) -> float:
        return (strength * self.damage_coefficient)