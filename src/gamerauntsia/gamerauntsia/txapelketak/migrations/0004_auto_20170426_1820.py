# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 16:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ("txapelketak", "0003_auto_20170328_1512"),
    ]

    operations = [
        migrations.AddField(
            model_name="txapelketa",
            name="mod_date",
            field=models.DateTimeField(
                default=datetime.datetime(2017, 4, 26, 16, 20, 20, 648538, tzinfo=utc),
                verbose_name="modifikazio data",
            ),
        ),
        migrations.AlterField(
            model_name="txapelketa",
            name="insk_date",
            field=models.DateTimeField(
                default=datetime.datetime(2017, 4, 26, 16, 20, 20, 648559, tzinfo=utc),
                verbose_name="Izen ematea",
            ),
        ),
        migrations.AlterField(
            model_name="txapelketa",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(2017, 4, 26, 16, 20, 20, 648507, tzinfo=utc),
                verbose_name="Publikazio data",
            ),
        ),
    ]
