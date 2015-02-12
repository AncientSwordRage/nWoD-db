from enumfields import Enum, EnumField
from django.db import models


class AutoNumber(Enum):

    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class Category(AutoNumber):
    MENTAL = ()
    PHYSICAL = ()
    SOCIAL = ()


class CategoryManager(models.Manager):

    '''
    Class to manage instances that rely on the category enum
    '''

    def physical(self):
        return [categorised_item for categorised_item in super(CategoryManager, self).get_queryset().all()
                if categorised_item.category == Category['PHYSICAL']]

    def mental(self):
        return [categorised_item for categorised_item in super(CategoryManager, self).get_queryset().all()
                if categorised_item.category == Category['MENTAL']]

    def social(self):
        return [categorised_item for categorised_item in super(CategoryManager, self).get_queryset().all()
                if categorised_item.category == Category['SOCIAL']]


class SkillAbility(models.Model):

    class Skills(AutoNumber):
        ACADEMICS = ()  # Mental
        COMPUTER = ()  # Mental
        CRAFTS = ()  # Mental
        INVESTIGATION = ()  # Mental
        MEDICINE = ()  # Mental
        OCCULT = ()  # Mental
        POLITICS = ()  # Mental
        SCIENCE = ()  # Mental
        ATHLETICS = ()  # Physical
        BRAWL = ()  # Physical
        DRIVE = ()  # Physical
        FIREARMS = ()  # Physical
        LARCENY = ()  # Physical
        STEALTH = ()  # Physical
        SURVIVAL = ()  # Physical
        WEAPONRY = ()  # Physical
        ANIMAL_KEN = ()  # Social
        EMPATHY = ()  # Social
        EXPRESSION = ()  # Social
        INTIMIDATION = ()  # Social
        PERSUASION = ()  # Social
        SOCIALIZE = ()  # Social
        STREETWISE = ()  # Social
        SUBTERFUGE = ()  # Social

    skill = EnumField(Skills)
    objects = CategoryManager()

    @property
    def category(self):
        skill_group = lambda skill: (
            int((skill.value - 1) / 8)) + 1 % 3

        return Category(skill_group(self.skill))

    class Meta:
        verbose_name_plural = "Skill Abilities"

    def __str__(self):
        return self.skill.label


class AttributeAbility(models.Model):

    class Attributes(AutoNumber):
        INTELLIGENCE = ()  # Mental, Power
        WITS = ()  # Mental', 'Finesse
        RESOLVE = ()  # Mental', 'Resistance
        STRENGTH = ()  # Physical', 'Power
        DEXTERITY = ()  # Physical', 'Finesse
        STAMINA = ()  # Physical', 'Resistance
        PRESENCE = ()  # Social', 'Power
        MANIPULATION = ()  # Social', 'Finesse
        COMPOSURE = ()  # Social', 'Resistance

    attribute = EnumField(Attributes)
    objects = CategoryManager()

    @property
    def category(self):
        attribute_group = lambda attribute: (
            int((attribute.value - 1) / 3)) + 1 % 3

        return Category(attribute_group(self.attribute))

    class Meta:
        verbose_name_plural = "Attribute Abilities"

    def __str__(self):
        return self.attribute.label


class ArcanumAbility(models.Model):

    class Arcana(AutoNumber):
        FATE = ()
        MIND = ()
        SPIRIT = ()
        DEATH = ()
        FORCES = ()
        TIME = ()
        SPACE = ()
        LIFE = ()
        MATTER = ()
        PRIME = ()

    arcanum = EnumField(Arcana)

    class Meta:
        verbose_name_plural = "Arcana Abilities"

    def __str__(self):
        return self.arcanum.label
