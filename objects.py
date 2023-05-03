class objects():
    def __init__(self, name, use):
        self.name = name
        self.use = use

class potions(objects):
    def __init__(self, name, use):
        self.name = "Health Potion"
        self.use = "Heal 5 lives"

class gold(objects):
    def __init__(self, name, use):
        self.name = "Gold"
        self.use = "Purchase stuff"

class armor(objects):
    def __init__(self, name, use, defense):
        self.name = "Armor"
        self.use = "Increase your defense"
        self.defense = "+20 defense"

class shield(armor):
    def __init__(self, name, use, defense):
        super()__init__(use, defense)
        self.name = "Bronze Shield"

class weapon(objects):
    def __init__(self, use, name, damage):
        super()__init__(name)
        self.use = "Damage enemies"
        self.damage = damage

class sword(weapon):
    def __init__(self, use, name, damage):
        super()__init__(use, name, damage)
