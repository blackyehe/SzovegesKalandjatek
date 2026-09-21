from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.ItemScripts.everyItemEnum import ArmourTypes
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter
from everyItemEnum import ItemTypes

class Armor(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, armorType:ArmourTypes):
        super().__init__(itemName, itemType)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.itemName = itemName
        self.itemType = itemType
        self.armorType = armorType


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

            case "ArmorClass" | "AC" | "ac":
                player.CurrentArmorClass += self.statNumber

        player.NormalInventory.append(player.EquippedInventory[self.armorType])
        player.EquippedInventory[self.armorType] = self
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

            case "ArmorClass" | "AC" | "ac":
                player.CurrentArmorClass -= self.statNumber

        player.NormalInventory.append(player.EquippedInventory[self.armorType])
        player.EquippedInventory[self.armorType] = None