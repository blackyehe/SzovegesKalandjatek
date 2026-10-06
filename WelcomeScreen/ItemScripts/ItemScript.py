from WelcomeScreen.Enums.everyEnum import ItemTypes
from random import randint
class Item:
    def __init__(self, itemName, itemType:ItemTypes,itemPrice):
        self.itemName = itemName
        self.itemType = itemType
        self.itemIndex = 1
        self.itemPrice = itemPrice

healingPotion = Item("Healing Potion", ItemTypes.OTHER,150)

def DrinkHealingPotion(player):
    amount = randint(3,12) + (player.Constitution-10)
    player.playerCurrentHP += amount
    print(f"You drink a healing potion, your injuries start to fade, you healed: {amount} HP back.\n"
          f"your current hp is now: {player.playerCurrentHP} / {player.playerMaxHP}")