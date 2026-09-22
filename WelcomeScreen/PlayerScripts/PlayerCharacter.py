from WelcomeScreen.ItemScripts.everyItemEnum import ArmourTypes
from WelcomeScreen.VisitablePlacesDatabase.PlacesClass import Places
from WelcomeScreen.VisitablePlacesDatabase.PlacesDatabase import StarterFountain
from typing import Dict


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