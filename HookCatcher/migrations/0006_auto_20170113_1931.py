# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HookCatcher', '0005_auto_20170113_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diff',
            name='url',
            field=models.URLField(),
        ),
    ]
