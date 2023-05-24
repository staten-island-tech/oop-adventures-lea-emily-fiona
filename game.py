from time import sleep
restart = "yes"
while restart == "yes":
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
    while start != "y" or "n":
        start = input("y/n").lower()
        if start == "y":
            print("Then let's begin...")
            break
        elif start == "n":
            print("Too bad!")
            break
        else:
            print("that's not an option, sorry!")    
    sleep(2)
    print("Your friend has been captured by the leader of a village far, far away")
    sleep(2)
    print("You venture out to save him, and finally reach the village")
    sleep(2)
    print("Once you reach the village, you stumble upon your first fork in the road")
    sleep(2)
    print("You must choose...")
    sleep(2)
    print("Would you like to see the blacksmith or the villager")
    sleep(1)
    while choice1 != "blacksmith" or "villager":
        choice1 = input("blacksmith or villager:").lower()
        if choice1 == "blacksmith":
            def black_smith():
                blacksmith
            black_smith()
            while iron != "y" or "n":
                iron = input("Do you help him? y/n").lower()
                if iron == "y":
                    def side_quest():
                        blacksmith_iron
                    side_quest()
                    blacksmith.impact = items.append("Iron sword")
                    blacksmith.impact = coins.append(5)
                    break
                elif iron == "n":
                    sleep(2)
                    print("He's mad and yells at you")
                    sleep(2)
                    print("You take emotional damage")
                    sleep(1.5)
                    blacksmith.impact = print("-1 life")
                    lives = (lives-1)
                    break
                else:
                    print("that's not an option, sorry!")
            break
        elif choice1 == "villager":
            def village():
                print("The villager isn't home, but you see a chest in his home!")
                sleep(2)
                print("You open the chest and find coins!")
                sleep(1.5)
                villager
            break
        else:
            print("that's not an option, sorry!")
    sleep(2)
    print("You venture farther through the village and meet your next obstacle")
    sleep(2)
    print("Two houses stand before you, the villager's and the armorer's")
    sleep(2)
    print("Would you like to visit the villager or the armorer?")
    sleep(1)
    while choice2 != "armorer" or "villager":
        choice2 = input("villager or armorer:").lower()
        if choice2 == "villager":
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
            print("The armorer is pleasantly surprised by your visit, and wants to help you")
            sleep(2)
            print("He says he's going to teach you how to make defensive items!")
            sleep(2)
            print("After hours of working and talking, together you've made armor and a shield!")
            sleep(2)
            print("The armorer decides he likes you, and he let's you keep the armor and shield!")
            sleep(1.5)
            def armor_give():
                armorer
            armor_give()
            break
        else:
            print("that's not an option, sorry!")
    sleep(2)
    print("After your visit, you continue walking")
    sleep(2)
    print("Here at this fork you'll meet your last villager")
    sleep(2)
    print("Would you like to see the witch or the alchemist?")
    sleep(1)
    while choice3 != "witch" or "alchemist":
        choice3 = input("witch or alchemist:").lower()
        if choice3 == "witch":
            def healer():
                witch
            healer()
            break
        elif choice3 == "alchemist":
            print("The alchemist has been studying how to turn metal into gold, and upon your arrival, he makes his breakthrough!")
            sleep(2)
            print(f"the weapon(s) you have are {items}")
            sleep(1)
            if "Iron sword" in items:
                print("To show his appreciation, the alchemist turns your sword to gold!")
                sleep(1.5)
                print("Your gold sword now does more damage")
                items.remove("Iron sword")
                items.append("Gold sword")
            elif "Iron sword" not in items and "Iron shield" in items:
                print("To show his appreciation, the alchemist turns your shield to gold!")
                sleep(1.5)
                print("Your gold shield now has better defense abilities")
                items.remove("Iron shield")
                items.append("Gold shield")
            elif "Iron sword" not in items and "Iron shield" not in items:
                print("The alchemist is very grateful to you, and wants to show his appreciation")
                sleep(2)
                print("However, you don't have any weapons for the alchemist to work his craft on")
                sleep(2)
                print("He gives you 10 coins and sends you on your way")
                sleep(1.5)
                print("+10 coins")
                coins.append(10)
            break
        else:
            print("that's not an option, sorry!")
    x = sum(coins)
    sleep(2)
    print("Now that you've met all the villagers, you've reached the village leader's house!")
    sleep(2)
    print("Time to get your friend back!")
    sleep(2)
    print("Before you enter, which approach would you like to take?")
    sleep(1)
    print(f"You have {lives} lives and these items: {items}")
    while choice4 != "stealthy" or "aggressive":
        choice4 = input("stealthy or aggressive: ").lower()
        sleep(2)
        if choice4 == "stealthy":
            print(f"You have {x} coins")
            sleep(2)
            print("You sneak past the village leader and his guards and find your friend in the dungeons!")
            if "Gold sword" in items:
                print("You slash through the bars of the dungeon with your gold sword and your friend is saved!")
                sleep(2)
                print("The two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
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
                print("With great difficulty, you slash through the bars of iron detaining your friend")
                sleep(2)
                print("Finally, you break through, and your friend comes out, hungry, tired, and ready to go home")
                sleep(2)
                print("The two of you leave the dungeon and trek home")
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
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
                print("You wedge your gold shield under the bars of the dungeon and pry them open")
                sleep(2)
                print("Your friend crawls out, and the two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
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
                print("You try to use your shield to dent open the bars of the dungeon, but the force is too great and the shield snaps")
                sleep(2)
                print("You try to look around and find anohter way to save him, but to no avail")
                sleep(2)
                print("You and your friend are stuck down there...")
                sleep(2)
                print("...forever")
                sleep(2)
                if x >= 7:
                    print("OH!")
                    sleep(2)
                    print("Good news!!")
                    sleep(2)
                    print("You have enough coins to restart!")
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
                print("You find your friend, but see he is trapped behind heavy iron bars")
                sleep(2)
                print("In vain, you look around for something to rescue them with")
                sleep(2)
                print("However, after about an hour of looking and thinking, you come to your senses")
                sleep(2)
                print("There's nothing here...")
                sleep(2)
                print("You and your friend are stuck down there...")
                sleep(2)
                print("...forever")
                sleep(2)
                if x >= 7:
                    print("OH!")
                    sleep(2)
                    print("Good news!!")
                    sleep(2)
                    print("You have enough coins to restart!")
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
            print(f"You have {x} coins")
            sleep(2)
            print("You seek out the village chief, with intent to harm, however, because of how reckless you were being, he snuck up on you")
            sleep(0.5)
            print("-1 life")
            sleep(2)
            lives = (lives-1)
            if "Gold sword" in items and lives >= 3:
                print("Good job, you have collected a golden sword and kept your lives up, you have the ability to defeat the village leader")
                sleep(2)
                print("After a tiring and eventful battle, you've defeated the village leader and rescued your friend")
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
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
                print("You've made many poor decisions in our village, and it will show in this battle")
                sleep(2)
                print("You have no effective weapon and not enough lives to last very long")
                sleep(2)
                print("You lost to the village chief and you and your friend are stuck there...")
                sleep(2)
                print("...forever")
                if x >= 7:
                    print("OH!")
                    sleep(2)
                    print("Good news!!")
                    sleep(2)
                    print("You have enough coins to restart!")
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
                print("You have barely the necessities for this fight, but I think we can make in work")
                sleep(2)
                print("You fight like there is no tomorrow for your friend, and after a long and tired battle, you've emerged victorious")
                sleep(2)
                print("Exhaused and weak, you and your friend trek home")
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
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
                print("You clutch your gold shield tight, confident you will win your friend back")
                sleep(2)
                print("And you were right!")
                sleep(2)
                print("The battle was tough, but the village leader could not break through your defenses")
                sleep(2)
                print("He gives up and gives you your friend as a means of surrender")
                sleep(2)
                print("CONGRATS! YOU'VE BEAT THE GAME🥳🥳")
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
                print("You have a few items and rationed your lives well, but unfortunately it will not be enough")
                sleep(2)
                print("You lost to the village chief and you and your friend are stuck there...")
                sleep(2)
                print("...forever")
                sleep(2)
                if x >= 7:
                    print("OH!")
                    sleep(2)
                    print("Good news!!")
                    sleep(2)
                    print("You have enough coins to restart!")
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
        else:
            print("that's not an option, sorry!")           