# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tour',
            name='gps_track',
            field=models.FileField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='length',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='level',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='preview_img',
            field=models.ImageField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='release_state',
            field=models.CharField(default=1, max_length=50, choices=[('1', 'uploaded'), ('2', 'in progress'), ('3', 'released')]),
        ),
        migrations.AlterField(
            model_name='tour',
            name='video',
            field=models.FileField(upload_to='', blank=True),
        ),
    ]
