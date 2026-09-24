from enum import Enum

class ItemTypes(Enum):
    ARMOR = 1
    WEAPON = 2
    OTHER = 3

class WeaponTypes(Enum):
    SHORTSWORD = 1
    DAGGER = 2
    LONGSWORD = 3
    SHORTBOW = 4
    RAPIER = 5
    MAGICWAND = 6
    QUARTERSTAFF = 7

class ArmourTypes(Enum):
    HEAD = 1
    CHEST = 2
    GLOVES = 3
    BOOTS = 4
    MAINHAND = 5
