# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voivodeships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voivodeship',
            name='wazny_do',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voivodeship',
            name='wazny_od',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voivodeship',
            name='wersja_do',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voivodeship',
            name='wersja_od',
            field=models.DateField(blank=True, null=True),
        ),
    ]
