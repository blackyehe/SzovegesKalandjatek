from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.Enums.everyEnum import WeaponTypes, ItemTypes
from WelcomeScreen.Enums.everyEnum import ArmourTypes

class Weapon(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, weaponType:WeaponTypes):
        super().__init__(itemName, itemType)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.weaponType = weaponType

    def OnEquip(self,player):
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
                player.RemoveItemFromInventory(self)


        else:
            player.AddItemToInventory(player.EquippedInventory[ArmourTypes.MAINHAND])
            player.EquippedInventory[ArmourTypes.MAINHAND] = self
            if self in player.NormalInventory:
                player.RemoveItemFromInventory(self)

    def OnUnequip(self,player):
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

        player.AddItemToInventory(player.EquippedInventory[ArmourTypes.MAINHAND ])
        player.EquippedInventory[ArmourTypes.MAINHAND] = None


Shortsword = Weapon("str", 1, "Rusty Shortsword", ItemTypes.WEAPON,WeaponTypes.SHORTSWORD)
Longsword = Weapon("str", 3, "Silver Longsword", ItemTypes.WEAPON, WeaponTypes.LONGSWORD)
Quarterstaff = Weapon("int", 1, "Common Staff", ItemTypes.WEAPON, WeaponTypes.QUARTERSTAFF)
Wand = Weapon("int", 2, "Basic Magic Wand", ItemTypes.WEAPON, WeaponTypes.MAGICWAND)
Dagger = Weapon("dex", 2, "Sharp Dagger", ItemTypes.WEAPON, WeaponTypes.DAGGER)
Shortbow = Weapon("dex", 1, "Common Shortbow", ItemTypes.WEAPON, WeaponTypes.SHORTBOW)
Rapier = Weapon("dex", 3, "Ceremonial Rapier", ItemTypes.WEAPON,WeaponTypes.RAPIER)