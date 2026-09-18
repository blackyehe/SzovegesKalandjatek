from PlayerClass import PlayableClass
from PlayerCharacter import PlayerCharacter

Fighter = PlayableClass("Fighter", 18, 12, 14, 10, 12, 8)
Rogue = PlayableClass("Rogue", 8, 18, 10, 12, 12, 14)
Wizard = PlayableClass("Wizard", 8, 10, 12, 18, 14, 12)

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
    return newPlayer

def WelcomeMessage():
    global playerCharacter
    print("===========================================================================================================")
    charName = input("Add your new character's name: ")
    print(f"Welcome to the game, {charName}!")
    print("===========================================================================================================\n")
    print("===========================================================================================================")
    print(f"Choose a Class for yourself, {charName}: ")
    print(f"1. Fighter - High Strength and Good Constitution\n2. Rogue - High Dexterity and good Charisma\n3. Wizard - High Intelligence and good Wisdom")
    classChoice = input("Write 1/2/3 or the class' full name to choose: ")

    if classChoice == "1" or classChoice == "Fighter":
        playerCharacter = CreateCharacterBasedOnClass(charName, Fighter)

    elif classChoice == "2" or classChoice == "Rogue":
        playerCharacter = CreateCharacterBasedOnClass(charName, Rogue)

    elif classChoice == "3" or classChoice == "Wizard":
        playerCharacter = CreateCharacterBasedOnClass(charName, Wizard)
    print("===========================================================================================================")
    PrintCharacterSheet(playerCharacter)

def PrintCharacterSheet(character:PlayerCharacter):
    print("\n")
    print("===========================================================================================================")
    print(f"Character Name: {character.playerName}\n"
          f"Chosen Class: {character.playerClass.classname} { character.playerCurrentHP} / {character.playerMaxHP}\n"
          f"Strength: {character.playerClass.strength}\n"
          f"Dexterity: {character.playerClass.dexterity}\n"
          f"Constitution: {character.playerClass.constitution}\n"
          f"Intelligence: {character.playerClass.intelligence}\n"
          f"Wisdom: {character.playerClass.wisdom}\n"
          f"Charisma: {character.playerClass.charisma}")
    print("===========================================================================================================\n")

WelcomeMessage()