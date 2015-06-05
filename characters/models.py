from django.db import models
from nwod_characters.util import IntegerRangeField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from characters.enums import SkillAbility, AttributeAbility, Category  # NOQA
from django.utils import timezone

# import csv

# Create your models here.


class NWODCharacter(models.Model):

    name = models.CharField(max_length=200)
    player = models.ForeignKey('auth.User', related_name="%(class)s_by_user")
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    virtue = models.CharField(choices=VIRTUE_CHOICES, max_length=50)
    vice = models.CharField(choices=VICE_CHOICES, max_length=50)
    integrity = IntegerRangeField(min_value=0, max_value=10, default=7)
    size = IntegerRangeField(min_value=1, max_value=10, default=5)

    TYPE_CHOICES = (
        ('Mortal','Mortal'),
        ('Mage','Mage'),
        ('Werewolf','Werewolf'),
        ('Vampire','Vampire'),
        )

    character_type = models.CharField(max_length=128,choices=TYPE_CHOICES)
    sub_race = models.CharField(max_length=255, null=True, default=None)
    faction = models.CharField(max_length=255, null=True, default=None)