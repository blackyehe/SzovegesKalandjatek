from WelcomeScreen.Enums.everyEnum import ArmourTypes, ItemTypes
from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
import WelcomeScreen.ItemScripts.WeaponScript
from random import randint
import WelcomeScreen.ItemScripts.ArmorScript
from tabulate import tabulate
import WelcomeScreen.EnemiesAndQuests.Quests
import introcs
import WelcomeScreen.DiceRoll
import WelcomeScreen.VisitablePlacesDatabase.Dungeon

dungeon = WelcomeScreen.VisitablePlacesDatabase.Dungeon
diceRoll = WelcomeScreen.DiceRoll
quest = WelcomeScreen.EnemiesAndQuests.Quests
armor = WelcomeScreen.ItemScripts.ArmorScript
weapon = WelcomeScreen.ItemScripts.WeaponScript
#-------------------------

StarterFountain = Places("Fountain ")
StarterFountain.description = "You begin your journey near the town square's fountain"
StarterFountain.dict= SFDict = {
    "StarterFountainOption1" : "Check out the fountain",
    "StarterFountainOption2" : "Go somewhere else",
}
StarterFountain.whatCanUDoHere.extend([SFDict["StarterFountainOption1"],SFDict["StarterFountainOption2"]])

#----------------------------------------

AlchemyShop = Places("Alchemy Shop ")
AlchemyShop.description = "A fairly big shop called the Mystic Vagrant, alchemical supplies and equipment can be found here for a decent prize"
AlchemyShop.dict= ASDict = {
    "AlchemyShopOption1" : "Speak with the shopkeeper",
    "AlchemyShopOption2" : "You can see a chest in the corner, you could attempt to lockpick it without being seen [DC 22 - Dex]",
    "AlchemyShopOption3" : "Leave the shop"
}
AlchemyShop.whatCanUDoHere.extend([ASDict["AlchemyShopOption1"],ASDict["AlchemyShopOption2"],ASDict["AlchemyShopOption3"]])

shopInventory = [
    armor.WizardHat,armor.Monocle,
    armor.LeatherChest,armor.WizardRobe,
    armor.BerserkGlove,armor.WizardGlove,armor.ThiefGlove,
    armor.LeatherBoots, armor.EvasiveBoots,
    weapon.Longsword,weapon.Wand,weapon.Dagger,
]
#----------------------
GuildHall = Places("Guild Hall ")
GuildHall.description = "The Guild Hall, this is where you can find various jobs to do"
GuildHall.dict = GHDict = {
    "GuildHallOption1" : "Take a look at the job postings on the main wall",
    "GuildHallOption2" : "Leave the Guild Hall"
}
GuildHall.whatCanUDoHere.extend([GHDict["GuildHallOption1"],GHDict["GuildHallOption2"]])
#---------------------
TownGate = Places("Town Gate ")
TownGate.description = "You can leave the town through this Gate"
TownGate.dict = TGDict = {
    "TownGateOption1" : "Embark on a journey",
    "TownGateOption2" : "Turn back from the Town Gate",

}
TownGate.whatCanUDoHere.extend([TGDict["TownGateOption1"], TGDict["TownGateOption2"]])
#------------------------------

#------------------------------
PlacesList = [StarterFountain, AlchemyShop, GuildHall, TownGate]

def GoSomewhere(player):
    ShowVisitablePlaces(player)
    visitChoice = input(f"Type the number you wish to visit, or X to go back to the menu: ")

    if visitChoice == "x" or visitChoice == "X":
        player.ShowUserMenu()
    else:
        VisitPlace(player, visitChoice)

def ShowVisitablePlaces(player):
    print("===========================================================================================================")
    print(f"From your current place - The {player.CurrentPlace.placeName} - you can go to these locations:\n ")
    PrintPlaceOptions(player)

def VisitPlace(player, number):
    print("===========================================================================================================")
    newList = []
    for place in PlacesList:
        if place.placeName != player.CurrentPlace.placeName:
            newList.append(place)

    funcDict = {
        "StarterFountainOption1" : CheckTheFountain,
        "StarterFountainOption2" : GoSomewhere,

        "AlchemyShopOption1": TalkToTheShopKeeper,
        "AlchemyShopOption2": LockPickAlchemyShopChest,
        "AlchemyShopOption3": GoSomewhere,

        "GuildHallOption1" : JobPostings,
        "GuildHallOption2" : GoSomewhere,

        "TownGateOption1" : dungeon.EmbarkOutside,
        "TownGateOption2" : GoSomewhere,
    }
    if len(newList) >= int(number) - 1:
        player.CurrentPlace = newList[int(number) - 1]
        optionID = PrintDoableOptions(newList[int(number) - 1])  # 0. Index miatt -1
        funcDict[optionID](player)
        print(player.currentPlace.placeName)
    print("===========================================================================================================")

def PrintPlaceOptions(player):
    newList = []
    for i in range(len(PlacesList)):
        if player.CurrentPlace.placeName != PlacesList[i].placeName:
            newList.append(PlacesList[i])
    for i in range (len(newList)):
            print(f"{i+1}.{newList[i].placeName}: {newList[i].description}\n")
    print("===========================================================================================================")


def PrintDoableOptions(place:Places):
    i = 1
    for ttd in place.whatCanUDoHere:
        print(f"{i}. {ttd}")
        i+=1
    choice = input("What will you do? (1/2/3..): ")
    keyNeeded = SearchDictKey(place.whatCanUDoHere[int(choice)-1],place.dict)
    return keyNeeded
#------------------------------------------ Opció Dictionary method value-val innentől, meg helper methodok.
def SearchDictKey(value, dictionary):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return key
    return None

def GetType(item):
    if item.itemType is ItemTypes.ARMOR:
        return item.armorType.value
    elif item.itemType is ItemTypes.WEAPON:
        return item.weaponType.value
    else:
        return "Other"
def GetShopItems():
    global shopInventory
    return [[i,item.itemName,GetType(item), f"+{item.statNumber} to {item.statToIncrease}",item.itemPrice] for i,item in enumerate(shopInventory,1)]
def OpenShop(player):
    global shopInventory
    print(tabulate(
            GetShopItems(),
            headers=['#','Item Name','Item Slot Type','Description','Price'],
            tablefmt="fancy_grid",
            colglobalalign ='center',
        ))
    print(f"Your current gold: {player.Gold}")
    choice = input(f"Type the number of the item you wish to buy, or X to exit the shopping menu: ")
    if choice.lower() == "x":
        TalkToTheShopKeeper(player)
    item = shopInventory[int(choice)-1]

    if player.Gold >= item.itemPrice:
        confirm = input(f"Would you like to buy {item.itemName} for {item.itemPrice}? [Y/N]: ")

        if confirm.lower() == "y":
            player.Gold -= item.itemPrice
            shopInventory.pop(int(choice)-1)
            player.AddItemToInventory(item)
            input("Press Enter to continue...")
            OpenShop(player)

        elif confirm.lower() == "n":
            OpenShop(player)
    else:
        print("You lack the funds to buy this item. Yikes.")
        input("Press Enter to continue...")
        OpenShop(player)

checkedFirst = False
successFirst = False
checkedSecond = False
def CheckTheFountain(player):
    global checkedFirst, successFirst, checkedSecond

    while True:
        print("\n===========================================================================================================")
        print(f"While checking out the fountain, you seem to notice something shimmering at the bottom\n")
        print(f"1. Try to ascertain what is exactly at the bottom [DC 15 - Wisdom]\n2. Try to carefully reach for the bottom [DC 14 Dexterity]\n3. Leave the fountain behind.")
        print("===========================================================================================================")

        choice = input("What will you do? (1/2/3): ")

        match choice:
            case "1":
                if checkedFirst:
                    print("You have already checked out this option\n")
                    input("\nPress ENTER to continue...")
                    continue

                successFirst = diceRoll.DiceRoll(15, player, "wis")
                checkedFirst = True

                if successFirst:
                    print("Your eye catches a surprisingly expensive looking Dagger, and a hefty amount of gold coins")

                else:
                    print("For some reason you can't make out what's exactly at the bottom...")
                input("Press ENTER to continue...")

            case "2":
                print("\nYou try to reach for the bottom of the fountain")
                if checkedSecond:
                    print("You have already checked out this option\n")
                    input("Press ENTER to continue...")
                    continue

                if successFirst:
                    success = diceRoll.DiceRoll(10, player, "dex")
                else:
                    success = diceRoll.DiceRoll(14, player, "dex")

                if success:
                    print(f"You have found a {weapon.Dagger.itemName}. Wicked.")
                else:
                    print(
                        "While trying to reach for the bottom, you slipped "
                        "and hit your head on the wall."
                    )
                    player.TakeDamage(5)
                    print(
                        f"You're soaking wet, but, you reach down and "
                        f"find a {weapon.Dagger.itemName}."
                    )

                player.AddItemToInventory(weapon.Dagger)
                checkedSecond = True

                input("Press ENTER to continue...")

            case "3":
                GoSomewhere(player)
                return

def TalkToTheShopKeeper(player):
    while True:
        print("\n===========================================================================================================")
        print(f"The Mystic Vagrant welcomes you humbly, what can I do for you?\n")
        print(f"1. Browse his items - (Open his shop)\n2. Exit the shop and go somewhere else\n3. Check out the chest")
        print("===========================================================================================================")

        choice = input("Choose between the options 1/2/3..: ")

        match choice:
            case "1":
                OpenShop(player)
            case "2":
                GoSomewhere(player)
            case "3":
                LockPickAlchemyShopChest(player)

asCheckedFirst = False
asSuccessFirst = False
asCheckedSecond = False
asKickedOutFirst = False
def LockPickAlchemyShopChest(player):
    global asCheckedFirst, asSuccessFirst, asCheckedSecond, asKickedOut #as = Alchemy Shop

    while True:
        print("\n===========================================================================================================")
        print(f"The heavy chest in the corner seems filled to the brim, but is locked with a rusty old lock\n")
        print(f"1. Inspect the rusty old lock [DC 21 Wis]\n2. Try to pick the lock without the shopkeeper catching you [DC 22 Dex]\n3. Leave the chest")
        print("===========================================================================================================")

        choice = input("Choose between the options 1/2/3..: ")
        match choice:
            case "1":
                if asCheckedFirst:
                    print("You have already checked out this option\n")
                    input("\nPress ENTER to continue...")
                    continue

                asSuccessFirst = diceRoll.DiceRoll(21, player, "wis")
                asCheckedFirst = True

                if asSuccessFirst:
                    print("The lock seems really rusty, even a little force would break it")

                else:
                    print("Aside from the lock being really rusty, you can't find anything interesting about it")
                input("Press ENTER to continue...")

            case "2":
                if asCheckedSecond:
                    print("You have already checked out this option\n")
                    input("\nPress ENTER to continue...")
                    continue

                if asSuccessFirst:
                    asSuccessSecond = diceRoll.DiceRoll(19, player, "dex")
                else:
                    asSuccessSecond = diceRoll.DiceRoll(22, player, "dex")

                if asSuccessSecond:
                    print(f"You managed to open the chest without anyone catching you, the chest contained a sack of gold and a {armor.LeatherChest.itemName}. Nice. ")
                    player.ManageGold(250, True)
                    player.AddItemToInventory(armor.LeatherChest)
                    asCheckedSecond = True
                    input("Press ENTER to continue...")
                else:
                    print(f"It seems you weren't quick enough, the shopkeeper caught you, beat you up and kicked you out, it seems you're forbidden from entering the shop ever again.")
                    asCheckedSecond = True
                    asKickedOut = True
                    player.TakeDamage(5)
                    input("Press ENTER to continue...")
                    GoSomewhere(player)

            case "3":
                TalkToTheShopKeeper(player)

def JobPostings(player):
    while True:
        print("\n===========================================================================================================")
        print(f"It seems the job board is pretty empty right now, only one quest is available.\n")
        print(f"Rumors say that the surrounding dungeons are infested with goblin scum.\n "
              f"Adventurers brave enough to venture into the dungeons and slay these foul creatures will receive a 500 Gold reward.\n"
              f"[QUEST REWARD: 500 GOLD]\n\n")
        choice = input("Type Y/N to accept the quest.")
        if choice.lower() == "y":
            print(f"You have accepted the quest [{quest.GoblinHunt.QuestTitle}]")
            player.ActiveQuests.append(quest.GoblinHunt)
            input("Press ENTER to continue...")
            GoSomewhere(player)

        elif choice.lower() == "n":
            print(f"You leave the job posting board")
            input("Press ENTER to continue...")
            GoSomewhere(player)