class objects():
    def __init__(self, name, use):
        self.name = name
        self.use = use

class gold(objects):
    def __init__(self, name, use):
        self.name = "Gold"
        self.use = "Purchase stuff"

class weapon(objects):
    def __init__(self, use, name, damage):
        super()__init__(name)
        self.use = "Damage enemies"
        self.damage = damage

class sword(weapon):
    def __init__(self, use, name, damage):
        super()__init__(use, name, damage)

