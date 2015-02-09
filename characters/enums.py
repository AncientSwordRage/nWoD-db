from enumfields import Enum, EnumField
from django.db import models


class SkillAbility(models.Model):

    class Skills(Enum):
        ACADEMICS = ('Academics', 'Mental')
        COMPUTER = ('Computer', 'Mental')
        CRAFTS = ('Crafts', 'Mental')
        INVESTIGATION = ('Investigation', 'Mental')
        MEDICINE = ('Medicine', 'Mental')
        OCCULT = ('Occult', 'Mental')
        POLITICS = ('Politics', 'Mental')
        SCIENCE = ('Science', 'Mental')
        ATHLETICS = ('Athletics', 'Physical')
        BRAWL = ('Brawl', 'Physical')
        DRIVE = ('Drive', 'Physical')
        FIREARMS = ('Firearms', 'Physical')
        LARCENY = ('Larceny', 'Physical')
        STEALTH = ('Stealth', 'Physical')
        SURVIVAL = ('Survival', 'Physical')
        WEAPONRY = ('Weaponry', 'Physical')
        ANIMAL = ('Animal', 'Social')
        EMPATHY = ('Empathy', 'Social')
        EXPRESSION = ('Expression', 'Social')
        INTIMIDATION = ('Intimidation', 'Social')
        PERSUASION = ('Persuasion', 'Social')
        SOCIALIZE = ('Socialize', 'Social')
        STREETWISE = ('Streetwise', 'Social')
        SUBTERFUGE = ('Subterfuge', 'Social')

        def __init__(self, label, skill_type):
            self.label = label
            self.skill_type = skill_type

        @property
        def type(self):
            return self.skill_type
    skill = EnumField(Skills)


class AttributeAbility(models.Model):

    class Attributes(Enum):
        INTELLIGENCE = ('Intelligence', 'Mental', 'Power')
        WITS = ('Wits', 'Mental', 'Finesse')
        RESOLVE = ('Resolve', 'Mental', 'Resistance')
        STRENGTH = ('Strength', 'Physical', 'Power')
        DEXTERITY = ('Dexterity', 'Physical', 'Finesse')
        STAMINA = ('Stamina', 'Physical', 'Resistance')
        PRESENCE = ('Presence', 'Social', 'Power')
        MANIPULATION = ('Manipulation', 'Social', 'Finesse')
        COMPOSURE = ('Composure', 'Social', 'Resistance')

        def __init__(self, label, attr_type, category):
            self.label = label
            self.attr_type = attr_type
            self.category = category

        @property
        def type(self):
            return self.attr_type
    attribute = EnumField(Attributes)
