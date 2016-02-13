# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0012_auto_20150722_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='description_short',
            field=models.TextField(default='short descr.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='video_id',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
