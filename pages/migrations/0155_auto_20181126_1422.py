# Generated by Django 2.0.2 on 2018-11-26 20:22

from django.db import migrations
import pages.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0154_auto_20181109_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_images',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())])), ('identifier', wagtail.core.blocks.CharBlock(required=False))], null=True),
        ),
    ]
