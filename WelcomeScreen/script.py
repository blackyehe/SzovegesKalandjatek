class PlayableClass:
    def __init__(self, className, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma):
        self.classname = className
        self.strength = Strength
        self.dexterity = Dexterity
        self.constitution = Constitution
        self.intelligence = Intelligence
        self.wisdom = Wisdom
        self.charisma = Charisma


Fighter = PlayableClass("Fighter", 18, 12, 14, 10, 12, 8)
Rogue = PlayableClass("Rogue", 8, 18, 10, 12, 12, 14)
Wizard = PlayableClass("Wizard", 8, 10, 12, 18, 14, 12)


class PlayerCharacter:
    def __init__(self,playerName,playerClass:PlayableClass,playerMaxHP,playerCurrentHP,Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma):
        self.playerName = playerName
        self.playerClass = playerClass
        self.playerMaxHP = playerMaxHP
        self.playerCurrentHP = playerCurrentHP

        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Constitution = Constitution
        self.intelligence = Intelligence
        self.wisdom = Wisdom
        self.charisma = Charisma

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
    global newCharacter
    print("===========================================")
    charName = input("Add your new character's name: ")
    print(f"Welcome to the game, {charName}!")
    print("===========================================\n")
    print(f"Choose a Class for yourself, {charName}: ")
    print(f"1. Fighter - High Strength and Good Constitution\n2. Rogue - High Dexterity and good Charisma\n3. Wizard - High Intelligence and good Wisdom")
    classChoice = input("Write 1/2/3 or the class' full name to choose: ")

    if classChoice == "1" or classChoice == "Fighter":
        newCharacter = CreateCharacterBasedOnClass(charName,Fighter)

    elif classChoice == "2" or classChoice == "Rogue":
        newCharacter = CreateCharacterBasedOnClass(charName,Rogue)

    elif classChoice == "3" or classChoice == "Wizard":
        newCharacter = CreateCharacterBasedOnClass(charName,Wizard)

    PrintCharacterSheet(newCharacter)

def PrintCharacterSheet(character:PlayerCharacter):
    print("===========================================\n")
    print(f"Character Name: {character.playerName}\n"
          f"Chosen Class: {character.playerClass.classname} { character.playerCurrentHP} / {character.playerMaxHP}\n"
          f"Strength: {character.playerClass.strength}\n"
          f"Dexterity: {character.playerClass.dexterity}\n"
          f"Constitution: {character.playerClass.constitution}\n"
          f"Intelligence: {character.playerClass.intelligence}\n"
          f"Wisdom: {character.playerClass.wisdom}\n"
          f"Charisma: {character.playerClass.charisma}")
    print("===========================================\n")

WelcomeMessage()