class objects():
    def __init__(self, thing):
        self.thing = thing

class weapon(objects):
    def __init__(self, thing, use, name):
        super().__init__(thing)
        self.name = name
        self.use = use

class sword(weapon):
    def __init__(self, thing, use, name, damage):
        super().__init__(thing, use)
        self.name = name
        self.damage = damage

