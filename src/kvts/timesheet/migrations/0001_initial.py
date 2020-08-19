# Generated by Django 3.1 on 2020-08-19 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('normal_quarterhours', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Fortnight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('current', models.BooleanField(default=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarterhours', models.PositiveIntegerField()),
                ('worktype', models.CharField(choices=[('N', 'Working'), ('S', 'Sick Leave'), ('L', 'Paid Leave'), ('P', 'Public Holiday'), ('Z', 'Sudy Leave')], default='N', max_length=1)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheet.day')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='fortnight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheet.fortnight'),
        ),
        migrations.AddField(
            model_name='day',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timesheet.person'),
        ),
    ]
