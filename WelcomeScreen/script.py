from WelcomeScreen.ItemScripts.everyItemEnum import ItemTypes, WeaponTypes, ArmourTypes
from WelcomeScreen.PlayerScripts.PlayerClass import PlayableClass
from VisitablePlacesDatabase import PlacesDatabase
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter
from WelcomeScreen.ItemScripts.WeaponScript import Weapon

Shortsword = Weapon("str", 1, "Rusty Shortsword", ItemTypes.WEAPON,WeaponTypes.SHORTSWORD)
Longsword = Weapon("str", 3, "Silver Longsword", ItemTypes.WEAPON, WeaponTypes.LONGSWORD)
Quarterstaff = Weapon("int", 1, "Common Staff", ItemTypes.WEAPON, WeaponTypes.QUARTERSTAFF)
Wand = Weapon("int", 2, "Basic Magic Wand", ItemTypes.WEAPON, WeaponTypes.MAGICWAND)
Dagger = Weapon("dex", 2, "Sharp Dagger", ItemTypes.WEAPON, WeaponTypes.DAGGER)
Shortbow = Weapon("dex", 1, "Common Shortbow", ItemTypes.WEAPON, WeaponTypes.SHORTBOW)
Rapier = Weapon("dex", 3, "Ceremonial Rapier", ItemTypes.WEAPON,WeaponTypes.RAPIER)


Fighter = PlayableClass("Fighter", 18, 12, 14, 10, 12, 8, Shortsword)
Rogue = PlayableClass("Rogue", 8, 18, 10, 12, 12, 14, Dagger)
Wizard = PlayableClass("Wizard", 8, 10, 12, 18, 14, 12, Quarterstaff)

def CreateCharacterBasedOnClass(characterName,chosenClass:PlayableClass):
    newPlayer = PlayerCharacter(characterName,chosenClass,
                                10 + chosenClass.constitution,
                                10 + chosenClass.constitution,
                                chosenClass.strength,
                                chosenClass.dexterity,
                                chosenClass.constitution,
                                chosenClass.intelligence,
                                chosenClass.wisdom,
                                chosenClass.charisma)
    newPlayer.playerClass.starterWeapon.OnEquip(newPlayer)
    return newPlayer

def ShowUserMenu(player:PlayerCharacter):
    print("===========================================================================================================")
    print(f"The list of things you can do now: \n1. [GO SOMEWHERE]\n2. [SHOW CHARACTER SHEET]\n3. [OPEN INVENTORY]\n4. [ATTRIBUTES INFORMATION]")
    choice = input(f"Type your command (1/2/3/4): "
                   f"\n===========================================================================================================\n")
    match choice:
        case "1":
            ShowVisitablePlaces(player)
            visitChoice = input(f"Type the number you wish to visit, or X to go back to the menu: ")
            print("===========================================================================================================\n")
            if visitChoice == "x" or visitChoice == "X":
                ShowUserMenu(player)
            else:
                VisitPlace(player,visitChoice)

        case "2":
            PrintCharacterSheet(player)
            input("Press ENTER to continue")
            ShowUserMenu(player)
        case "3":
            ShowPlayerNormalInventory(player)
            input("Press ENTER to continue")
            ShowUserMenu(player)
        case "4":
            pass

def VisitPlace(player:PlayerCharacter, number):
    print("===========================================================================================================")
    newList = []
    for place in PlacesDatabase.PlacesList:
        if place.placeName != player.CurrentPlace.placeName:
            newList.append(place)

    if len(newList) >= int(number)-1:
        choice = PlacesDatabase.PrintDoableOptions(newList[int(number)-1])


    print("===========================================================================================================")


def ShowVisitablePlaces(player:PlayerCharacter):
    print("===========================================================================================================")
    print(f"From your current place - The {player.CurrentPlace.placeName} - you can go to these locations:\n ")
    PlacesDatabase.PrintPlaceOptions(player)

def ShowPlayerNormalInventory(player:PlayerCharacter):
    if len(player.NormalInventory) == 0:
        print("[EMPTY]")
    else:
        for item in player.NormalInventory:
            print(f"[{item.itemName}]")
            print("\n")
def WelcomeMessage():
    global PlayerCharacter
    print("===========================================================================================================")
    charName = input("Add your new character's name: ")
    print(f"Welcome to the game, {charName}!")
    print("===========================================================================================================\n")
    print("===========================================================================================================")
    print(f"Choose a Class for yourself, {charName}: ")

    print(f"1. Fighter - High Strength and Good Constitution\n"
          f"2. Rogue - High Dexterity and good Charisma\n"
          f"3. Wizard - High Intelligence and good Wisdom")

    classChoice = input("Write 1/2/3 or the class' full name to choose: ")

    if classChoice == "1" or classChoice == "Fighter":
        PlayerCharacter = CreateCharacterBasedOnClass(charName, Fighter)

    elif classChoice == "2" or classChoice == "Rogue":
        PlayerCharacter = CreateCharacterBasedOnClass(charName, Rogue)

    elif classChoice == "3" or classChoice == "Wizard":
        PlayerCharacter = CreateCharacterBasedOnClass(charName, Wizard)
    print("===========================================================================================================")
    PrintCharacterSheet(PlayerCharacter)
def PrintCharacterSheet(character:PlayerCharacter):
    print("\n===========================================================================================================")
    print(f"Character Name: {character.playerName}\n"
          f"Chosen Class: {character.playerClass.className} { character.playerCurrentHP} / {character.playerMaxHP}\n"
          f"Strength: {character.playerClass.strength}\n"
          f"Dexterity: {character.playerClass.dexterity}\n"
          f"Constitution: {character.playerClass.constitution}\n"
          f"Intelligence: {character.playerClass.intelligence}\n"
          f"Wisdom: {character.playerClass.wisdom}\n"
          f"Charisma: {character.playerClass.charisma}")
    print("===========================================================================================================\n")

WelcomeMessage()
print(f"{PlayerCharacter.CurrentPlace.description}")
ShowUserMenu(PlayerCharacter)

