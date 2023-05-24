from time import sleep
restart = "yes"
while restart == "yes":
    longsleep = 2
    medsleep = 1.5
    shortsleep = 1
    from objects import *
    lives = 5
    coins = []
    items = []
    choice1 = []
    start = []
    iron = []
    choice2 = []
    choice3 = []
    choice4 = []
    print("Hello! And welcome to the game! Are you ready to begin?")
    sleep(shortsleep)
    while start != "y":
        start = input("y/n ").lower()
    while start != "y" or "n":
        start = input("y/n").lower()
        if start == "y":
            print("Then let's begin...")
            break
        elif start == "n":
            print("Too bad!")
            break
        elif start != "y" or "n":
            print("that's not an option, sorry!") 
    sleep(shortsleep)
        else:
            print("that's not an option, sorry!")    
    sleep(2)
    print("Your friend has been captured by the leader of a village far, far away")
    sleep(longsleep)
    sleep(2)
    print("You venture out to save him, and finally reach the village")
    sleep(longsleep)
    sleep(2)
    print("Once you reach the village, you stumble upon your first fork in the road")
    sleep(longsleep)
    sleep(2)
    print("You must choose...")
    sleep(longsleep)
    sleep(2)
    print("Would you like to see the blacksmith or the villager")
    sleep(shortsleep)
    sleep(1)
    while choice1 != "blacksmith" or "villager":
        choice1 = input("blacksmith or villager: ").lower()
        choice1 = input("blacksmith or villager:").lower()
        if choice1 == "blacksmith":
            sleep(longsleep)
            print("The blacksmith asks for your help to find iron")
            sleep(shortsleep)
            while start != "y" or "n":
                iron = input("Do you help him? y/n ").lower()
            def black_smith():
                blacksmith
            black_smith()
            while iron != "y" or "n":
                iron = input("Do you help him? y/n").lower()
                if iron == "y":
                    sleep(longsleep)
                    print("On your quest to find iron, you trip and fall")
                    sleep(medsleep)
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
                    items.append("Iron sword")
                    coins.append(5)
                    def side_quest():
                        blacksmith_iron
                    side_quest()
                    blacksmith.impact = items.append("Iron sword")
                    blacksmith.impact = coins.append(5)
                    break
                elif iron == "n":
                    sleep(longsleep)
                    sleep(2)
                    print("He's mad and yells at you")
                    sleep(longsleep)
                    sleep(2)
                    print("You take emotional damage")
                    sleep(medsleep)
                    print("-1 life")
                    sleep(1.5)
                    blacksmith.impact = print("-1 life")
                    lives = (lives-1)
                    break
                elif iron != "y" or "n":
                else:
                    print("that's not an option, sorry!")
            break
        elif choice1 == "villager":
            sleep(longsleep)
            print("The villager isn't home, but you see a chest in his home!")
            sleep(longsleep)
            print("You open the chest and find coins!")
            sleep(medsleep)
            print("+10 coins")
            coins.append(10)
            def village():
                print("The villager isn't home, but you see a chest in his home!")
                sleep(2)
                print("You open the chest and find coins!")
                sleep(1.5)
                villager
            break
        elif choice1 != "blacksmith" or "villager":
        else:
            print("that's not an option, sorry!")
    sleep(longsleep)
    sleep(2)
    print("You venture farther through the village and meet your next obstacle")
    sleep(longsleep)
    sleep(2)
    print("Two houses stand before you, the villager's and the armorer's")
    sleep(longsleep)
    sleep(2)
    print("Would you like to visit the villager or the armorer?")
    sleep(shortsleep)
    sleep(1)
    while choice2 != "armorer" or "villager":
        choice2 = input("villager or armorer: ").lower()
        choice2 = input("villager or armorer:").lower()
        if choice2 == "villager":
            sleep(longsleep)
            print("You walk in, and the villager is sleeping")
            sleep(longsleep)
            print("While walking around, you step on a squeaky floorboard")
            sleep(longsleep)
            print("The noise awakens the villager and he punches you for interrupting his beauty sleep!")
            sleep(medsleep)
            print("-2 lives")
            def sleeper():
                sleeping_villager
            sleeper()
            lives = (lives-2)
            break
        elif choice2 == "armorer":
            armor.defense = "+20 defense"
            armor.name = "Iron armor"
            shield.defense = "+20 defense"
            shield.name = "Iron shield"
            sleep(longsleep)
            print("The armorer is pleasantly surprised by your visit, and wants to help you")
            sleep(longsleep)
            sleep(2)
            print("He says he's going to teach you how to make defensive items!")
            sleep(longsleep)
            sleep(2)
            print("After hours of working and talking, together you've made armor and a shield!")
            sleep(longsleep)
            sleep(2)
            print("The armorer decides he likes you, and he let's you keep the armor and shield!")
            sleep(medsleep)
            print("+1", shield.name)
            sleep(medsleep)
            print("+1", armor.name)
            sleep(medsleep)
            print("The", shield.name, "gives you", shield.defense)
            sleep(medsleep)
            print("The", armor.name, "gives you", armor.defense)
            items.append("Iron shield")
            items.append("Iron armor")
            sleep(1.5)
            def armor_give():
                armorer
            armor_give()
            break
        elif choice2 != "armorer" or "villager":
        else:
            print("that's not an option, sorry!")
    sleep(longsleep)
    sleep(2)
    print("After your visit, you continue walking")
    sleep(longsleep)
    sleep(2)
    print("Here at this fork you'll meet your last villager")
    sleep(longsleep)
    sleep(2)
    print("Would you like to see the witch or the alchemist?")
    sleep(shortsleep)
    sleep(1)
    while choice3 != "witch" or "alchemist":
        choice3 = input("witch or alchemist: ").lower()
        choice3 = input("witch or alchemist:").lower()
        if choice3 == "witch":
            sleep(longsleep)
            print("To your surprise, this witch is a good witch!")
            sleep(longsleep)
            potions.name = "healing potion"
            potions.use = "your lives get restored!"
            print("She gives you a", potions.name, "and", potions.use)
            sleep(medsleep)
            print("reset : you now have 5 lives")
            lives = 5
            def healer():
                witch
            healer()
            break
        elif choice3 == "alchemist":
            sleep(longsleep)
            print("The alchemist has been studying how to turn metal into gold, and upon your arrival, he makes his breakthrough!")
            sleep(longsleep)
            sleep(2)
            print(f"the weapon(s) you have are {items}")
            sleep(shortsleep)
            sleep(1)
            if "Iron sword" in items:
                print("To show his appreciation, the alchemist turns your sword to gold!")
                sleep(medsleep)
                sleep(1.5)
                print("Your gold sword now does more damage")
                items.remove("Iron sword")
                items.append("Gold sword")
            elif "Iron sword" not in items and "Iron shield" in items:
                print("To show his appreciation, the alchemist turns your shield to gold!")
                sleep(medsleep)
                sleep(1.5)
                print("Your gold shield now has better defense abilities")
                items.remove("Iron shield")
                items.append("Gold shield")
            elif "Iron sword" not in items and "Iron shield" not in items:
                print("The alchemist is very grateful to you, and wants to show his appreciation")
                sleep(longsleep)
                sleep(2)
                print("However, you don't have any weapons for the alchemist to work his craft on")
                sleep(longsleep)
                sleep(2)
                print("He gives you 10 coins and sends you on your way")
                sleep(medsleep)
                sleep(1.5)
                print("+10 coins")
                coins.append(10)
            break
        elif choice3 != "witch" or "alchemist":
        else:
            print("that's not an option, sorry!")
    x = sum(coins)
    sleep(longsleep)
    sleep(2)
    print("Now that you've met all the villagers, you've reached the village leader's house!")
    sleep(longsleep)
    sleep(2)
    print("Time to get your friend back!")
    sleep(longsleep)
    sleep(2)
    print("Before you enter, which approach would you like to take?")
    sleep(shortsleep)
    sleep(1)
    print(f"You have {lives} lives and these items: {items}")
    while choice4 != "stealthy" or "aggressive":
        choice4 = input("stealthy or aggressive: ").lower()
        sleep(2)
        if choice4 == "stealthy":
            sleep(longsleep)
            print(f"You have {x} coins")
            sleep(longsleep)
            sleep(2)
            print("You sneak past the village leader and his guards and find your friend in the dungeons!")
            if "Gold sword" in items:
                sleep(longsleep)
                print("You slash through the bars of the dungeon with your gold sword and your friend is saved!")
                sleep(longsleep)
                sleep(2)
                print("The two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                sleep(longsleep)
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
                while restart != "yes" or "no":
                        restart = input("Would you like to play again? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
            elif "Iron sword" in items:
                sleep(longsleep)
                print("With great difficulty, you slash through the bars of iron detaining your friend")
                sleep(longsleep)
                sleep(2)
                print("Finally, you break through, and your friend comes out, hungry, tired, and ready to go home")
                sleep(longsleep)
                sleep(2)
                print("The two of you leave the dungeon and trek home")
                sleep(longsleep)
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
                while restart != "yes" or "no":
                        restart = input("Would you like to play again? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
            elif "Gold shield" in items:
                sleep(longsleep)
                print("You wedge your gold shield under the bars of the dungeon and pry them open")
                sleep(longsleep)
                sleep(2)
                print("Your friend crawls out, and the two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                sleep(longsleep)
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                sleep(longsleep)
                restart = "no"
                while restart != "yes" or "no":
                        restart = input("Would you like to play again? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
            elif "Iron shield" in items:
                sleep(longsleep)
                print("You try to use your shield to dent open the bars of the dungeon, but the force is too great and the shield snaps")
                sleep(longsleep)
                sleep(2)
                print("You try to look around and find anohter way to save him, but to no avail")
                sleep(longsleep)
                sleep(2)
                print("You and your friend are stuck down there...")
                sleep(longsleep)
                sleep(2)
                print("...forever")
                sleep(longsleep)
                sleep(2)
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    sleep(2)
                    print("Good news!!")
                    sleep(longsleep)
                    sleep(2)
                    print("You have enough coins to restart!")
                    sleep(longsleep)
                    restart = input("Would you like to restart? yes/no ").lower()
                    while restart != "yes" or "no":
                        restart = input("Would you like to restart? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
                    break
            elif "gold sword" not in items and "sword" not in items and "gold shield" not in items and "shield" not in items:
                sleep(longsleep)
                print("You find your friend, but see he is trapped behind heavy iron bars")
                sleep(longsleep)
                sleep(2)
                print("In vain, you look around for something to rescue them with")
                sleep(longsleep)
                sleep(2)
                print("However, after about an hour of looking and thinking, you come to your senses")
                sleep(longsleep)
                sleep(2)
                print("There's nothing here...")
                sleep(longsleep)
                sleep(2)
                print("You and your friend are stuck down there...")
                sleep(longsleep)
                sleep(2)
                print("...forever")
                sleep(longsleep)
                sleep(2)
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    sleep(2)
                    print("Good news!!")
                    sleep(longsleep)
                    sleep(2)
                    print("You have enough coins to restart!")
                    sleep(longsleep)
                    restart = input("Would you like to restart? yes/no ").lower()
                    while restart != "yes" or "no":
                        restart = input("Would you like to restart? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            break
        if choice4 == "aggressive":
            sleep(longsleep)
            print(f"You have {x} coins")
            sleep(longsleep)
            sleep(2)
            print("You seek out the village chief, with intent to harm, however, because of how reckless you were being, he snuck up on you")
            sleep(medsleep)
            sleep(0.5)
            print("-1 life")
            sleep(2)
            lives = (lives-1)
            if "Gold sword" in items and lives >= 3:
                sleep(longsleep)
                print("Good job, you have collected a golden sword and kept your lives up, you have the ability to defeat the village leader")
                sleep(longsleep)
                sleep(2)
                print("After a tiring and eventful battle, you've defeated the village leader and rescued your friend")
                sleep(longsleep)
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
                while restart != "yes" or "no":
                        restart = input("Would you like to play again? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
            elif "Iron Shield" not in items and "Gold Shield" not in items and "Gold Sword" not in items and lives < 3:
                sleep(longsleep)
                print("You've made many poor decisions in our village, and it will show in this battle")
                sleep(longsleep)
                sleep(2)
                print("You have no effective weapon and not enough lives to last very long")
                sleep(longsleep)
                sleep(2)
                print("You lost to the village chief and you and your friend are stuck there...")
                sleep(longsleep)
                sleep(2)
                print("...forever")
                sleep(longsleep)
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    sleep(2)
                    print("Good news!!")
                    sleep(longsleep)
                    sleep(2)
                    print("You have enough coins to restart!")
                    sleep(longsleep)
                    restart = input("Would you like to restart? yes/no ").lower()
                    while restart != "yes" or "no":
                        restart = input("Would you like to restart? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            elif "Iron sword" in items and "Iron armor" in items:
                sleep(longsleep)
                print("You have barely the necessities for this fight, but I think we can make in work")
                sleep(longsleep)
                sleep(2)
                print("You fight like there is no tomorrow for your friend, and after a long and tired battle, you've emerged victorious")
                sleep(longsleep)
                sleep(2)
                print("Exhaused and weak, you and your friend trek home")
                sleep(longsleep)
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
                while restart != "yes" or "no":
                        restart = input("Would you like to play again? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
            elif "Gold shield" in items and lives >= 3:
                sleep(longsleep)
                print("You clutch your gold shield tight, confident you will win your friend back")
                sleep(longsleep)
                sleep(2)
                print("And you were right!")
                sleep(longsleep)
                sleep(2)
                print("The battle was tough, but the village leader could not break through your defenses")
                sleep(longsleep)
                sleep(2)
                print("He gives up and gives you your friend as a means of surrender")
                sleep(longsleep)
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
                restart = "no"
                while restart != "yes" or "no":
                        restart = input("Would you like to play again? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
            else:
                sleep(longsleep)
                print("You have a few items and rationed your lives well, but unfortunately it will not be enough")
                sleep(longsleep)
                sleep(2)
                print("You lost to the village chief and you and your friend are stuck there...")
                sleep(longsleep)
                sleep(2)
                print("...forever")
                sleep(longsleep)
                sleep(2)
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    sleep(2)
                    print("Good news!!")
                    sleep(longsleep)
                    sleep(2)
                    print("You have enough coins to restart!")
                    sleep(longsleep)
                    restart = input("Would you like to restart? yes/no ").lower()
                    while restart != "yes" or "no":
                        restart = input("Would you like to restart? y/n").lower()
                        if restart == "y":
                            restart = "yes"
                            break
                        elif restart == "n":
                            restart = "no"
                            break
                        else:
                            print("that's not an option, sorry!")
                elif x < 7:
                    print("Better luck next time😢")
                    restart = "no"
            break
        elif choice4 != "stealthy" or "aggressive":
            print("that's not an option, sorry!")
            
        else:
            print("that's not an option, sorry!")   