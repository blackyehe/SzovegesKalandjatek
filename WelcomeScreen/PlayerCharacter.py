from PlayerClass import PlayableClass
from WelcomeScreen.PlacesClass import Places
import PlacesDatabase
from WelcomeScreen.PlacesDatabase import StarterFountain


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
