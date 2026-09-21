from everyItemEnum import ItemTypes
class Item:
    def __init__(self, itemName, itemType:ItemTypes):
        self.itemName = itemName
        self.itemType = itemType

