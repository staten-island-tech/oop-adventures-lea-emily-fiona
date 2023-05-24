from time import sleep
longsleep = 2
medsleep = 1.5
shortsleep = 1
class objects():
    def __init__(self, name, use):
        self.name = name
        self.use = use

class potions(objects):
    def __init__(self, name, use):
        super().__init__(name, use)

class gold(objects):
    def __init__(self, name, use):
        super().__init__(name, use)
    
class blacksmith_iron(objects):
    def __init__(self, name, use):
        super().__init__(name, use)
        self.side_quest = sleep(longsleep)
        print("On your quest to find iron, you trip and fall")
        print("-1 life")
        lives = (lives-1)
        sleep(longsleep)
        print("However, you do end up finding iron, and the blacksmith is very grateful")
        sleep(longsleep)
        print("He gives you a sword and five pieces of gold to show his appreciation")
        sleep(medsleep)
        sword.name = "Iron sword"
        sword.damage = "40 damage"
        print("+1", sword.name)
        sleep(medsleep)
        print("+5 coins")
        sleep(longsleep)
        print("Your", sword.name, "does", sword.damage)

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
        



class user():
    def __init__(self, lives, coins, items, restart):
        self.lives = lives
        self.coins = coins
        self.items = items
        self.restart = restart
    lives = 5
    coins = []
    items = []
    restart = "yes"
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
        sleep(longsleep)
        print("While walking around, you step on a squeaky floorboard")
        sleep(longsleep)
        print("The noise awakens the villager and he punches you for interrupting his beauty sleep!")
        sleep(medsleep)
        print("-2 lives")
class blacksmith(villager):
    def __init__(self, service, coins, items, impact):
        super().__init__(service, coins, items)
        self.impact = impact
        self.ask = print("The blacksmith asks for your help to find iron")
        sleep(shortsleep)
class armorer(villager):
    def __init__(self, service, coins, items):
        super().__init__(service, coins, items)
        self.impact = print("+1", shield.name)
        sleep(medsleep)
        print("+1", armor.name)
        sleep(medsleep)
        print("The", shield.name, "gives you", shield.defense)
        sleep(medsleep)
        print("The", armor.name, "gives you", armor.defense)
        items.append("Iron shield")
        items.append("Iron armor")
class witch(villager):
    def __init__(self, service, coins, items):
        super().__init__(service, coins, items, lives)
        self.surprise = print("To your surprise, this witch is a good witch!")
        sleep(longsleep)
        self.items = potions
        potions.name = "healing potion"
        potions.use = "your lives get restored!"
        self.impact = print("She gives you a", potions.name, "and", potions.use)
        sleep(medsleep)
        print("reset : you now have 5 lives")
        lives = 5