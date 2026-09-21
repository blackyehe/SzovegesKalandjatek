class PlayableClass:
    def __init__(self, className, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma):
        self.className = className
        self.strength = Strength
        self.dexterity = Dexterity
        self.constitution = Constitution
        self.intelligence = Intelligence
        self.wisdom = Wisdom
        self.charisma = Charisma

    Fighter = PlayableClass("Fighter", 18, 12, 14, 10, 12, 8)
    Rogue = PlayableClass("Rogue", 8, 18, 10, 12, 12, 14)
    Wizard = PlayableClass("Wizard", 8, 10, 12, 18, 14, 12)