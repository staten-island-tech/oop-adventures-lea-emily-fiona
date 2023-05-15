restart = "yes"
while restart == "yes":
    from objects import *
    lives = 5
    coins = []
    items = []
    print("Hello! And welcome to the game! Are you ready to begin?")
    start = input("y/n ").lower()
    while start != "y":
        start = input("y/n ").lower()
        if start == "y":
            print("Then let's begin...")
            break
        elif start == "n":
            print("Too bad!")
            break
        elif start != "y" or "n":
            print("that's not an option, sorry!")    
    print("    ")
    print("Your friend has been captured by the leader of a village far, far away")
    print("    ")
    print("You venture out to save him, and finally reach the village")
    print("    ")
    print("Once you reach the village, you stumble upon your first fork in the road")
    print("    ")
    print("You must choose...")
    print("Would you like to see the blacksmith or the villager")
    choice1 = input("blacksmith or villager: ").lower()
    if choice1 == "blacksmith":
        print("The blacksmith asks for your help to find iron")
        iron = input("Do you help him? y/n ").lower()
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
            print("Your", sword.name, "does", sword.damage)
            items.append("Iron sword")
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
    choice2 = input("villager or armorer: ").lower()
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
        shield.name = "Iron shield"
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
        items.append("Iron shield")
        items.append("Iron Armor")
    print("After your visit, you continue walking")
    print("    ")
    print("Here at this fork you'll meet your last villager")
    print("    ")
    print("Would you like to see the witch or the alchemist?")
    choice3 = input("witch or alchemist: ").lower()
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
        print(f"the weapon(s) you have are {items}")
        if "Iron sword" in items:
            print("To show his appreciation, the alchemist turns your sword to gold!")
            print("Your gold sword now does more damage")
            items.remove("Iron sword")
            items.append("Gold sword")
        elif "Iron shield" in items:
            print("To show his appreciation, the alchemist turns your shield to gold!")
            print("Your gold shield now has better defense abilities")
            items.remove("Iron shield")
            items.append("Gold shield")
        elif "Iron sword" != items and "Iron shield" != items:
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
    print(f"You have {lives} lives and these items: {items}")
    while choice4 != "stealthy" or "aggressive":
        choice4 = input("stealthy or aggressive: ").lower()
        if choice4 == "stealthy":
            print(f"You have {x} coins")
            print("You sneak past the village leader and his guards and find your friend in the dungeons!")
            if "Gold sword" in items:
                print("You slash through the bars of the dungeon with your gold sword and your friend is saved!")
                print("The two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
            elif "Iron sword" in items:
                print("With great difficulty, you slash through the bars of iron detaining your friend")
                print("Finally, you break through, and your friend comes out, hungry, tired, and ready to go home")
                print("The two of you leave the dungeon and trek home")
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
            elif "Gold shield" in items:
                print("You wedge your gold shield under the bars of the dungeon and pry them open")
                print("Your friend crawls out, and the two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
            elif "Iron shield" in items:
                print("You try to use your shield to dent open the bars of the dungeon, but the force is too great and the shield snaps")
                print("You try to look around and find anohter way to save him, but to no avail")
                print("You and your friend are stuck down there...")
                print("...forever")
                if x >= 7:
                    print("OH!")
                    print("Good news!!")
                    print("You have enough coins to restart!")
                    restart = input("Would you like to restart? y/n").lower()
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            elif "gold sword" not in items and "sword" not in items and "gold shield" not in items and "shield" not in items:
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
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            break
        if choice4 == "aggressive":
            print(f"You have {x} coins")
            print("You seek out the village chief, with intent to harm, however, because of how reckless you were being, he snuck up on you")
            print("-1 life")
            lives = (lives-1)
            if "Gold sword" in items and lives >= 3:
                print("Good job, you have collected a golden sword and kept your lives up, you have the ability to defeat the village leader")
                print("After a tiring and eventful battle, you've defeated the village leader and rescued your friend")
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
            elif "Iron Shield" not in items and "Gold Shield" not in items and "Gold Sword" not in items and lives < 3:
                print("You've made many poor decisions in our village, and it will show in this battle")
                print("You have no effective weapon and not enough lives to last very long")
                print("You lost to the village chief and you and your friend are stuck there...")
                print("...forever")
                if x >= 7:
                    print("OH!")
                    print("Good news!!")
                    print("You have enough coins to restart!")
                    restart = input("Would you like to restart? yes/no").lower()
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            elif "Iron sword" in items and "Iron armor" in items:
                print("You have barely the necessities for this fight, but I think we can make in work")
                print("You fight like there is no tomorrow for your friend, and after a long and tired battle, you've emerged victorious")
                print("Exhaused and weak, you and your friend trek home")
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
            elif "Gold shield" in items and lives >= 3:
                print("You clutch your gold shield tight, confident you will win your friend back")
                print("And you were right!")
                print("The battle was tough, but the village leader could not break through your defenses")
                print("He gives up and gives you your friend as a means of surrender")
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
            else:
                print("You have a few items and rationed your lives well, but unfortunately it will not be enough")
                print("You lost to the village chief and you and your friend are stuck there...")
                print("...forever")
                if x >= 7:
                    print("OH!")
                    print("Good news!!")
                    print("You have enough coins to restart!")
                    restart = input("Would you like to restart? yes/no").lower()
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            break
        elif choice4 != "stealthy" or "aggressive":
            print("that's not an option, sorry!")
            
