from django.db import models
from nwod_characters.util import IntegerRangeField
from .choices import ATTRIBUTE_CHOICES, SKILL_CHOICES
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# import csv

# Create your models here.
class NWODCharacter(models.Model):
    class Meta:
        abstract = True
    SUB_RACE_CHOICES = ()
    FACTION_CHOICES = ()

    name = models.CharField(max_length=200)
    player = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    sub_race = models.CharField(choices=SUB_RACE_CHOICES, max_length=50)
    faction = models.CharField(choices=FACTION_CHOICES, max_length=50, null=True)
    
class Characteristics(models.Model):
    class Meta:
        abstract = True
    VIRTUE_CHOICES = (('prudence', 'Prudence'), ('justice', 'Justice'),
     ('temperance', 'Temperance'), ('fortitude', 'Fortitude'), ('faith', 'Faith'), 
     ('hope', 'Hope'), ('charity', 'Charity'))
    VICE_CHOICES = (('lust', 'Lust'), ('gluttony', 'Gluttony'), ('greed', 'Greed'),
     ('sloth', 'Sloth'), ('wrath', 'Wrath'), ('envy', 'Envy'), ('pride', 'Pride'))

    power_level = IntegerRangeField(min_value=1, max_value=10)
    energy_trait = IntegerRangeField(min_value=1, max_value=10)
    virtue = models.CharField(choices=VIRTUE_CHOICES, max_length=50)
    vice = models.CharField(choices=VICE_CHOICES, max_length=50)
    morality = IntegerRangeField(min_value=0, max_value=10)
    size = IntegerRangeField(min_value=1, max_value=10, default=5)


def resistance_attributes():
    res = [ATTRIBUTE_CHOICES[i][-1][-1] for i in range(len(ATTRIBUTE_CHOICES))]
    return res

class Trait(models.Model):
    MIN = 0
    MAX = 5
    current_value = IntegerRangeField(min_value=MIN, max_value=MAX)
    maximum_value = IntegerRangeField(min_value=MIN, max_value=MAX)
    class Meta:
        abstract = True

class BookReference(models.Model):
    things_in_books = models.Q(app_label='mage', model='spell') | models.Q(app_label='characters', model='merit')
    content_type = models.ForeignKey(ContentType, limit_choices_to=things_in_books,
        null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')    
    book_name = models.CharField(max_length=50)
    book_page = models.PositiveSmallIntegerField(default=0)


class Merit(Trait, models.Model):
    name = models.CharField(max_length=50)
    book_ref = models.ForeignKey('BookReference')

class Skill(models.Model):
    name = models.CharField(max_length=50, choices=SKILL_CHOICES)

class Attribute(models.Model):
    name = models.CharField(max_length=50, choices=ATTRIBUTE_CHOICES)

class CrossCharacterMixin(models.Model):
    cross_character_types = models.Q(app_label='mage', model='mage')
    content_type = models.ForeignKey(ContentType, limit_choices_to=cross_character_types,
        null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    class Meta:
        abstract = True

class SkillLink(models.Model):
    skill = models.ForeignKey('Skill', choices=SKILL_CHOICES)
    class Meta:
        abstract = True

class AttributeLink(models.Model):
    attribute = models.ForeignKey('Attribute', choices=ATTRIBUTE_CHOICES)
    class Meta:
        abstract = True  
     
class CharacterSkillLink(SkillLink, Trait, CrossCharacterMixin):
    PRIORITY_CHOICES = (
        (1, 'Primary'), (2, 'Secondary'), (3, 'Tertiary')
        )
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=None)
    speciality = models.CharField(max_length=200, null=True, blank=True)

class CharacterAttributeLink(AttributeLink, Trait, CrossCharacterMixin):
    MIN = 1
    PRIORITY_CHOICES = (
        (1, 'Primary'), (2, 'Secondary'), (3, 'Tertiary')
        )
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=None)



# def parse_wod_index_spell_row(file):
#     import re
#     arcanum_and_level_pattern = re.compile(r'(?P<delim_type>|\s+and/or\s+|\s+opt\s+)(?P<arcana_list>(?:\w+?\s\d)(?:(?:[,+]|\s+or)\s+(?:\w+?\s\d))*)')
#     with open(file) as f:
#         reader = csv.reader(f, delimiter=',')
#         # header = reader.next()
#         for row in reader:
#             name = row[0]
#             primary_arcana = row[1]
#             other_arcarna = [m.groupdict() for m in arcanum_and_level_pattern.finditer(row[2])]
#             if other_arcarna['delim_type']=='':
#                 print('hello')
#             secondary_arcana = other_arcarna
#             return Spell.objects.bulk_create(name=name,
#                 primary_arcana=primary_arcana,
#                 secondary_arcana=secondary_arcana)
