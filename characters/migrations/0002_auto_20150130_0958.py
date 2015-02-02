# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='optional_arcana',
            field=models.ManyToManyField(null=True, default=None, related_name='spell_by_optional_arcanum', to='characters.Arcana', choices=[('Prime', 'Prime'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spell',
            name='secondary_arcana',
            field=models.ManyToManyField(null=True, default=None, related_name='spell_by_secondary_arcanum', to='characters.Arcana', choices=[('Prime', 'Prime'), ('Fate', 'Fate'), ('Mind', 'Mind'), ('Spirit', 'Spirit'), ('Death', 'Death'), ('Forces', 'Forces'), ('Time', 'Time'), ('Space', 'Space'), ('Life', 'Life'), ('Matter', 'Matter')]),
            preserve_default=True,
        ),
    ]
