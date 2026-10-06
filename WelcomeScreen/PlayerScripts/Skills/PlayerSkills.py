from abc import ABC
class Skills(ABC):
   def DoSkill(self, target):
       pass

class Scorch(Skills):
    def __init__(self,Damage):
        self.skillName = "Scorch"
        self.Class = "Wizard"
        self.SkillDescription = "You summon magical flames from your hand, scorching your enemy"
        self.SkillDamage = Damage
        self.IsAttack = True
    def DoSkill(self, target):
        target.TakeDamage(self.SkillDamage*2)


class MageArmour(Skills):
    def __init__(self,Increase):
        self.skillName = "Mage Armour"
        self.Class = "Wizard"
        self.SkillDescription = f"You surround yourself with Arcane energy, your AC increases by {Increase}"
        self.SkillDamage = Increase
        self.IsAttack = False

    def DoSkill(self, target):
        target.CurrentArmorClass = target.Dexterity + self.SkillDamage

class Assassinate(Skills):
    def __init__(self,Damage):
        self.skillName = "Assassinate"
        self.Class = "Rogue"
        self.SkillDescription = "You swiftly move into the enemy's blindspot, and strike at them, dealing extra damage to enemies with full health"
        self.SkillDamage = Damage
        self.IsAttack = True

    def DoSkill(self, target):
        if target.HP == target.MaxHP:
            target.TakeDamage(self.SkillDamage*2)
        else:
            target.TakeDamage(self.SkillDamage)

class ElusiveShadow(Skills):
    def __init__(self,Increase):
        self.skillName = "Elusive Shadow"
        self.Class = "Rogue"
        self.SkillDescription = f"You blend into the surrounding shadows, increasing your AC by {Increase}"
        self.SkillDamage = Increase
        self.IsAttack = False
    def DoSkill(self, target):
        target.CurrentArmorClass = target.Dexterity + self.SkillDamage

class MenacingStrike(Skills):
    def __init__(self,Damage):
        self.skillName = "Menacing Strike"
        self.Class = "Warrior"
        self.SkillDescription = "You emanate a menacing aura, striking your enemy with chilling precision"
        self.SkillDamage = Damage
        self.IsAttack = True

    def DoSkill(self, target):
        target.TakeDamage(self.SkillDamage*2)

class ArmourUpgrade(Skills):
    def __init__(self,Increase):
        self.skillName = "Armour Upgrade"
        self.Class = "Rogue"
        self.SkillDescription = f"Your armour starts to hardens, increasing your AC by {Increase}"
        self.SkillDamage = Increase
        self.IsAttack = False

    def DoSkill(self, target):
        target.CurrentArmorClass = target.Dexterity + self.SkillDamage

Scorch = Scorch(10)
MageArmor = MageArmour(3)

Assassinate = Assassinate(8)
ElusiveShadow = ElusiveShadow(5)

MenacingStrike = MenacingStrike(6)
ArmourUpgrade = ArmourUpgrade(2)