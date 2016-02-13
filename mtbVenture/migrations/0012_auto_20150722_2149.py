# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mtbVenture.models


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0011_auto_20150722_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='gps_track',
            field=models.FileField(upload_to=mtbVenture.models.get_unique_gpx_file_path, blank=True),
        ),
    ]
