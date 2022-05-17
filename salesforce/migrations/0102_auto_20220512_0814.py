# Generated by Django 3.2.5 on 2022-05-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0101_merge_20220506_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionopportunityrecord',
            name='fall_student_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adoptionopportunityrecord',
            name='spring_student_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adoptionopportunityrecord',
            name='summer_student_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
