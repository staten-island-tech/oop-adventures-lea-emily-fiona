while restart == "no":
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
            print("+1 bronze sword")
            print("+5 coins")
            items.append("sword")
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
        print("The armorer is pleasantly surprised by your visit, and wants to help you")
        print("    ")
        print("He says he's going to teach you how to make a shield")
        print("    ")
        print("After hours of working and talking, together you've made a shield!")
        print("    ")
        print("The armorer decides he likes you, and he let's you keep the shield")
        print("+1 bronze shield")
        items.append("shield")
    print("After your visit, you continue walking")
    print("    ")
    print("Here at this fork you'll meet your last villager")
    print("    ")
    print("Would you like to see the witch or the alchemist?")
    choice3 = input("witch or alchemist").lower()
    if choice3 == "witch":
        print("To your surprise, this witch is a good witch!")
        print("    ")
        print("She gives you a healing potion and your lives are restored")
        print("reset - 5 lives")
        lives = 5
    elif choice3 == "alchemist":
        print("The alchemist has been studying how to turn metal into gold, and upon your arrival, he makes his breakthrough!")
        print("    ")
        def select_weapon(name, damage):
            new_weapon = weapon(name, damage)
            items.append(new_weapon)
            for weapon in items:
                print(items)
        w = "Y"
        while w == "Y":
            print(f"the weapon(s) you have are {items}")
            if "sword" == items:
                print("To show his appreciation, the alchemist turns your sword to gold!")
                print("Your gold sword now does more damage")
                items.remove("sword")
                items.append("gold sword")
            elif "sword" != items and "shield" == items:
                print("To show his appreciation, the alchemist turns your shield to gold!")
                print("Your gold shield now has better defense abilities")
                items.remove("shield")
                items.append("gold shield")
            elif "sword" != items and "shield" != items:
                print("The alchemist is very grateful to you, and wants to show his appreciation")
                print("    ")
                print("However, you don't have any weapons for the alchemist to work his craft on")
                print("    ")
                print("He gives you 10 coins and sends you on your way")
                print("+10 coins")
                coins.append(10)
    x = sum(coins)
    print("Now that you've met all the villagers, you've reached the village leader's house!")
    print("    ")
    print("Time to get your friend back!")
    print("    ")
    print("Before you enter, which approach would you like to take?")
    print(f"the weapon(s) you have are {items}")
    choice4 = input("stealthy or aggressive").lower()
    if choice4 == "stealthy":
        print("You sneak past the village leader and his guards and find your friend in the dungeons!")
        if "gold sword" == items:
            print("You slash through the bars of the dungeon with your gold sword and your friend is saved!")
            print("The two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
            print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
        elif "sword" == items:
            print("With great difficulty, you slash through the bars of iron detaining your friend")
            print("Finally, you break through, and your friend comes out, hungry, tired, and ready to go home")
            print("The two of you leave the dungeon and trek home")
            print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
        elif "gold shield" == items:
            print("You wedge your gold shield under the bars of the dungeon and pry them open")
            print("Your friend crawls out, and the two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
            print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
        elif "shield" == items:
            print("You try to use your shield to dent open the bars of the dungeon, but the force is too great and the shield snaps")
            print("You try to look around and find anohter way to save him, but to no avail")
            print("You and your friend are stuck down there...")
            print("...forever")
            if x >= 7:
                print("OH!")
                print("Good news!!")
                print("You have enough coins to restart!")
                restart = input("Would you like to restart? y/n").lower()
            if x < 7:
                print("Better luck next time😢")
        elif "gold sword" != items and "sword" != items and "gold shield" != items and "shield" != items:
            print("You find your friend, but see he is trapped behind heavy iron bars")
            print("In vain, you look around for something to rescue them with")
            print("However, after about an hour of looking and thinking, you come to your senses")
            print("There's nothing here...")
            print("You and your friend are stuck down there...")
            print("...forever")
            if x >= 7:
                print("OH!")
                print("Good news!!")
                print("You have enough coins to restart!")
                restart = input("Would you like to restart? y/n").lower()
            if x < 7:
                print("Better luck next time😢")

