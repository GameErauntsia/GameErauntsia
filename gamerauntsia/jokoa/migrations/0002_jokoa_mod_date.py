# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jokoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokoa',
            name='mod_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 26, 16, 21, 0, 188826, tzinfo=utc), verbose_name=b'modifikazio data'),
        ),
    ]
