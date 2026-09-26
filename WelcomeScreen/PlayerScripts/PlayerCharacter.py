from WelcomeScreen.Enums.everyEnum import ArmourTypes
from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
from WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase import StarterFountain
import WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase
from WelcomeScreen.PlayerScripts.PlayerClass import PlayableClass
from typing import Dict


PlacesDatabase = WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase
class PlayerCharacter:
    def __init__(self,playerName,playerClass,playerMaxHP,playerCurrentHP,Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma):
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
        self.CurrentPlace:Places = StarterFountain
        self.CurrentArmorClass = 3 + self.Dexterity
        self.EquippedInventory = Dict[ArmourTypes, str]
        self.EquippedInventory = {ArmourTypes.HEAD : None, ArmourTypes.CHEST : None, ArmourTypes.GLOVES : None, ArmourTypes.BOOTS : None, ArmourTypes.MAINHAND : None}
        self.NormalInventory = []

    def TakeDamage(self, dmgNumber):
        self.playerCurrentHP -= dmgNumber

    def AddItemToInventory(self, item):
        self.NormalInventory.append(item)

    def RemoveItemFromInventory(self, item):
        self.NormalInventory.remove(item)


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

def ShowPlayerNormalInventory(player):
    if len(player.NormalInventory) == 0:
        print("[EMPTY]")
    else:
        for item in player.NormalInventory:
            print(f"[{item.itemName}]")
            print("\n")
def PrintCharacterSheet(self):
        print(
            "\n===========================================================================================================")
        print(f"Character Name: {self.playerName}\n"
              f"Chosen Class: {self.playerClass.className} {self.playerCurrentHP} / {self.playerMaxHP}\n"
              f"Strength: {self.playerClass.strength}\n"
              f"Dexterity: {self.playerClass.dexterity}\n"
              f"Constitution: {self.playerClass.constitution}\n"
              f"Intelligence: {self.playerClass.intelligence}\n"
              f"Wisdom: {self.playerClass.wisdom}\n"
              f"Charisma: {self.playerClass.charisma}")
        print(
            "===========================================================================================================\n")
def ShowUserMenu(self):
        print(
            "===========================================================================================================")
        print(f"The list of things you can do now: \n"
              f"1. [GO SOMEWHERE]\n"
              f"2. [SHOW CHARACTER SHEET]\n"
              f"3. [OPEN INVENTORY]\n"
              f"4. [ATTRIBUTES INFORMATION]")
        choice = input(f"Type your command (1/2/3/4): "
                       f"\n===========================================================================================================\n")
        match choice:
            case "1":
                PlacesDatabase.GoSomewhere(self)
            case "2":
                PrintCharacterSheet(self)
                input("Press ENTER to continue")
                ShowUserMenu(self)
            case "3":
                ShowPlayerNormalInventory(self)
                input("Press ENTER to continue")
                ShowUserMenu(self)
            case "4":
                pass
