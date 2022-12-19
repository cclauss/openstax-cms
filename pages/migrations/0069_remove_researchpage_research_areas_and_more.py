# Generated by Django 4.0.8 on 2022-12-19 17:18

from django.db import migrations, models
import pages.custom_blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0068_rename_projects_header_researchpage_research_area_header_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchpage',
            name='research_areas',
        ),
        migrations.AddField(
            model_name='researchpage',
            name='research_area_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='researchpage',
            name='research_areas_list',
            field=wagtail.core.fields.StreamField([('research_area_section', wagtail.core.blocks.StructBlock([('research_area_title', wagtail.core.blocks.CharBlock()), ('research_area_blurb', wagtail.core.blocks.RichTextBlock()), ('research_area_blurb_mobile', wagtail.core.blocks.RichTextBlock()), ('research_areas', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('short_description', wagtail.core.blocks.CharBlock()), ('photo', pages.custom_blocks.APIImageChooserBlock(required=False)), ('cta_text', wagtail.core.blocks.CharBlock(required=False)), ('cta_link', wagtail.core.blocks.URLBlock(required=False)), ('publication', wagtail.core.blocks.URLBlock(required=False)), ('github', wagtail.core.blocks.URLBlock(required=False))])))]))], default=''),
        ),
    ]
