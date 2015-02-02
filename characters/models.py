from django.db import models
from nwod_characters.util import IntegerRangeField, modify_verbose
from .choices import ATTRIBUTE_CHOICES, SKILL_CHOICES
import csv

# Create your models here.

class NWODCharacter(models.Model):
    SUB_RACE_CHOICES = ()
    FACTION_CHOICES = ()
    VIRTUE_CHOICES = (('prudence', 'Prudence'), ('justice', 'Justice'),
     ('temperance', 'Temperance'), ('fortitude', 'Fortitude'), ('faith', 'Faith'), 
     ('hope', 'Hope'), ('charity', 'Charity'))
    VICE_CHOICES = (('lust', 'Lust'), ('gluttony', 'Gluttony'), ('greed', 'Greed'),
     ('sloth', 'Sloth'), ('wrath', 'Wrath'), ('envy', 'Envy'), ('pride', 'Pride'))

    name = models.CharField(max_length=200)
    player = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    sub_race = models.CharField(choices=SUB_RACE_CHOICES, max_length=50)
    faction = models.CharField(choices=FACTION_CHOICES, max_length=50, null=True)
    power_level = IntegerRangeField(min_value=1, max_value=10)
    energy_trait = IntegerRangeField(min_value=1, max_value=10)
    virtue = models.CharField(choices=VIRTUE_CHOICES, max_length=50)
    vice = models.CharField(choices=VICE_CHOICES, max_length=50)
    morality = IntegerRangeField(min_value=0, max_value=10)


@modify_verbose({'power_level': 'Gnosis',
                'energy_trait': 'Mana',
                'faction': 'Order',
                'sub_race': 'Path',
                'morality': 'Wisdom',
                })
class Mage(NWODCharacter):
    SUB_RACE_CHOICES = (
        ('AC', 'Acanthus'),
        ('Ma', 'Mastigos'),
        ('Mo', 'Moros'),
        ('Ob', 'Obrimos'),
        ('Th', 'Thyrsus'),
    )
    FACTION_CHOICES = (
        ('AA', 'The Adamantine Arrow'),
        ('GotV', 'Guardians of the Veil'),
        ('Myst', 'The Mysterium'),
        ('SL', 'The Silver Ladder'),
        ('FC', 'The Free Council')
    )
    def __str__(self):
        return self.name

ARCANUM_CHOICES = (
        (None, '----'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'),
         ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter'),
         ('Prime', 'Prime')
    )

def resistance_attributes():
    res = [ATTRIBUTE_CHOICES[i][-1][-1] for i in range(len(ATTRIBUTE_CHOICES))]
    return res

class Spell(models.Model):
    name = models.CharField(max_length=50)
    vulgar = models.BooleanField(default=False)
    # All spells have a primary arcana, and 0-Many secondary arcana.
    # Each spell's arcanum have different rating. E.g. Fate 1, Prime 1
    primary_arcana = models.ManyToManyField('Arcana', choices=ARCANUM_CHOICES, 
        related_name='spell_by_primary_arcanum')
    secondary_arcana = models.ManyToManyField('Arcana', choices=ARCANUM_CHOICES, blank=True, null=True, 
        related_name='spell_by_secondary_arcanum', default=None)
    optional_arcana = models.ManyToManyField('Arcana', choices=ARCANUM_CHOICES, blank=True, null=True, 
        related_name='spell_by_optional_arcanum', default=None)
    # All spells have a 'Attribute+Skill+Primary arcana' pool for casting
    rote_skill = models.ManyToManyField('Skill', choices=SKILL_CHOICES, related_name='spell_by_rote_skill')
    rote_attribute = models.ManyToManyField('Attribute', choices=ATTRIBUTE_CHOICES, 
        related_name='spell_by_rote_attribute')
    # Mages can own spells
    mage = models.ManyToManyField('Mage', related_name='spell_by_mage')
    # Optional contested skill check, e.g. 'Attribute+Skill+Primary arcana vs Attribute+Skill'
    contested = models.BooleanField(default=False)
    contested_attribute = models.ManyToManyField('Attribute', choices=ATTRIBUTE_CHOICES, 
        related_name='spell_by_contested_attribute', default=None, blank=True)
    contested_skill = models.ManyToManyField('Skill', choices=SKILL_CHOICES, 
        related_name='spell_by_contested_skill', default=None, blank=True)
    # Optional attribute to subtract from casting dicepool, 
    # e.g. 'Attribute+Skill+Primary arcana-Resist Attribute'
    resisted = models.BooleanField(default=False)
    resisted_by_attribute = models.ManyToManyField('Attribute', choices=resistance_attributes(), 
        related_name='dice_pools_by_resistance_attribute', default=None, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50, choices=SKILL_CHOICES)
    value = IntegerRangeField(min_value=0, max_value=5)
    character = models.ForeignKey('NWODCharacter', related_name='%(class)s_by_skill')

class Attribute(models.Model):
    name = models.CharField(max_length=50, choices=ATTRIBUTE_CHOICES)
    value = IntegerRangeField(min_value=0, max_value=5)
    # Characters each have several 
    character = models.ForeignKey('NWODCharacter', related_name='%(class)s_by_attribute')

class Arcana(models.Model):
    name = models.CharField(max_length=50, choices=ARCANUM_CHOICES)
    value = IntegerRangeField(min_value=0, max_value=5)
    # Mages have several arcana
    mage = models.ForeignKey('Mage', related_name='mage_by_arcana')

def parse_wod_index_spell_row(file):
    import re
    arcanum_and_level_pattern = re.compile(r'(?P<delim_type>|\s+and/or\s+|\s+opt\s+)(?P<arcana_list>(?:\w+?\s\d)(?:(?:[,+]|\s+or)\s+(?:\w+?\s\d))*)')
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        # header = reader.next()
        for row in reader:
            name = row[0]
            primary_arcana = row[1]
            other_arcarna = [m.groupdict() for m in arcanum_and_level_pattern.finditer(row[2])]
            if other_arcarna['delim_type']=='':
                print('hello')
            secondary_arcana = other_arcarna
            return Spell.objects.bulk_create(name=name,
                primary_arcana=primary_arcana,
                secondary_arcana=secondary_arcana)
