# Generated by Django 2.0.13 on 2019-02-25 19:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0188_auto_20190225_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionalpartnership',
            name='program_tab_content',
            field=wagtail.core.fields.StreamField([('tab', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock())])))], null=True),
        ),
    ]
