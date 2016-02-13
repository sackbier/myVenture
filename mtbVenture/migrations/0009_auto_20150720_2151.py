# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0008_auto_20150720_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='tour',
        ),
        migrations.AddField(
            model_name='tour',
            name='place',
            field=models.ForeignKey(null=True, blank=True, to='mtbVenture.Place'),
        ),
    ]
