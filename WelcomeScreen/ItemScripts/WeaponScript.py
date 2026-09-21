from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.ItemScripts.everyItemEnum import WeaponTypes, ItemTypes
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter
import everyItemEnum

class Weapon(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, weaponType:WeaponTypes):
        super().__init__(itemName, itemType)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.itemName = itemName
        self.itemType = itemType
        self.weaponType = weaponType


    def OnEquip(self,player:PlayerCharacter):
        match self.statToIncrease:
            case "Strength" | "str":
                player.Strength += self.statNumber

            case "Dexterity" | "dex":
                player.Dexterity += self.statNumber

            case "Constitution" | "con":
                player.Constitution += self.statNumber

            case "Intelligence" | "int":
                player.intelligence += self.statNumber

            case "Wisdom" | "wis":
                player.wisdom += self.statNumber

            case "Charisma" | "cha":
                player.charisma += self.statNumber

        if player.EquippedInventory["mainHand"] is None:
            player.EquippedInventory["mainHand"] = self
            player.NormalInventory.remove(self)

        else:
            player.NormalInventory.append(player.EquippedInventory["mainHand"])
            player.EquippedInventory["mainHand"] = self
            player.NormalInventory.remove(self)

    def OnUnequip(self,player:PlayerCharacter):
        match self.statToIncrease:
            case "Strength" | "str":
                player.Strength -= self.statNumber

            case "Dexterity" | "dex":
                player.Dexterity -= self.statNumber

            case "Constitution" | "con":
                player.Constitution -= self.statNumber

            case "Intelligence" | "int":
                player.intelligence += self.statNumber

            case "Wisdom" | "wis":
                player.wisdom -= self.statNumber

            case "Charisma" | "cha":
                player.charisma -= self.statNumber

        player.NormalInventory.append(player.EquippedInventory["mainHand"])
        player.EquippedInventory["mainHand"] = None


