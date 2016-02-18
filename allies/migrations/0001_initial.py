# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ally_category', models.CharField(choices=[('OH', 'Online Homework'), ('AC', 'Adaptive Courseware'), ('CT', 'Customized Tools')], max_length=2)),
                ('heading', models.CharField(max_length=255)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('link_url', models.URLField(blank=True, help_text='Call to Action Link')),
                ('link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]
