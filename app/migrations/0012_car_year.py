# Generated by Django 2.2.10 on 2020-09-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, default=2020, null=True),
        ),
    ]
