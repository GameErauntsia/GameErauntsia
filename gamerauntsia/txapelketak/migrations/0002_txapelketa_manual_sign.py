# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("txapelketak", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="txapelketa",
            name="manual_sign",
            field=models.BooleanField(default=False),
        ),
    ]
