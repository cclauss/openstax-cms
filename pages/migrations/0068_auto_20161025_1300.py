# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 18:00
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0067_merge_20161024_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ap',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='ap',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('tagline', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('multicolumn', wagtail.wagtailcore.blocks.StreamBlock((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),), icon='placeholder')), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()))),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='highereducation',
            name='row_3',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_3',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_4',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_5',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
        migrations.AlterField(
            model_name='ourimpact',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), help_text='Callout boxes 940x400, Home page boxes 1464x640', required=False)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),)),
        ),
    ]
