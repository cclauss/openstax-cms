# Generated by Django 2.0.2 on 2018-04-03 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('books', '0040_auto_20180402_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='community_resources_feature_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_color',
            field=models.CharField(choices=[('blue', 'Blue'), ('deep-green', 'Deep Green'), ('gold', 'Gold'), ('gray', 'Gray'), ('green', 'Green'), ('light-blue', 'Light Blue'), ('light-gray', 'Light Gray'), ('medium-blue', 'Medium Blue'), ('orange', 'Orange'), ('red', 'Red'), ('yellow', 'Yellow')], default='Blue', max_length=255),
        ),
    ]
