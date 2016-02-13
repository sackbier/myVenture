# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mtbVenture.models


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0004_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('video', models.FileField(upload_to=mtbVenture.models.get_unique_video_file_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='tour',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, to='mtbVenture.Tour', related_name='video'),
        ),
    ]
