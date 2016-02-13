# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0007_auto_20150720_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='tour',
            field=models.OneToOneField(related_name='places', blank=True, to='mtbVenture.Tour', null=True),
        ),
    ]
