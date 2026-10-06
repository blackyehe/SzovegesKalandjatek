import introcs

dungeonDict = {
    "0": introcs.Vector2(x =-1, y= -1),
    "1": introcs.Vector2(x =0,y=-1),
    "2": introcs.Vector2(x =-1,y=1),
    "3": introcs.Vector2(x =-1,y=0),
    "4": introcs.Vector2(x =0,y=0),
    "5": introcs.Vector2(x =1,y=0),
    "6": introcs.Vector2(x =-1,y=1),
    "7": introcs.Vector2(x =0,y=1),
    "8": introcs.Vector2(x =1,y=1),
}

rooms =["0", "1", "2", "3", "4", "5", "6", "7", "8"]

def SearchDictKey(value, dictionary):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return key
    return None

currentPos = dungeonDict["4"]
def ShowDungeonGrid(currentPos, alreadyVisited, roomDict, everyRoom):
    rooms = ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]",]
    for i in range(len(alreadyVisited)):
        if len(alreadyVisited) > 0:
            roomIndex = SearchDictKey(alreadyVisited[i], dungeonDict)
            rooms[int(roomIndex)] = "[X]"

    for i  in range(9):
        if currentPos == dungeonDict[everyRoom[i]]:
            rooms[i] = "[O]"

    for i in range(len(rooms)):
        if i == 3 or i == 6:
            print(f"\n{rooms[i]}", end=' ')
        else:
            print(f"{rooms[i]}", end=' ')

def EmbarkOutside():
    dungeonDict = {
        "0": introcs.Vector2(x=-1, y=-1),
        "1": introcs.Vector2(x=0, y=-1),
        "2": introcs.Vector2(x=-1, y=1),
        "3": introcs.Vector2(x=-1, y=0),
        "4": introcs.Vector2(x=0, y=0),
        "5": introcs.Vector2(x=1, y=0),
        "6": introcs.Vector2(x=-1, y=1),
        "7": introcs.Vector2(x=0, y=1),
        "8": introcs.Vector2(x=1, y=1),
    }
    rooms = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    currentPos = dungeonDict["0"]
    alreadyVisited = []
    while True:
        print("The dungeon is infested with goblins, you can see the blood trail leading into the massive cave structure.")
        ShowDungeonGrid(currentPos, alreadyVisited, dungeonDict, rooms)
        input("Press Enter to continue...")

        pass


def AvailableDirections(currentPos, roomDict, everyRoom):

    DirDict = {
        "North": False,
        "South": False,
        "West": False,
        "East": False,
    }

    northPos = introcs.Vector2(currentPos.x, currentPos.y - 1)
    southPos = introcs.Vector2(currentPos.x, currentPos.y + 1)
    westPos = introcs.Vector2(currentPos.x - 1, currentPos.y)
    eastPos = introcs.Vector2(currentPos.x + 1, currentPos.y)

    for i in range(len(everyRoom)):

        random = roomDict[everyRoom[i]]

        if roomDict[everyRoom[i]].x == northPos.x and roomDict[everyRoom[i]].y == northPos.y:
            DirDict["North"] = True

        elif roomDict[everyRoom[i]].x == southPos.x and roomDict[everyRoom[i]].y == southPos.y:
            DirDict["South"] = True

        elif roomDict[everyRoom[i]].x == westPos.x and roomDict[everyRoom[i]].y == westPos.y:
            DirDict["West"] = True

        elif roomDict[everyRoom[i]].x == eastPos.x and roomDict[everyRoom[i]].y == eastPos.y:
            DirDict["East"] = True

    availableList = []
    for i in DirDict.keys():
        if DirDict[i]:
            availableList.append(i)

    for i, dir in enumerate(availableList, 1):
        print(f"{i}. {dir}")

    input(f"Type the number of the direction you wish to go forward: ")

EmbarkOutside()
AvailableDirections(currentPos,dungeonDict,rooms,)