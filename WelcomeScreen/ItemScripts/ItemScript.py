from WelcomeScreen.Enums.everyEnum import ItemTypes
class Item:
    def __init__(self, itemName, itemType:ItemTypes,itemPrice):
        self.itemName = itemName
        self.itemType = itemType
        self.itemIndex = 1
        self.itemPrice = itemPrice