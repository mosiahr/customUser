# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('accounts', '0002_auto_20171108_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': set([]), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
    ]
