from abc import ABC, abstractmethod
from ItemScript import Item
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter

class EquipableItem(Item, ABC):
    def OnEquip(self, player:PlayerCharacter):
        pass

    def OnUnequip(self, player:PlayerCharacter):
        pass




