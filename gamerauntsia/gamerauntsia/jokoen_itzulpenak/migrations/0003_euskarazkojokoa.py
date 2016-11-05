# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 12:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jokoa', '__first__'),
        ('jokoen_itzulpenak', '0002_auto_20160511_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='EuskarazkoJokoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publikoa_da', models.BooleanField(default=False, verbose_name=b'Publikoa da')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'publikazio data')),
                ('jokoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jokoa.Jokoa')),
                ('plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jokoa.Plataforma')),
            ],
            options={
                'verbose_name': 'Euskarazko jokoa',
                'verbose_name_plural': 'Euskarazko jokoak',
            },
        ),
    ]
