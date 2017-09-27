# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-27 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0036_auto_20170707_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kindle_link',
            field=models.URLField(blank=True, help_text='Link to Kindle version'),
        ),
    ]
