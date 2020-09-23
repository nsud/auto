# Generated by Django 2.2.10 on 2020-09-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200923_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.SmallIntegerField(choices=[(1, 'manual'), (2, 'auto'), (3, 'robot')]),
        ),
    ]
