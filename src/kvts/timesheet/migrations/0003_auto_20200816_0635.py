# Generated by Django 3.1 on 2020-08-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0002_auto_20200816_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='normal_quarterhours',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='interval',
            name='quarterhours',
            field=models.PositiveIntegerField(),
        ),
    ]
