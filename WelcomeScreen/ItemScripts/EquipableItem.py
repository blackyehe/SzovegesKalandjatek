from abc import ABC, abstractmethod
from WelcomeScreen.ItemScripts.ItemScript import Item


class EquipableItem(Item, ABC):
    def OnEquip(self, player):
        pass

    def OnUnequip(self, player):
        pass




