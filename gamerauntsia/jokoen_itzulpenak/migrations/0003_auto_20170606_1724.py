# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jokoa", "0003_auto_20170606_1607"),
        ("jokoen_itzulpenak", "0002_auto_20170606_1609"),
    ]

    operations = [
        migrations.AddField(
            model_name="euskarazkojokoa",
            name="garatzaileak_itzulia",
            field=models.BooleanField(
                default=False, verbose_name="Garatzaileak itzulia"
            ),
        ),
    ]
