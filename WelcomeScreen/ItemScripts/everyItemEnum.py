from enum import Enum

class ItemTypes(Enum):
    Armor = 1
    Weapon = 2
    Other = 3

class WeaponTypes(Enum):
    Shortsword = 1
    Dagger = 2
    Longsword = 3
    Shortbow = 4
    Rapier = 5
    MagicWand = 6
    QuarterStaff = 7

class ArmourTypes(Enum):
    head = 1
    chest = 2
    gloves = 3
    boots = 4