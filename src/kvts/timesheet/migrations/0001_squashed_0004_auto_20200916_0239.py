# Generated by Django 3.1 on 2020-09-16 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('timesheet', '0001_initial'), ('timesheet', '0002_unique_intervals'), ('timesheet', '0003_auto_20200902_0131'), ('timesheet', '0004_auto_20200916_0239')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fortnight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('current', models.BooleanField(default=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('fortnight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheet.fortnight')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('leave_qh', models.PositiveIntegerField(default=0)),
                ('normal_qh', models.PositiveIntegerField(default=32)),
                ('publich_qh', models.PositiveIntegerField(default=0)),
                ('sick_qh', models.PositiveIntegerField(default=0)),
                ('study_qh', models.PositiveIntegerField(default=0)),
                ('worked_qh', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]