# Generated by Django 2.2.5 on 2019-12-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0029_partner_visible_on_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='affordability_cost',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
