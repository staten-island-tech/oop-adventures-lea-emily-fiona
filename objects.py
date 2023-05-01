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
        thing.use = "Attack stuff"
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

ironswords = []
goldswords = []

swordquestion = input("Do you want a sword? ")
whichsword = input("Which sword do you want? ")

def getgoldsword(name, damage):
    goldsword = gold_sword(name, damage)
    goldswords.append(goldsword)
    for sword in goldswords:
        print(sword)

def getironsword(name, damage):
    ironsword = iron_sword(name, damage)
    ironswords.append(ironsword)
    for sword in ironswords:
        print(sword)

if swordquestion.lower() == "yes":
    if whichsword.lower() == "gold":
        print(gold)
    elif whichsword.lower() == "iron":
        print(gold)
print(ironswords)