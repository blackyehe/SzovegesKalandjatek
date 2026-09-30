import WelcomeScreen.PlayerScripts.PlayerCharacter
from WelcomeScreen.ItemScripts.WeaponScript import Weapon
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter
from WelcomeScreen.PlayerScripts.PlayerClass import PlayableClass

WeaponScript = WelcomeScreen.ItemScripts.WeaponScript
PlayerScript2 = WelcomeScreen.PlayerScripts.PlayerCharacter
#----------------------------------------------------------------

Fighter = PlayableClass("Fighter", 18, 12, 14, 10, 12, 8, WeaponScript.Shortsword)
Rogue = PlayableClass("Rogue", 8, 18, 10, 12, 12, 14, WeaponScript.Shortbow)
Wizard = PlayableClass("Wizard", 8, 10, 12, 18, 14, 12, WeaponScript.Quarterstaff)
#----------------------------------------------------------------------------
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
        PlayerCharacter = PlayerScript2.CreateCharacterBasedOnClass(charName, Fighter)
    elif classChoice == "2" or classChoice == "Rogue":
        PlayerCharacter = PlayerScript2.CreateCharacterBasedOnClass(charName, Rogue)

    elif classChoice == "3" or classChoice == "Wizard":
        PlayerCharacter = PlayerScript2.CreateCharacterBasedOnClass(charName, Wizard)
    print("===========================================================================================================")
    PlayerCharacter.PrintCharacterSheet()
#----------------------------------------------------------------------------

WelcomeMessage()
print(f"{PlayerCharacter.CurrentPlace.description}")
PlayerCharacter.ShowUserMenu()

