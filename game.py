from time import sleep
restart = "yes"
from objects import *
while restart == "yes":
    longsleep = 2
    medsleep = 1.5
    shortsleep = 1
    lives = 5
    coins = []
    items = []
    choice1 = ""
    start = ""
    iron = ""
    choice2 = ""
    choice3 = ""
    choice4 = ""
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
    sleep(longsleep)
    print("Your friend has been captured by the leader of a village far, far away")
    sleep(longsleep)
    print("You venture out to save him, and finally reach the village")
    sleep(longsleep)
    print("Once you reach the village, you stumble upon your first fork in the road")
    sleep(longsleep)
    print("You must choose...")
    sleep(longsleep)
    print("Would you like to see the blacksmith or the villager")
    sleep(shortsleep)
    while choice1 != "blacksmith" or "villager":
        choice1 = input("blacksmith or villager:").lower()
        if choice1 == "blacksmith":
            print("The blacksmith asks for your help to find iron")
            sleep(shortsleep)
            while iron != "y" or "n":
                iron = input("Do you help him? y/n").lower()
                if iron == "y":
                    sidequest = blacksmith_iron("help", "iron", abc())
                    items.append("Iron sword")
                    coins.append(5)
                    break
                elif iron == "n":
                    sleep(longsleep)
                    print("He's mad and yells at you")
                    sleep(longsleep)
                    print("You take emotional damage")
                    sleep(medsleep)
                    blacksmith.impact = print("-1 life")
                    print(lives)
                    lives = (lives-1)
                    break
                else:
                    print("that's not an option, sorry!")
            break
        elif choice1 == "villager":
            def village():
                print("The villager isn't home, but you see a chest in his home!")
                sleep(longsleep)
                print("You open the chest and find coins!")
                sleep(medsleep)
                villager.impact
                villager.service
            village()
            break
        else:
            print("that's not an option, sorry!")
    sleep(longsleep)
    print("You venture farther through the village and meet your next obstacle")
    sleep(longsleep)
    print("Two houses stand before you, the villager's and the armorer's")
    sleep(longsleep)
    print("Would you like to visit the villager or the armorer?")
    sleep(shortsleep)
    while choice2 != "armorer" or "villager":
        choice2 = input("villager or armorer:").lower()
        if choice2 == "villager":
            def sleeper():
                sleeping_villager
            sleeper()
            lives = (lives-2)
            break
        elif choice2 == "armorer":
            print("The armorer is pleasantly surprised by your visit, and wants to help you")
            sleep(longsleep)
            print("He says he's going to teach you how to make defensive items!")
            sleep(longsleep)
            print("After hours of working and talking, together you've made armor and a shield!")
            sleep(longsleep)
            print("The armorer decides he likes you, and he let's you keep the armor and shield!")
            sleep(medsleep)
            armorer
            break
        else:
            print("that's not an option, sorry!")
    sleep(longsleep)
    print("After your visit, you continue walking")
    sleep(longsleep)
    print("Here at this fork you'll meet your last villager")
    sleep(longsleep)
    print("Would you like to see the witch or the alchemist?")
    sleep(shortsleep)
    while choice3 != "witch" or "alchemist":
        choice3 = input("witch or alchemist:").lower()
        if choice3 == "witch":
            def healer():
                witch
            healer()
            break
        elif choice3 == "alchemist":
            def alchemy():
                alchemist
            alchemy()
            break
        else:
            print("that's not an option, sorry!")
    x = sum(coins)
    sleep(longsleep)
    print("Now that you've met all the villagers, you've reached the village leader's house!")
    sleep(longsleep)
    print("Time to get your friend back!")
    sleep(longsleep)
    print("Before you enter, which approach would you like to take?")
    sleep(shortsleep)
    print(f"You have {lives} lives and these items: {items}")
    while choice4 != "stealthy" or "aggressive":
        choice4 = input("stealthy or aggressive: ").lower()
        sleep(longsleep)
        if choice4 == "stealthy":
            print(f"You have {x} coins")
            sleep(longsleep)
            print("You sneak past the village leader and his guards and find your friend in the dungeons!")
            if "Gold sword" in items:
                print("You slash through the bars of the dungeon with your gold sword and your friend is saved!")
                sleep(longsleep)
                print("The two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                sleep(longsleep)
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
                sleep(longsleep)
                print("Finally, you break through, and your friend comes out, hungry, tired, and ready to go home")
                sleep(longsleep)
                print("The two of you leave the dungeon and trek home")
                sleep(longsleep)
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
                sleep(longsleep)
                print("Your friend crawls out, and the two of you sneak out of the dungeon, back past the village leader and his guards, and travel home")
                sleep(longsleep)
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
                sleep(longsleep)
                print("You try to look around and find anohter way to save him, but to no avail")
                sleep(longsleep)
                print("You and your friend are stuck down there...")
                sleep(longsleep)
                print("...forever")
                sleep(longsleep)
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    print("Good news!!")
                    sleep(longsleep)
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
                sleep(longsleep)
                print("In vain, you look around for something to rescue them with")
                sleep(longsleep)
                print("However, after about an hour of looking and thinking, you come to your senses")
                sleep(longsleep)
                print("There's nothing here...")
                sleep(longsleep)
                print("You and your friend are stuck down there...")
                sleep(longsleep)
                print("...forever")
                sleep(longsleep)
                if x >= 7:
                    print("OH!") 
                    sleep(longsleep)
                    print("Good news!!")
                    sleep(longsleep)
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
            sleep(longsleep)
            print("You seek out the village chief, with intent to harm, however, because of how reckless you were being, he snuck up on you")
            sleep(shortsleep)
            print("-1 life")
            sleep(longsleep)
            lives = (lives-1)
            if "Gold sword" in items and lives >= 3:
                print("Good job, you have collected a golden sword and kept your lives up, you have the ability to defeat the village leader")
                sleep(longsleep)
                print("After a tiring and eventful battle, you've defeated the village leader and rescued your friend")
                sleep(longsleep)
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
                sleep(longsleep)
                print("You have no effective weapon and not enough lives to last very long")
                sleep(longsleep)
                print("You lost to the village chief and you and your friend are stuck there...")
                sleep(longsleep)
                print("...forever")
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    print("Good news!!")
                    sleep(longsleep)
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
                sleep(longsleep)
                print("You fight like there is no tomorrow for your friend, and after a long and tired battle, you've emerged victorious")
                sleep(longsleep)
                print("Exhaused and weak, you and your friend trek home")
                sleep(longsleep)
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
                sleep(longsleep)
                print("And you were right!")
                sleep(longsleep)
                print("The battle was tough, but the village leader could not break through your defenses")
                sleep(longsleep)
                print("He gives up and gives you your friend as a means of surrender")
                sleep(longsleep)
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
                sleep(longsleep)
                print("You lost to the village chief and you and your friend are stuck there...")
                sleep(longsleep)
                print("...forever")
                sleep(longsleep)
                if x >= 7:
                    print("OH!")
                    sleep(longsleep)
                    print("Good news!!")
                    sleep(longsleep)
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