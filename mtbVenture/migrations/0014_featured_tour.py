# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0013_auto_20150805_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Tour',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('feature_title', models.CharField(max_length=300, blank=True)),
                ('feature_description', models.TextField()),
                ('tour', models.ForeignKey(to='mtbVenture.Tour')),
            ],
        ),
    ]
