from ability import Ability

class Character:
    def __init__(
            self
    ) -> None:
        self.name: str | None = None
        self.max_health: float = 1000.0
        self.current_health: float = 1000.0
        self.strength: int = 0
        self.dexterity: int = 0
        self.max_mana: int = 0
        self.mana: int = 0
        self.abilities: list[Ability] = []

    def add_ability(self, ability: Ability) -> None:
        self.abilities.append(ability)

    def is_alive(self) -> bool:
        return self.current_health > 0

class Tank(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Tank'
        self.max_health = 1000
        self.current_health = 1000
        self.strength = 10
        self.dexterity = 0

class Enemy(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Enemy'
        self.max_health = 1000
        self.current_health = 1000
        self.strength = 10
        self.dexterity = 10