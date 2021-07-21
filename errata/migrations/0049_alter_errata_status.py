# Generated by Django 3.2.4 on 2021-07-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0048_auto_20200807_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errata',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Editorial Review', 'Editorial Review'), ('K-12 Editorial Review', 'K-12 Editorial Review'), ('Associate Editorial Review', 'Kelsey Editorial Review'), ('Anthony Editorial Review', 'Anthony Editorial Review'), ('Reviewed', 'Reviewed'), ('Completed', 'Completed')], default='New', max_length=100),
        ),
    ]
