from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.ItemScripts.everyItemEnum import WeaponTypes, ItemTypes
from WelcomeScreen.PlayerScripts.PlayerCharacter import PlayerCharacter
from WelcomeScreen.ItemScripts.everyItemEnum import ArmourTypes

class Weapon(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, weaponType:WeaponTypes):
        super().__init__(itemName, itemType)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
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

        if player.EquippedInventory[ArmourTypes.MAINHAND] is None:
            player.EquippedInventory[ArmourTypes.MAINHAND] = self
            if self in player.NormalInventory:
                player.NormalInventory.remove(self)


        else:
            player.NormalInventory.append(player.EquippedInventory[ArmourTypes.MAINHAND])
            player.EquippedInventory[ArmourTypes.MAINHAND] = self
            if self in player.NormalInventory:
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
                player.intelligence -= self.statNumber

            case "Wisdom" | "wis":
                player.wisdom -= self.statNumber

            case "Charisma" | "cha":
                player.charisma -= self.statNumber

        player.NormalInventory.append(player.EquippedInventory[ArmourTypes.MAINHAND ])
        player.EquippedInventory[ArmourTypes.MAINHAND] = None


