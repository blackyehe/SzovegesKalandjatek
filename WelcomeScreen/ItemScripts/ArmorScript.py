from WelcomeScreen.ItemScripts.EquipableItem import EquipableItem
from WelcomeScreen.Enums.everyEnum import ArmourTypes, ItemTypes

from WelcomeScreen.Enums.everyEnum import ItemTypes

class Armor(EquipableItem):
    def __init__(self, statToIncrease, statNumber, itemName, itemType: ItemTypes, armorType:ArmourTypes,itemPrice):
        super().__init__(itemName, itemType,itemPrice)
        self.statToIncrease = statToIncrease
        self.statNumber = statNumber
        self.itemName = itemName
        self.itemType = itemType
        self.armorType = armorType
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

            case "ArmorClass" | "AC" | "ac":
                player.CurrentArmorClass += self.statNumber

        player.NormalInventory.append(player.EquippedInventory[self.armorType])
        player.EquippedInventory[self.armorType] = self
        player.NormalInventory.remove(self)

    def OnUnequip(self,player):
        match self.statToIncrease:
            case "Strength" | "str":
                player.Strength -= self.statNumber

            case "Dexterity" | "dex":
                player.Dexterity -= self.statNumber

            case "Constitution" | "con":
                player.Constitution -= self.statNumber

            case "Intelligence" | "int":
                player.Intelligence += self.statNumber

            case "Wisdom" | "wis":
                player.Wisdom -= self.statNumber

            case "Charisma" | "cha":
                player.Charisma -= self.statNumber

            case "ArmorClass" | "AC" | "ac":
                player.CurrentArmorClass -= self.statNumber

        player.NormalInventory.append(player.EquippedInventory[self.armorType])
        player.EquippedInventory[self.armorType] = None

WizardHat = Armor("int", 1, "Pointy Wizard Hat",ItemTypes.ARMOR,ArmourTypes.HEAD,150)
Monocle = Armor("wis", 2, "Noble Monocle", ItemTypes.ARMOR,ArmourTypes.HEAD,200)

FullPlate = Armor("ac", 4, "Breastplate", ItemTypes.ARMOR,ArmourTypes.CHEST,400)
LeatherChest = Armor("ac", 2, "Padded Leather Armour", ItemTypes.ARMOR,ArmourTypes.CHEST,150)
WizardRobe = Armor("int", 2, "Scholar's Robe", ItemTypes.ARMOR,ArmourTypes.CHEST,200)

ThiefGlove = Armor("dex", 2, "Thief's Glove", ItemTypes.ARMOR,ArmourTypes.GLOVES,100)
BerserkGlove = Armor("str", 2, "Berserker Wraps", ItemTypes.ARMOR,ArmourTypes.GLOVES,100)
WizardGlove = Armor("int", 2, "Gem Glove", ItemTypes.ARMOR,ArmourTypes.GLOVES,150)

LeatherBoots = Armor("con", 2, "Leather Boots", ItemTypes.ARMOR,ArmourTypes.BOOTS,200)
MetalBoots = Armor("con", 3, "Metallic Boots", ItemTypes.ARMOR,ArmourTypes.BOOTS,300)
EvasiveBoots = Armor("dex", 2, "Evasive Boots", ItemTypes.ARMOR,ArmourTypes.BOOTS,150)