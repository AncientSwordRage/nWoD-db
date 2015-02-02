# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20150130_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='nwodcharacter',
            name='published_date',
            field=models.DateTimeField(default=None, blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arcana',
            name='name',
            field=models.CharField(max_length=50, choices=[(None, '----'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter'), ('Prime', 'Prime')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spell',
            name='optional_arcana',
            field=models.ManyToManyField(blank=True, choices=[(None, '----'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter'), ('Prime', 'Prime')], null=True, related_name='spell_by_optional_arcanum', to='characters.Arcana', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spell',
            name='primary_arcana',
            field=models.ManyToManyField(related_name='spell_by_primary_arcanum', choices=[(None, '----'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter'), ('Prime', 'Prime')], to='characters.Arcana'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spell',
            name='secondary_arcana',
            field=models.ManyToManyField(blank=True, choices=[(None, '----'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter'), ('Prime', 'Prime')], null=True, related_name='spell_by_secondary_arcanum', to='characters.Arcana', default=None),
            preserve_default=True,
        ),
    ]
