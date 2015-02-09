from enumfields import Enum, EnumField
from django.db import models


class SkillAbility(models.Model):

    class Skills(Enum):
        ACADEMICS = 'Academics'  # Mental
        COMPUTER = 'Computer'  # Mental
        CRAFTS = 'Crafts'  # Mental
        INVESTIGATION = 'Investigation'  # Mental
        MEDICINE = 'Medicine'  # Mental
        OCCULT = 'Occult'  # Mental
        POLITICS = 'Politics'  # Mental
        SCIENCE = 'Science'  # Mental
        ATHLETICS = 'Athletics'  # Physical
        BRAWL = 'Brawl'  # Physical
        DRIVE = 'Drive'  # Physical
        FIREARMS = 'Firearms'  # Physical
        LARCENY = 'Larceny'  # Physical
        STEALTH = 'Stealth'  # Physical
        SURVIVAL = 'Survival'  # Physical
        WEAPONRY = 'Weaponry'  # Physical
        ANIMAL = 'Animal Ken'  # Social
        EMPATHY = 'Empathy'  # Social
        EXPRESSION = 'Expression'  # Social
        INTIMIDATION = 'Intimidation'  # Social
        PERSUASION = 'Persuasion'  # Social
        SOCIALIZE = 'Socialize'  # Social
        STREETWISE = 'Streetwise'  # Social
        SUBTERFUGE = 'Subterfuge'  # Social

    skill = EnumField(Skills)

    class Meta:
        verbose_name_plural = "Skill Abilities"

    def __str__(self):
        return self.skill.label


class AttributeAbility(models.Model):

    class Attributes(Enum):
        INTELLIGENCE = 'Intelligence'  # Mental, Power
        WITS = 'Wits'  # Mental', 'Finesse
        RESOLVE = 'Resolve'  # Mental', 'Resistance
        STRENGTH = 'Strength'  # Physical', 'Power
        DEXTERITY = 'Dexterity'  # Physical', 'Finesse
        STAMINA = 'Stamina'  # Physical', 'Resistance
        PRESENCE = 'Presence'  # Social', 'Power
        MANIPULATION = 'Manipulation'  # Social', 'Finesse
        COMPOSURE = 'Composure'  # Social', 'Resistance

    attribute = EnumField(Attributes)

    class Meta:
        verbose_name_plural = "Attribute Abilities"

    def __str__(self):
        return self.attribute.label
