from objects import *
lives = 5
coins = []
items = []
print("Hello! And welcome to the game! Are you ready to begin?")
start = input("y/n").lower()
if start == "y":
    print("Then let's begin...")
if start == "n":
    print("Too bad!")
print("    ")
print("Your friend has been captured by the leader of a village far, far away")
print("    ")
print("You venture out to save him, and finally reach the village")
print("    ")
print("Once you reach the village, you stumble upon your first fork in the road")
print("    ")
print("You must choose...")
print("Would you like to see the blacksmith or the villager")
choice1 = input("blacksmith or villager").lower()
if choice1 == "blacksmith":
    print("The blacksmith asks whether or not you'd like to help him find iron")
    iron = input("Do you help him? y/n").lower()
    if iron == "y":
        print("    ")
        print("On your quest to find iron, you trip and fall")
        print("-1 life")
        lives = (lives-1)
        print("    ")
        print("However, you do end up finding iron, and the blacksmith is very grateful")
        print("    ")
        print("He gives you a sword and five pieces of gold to show his appreciation")
        sword.name = "Iron sword"
        sword.damage = "40 damage"
        print("+1", sword.name)
        print("+5 coins")
        print("The stats of the", sword.name, "is:", sword.damage)
        items.append(sword)
        coins.append(5)
    elif iron == "n":
        print("He's mad and yells at you")
        print("    ")
        print("You take emotional damage")
        print("-1 life")
        lives = (lives-1)
elif choice1 == "villager":
    print("The villager isn't home, but you see a chest in his home!")
    print("    ")
    print("You open the chest and find coins!")
    print("+10 coins")
    coins.append(10)
print("You venture farther through the village and meet your next obstacle")
print("    ")
print("Two houses stand before you, the villager's and the armorer's")
print("Would you like to visit the villager or the armorer?")
choice2 = input("villager or armorer").lower()
if choice2 == "villager":
    print("You walk in, and the villager is sleeping")
    print("    ")
    print("While walking around, you step on a squeaky floorboard")
    print("    ")
    print("The noise awakens the villager and he punches you for interrupting his beauty sleep!")
    print("-2 lives")
    lives = (lives-2)
elif choice2 == "armorer":
    armor.defense = "+20 defense"
    armor.name = "Iron armor"
    shield.defense = "+20 defense"
    shield.name = "Bronze shield"
    print("The armorer is pleasantly surprised by your visit, and wants to help you")
    print("    ")
    print("He says he's going to teach you how to make defensive items!")
    print("    ")
    print("After hours of working and talking, together you've made armor and a shield!")
    print("    ")
    print("The armorer decides he likes you, and he let's you keep the armor and shield!")
    print("+1", shield.name)
    print("+1", armor.name)
    print("The", shield.name, "gives you", shield.defense)
    print("The", armor.name, "gives you", armor.defense)
    items.append(shield)
    items.append(armor)
print("After your visit, you continue walking")
print("    ")
print("Here at this fork you'll meet your last villager")
print("    ")
print("Would you like to see the witch or the alchemist?")
choice3 = input("witch or alchemist").lower()
if choice3 == "witch":
    print("To your surprise, this witch is a good witch!")
    print("    ")
    potions.name = "healing potion"
    potions.use = "your lives get restored!"
    print("She gives you a", potions.name, "and", potions.use)
    print("reset - you now have 5 lives")
    lives = 5
elif choice3 == "alchemist":
    print("The alchemist has been studying how to turn metal into gold, and upon your arrival, he makes his breakthrough!")
    print("    ")
    def select_weapon(name, damage):
        new_weapon = weapon(name, damage)
        items.append(new_weapon)
        for weapon in items:
            print(items)
    print("To show his appreciation, the alchemist turns your sword")
    print("To show his appreciation, the alchemist turns your sword into a golden sword")
    print(" -1 Iron sword")
    print("+1 Golden Sword")
    sword.name = "Golden Sword"
    sword.damage = "80 damage"
    print("The stats of the", sword.name, "is:", sword.damage)
