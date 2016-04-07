# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 16:54
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_book_license_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='license_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Text blurb that describes the license.', null=True),
        ),
    ]
