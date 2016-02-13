# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0010_auto_20150720_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='start_lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='start_lng',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
