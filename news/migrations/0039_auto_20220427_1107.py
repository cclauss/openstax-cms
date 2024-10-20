# Generated by Django 3.2.9 on 2022-04-27 16:07

from django.db import migrations
import news.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0038_auto_20220420_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenttype',
            name='blog_content_type',
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='content_types',
            field=wagtail.core.fields.StreamField([('content_type', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('conte_type', news.models.ContentTypeChooserBlock(label='Blog Content Type', required=True, target_model='snippets.BlogContentType'))])))], null=True),
        ),
        migrations.DeleteModel(
            name='BlogType',
        ),
        migrations.DeleteModel(
            name='ContentType',
        ),
    ]
