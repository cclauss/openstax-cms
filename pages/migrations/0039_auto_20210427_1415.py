# Generated by Django 3.0.4 on 2021-04-27 19:15

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_auto_20210427_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_get_started_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_headline',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_logged_in_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_login_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features_headline',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features_tab1_explore_logged_in_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features_tab1_explore_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features_tab1_heading',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features_tab2_explore_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features_tab2_heading',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='quotes',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('testimonial', wagtail.core.blocks.TextBlock(required=False)), ('author', wagtail.core.blocks.CharBlock(Required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='quotes_headline',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tutor_button_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tutor_demo_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='tutor_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='whats_openstax_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='whats_openstax_donate_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='whats_openstax_give_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='whats_openstax_headline',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='whats_openstax_learn_more_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
