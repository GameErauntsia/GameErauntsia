# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atala',
            name='mod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'modifikazio data'),
        ),
        migrations.AlterField(
            model_name='atala',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'publikazio data'),
        ),
    ]
