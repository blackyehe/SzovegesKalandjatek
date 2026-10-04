class Quest:
    def __init__(self,QuestTitle):
        self.QuestTitle = QuestTitle
        self.QuestDescription = ""
        self.IsFinished = False
        self.KillTracker = 0
        self.KillToFinish = 0

    def TrackerIncrement(self,quest):
        if quest.KillTracker < quest.KillToFinish:
            quest.KillTracker += 1
            print(f"Current Progress: {quest.KillTracker}/{quest.KillToFinish}")

        if quest.KillTracker >= quest.KillToFinish and quest.IsFinished is False:
            quest.IsFinished = True
            print(f"{self.QuestTitle} is finished")

GoblinHunt = Quest("GOBLIN HUNT")
GoblinHunt.QuestDescription = "Kill 5 Goblins and report it to the Adventurer's Guild"
GoblinHunt.KillToFinish = 5