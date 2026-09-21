from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.ItemScripts.everyItemEnum import ArmourTypes
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter

class Armor(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, armorType:ArmourTypes):
        super().__init__(itemName, itemType)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.itemName = itemName
        self.itemType = itemType
        self.armorType = armorType


    def OnEquip(self,player:PlayerCharacter):
        match statToIncrease:
            case "Strength" | "str":
                player.Strength += statNumber

            case "Dexterity" | "dex":
                player.Dexterity += statNumber

            case "Constitution" | "con":
                player.Constitution += statNumber

            case "Intelligence" | "int":
                player.intelligence += statNumber

            case "Wisdom" | "wis":
                player.wisdom += statNumber

            case "Charisma" | "cha":
                player.charisma += statNumber

            case "ArmorClass" | "AC" | "ac":
                player.CurrentArmorClass += statNumber

    def OnUnequip(self,player:PlayerCharacter):
        match statToIncrease:
            case "Strength" | "str":
                player.Strength -= statNumber

            case "Dexterity" | "dex":
                player.Dexterity -= statNumber

            case "Constitution" | "con":
                player.Constitution -= statNumber

            case "Intelligence" | "int":
                player.intelligence += statNumber

            case "Wisdom" | "wis":
                player.wisdom -= statNumber

            case "Charisma" | "cha":
                player.charisma -= statNumber

            case "ArmorClass" | "AC" | "ac":
                player.CurrentArmorClass -= statNumber