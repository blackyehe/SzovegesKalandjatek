from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.ItemScripts.everyItemEnum import WeaponTypes
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter


class Weapon(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, weaponType:WeaponTypes):
        super().__init__(itemName, itemType)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.itemName = itemName
        self.itemType = itemType
        self.weaponType = weaponType


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

        if player.EquippedInventory[mainHand] is None:
            player.EquippedInventory[mainHand] = self
            player.NormalInventory.remove(self)

        else:
            player.NormalInventory.append(player.EquippedInventory[mainHand])
            player.EquippedInventory[mainHand] = self
            player.NormalInventory.remove(self)

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
