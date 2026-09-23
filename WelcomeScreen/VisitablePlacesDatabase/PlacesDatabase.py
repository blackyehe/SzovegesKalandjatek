from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
#---------------------------------------
StarterFountain = Places("Fountain ")
StarterFountain.description = "You begin your journey near the town square's fountain"
StarterFountainOption1 = "Check out the fountain"
StarterFountainOption2 = "Go somewhere else"

StarterFountain.whatCanUDoHere.extend([StarterFountainOption1,StarterFountainOption2])
#----------------------------------------
AlchemyShop = Places("Alchemy Shop ")
AlchemyShop.description = "A small Alchemy shop, you can buy potions here"
AlchemyShopOption1 = "Speak with the shopkeeper"
AlchemyShopOption2 = "You can see a chest in the corner, you could attempt to lockpick it without being seen [DC 15 - Dex]"
AlchemyShopOption3 = "Leave the shop"

AlchemyShop.whatCanUDoHere.extend([AlchemyShopOption1,AlchemyShopOption2,AlchemyShopOption3])
#----------------------
GuildHall = Places("Guild Hall ")
GuildHall.description = "The Guild Hall, this is where you can find various jobs to do"
GuildHallOption1 = "Take a look at the job postings on the main wall"
GuildHallOption2 = "Leave the Guild Hall"

GuildHall.whatCanUDoHere.extend([GuildHallOption1,GuildHallOption2])
#---------------------
TownGate = Places("Town Gate ")
TownGate.description = "You can leave the town through this Gate"
TownGateOption1 = ""
TownGateOption2 = ""

TownGate.whatCanUDoHere.extend([TownGateOption1, TownGateOption2])
#------------------------------
PlacesList = [StarterFountain, AlchemyShop, GuildHall, TownGate]
def PrintPlaceOptions(player):
    i = 0
    for place in PlacesList:
        if player.CurrentPlace.placeName != place.placeName:
            print(f"{i}.{place.placeName}: {place.description}\n")
        i += 1
    print("===========================================================================================================")

def PrintDoableOptions(place:Places):
    i = 1
    for ttd in place.whatCanUDoHere:
        print(f"{i}. {ttd}")
        i+=1
    choice = input("What will you do? (1/2/3..): ")
    return choice
