from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
import WelcomeScreen.ItemScripts.WeaponScript
from random import randint


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
AlchemyShop.description = "A small Alchemy shop, you can buy potions here"
AlchemyShop.dict= ASDict = {
    "AlchemyShopOption1" : "Speak with the shopkeeper",
    "AlchemyShopOption2" : "You can see a chest in the corner, you could attempt to lockpick it without being seen [DC 15 - Dex]",
    "AlchemyShopOption3" : "Leave the shop"
}
AlchemyShop.whatCanUDoHere.extend([ASDict["AlchemyShopOption1"],ASDict["AlchemyShopOption2"],ASDict["AlchemyShopOption3"]])
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
TownGate.Dict = TGDict = {
    "TownGateOption1" : "Embark on a journey",
    "TownGateOption2" : "Turn back from the Town Gate",

}
TownGate.whatCanUDoHere.extend([TGDict["TownGateOption1"], TGDict["TownGateOption2"]])
#------------------------------
PlacesList = [StarterFountain, AlchemyShop, GuildHall, TownGate]
def GoSomewhere(player):
    ShowVisitablePlaces(player)
    visitChoice = input(f"Type the number you wish to visit, or X to go back to the menu: ")
    print(
        "===========================================================================================================\n")
    if visitChoice == "x" or visitChoice == "X":
        player.ShowUserMenu(player)
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

    if len(newList) >= int(number) - 1:
        player.CurrentPlace = newList[int(number) - 1]
        optionID = PrintDoableOptions(newList[int(number) - 1])  # 0. Index miatt -1

    print("===========================================================================================================")

def PrintPlaceOptions(player):
    i = 0
    for place in PlacesList:
        if player.CurrentPlace.placeName != place.placeName:
            print(f"{i}.{place.placeName}: {place.description}\n")
        i += 1
    print("===========================================================================================================")

def SearchDictKey(value, dictionary):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return key
    return None

def PrintDoableOptions(place:Places):
    i = 1
    for ttd in place.whatCanUDoHere:
        print(f"{i}. {ttd}")
        i+=1
    choice = input("What will you do? (1/2/3..): ")
    keyNeeded = SearchDictKey(place.whatCanUDoHere[int(choice)-1],place.dict)
    return keyNeeded
#------------------------------------------ Opció szótár metódusokkal valuenak innentől
def DiceRoll(numberToBeat, player, dcType):
    rnd = randint(1, 10)
    playerDc = 0
    success = False
    match dcType:
        case "dex" | "dexterity" | "DEX":
            playerDc = player.Dexterity
        case "str" | "strength" | "STR":
            playerDc = player.Strength
        case "wis" | "wisdom" | "WIS":
            playerDc = player.Wisdom
        case "int" | "intelligence" | "INT":
            playerDc = player.Intelligence
        case "cha" | "charisma" | "CHA":
            playerDc = player.Charisma
        case "con" | "constitution" | "CON":
            playerDc = player.Constitution

    if playerDc + rnd > numberToBeat:
        success = True
        print(f"SUCCESS: your modifier:{playerDc} + random number:{rnd} beats {numberToBeat}")
    else:
        success = False
        print(f"FAILURE: your modifier:{playerDc} + random number:{rnd} beats {numberToBeat} ")

    return success

def CheckTheFountain(player):
    checkedFirst = False
    successFirst = False
    checkedSecond = False

    print(f"While checking out the fountain, you seem to notice something shimmering at the bottom")
    print(f"1. Try to ascertain what is exactly at the bottom [DC 15 - Wisdom]\n"
          f"2. Try to carefully reach for the bottom.[DC 7 Dexterity]\n"
          f"3. Leave the fountain behind.")
    choice = input("What will you do? (1/2/3..): ")

    match choice:
        case "1":
            if DiceRoll(15,player,"wis") and checkedFirst is False:
                print(f"Your eye catches a surprisingly expensive looking Dagger, and a hefty amount of gold coins")
                checkedFirst = True
                successFirst = True
                input("Press ENTER to continue...")
                CheckTheFountain(player)

            elif checkedFirst:
                print(f"You have already checked out this option")
                CheckTheFountain(player)

            elif DiceRoll(15,player,"wis") is False and checkedFirst is False:
                print(f"For some reason you can't make out what's exactly at the bottom...")
                checkedFirst = True
                successFirst = False
                input("Press ENTER to continue...")
                CheckTheFountain(player)

        case "2":
            print(f"You try to reach for the bottom of the fountain")
            if successFirst and checkedSecond is False:
                if DiceRoll(4,player,"dex"):
                    print(f"You have found a {weapon.Dagger.itemName}. Wicked")
                    player.AddItemToInventory(weapon.Dagger)
                    checkedSecond = True
                    input("Press ENTER to continue...")
                    CheckTheFountain(player)
                else:
                    print(f"While trying to reach for the bottom, you slipped and hit your head on the wall (You lost 5 HP)")
                    player.TakeDamage(5)
                    print(f"You're soaking wet, but, you reach down and find a {weapon.Dagger.itemName}.")
                    player.AddItemToInventory(weapon.Dagger)
                    checkedSecond = True
                    input("Press ENTER to continue...")
                    CheckTheFountain(player)

            elif not successFirst and checkedSecond is False:
                if DiceRoll(7,player,"dex"):
                    print(f"You have found a {weapon.Dagger.itemName}. Wicked")
                    player.AddItemToInventory(weapon.Dagger)
                    checkedSecond = True
                    input("Press ENTER to continue...")
                    CheckTheFountain(player)
                else:
                    print(f"While trying to reach for the bottom, you slipped and hit your head on the wall (You lost 5 HP)")
                    player.TakeDamage(5)
                    print(f"You're soaking wet, but, you reach down and find a {weapon.Dagger.itemName}.")
                    player.AddItemToInventory(weapon.Dagger)
                    checkedSecond = True
                    input("Press ENTER to continue...")
                    CheckTheFountain(player)
            elif checkedSecond:
                print(f"You have already checked out this option")
                CheckTheFountain(player)

        case "3":
            GoSomewhere(player)
    pass

