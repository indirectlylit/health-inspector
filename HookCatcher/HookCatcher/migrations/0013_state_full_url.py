# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HookCatcher', '0012_auto_20171109_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='full_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
