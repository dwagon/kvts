# Generated by Django 3.1 on 2020-08-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_fortnight_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='normal_quarterhours',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
