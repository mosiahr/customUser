# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toast', '0010_auto_20171025_1357'),
    ]

    operations = [
        migrations.RenameModel('ToasterLocation', 'Location')

    ]
