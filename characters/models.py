from django.db import models
from nwod_characters.util import IntegerRangeField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from characters.enums import SkillAbility, AttributeAbility, Category  # NOQA
from django.utils import timezone

# import csv

# Create your models here.


class NWODCharacter(models.Model):

    class Meta:
        abstract = True
        ordering = ['updated_date', 'created_date']

    SUB_RACE_CHOICES = ()
    FACTION_CHOICES = ()

    name = models.CharField(max_length=200)
    player = models.ForeignKey('auth.User', related_name="%(class)s_by_user")
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    sub_race = models.CharField(choices=SUB_RACE_CHOICES, max_length=50)
    faction = models.CharField(
        choices=FACTION_CHOICES, max_length=50, null=True, default=None)

    def save(self, *args, **kwargs):
        initialise_all_links = kwargs.pop('initialise_all_links', not self.pk)
        super(NWODCharacter, self).save(*args, **kwargs)
        if initialise_all_links:
            all_skills = [
                CharacterSkillLink(
                    skill=SkillAbility.objects.get_or_create(skill=skill)[0],
                    content_object=self,
                    speciality=""
                )
                for skill in SkillAbility.Skills
            ]
            "\n".join([str(foo) for foo in all_skills])
            CharacterSkillLink.objects.bulk_create(all_skills)
            all_attrributes = [
                CharacterAttributeLink(
                    attribute=AttributeAbility.objects.get_or_create(
                        attribute=attribute)[0],
                    content_object=self,
                )
                for attribute in AttributeAbility.Attributes
            ]
            CharacterAttributeLink.objects.bulk_create(all_attrributes)

    @property
    def is_published(self):
        return self.published_date is not None and self.published_date >= timezone.now()

    attributes = GenericRelation('CharacterAttributeLink')
    skills = GenericRelation('CharacterSkillLink')

    @property
    def physical_attributes(self):
        return [self.attributes.filter(attribute=attribute) for attribute
                in AttributeAbility.objects.physical()]

    @property
    def mental_attributes(self):
        return [self.attributes.filter(attribute=attribute) for attribute
                in AttributeAbility.objects.mental()]

    @property
    def social_attributes(self):
        return [self.attributes.filter(attribute=attribute) for attribute
                in AttributeAbility.objects.social()]

    @property
    def physical_skills(self):
        return [self.skills.filter(skill=skill) for skill
                in SkillAbility.objects.physical()]

    @property
    def mental_skills(self):
        return [self.skills.filter(skill=skill) for skill
                in SkillAbility.objects.mental()]

    @property
    def social_skills(self):
        return [self.skills.filter(skill=skill) for skill
                in SkillAbility.objects.social()]


class Characteristics(models.Model):

    class Meta:
        abstract = True
    VIRTUE_CHOICES = (('prudence', 'Prudence'), ('justice', 'Justice'),
                      ('temperance', 'Temperance'), ('fortitude',
                                                     'Fortitude'), ('faith', 'Faith'),
                      ('hope', 'Hope'), ('charity', 'Charity'))
    VICE_CHOICES = (('lust', 'Lust'), ('gluttony', 'Gluttony'), ('greed', 'Greed'),
                    ('sloth', 'Sloth'), ('wrath', 'Wrath'), ('envy', 'Envy'), ('pride', 'Pride'))

    power_level = IntegerRangeField(min_value=1, max_value=10, default=1)
    energy_trait = IntegerRangeField(min_value=1, max_value=10, default=7)
    virtue = models.CharField(choices=VIRTUE_CHOICES, max_length=50)
    vice = models.CharField(choices=VICE_CHOICES, max_length=50)
    morality = IntegerRangeField(min_value=0, max_value=10, default=7)
    size = IntegerRangeField(min_value=1, max_value=10, default=5)


class Trait(models.Model):
    MIN = 0
    MAX = 5
    current_value = IntegerRangeField(
        min_value=MIN, max_value=MAX, default=MIN)
    maximum_value = IntegerRangeField(
        min_value=MIN, max_value=MAX, default=MIN)

    class Meta:
        abstract = True


class BookReference(models.Model):
    things_in_books = models.Q(app_label='mage', model='spell') | models.Q(
        app_label='characters', model='merit')
    content_type = models.ForeignKey(ContentType, limit_choices_to=things_in_books,
                                     null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    book_name = models.CharField(max_length=50)
    book_page = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.book_name


class CrossCharacterMixin(models.Model):
    cross_character_types = models.Q(app_label='mage', model='mage')
    content_type = models.ForeignKey(ContentType, limit_choices_to=cross_character_types,
                                     null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class CharacterSkillLink(Trait, CrossCharacterMixin):
    PRIORITY_CHOICES = (
        (0, 'Unassigned'), (1, 'Primary'), (2, 'Secondary'), (3, 'Tertiary')
    )
    skill = models.ForeignKey('SkillAbility')
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES, default=0)
    speciality = models.CharField(
        max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return self.skill.skill.label


class CharacterAttributeLink(Trait, CrossCharacterMixin):
    MIN = 1
    PRIORITY_CHOICES = (
        (0, 'Unassigned'), (1, 'Primary'), (2, 'Secondary'), (3, 'Tertiary')
    )
    attribute = models.ForeignKey('AttributeAbility')
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES, default=0
    )

    def __str__(self):
        return self.attribute.attribute.label


# def parse_wod_index_spell_row(file):
#     import re
#     arcanum_and_level_pattern = re.compile(r'(?P<delim_type>|\s+and/or\s+|\s+opt\s+)(?P<arcana_list>(?:\w+?\s\d)(?:(?:[,+]|\s+or)\s+(?:\w+?\s\d))*)')
#     with open(file) as f:
#         reader = csv.reader(f, delimiter=',')
# header = reader.next()
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
