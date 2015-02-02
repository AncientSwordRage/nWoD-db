# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import nwod_characters.util


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arcana',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, choices=[('Prime', 'Prime'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter')])),
                ('value', nwod_characters.util.IntegerRangeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, choices=[('Mental', (('Intelligence', 'Intelligence'), ('Wits', 'Wits'), ('Resolve', 'Resolve'))), ('Physical', (('Strength', 'Strength'), ('Dexterity', 'Dexterity'), ('Stamina', 'Stamina'))), ('Social', (('Presence', 'Presence'), ('Manipulation', 'Manipulation'), ('Composure', 'Composure')))])),
                ('value', nwod_characters.util.IntegerRangeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NWODCharacter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('sub_race', models.CharField(max_length=50)),
                ('faction', models.CharField(null=True, max_length=50)),
                ('power_level', nwod_characters.util.IntegerRangeField()),
                ('energy_trait', nwod_characters.util.IntegerRangeField()),
                ('virtue', models.CharField(max_length=50, choices=[('prudence', 'Prudence'), ('justice', 'Justice'), ('temperance', 'Temperance'), ('fortitude', 'Fortitude'), ('faith', 'Faith'), ('hope', 'Hope'), ('charity', 'Charity')])),
                ('vice', models.CharField(max_length=50, choices=[('lust', 'Lust'), ('gluttony', 'Gluttony'), ('greed', 'Greed'), ('sloth', 'Sloth'), ('wrath', 'Wrath'), ('envy', 'Envy'), ('pride', 'Pride')])),
                ('morality', nwod_characters.util.IntegerRangeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('nwodcharacter_ptr', models.OneToOneField(serialize=False, primary_key=True, to='characters.NWODCharacter', parent_link=True, auto_created=True)),
            ],
            options={
            },
            bases=('characters.nwodcharacter',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, choices=[('Mental', (('Academics', 'Academics'), ('Computer', 'Computer'), ('Crafts', 'Crafts'), ('Investigation', 'Investigation'), ('Medicine', 'Medicine'), ('Occult', 'Occult'), ('Politics', 'Politics'), ('Science', 'Science'))), ('Physical', (('Athletics', 'Athletics'), ('Brawl', 'Brawl'), ('Drive', 'Drive'), ('Firearms', 'Firearms'), ('Larceny', 'Larceny'), ('Stealth', 'Stealth'), ('Survival', 'Survival'), ('Weaponry', 'Weaponry'))), ('Social', (('Animal Ken', 'Animal Ken'), ('Empathy', 'Empathy'), ('Expression', 'Expression'), ('Intimidation', 'Intimidation'), ('Persuasion', 'Persuasion'), ('Socialize', 'Socialize'), ('Streetwise', 'Streetwise'), ('Subterfuge', 'Subterfuge')))])),
                ('value', nwod_characters.util.IntegerRangeField()),
                ('character', models.ForeignKey(related_name='skill_by_skill', to='characters.NWODCharacter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vulgar', models.BooleanField(default=False)),
                ('contested', models.BooleanField(default=False)),
                ('resisted', models.BooleanField(default=False)),
                ('contested_attribute', models.ManyToManyField(blank=True, related_name='spell_by_contested_attribute', default=None, choices=[('Mental', (('Intelligence', 'Intelligence'), ('Wits', 'Wits'), ('Resolve', 'Resolve'))), ('Physical', (('Strength', 'Strength'), ('Dexterity', 'Dexterity'), ('Stamina', 'Stamina'))), ('Social', (('Presence', 'Presence'), ('Manipulation', 'Manipulation'), ('Composure', 'Composure')))], to='characters.Attribute')),
                ('contested_skill', models.ManyToManyField(blank=True, related_name='spell_by_contested_skill', default=None, choices=[('Mental', (('Academics', 'Academics'), ('Computer', 'Computer'), ('Crafts', 'Crafts'), ('Investigation', 'Investigation'), ('Medicine', 'Medicine'), ('Occult', 'Occult'), ('Politics', 'Politics'), ('Science', 'Science'))), ('Physical', (('Athletics', 'Athletics'), ('Brawl', 'Brawl'), ('Drive', 'Drive'), ('Firearms', 'Firearms'), ('Larceny', 'Larceny'), ('Stealth', 'Stealth'), ('Survival', 'Survival'), ('Weaponry', 'Weaponry'))), ('Social', (('Animal Ken', 'Animal Ken'), ('Empathy', 'Empathy'), ('Expression', 'Expression'), ('Intimidation', 'Intimidation'), ('Persuasion', 'Persuasion'), ('Socialize', 'Socialize'), ('Streetwise', 'Streetwise'), ('Subterfuge', 'Subterfuge')))], to='characters.Skill')),
                ('mage', models.ManyToManyField(related_name='spell_by_mage', to='characters.Mage')),
                ('optional_arcana', models.ManyToManyField(null=True, related_name='spell_by_optional_arcanum', choices=[('Prime', 'Prime'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter')], to='characters.Arcana')),
                ('primary_arcana', models.ManyToManyField(related_name='spell_by_primary_arcanum', choices=[('Prime', 'Prime'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter')], to='characters.Arcana')),
                ('resisted_by_attribute', models.ManyToManyField(blank=True, related_name='dice_pools_by_resistance_attribute', default=None, choices=[('Resolve', 'Resolve'), ('Stamina', 'Stamina'), ('Composure', 'Composure')], to='characters.Attribute')),
                ('rote_attribute', models.ManyToManyField(related_name='spell_by_rote_attribute', choices=[('Mental', (('Intelligence', 'Intelligence'), ('Wits', 'Wits'), ('Resolve', 'Resolve'))), ('Physical', (('Strength', 'Strength'), ('Dexterity', 'Dexterity'), ('Stamina', 'Stamina'))), ('Social', (('Presence', 'Presence'), ('Manipulation', 'Manipulation'), ('Composure', 'Composure')))], to='characters.Attribute')),
                ('rote_skill', models.ManyToManyField(related_name='spell_by_rote_skill', choices=[('Mental', (('Academics', 'Academics'), ('Computer', 'Computer'), ('Crafts', 'Crafts'), ('Investigation', 'Investigation'), ('Medicine', 'Medicine'), ('Occult', 'Occult'), ('Politics', 'Politics'), ('Science', 'Science'))), ('Physical', (('Athletics', 'Athletics'), ('Brawl', 'Brawl'), ('Drive', 'Drive'), ('Firearms', 'Firearms'), ('Larceny', 'Larceny'), ('Stealth', 'Stealth'), ('Survival', 'Survival'), ('Weaponry', 'Weaponry'))), ('Social', (('Animal Ken', 'Animal Ken'), ('Empathy', 'Empathy'), ('Expression', 'Expression'), ('Intimidation', 'Intimidation'), ('Persuasion', 'Persuasion'), ('Socialize', 'Socialize'), ('Streetwise', 'Streetwise'), ('Subterfuge', 'Subterfuge')))], to='characters.Skill')),
                ('secondary_arcana', models.ManyToManyField(null=True, related_name='spell_by_secondary_arcanum', choices=[('Prime', 'Prime'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter')], to='characters.Arcana')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nwodcharacter',
            name='player',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attribute',
            name='character',
            field=models.ForeignKey(related_name='attribute_by_attribute', to='characters.NWODCharacter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arcana',
            name='mage',
            field=models.ForeignKey(related_name='mage_by_arcana', to='characters.Mage'),
            preserve_default=True,
        ),
    ]
