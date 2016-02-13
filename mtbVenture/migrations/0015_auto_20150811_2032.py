# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtbVenture', '0014_featured_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_tour',
            name='feature_description',
            field=models.TextField(blank=True),
        ),
    ]
