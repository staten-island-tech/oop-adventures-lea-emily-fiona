class objects():
    def __init__(self, name, use):
        self.name = name
        self.use = use

class potions(objects):
    def __init__(self, name, use):
        super().__init__(name, use)

class healing_potion(potions):
    def __init__(self, name, use, healing):
        super().__init__(name, use)
        self.healing = healing

class gold(objects):
    def __init__(self, name, use):
        super().__init__(name, use)

class armor(objects):
    def __init__(self, name, use, defense):
        super().__init__(name, use)
        self.defense = defense

class shield(armor):
    def __init__(self, name, use, defense):
        super().__init__(use, defense, name)

class weapon(objects):
    def __init__(self, use, name, damage):
        super().__init__(name, use)
        self.damage = damage

class sword(weapon):
    def __init__(self, use, name, damage):
        super().__init__(use, name, damage)
        