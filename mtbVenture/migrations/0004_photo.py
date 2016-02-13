# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mtbVenture.models


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0003_auto_20150716_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to=mtbVenture.models.get_unique_image_file_path)),
                ('tour', models.ForeignKey(to='mtbVenture.Tour', null=True, blank=True, related_name='photos')),
            ],
        ),
    ]
