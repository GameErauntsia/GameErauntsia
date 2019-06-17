# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MC_Whitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mc_user', models.CharField(max_length=64, verbose_name='MC Erabiltzailea')),
                ('uuid', models.CharField(blank=True, max_length=64, null=True, verbose_name='UUID')),
                ('rol', models.CharField(choices=[('n', 'Normal'), ('v', 'VIP'), ('a', 'Administrator')], default='n', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='GE Erabiltzailea')),
            ],
            options={
                'verbose_name': 'MC Erabiltzailea',
                'verbose_name_plural': 'MC Erabiltzaileak',
            },
        ),
    ]
