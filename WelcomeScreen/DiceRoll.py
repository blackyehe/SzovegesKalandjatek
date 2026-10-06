from random import randint
def DiceRoll(numberToBeat, player, dcType):
    rnd = randint(1, 10)
    playerDc = 0
    global success
    success = False

    match dcType:
        case "dex" | "dexterity" | "DEX":
            playerDc = player.Dexterity
        case "str" | "strength" | "STR":
            playerDc = player.Strength
        case "wis" | "wisdom" | "WIS":
            playerDc = player.Wisdom
        case "int" | "intelligence" | "INT":
            playerDc = player.Intelligence
        case "cha" | "charisma" | "CHA":
            playerDc = player.Charisma
        case "con" | "constitution" | "CON":
            playerDc = player.Constitution

    if playerDc + rnd > numberToBeat:
        success = True
        print(f"\nSUCCESS: your modifier:{playerDc} + random number:{rnd} beats {numberToBeat}")
    else:
        success = False
        print(f"\nFAILURE: your modifier:{playerDc} + random number:{rnd} beats {numberToBeat} ")

    return success