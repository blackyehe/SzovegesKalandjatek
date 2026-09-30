from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.Enums.everyEnum import WeaponTypes, ItemTypes
from WelcomeScreen.Enums.everyEnum import ArmourTypes

class Weapon(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, weaponType:WeaponTypes, itemPrice):
        super().__init__(itemName, itemType,itemPrice)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.weaponType = weaponType
        self.itemPrice = itemPrice

    def OnEquip(self,player):
        match self.statToIncrease:
            case "Strength" | "str":
                player.Strength += self.statNumber

            case "Dexterity" | "dex":
                player.Dexterity += self.statNumber

            case "Constitution" | "con":
                player.Constitution += self.statNumber

            case "Intelligence" | "int":
                player.Intelligence += self.statNumber

            case "Wisdom" | "wis":
                player.Wisdom += self.statNumber

            case "Charisma" | "cha":
                player.Charisma += self.statNumber

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


Shortsword = Weapon("str", 1, "Rusty Shortsword", ItemTypes.WEAPON,WeaponTypes.SHORTSWORD,100)
Longsword = Weapon("str", 3, "Silver Longsword", ItemTypes.WEAPON, WeaponTypes.LONGSWORD,300)
Quarterstaff = Weapon("int", 1, "Common Staff", ItemTypes.WEAPON, WeaponTypes.QUARTERSTAFF,100)
Wand = Weapon("int", 2, "Basic Magic Wand", ItemTypes.WEAPON, WeaponTypes.MAGICWAND,200)
Dagger = Weapon("dex", 2, "Sharp Dagger", ItemTypes.WEAPON, WeaponTypes.DAGGER,200)
Shortbow = Weapon("dex", 1, "Common Shortbow", ItemTypes.WEAPON, WeaponTypes.SHORTBOW,100)
Rapier = Weapon("dex", 3, "Ceremonial Rapier", ItemTypes.WEAPON,WeaponTypes.RAPIER,300)