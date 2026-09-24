from WelcomeScreen.PlayerScripts import PlayerCharacter
from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
from random import randint
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
def DiceRoll(number, player):
    rnd = randint(1, 10)
    returnList = []
    #--- na ezt kicsit máshogy, paraméternek kéne a player statja, meg a szám amit megkell dobni.

def CheckTheFountain(player):
    print(f"While checking out the fountain, you seem to notice something shimmering at the bottom")
    print(f"1. Try to ascertain what is exactly at the bottom [DC 15 - Wisdom]\n"
          f"2. Try to carefully reach for the bottom.[DC 7 Dexterity]\n"
          f"3. Leave the fountain behind.")
    choice = input("What will you do? (1/2/3..): ")
    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
    pass


optionAndFunctionDict = {

}
