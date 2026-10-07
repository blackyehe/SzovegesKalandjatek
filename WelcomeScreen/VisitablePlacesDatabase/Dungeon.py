from unittest import case
import introcs
from random import randint
import WelcomeScreen.ItemScripts.ItemScript
import WelcomeScreen.DiceRoll

roll = WelcomeScreen.DiceRoll
itemScript = WelcomeScreen.ItemScripts.ItemScript
class Dungeon:
    def __init__(self):
        self.encounterRoom = "a sickly green looking monstrosity, attacking you as soon as you enter the room!"
        self.lootRoom = "a mostly empty room, a bunch of stolen goods are stored in here, no doubt the goblins did this."
    def LootTheRoom(self,player):
        GainedGold = randint(20,150)
        ChanceForPotion = randint(1,5)
        PotionGained = False
        if ChanceForPotion == 4 or ChanceForPotion == 5:
            PotionGained = True

        if PotionGained:
            print("===========================================================================================================")
            print(f"You begin to loot the seemingly empty room, you find these: [{GainedGold} Gold, [{itemScript.healingPotion.itemName}]\n")
            player.ManageGold(GainedGold,True)
            player.AddItemToInventory(itemScript.healingPotion)
        else:
            print(f"You begin to loot the seemingly empty room, you find these: [{GainedGold} Gold]\n")
            player.ManageGold(GainedGold, True)
        print("===========================================================================================================")
        input("Press ENTER to continue...")

dungeon = Dungeon()
class Goblin:
    def __init__(self, HP, AC):
        self.MaxHP = HP
        self.HP = HP
        self.AC = AC

    def TakeDamage(self, number):
        self.HP -= number
        print(f"The enemy took {number} damage, Current HP: {self.HP}")

    def TakeTurn(self,player):
        if self.HP <= 0:
            print(f"You have successfully killed this despicable beast!")
            if len(player.ActiveQuests) != 0:
                if not player.ActiveQuests[0].IsFinished:
                    player.ActiveQuests[0].TrackerIncrement(player.ActiveQuests[0])
        else:
            success = randint(1,25)
            if success >= player.CurrentArmorClass:
                player.TakeDamage(randint(1,5))

def GoToNewRoom(player, roomPos, alreadyVisited, everyRoom):

    if len(alreadyVisited) == 9:
        print(f"\nYou purged the Goblin threat, great job!\n"
              f"You venture back to the city, as nothing is left at the dungeon.\n")
        player.ShowUserMenu()

    if roomPos not in alreadyVisited:
        alreadyVisited.append(roomPos)
    else:
        print("The room is clear.\n")
        return

    rand = randint(1, 2)

    if rand == 1:
        currentRoom = dungeon.encounterRoom
        print("\n===========================================================================================================")
        print(f"You slowly approach a new room, you encounter {currentRoom}")
        StartEncounter(player)
    else:
        currentRoom = dungeon.lootRoom
        print("\n===========================================================================================================")
        print(f"You slowly approach a new room, you encounter {currentRoom}")
        dungeon.LootTheRoom(player)
def StartEncounter(player):
    goblin = Goblin(randint(22,25),randint(19,24))
    while goblin.HP > 0:
        print(f"You have been attacked by a Goblin! [GOBLIN: {goblin.HP} HP | {goblin.AC} AC]")
        print("===========================================================================================================\n")
        CombatOptions(player,goblin)

def CombatOptions(player,enemy):
    print(f"1. Attack with your Main Hand Weapon\n"
          f"2. Use one of your Abilities\n"
          f"3. Open Inventory\n"
          f"4. Try to flee\n")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print(f"You have decided to use your weapon!")
            success = roll.DiceRoll(enemy.AC,player,player.ReturnMainHand().statToIncrease)
            if success:
                dmg = max(player.Strength,player.Dexterity,player.Intelligence)+randint(1,10)
                enemy.TakeDamage(dmg)
                input("Press Enter to continue...\n")
                enemy.TakeTurn(player)
            else:
                print(f"The enemy evade your attack!")
                input("Press Enter to continue...\n")
                enemy.TakeTurn(player)
        case 2:
            skills = player.playerClass.skills
            for i in range(len(player.playerClass.skills)):
                print(f"{i+1}. {skills[i].skillName} - {skills[i].SkillDescription}")
            choice = int(input("Choose between 1/2/3..."))
            if skills[choice-1].IsAttack:
                target = enemy
            else:
                target = player
            skills[choice-1].DoSkill(target)
            input("Press Enter to continue...\n")
            enemy.TakeTurn(player)
        case 3:
            player.ShowPlayerNormalInventory()
        case 4:
            print("Your cowardly nature gets the better of you, and you try to run for your life.")
            success = roll.DiceRoll(16,player,"dex")
            if success:
                print(f"You safely return, it seems the only thing you've lost is your pride.")
                player.ShowUserMenu()
            else:
                print(f"You tried to escape the clutches of the enemy, but it seems you're not even good at running.")

def SearchDictKey(value, dictionary):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return key
    return None
def ShowDungeonGrid(currentPos, alreadyVisited, roomDict, everyRoom):
    roomsToPrint = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ]
    for i in range(len(alreadyVisited)):
        if len(alreadyVisited) > 0:
            roomIndex = SearchDictKey(alreadyVisited[i], roomDict)
            roomsToPrint[int(roomIndex)] = "[X]"

    for i in range(9):
        if currentPos == roomDict[everyRoom[i]]:
            roomsToPrint[i] = "[O]"

    for i in range(len(roomsToPrint)):
        if i == 3 or i == 6:
            print(f"\n{roomsToPrint[i]}", end=' ')
        else:
            print(f"{roomsToPrint[i]}", end=' ')
    print("\n")

def AvailableDirections(player, currentPos, roomDict, everyRoom, alreadyVisited):
    directions = {
        "North": introcs.Vector2(currentPos.x, currentPos.y - 1),
        "South": introcs.Vector2(currentPos.x, currentPos.y + 1),
        "West": introcs.Vector2(currentPos.x - 1, currentPos.y),
        "East": introcs.Vector2(currentPos.x + 1, currentPos.y)
    }
    availableList = []

    for direction, position in directions.items():
        for room in everyRoom:
            roomPosition = roomDict[room]

            if (roomPosition.x == position.x and
                    roomPosition.y == position.y):
                availableList.append(direction)
                break

    print("Available directions:")
    for i, direction in enumerate(availableList, 1):
        print(f"{i}. {direction}")

    choice = int(input("Type the number of the direction you wish to go: "))

    if choice < 1 or choice > len(availableList):
        print("Invalid choice.")
        return currentPos

    selectedDirection = availableList[choice - 1]

    newPos = directions[selectedDirection]

    print(f"You move {selectedDirection}.")
    GoToNewRoom(player,newPos,alreadyVisited,everyRoom)
    return newPos

def EmbarkOutside(player):
    dungeonDict = {
        "0": introcs.Vector2(x=-1, y=-1),
        "1": introcs.Vector2(x=0, y=-1),
        "2": introcs.Vector2(x=1, y=-1),

        "3": introcs.Vector2(x=-1, y=0),
        "4": introcs.Vector2(x=0, y=0),
        "5": introcs.Vector2(x=1, y=0),

        "6": introcs.Vector2(x=-1, y=1),
        "7": introcs.Vector2(x=0, y=1),
        "8": introcs.Vector2(x=1, y=1),
    }

    rooms = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    currentPos = dungeonDict["0"]
    alreadyVisited = [currentPos]
    print("The dungeon is infested with goblins, you can see a blood trail leading into the massive cave structure.\n"
          "Your current position is marked with an [O], and the rooms you have visited are marked with an [X]\n")
    while True:
        ShowDungeonGrid(currentPos,alreadyVisited,dungeonDict,rooms)
        currentPos = AvailableDirections(player,currentPos, dungeonDict, rooms, alreadyVisited)