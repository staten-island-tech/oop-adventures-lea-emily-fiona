class objects:
    def __init__(thing, name, use):
        thing.name = name
        thing.use = use

class gold(objects):
    def __init__(thing, name, use):
        super().__init__(name, use)
        name = "Gold"
        use = "Buy stuff"

class weapons(objects):
    def __init__(thing, name, use, damage):
        super().__init__(name, use)
        thing.damage = damage
    def str(thing):
        return f"{thing.name}, {thing.use}, {thing.damage}"

class iron_sword(weapons):
    def __init__(thing, name, use, damage):
        super().__init__(name, use, damage)
        thing.name = "Iron Sword"
        thing.damage = "40 damage per attack"
    def str(thing):
        return f"{thing.name}, {thing.use}, {thing.damage}"

class gold_sword(weapons):
    def __init__(thing, name, use, damage):
        super().__init__(name, use, damage)
        thing.name = "Golden Sword"
        thing.damage = "80 damage per attack"
    def str(thing):
        return f"{thing.name}, {thing.use}, {thing.damage}"

swords = []
def get_goldsword(name, damage):
    goldsword = gold_sword(name, damage)
    swords.append(goldsword)
    for sword in swords:
        print(sword)

def get_ironsword(name, damage):

whichsword = input("Which sword do you want? ")
if whichsword.lower() == "gold":
    get_goldsword(name, damage)