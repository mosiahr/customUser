# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toast', '0005_auto_20171022_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='toaster',
            name='publish',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Публикация'),
        ),
    ]
