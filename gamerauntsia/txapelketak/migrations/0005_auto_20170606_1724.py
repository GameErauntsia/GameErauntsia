# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("txapelketak", "0004_auto_20170426_1820"),
    ]

    operations = [
        migrations.AlterField(
            model_name="txapelketa",
            name="insk_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Izen ematea"
            ),
        ),
        migrations.AlterField(
            model_name="txapelketa",
            name="mod_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="modifikazio data"
            ),
        ),
        migrations.AlterField(
            model_name="txapelketa",
            name="pub_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Publikazio data"
            ),
        ),
    ]
