from time import sleep
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

def abc():
    sleep(2)
    print("On your quest to find iron, you trip and fall")
    print("-1 life")
    lives = (lives-1)
    sleep(2)
    print("However, you do end up finding iron, and the blacksmith is very grateful")
    sleep(2)
    print("He gives you a sword and five pieces of gold to show his appreciation")
    sleep(1.5)
    print(f"+1, {sword.name}")
    sleep(1.5)
    print("+5 coins")
    sleep(2)
    print(f"Your {sword.name} does {sword.damage} damage")
abc()

class blacksmith_iron(objects):
    def __init__(self, name, use, side_quest):
        super().__init__(name, use)
        self.side_quest = side_quest

class armor(objects):
    def __init__(self, name, use, defense):
        super().__init__(name, use) 
        self.defense = defense   
        self.defense = 20
        self.name = "Iron armor"

class shield(armor):
    def __init__(self, name, use, defense):
        super().__init__(use, defense, name)
        shield.defense = 20
        shield.name = "Iron shield"

class shield2(shield):
    def __init__(self, name, use, defense):
        super().__init__(use, defense, name)
        shield.defense = 40
        shield.name = "Gold shield"

class weapon(objects):
    def __init__(self, use, name, damage):
        super().__init__(name, use)
        self.damage = damage

class sword(weapon):
    def __init__(self, use, name, damage):
        super().__init__(use, name, damage)
        self.name = "Iron sword"
        self.damage = 40

class sword2(sword):
    def __init__(self, use, name, damage):
        super().__init__(use, name, damage)
        self.name = "Gold sword"
        self.damage = 80



class user():
    def __init__(self, lives, coins, items, restart):
        self.lives = lives
        self.coins = coins
        self.items = items
        self.restart = restart

class  villager(user):
    def __init__(self, service, coins, items):
        super().__init__(coins, items)
        self.service = service
        self.impact = print("+10 coins")
        self.service = coins.append(10)
class sleeping_villager(villager):
    def __init__(self, service):
        super().__init__(service)
        self.impact = print("You walk in, and the villager is sleeping")
        sleep(2)
        print("While walking around, you step on a squeaky floorboard")
        sleep(2)
        print("The noise awakens the villager and he punches you for interrupting his beauty sleep!")
        sleep(1.5)
        print("-2 lives")
class blacksmith(villager):
    def __init__(self, service, coins, items, impact):
        super().__init__(service, coins, items)
        blacksmith.impact = impact
        blacksmith.impact = blacksmith_iron.side_quest()
class armorer(villager):
    def __init__(self, service, coins, items):
        super().__init__(service, coins, items)
        print("+1", shield.name)
        sleep(1.5)
        print("+1", armor.name)
        sleep(1.5)
        print("The", shield.name, "gives you", shield.defense)
        sleep(1.5)
        print("The", armor.name, "gives you", armor.defense)
        self.impact = items.append("Iron shield")
        self.impact = items.append("Iron armor")
class witch(villager):
    def __init__(self, service, coins, items):
        super().__init__(service, coins, items, lives)
        self.surprise = print("To your surprise, this witch is a good witch!")
        sleep(2)
        self.items = potions
        potions.name = "healing potion"
        potions.use = "your lives get restored!"
        self.impact = print("She gives you a", potions.name, "and", potions.use)
        sleep(1.5)
        print("reset : you now have 5 lives")
        lives = 5
class alchemist(villager):
    def __init__(self, service, items, coins):
        super().__init__(service, items, coins)
        self.impact = print("The alchemist has been studying how to turn metal into gold, and upon your arrival, he makes his breakthrough!")
        sleep(2)
        user.items = items
        print(f"the weapon(s) you have are {items}")
        sleep(1)
        if sword.name in user.items:
                print("To show his appreciation, the alchemist turns your sword to gold!")
                sleep(1.5)
                print(f"+1 {sword2.name}")
                print(f"The {sword2.name} does {sword2.damage} damage")
                items.remove(sword.name)
                self.impact = items.append(sword2.name)
        elif sword.name not in items and shield.name in user.items:
                print("To show his appreciation, the alchemist turns your shield to gold!")
                sleep(1.5)
                print(f"+1 {shield2.name}")
                print(f"The {sword2.name} has {shield2.defense} defense")
                items.remove(shield.name)
                self.impact = items.append(shield2.name)
        elif sword.name not in items and shield.name not in user.items:
                print("The alchemist is very grateful to you, and wants to show his appreciation")
                sleep(2)
                print("However, you don't have any weapons for the alchemist to work his craft on")
                sleep(2)
                print("He gives you 10 coins and sends you on your way")
                sleep(1.5)
                print("+10 coins")
                self.impact = coins.append(10)
