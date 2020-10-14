# Generated by Django 3.1 on 2020-10-14 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_auto_20201001_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeefortnight',
            name='fortnight',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='timesheet.fortnight'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fortnight',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]