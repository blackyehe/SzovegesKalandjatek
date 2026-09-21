from PlayerClass import PlayableClass
from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
from WelcomeScreen.VisitablePlacesDatabase import PlacesDatabase
from WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase import StarterFountain



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
        self.CurrentPlace:Places = StarterFountain
        self.CurrentArmorClass = 3 + self.Dexterity
        self.EquippedInventory = dict(head = None, chest = None, gloves = None, boots = None, mainHand = None)
        self.NormalInventory = []