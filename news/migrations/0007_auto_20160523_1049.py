# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20160523_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='pin_to_top',
            field=models.BooleanField(default=False),
        ),
    ]
