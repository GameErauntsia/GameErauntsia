# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jokoa", "0003_auto_20170606_1607"),
        ("jokoen_itzulpenak", "0003_auto_20170606_1724"),
    ]

    operations = [
        migrations.AddField(
            model_name="euskarazkojokoa",
            name="plataformak",
            field=models.ManyToManyField(to="jokoa.Plataforma"),
        ),
    ]
