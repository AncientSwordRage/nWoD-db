from django.db import models
from characters.models import NWODCharacter, Characteristics, Trait
from nwod_characters.util import modify_verbose, IntegerRangeField
from characters.enums import ArcanumAbility  # NOQA
from django.contrib.contenttypes.fields import GenericRelation
# from enumfields import EnumField


@modify_verbose({'power_level': 'Gnosis',
                 'energy_trait': 'Mana',
                 'faction': 'Order',
                 'sub_race': 'Path',
                 'morality': 'Wisdom',
                 })
class Mage(NWODCharacter, Characteristics):
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
    arcana = models.ManyToManyField('ArcanumAbility', through='CharacterArcanumLink', related_name='mage_by_arcana')

    def save(self, *args, **kwargs):
        initialise_all_links = not self.pk
        super(Mage, self).save(
            initialise_all_links=initialise_all_links, *args, **kwargs)
        if initialise_all_links:
            CharacterArcanumLink.objects.bulk_create([
                CharacterArcanumLink(
                    arcana=ArcanumAbility.objects.get_or_create(
                        arcanum=arcana)[0],
                    mage=self,
                )
                for arcana in ArcanumAbility.Arcana
            ])

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=50)
    vulgar = models.BooleanField(default=False)
    # All spells have a primary arcana, and 0-Many secondary arcana.
    # Each spell's arcanum have different rating. E.g. Fate 1, Prime 1
    # non-optional arcana in addition to the main arcana
    # arcana that are not needed to cast the spell
    arcana = models.ManyToManyField('ArcanumAbility', through='SpellArcanumLink',
                                    related_name='spell_by_arcanum', null=True, blank=True, default=None)

    @property
    def primary_arcana(self):
        return self.arcana.filter(type="primary")

    @property
    def secondary_arcana(self):
        return self.arcana.filter(type="secondary")

    @property
    def optional_arcana(self):
        return self.arcana.filter(type="optional")

    # All spells have a 'Attribute+Skill+Primary arcana' pool for casting
    skill = models.ManyToManyField('SkillAbility', related_name='spell_by_skill',
                                   through='SpellSkillLink')
    attribute = models.ManyToManyField(
        'AttributeAbility', related_name='spell_by_attribute', through='SpellAttributeLink')

    @property
    def rote_skill(self):
        return self.skill.filter(type="rote") if self.contested else None

    @property
    def rote_attribute(self):
        return self.attribute.filter(type="rote") if self.contested else None
    # Mages can own spells
    mage = models.ManyToManyField(
        'Mage', related_name='spell_by_mage', through='SpellMageLink')
    # Optional contested skill check, e.g. 'Attribute+Skill+Primary arcana vs
    # Attribute+Skill'
    contested = models.BooleanField(default=False)

    @property
    def contested_attribute(self):
        return self.attribute.filter(type="contested") if self.contested else None

    @property
    def contested_skill(self):
        return self.skill.filter(type="contested") if self.contested else None
    # Optional attribute to subtract from casting dicepool,
    # e.g. 'Attribute+Skill+Primary arcana-Resist Attribute'
    resisted = models.BooleanField(default=False)

    @property
    def resisted_attribute(self):
        return self.attribute.filter(type="resisted") if self.resisted else None
    # Spells come from books
    book_ref = GenericRelation('BookReference', null=True, blank=True)

    def __str__(self):
        return self.name


class CharacterArcanumLink(Trait):
    PRIORITY_CHOICES = (
        (0, 'Unassigned'), (1, 'Ruling'), (2, 'Common'), (3, 'Inferior')
    )
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES, default=0)
    mage = models.ForeignKey('Mage')
    arcana = models.ForeignKey('ArcanumAbility')

    class Meta:
        unique_together = ('mage', 'arcana')

    def __str__(self):
        return self.arcana.arcanum.label


class SpellLink(models.Model):
    spell = models.ForeignKey('Spell')

    class Meta:
        abstract = True


class SpellArcanumLink(SpellLink):
    type = models.CharField(max_length=32,
                            choices=(
                                ('primary', 'primary'), ('secondary', 'secondary'), ('optional', 'optional'))
                            )
    value = IntegerRangeField(min_value=1, max_value=10)
    arcana = models.ForeignKey('ArcanumAbility')


class SpellAttributeLink(SpellLink):
    type = models.CharField(max_length=32,
                            choices=(
                                ('resisted', 'resisted'), ('contested', 'contested'), ('rote', 'rote'))
                            )
    attribute = models.ForeignKey('AttributeAbility')


class SpellSkillLink(SpellLink):
    type = models.CharField(max_length=32,
                            choices=(('contested', 'contested'), ('rote', 'rote')), default='Rote'
                            )
    skill = models.ForeignKey('SkillAbility')


class SpellMageLink(SpellLink):
    mage = models.ForeignKey('Mage')
