class objects():
    def __init__(self, thing):
        self.thing = thing

class gold(objects):
    def __init__(self, thing, name, use):
        super().__init__(name, use)
        self.thing = thing
        self.name = "Gold"
        self.use = use

class weapons(objects):
    def __init__(self, thing, name, use, damage):
        super().__init__(thing, name, use)
        self.damage = damage
        self.use = use
    def str(thing):
        return f"{thing.use}, {thing.damage}"

class iron_sword(weapons):
    def __init__(self, thing, name, use, damage):
        super().__init__(name, thing, use, damage)
        self.name = name
        self.damage = damage
    def str(thing):
        return f"{thing.name}, {thing.use}, {thing.damage}"

class gold_sword(weapons):
    def __init__(self, thing, name, use, damage):
        super().__init__(name, thing, use, damage)
        self.name = name
        self.damage = damage
    def str(thing):
        return f"{thing.name}, {thing.use}, {thing.damage}"

swordquestion = input("Do you want a sword? ")
whichsword = input("Which sword do you want? ")

def getgoldsword(name, damage):
    gold_sword(name, damage)
    name = "Gold Sword"
    damage = "80 damage"


def getironsword(name, damage):
    iron_sword(name, damage)

if swordquestion.lower() == "yes":
    if whichsword.lower() == "gold":
        getgoldsword("Gold sword", "80 damage")
    elif whichsword.lower() == "iron":
        print(gold_sword)