from enum import Enum

class ItemTypes(Enum):
    ARMOR = 1
    WEAPON = 2
    OTHER = 3

class WeaponTypes(Enum):
    SHORTSWORD = "Main Hand"
    DAGGER = "Main Hand"
    LONGSWORD = "Main Hand"
    SHORTBOW = "Main Hand"
    RAPIER = "Main Hand"
    MAGICWAND = "Main Hand"
    QUARTERSTAFF = "Main Hand"

class ArmourTypes(Enum):
    HEAD = "Headgear"
    CHEST = "Chestpiece"
    GLOVES = "Gloves"
    BOOTS = "Boots"
    MAINHAND = "Main Hand"
