# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('recv_time', models.DateTimeField(verbose_name='receive time')),
            ],
        ),
    ]
