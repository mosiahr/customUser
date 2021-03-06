# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toast', '0009_toaster_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 10, 25, 13, 55, 5, 731186, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='publish',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Публикация'),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='toasterlocation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toasterlocation',
            name='publish',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Публикация'),
        ),
        migrations.AddField(
            model_name='toasterlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
