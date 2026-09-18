from tkinter import Place

from PlacesClass import Places

StarterFountain = Places("Fountain: ")
StarterFountain.description = "You begin your journey near the town square's fountain"
fountainOption1 = "Check out the fountain"
fountainOption2 = "Go somewhere else"
StarterFountain.placesToVisitFromHere.append(fountainOption1,fountainOption2)
#----------------------------------------


AlchemyShop = Places("Alchemy Shop: ")
AlchemyShop.description = "A small Alchemy shop, while looking around, a humble shopkeeper greets you"
asOption = "Speak with the shopkeeper"
asOption2 = "You can see a chest in the corner, you could attempt to lockpick it without being seen"
asOption3 = ""

#----------------------
GuildHall = Places("Guild Hall: ")
GuildHall.description = "The Guild Hall, this is where you can find various jobs to do"


#---------------------

TownGate = Places("Town Gate: ")
TownGate.description = "You can leave the town through this Gate"

PlacesList = [Places, AlchemyShop, GuildHall, TownGate]

def PrintPlaceOptions():
    for place in PlacesList:
        print(f"{place.description}\n")

