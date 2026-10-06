from WelcomeScreen.Enums.everyEnum import ArmourTypes
from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
from WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase import StarterFountain
import WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase
from WelcomeScreen.PlayerScripts.PlayerClass import PlayableClass
from typing import Dict
from tabulate import tabulate

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
        self.Intelligence = Intelligence
        self.Wisdom = Wisdom
        self.Charisma = Charisma

        self.CurrentPlace:Places = WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase.AlchemyShop
        self.CurrentArmorClass = self.Dexterity
        self.EquippedInventory = Dict[ArmourTypes, str]
        self.EquippedInventory = {ArmourTypes.HEAD : None, ArmourTypes.CHEST : None, ArmourTypes.GLOVES : None, ArmourTypes.BOOTS : None, ArmourTypes.MAINHAND : None}
        self.NormalInventory = []
        self.Gold = 500
        self.ActiveQuests = []

    def TakeDamage(self, dmgNumber):
        self.playerCurrentHP -= dmgNumber
        print(f"You took [{dmgNumber}] damage. Current HP: {self.playerCurrentHP} ")

    def ReturnMainHand(self):
        return self.EquippedInventory[ArmourTypes.MAINHAND]

    def AddItemToInventory(self, item):
        self.NormalInventory.append(item)
        print(f"[{item.itemName}] added to the Inventory")

    def RemoveItemFromInventory(self, item):
        self.NormalInventory.remove(item)
    def ManageGold(self, number, bool):
        if bool is True:
            self.Gold += number
            print(f"+[{number}] Gold added to the Inventory")
        else:
            self.Gold -= number
            print(f"-[{number}] Gold spent/removed")
    def item_name(self,slot):
        inv = inv = self.EquippedInventory
        return getattr(inv.get(slot), 'itemName', 'EMPTY')
    def ShowPlayerNormalInventory(self):
        print(tabulate(
            [[self.item_name(ArmourTypes.HEAD),
        self.item_name(ArmourTypes.CHEST),
        self.item_name(ArmourTypes.GLOVES),
        self.item_name(ArmourTypes.BOOTS),
        self.item_name(ArmourTypes.MAINHAND),
        self.Gold]],
            headers=['Headgear', 'Chestplate', 'Gloves', 'Boots', 'Main hand weapon', 'Gold pieces'],
            tablefmt='outline',
            colglobalalign ='center'))

        if len(self.NormalInventory) == 0:
            print("\nItems Currently in your Inventory:\n[EMPTY]")
        else:
            for i,item in enumerate(self.NormalInventory,1):
                item.itemIndex = i
                print(f"{item.itemIndex}. [{item.itemName}] [+{item.statNumber} to {item.statToIncrease}]")
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
                    self.PrintCharacterSheet()
                    input("Press ENTER to continue")
                    self.ShowUserMenu()
                case "3":
                    self.ShowPlayerNormalInventory()
                    input("\nPress ENTER to continue")
                    self.ShowUserMenu()
                case "4":
                    pass

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