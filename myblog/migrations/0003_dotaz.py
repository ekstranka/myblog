# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20170324_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dotaz',
            fields=[
                ('dotaz_id', models.AutoField(primary_key=True, serialize=False)),
                ('sluzba', models.CharField(max_length=200)),
                ('jmeno', models.CharField(max_length=25)),
                ('prijmeni', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('zprava', models.TextField()),
                ('mobil', models.CharField(max_length=13)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
