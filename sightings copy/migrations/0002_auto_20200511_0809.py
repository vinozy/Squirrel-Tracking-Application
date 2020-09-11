# Generated by Django 3.0.6 on 2020-05-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='age',
            field=models.CharField(choices=[('None', 'None'), ('Juvenile', 'Juvenile'), ('Adult', 'Adult')], default=None, max_length=50, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Gray', 'Gray')], default=None, max_length=50, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='date',
            field=models.DateField(default=None, max_length=50, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=None, max_digits=50, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='location',
            field=models.CharField(choices=[('None', 'None'), ('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], default=None, max_length=50, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=None, max_digits=50, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default=None, max_length=50, verbose_name='Shift'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(default=None, max_length=50, verbose_name='Specific_location'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='unique_id',
            field=models.CharField(default=None, max_length=50, verbose_name='ID'),
        ),
    ]
