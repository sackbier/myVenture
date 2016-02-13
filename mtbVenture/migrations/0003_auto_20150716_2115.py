# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0002_auto_20150716_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='length',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='level',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
