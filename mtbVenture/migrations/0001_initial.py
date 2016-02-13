# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('length', models.IntegerField()),
                ('height', models.IntegerField()),
                ('level', models.IntegerField()),
                ('preview_img', models.ImageField(upload_to='')),
                ('video', models.FileField(upload_to='')),
                ('gps_track', models.FileField(upload_to='')),
                ('release_state', models.CharField(max_length=50, choices=[('1', 'uploaded'), ('2', 'in progress'), ('3', 'released')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_change', models.DateTimeField(auto_now=True)),
                ('owner_name', models.CharField(max_length=200)),
                ('owner_email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
                ('clicks', models.IntegerField()),
            ],
        ),
    ]
