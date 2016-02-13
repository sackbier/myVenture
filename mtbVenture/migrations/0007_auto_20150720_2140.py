# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0006_remove_tour_preview_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('coord_lat', models.FloatField(blank=True, null=True)),
                ('coord_lng', models.FloatField(blank=True, null=True)),
                ('parent', models.ForeignKey(to='mtbVenture.Place', null=True, blank=True, related_name='child_places')),
                ('tour', models.ForeignKey(to='mtbVenture.Tour', null=True, blank=True, related_name='places')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='tour',
            field=models.ForeignKey(to='mtbVenture.Tour', null=True, blank=True, related_name='videos'),
        ),
    ]
