# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("jokoa", "0002_jokoa_mod_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jokoa",
            name="mod_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="modifikazio data"
            ),
        ),
    ]