# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:51
from __future__ import unicode_literals

from django.utils import timezone
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photologue', '0010_auto_20160105_1307'),
        ('jokoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlaya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izenburua', models.CharField(max_length=64)),
                ('slug', models.SlugField(help_text=b'Eremu honetan game play honen URL helbidea zehazten ari zara.', unique=True)),
                ('desk', models.TextField(max_length=256)),
                ('iraupena_min', models.IntegerField(default=0)),
                ('iraupena_seg', models.IntegerField(default=0)),
                ('bideoa', models.CharField(blank=True, help_text=b'Eremu honetan Youtube bideoaren URL kodea itsatsi behar duzu. Adb.: c21XAuI3aMo', max_length=100, null=True)),
                ('publikoa_da', models.BooleanField(default=False, verbose_name=b'Publikatzeko prest')),
                ('pub_date', models.DateTimeField(default=timezone.now(), verbose_name=b'publikazio data')),
                ('mod_date', models.DateTimeField(default=timezone.now(), verbose_name=b'modifikazio data')),
                ('status', models.CharField(choices=[(b'0', b'Zirriborroa'), (b'1', b'Publikoa')], default=b'0', max_length=1)),
                ('shared', models.BooleanField(default=False, help_text=b'Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.')),
                ('argazkia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo')),
                ('erabiltzailea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameplayak', to=settings.AUTH_USER_MODEL)),
                ('jokoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameplay', to='jokoa.Jokoa')),
            ],
            options={
                'verbose_name': 'Gameplaya',
                'verbose_name_plural': 'Gameplayak',
            },
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=64)),
                ('slug', models.SlugField(help_text=b'Eremu honetan kategoria honen URL helbidea zehazten ari zara.', unique=True)),
                ('desk', models.TextField(blank=True, max_length=256, null=True)),
                ('irudia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategoriak',
            },
        ),
        migrations.CreateModel(
            name='Zailtasuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=64)),
                ('slug', models.SlugField(help_text=b'Eremu honetan zailtasun honen URL helbidea zehazten ari zara.', unique=True)),
            ],
            options={
                'verbose_name': 'Zailtasuna',
                'verbose_name_plural': 'Zailtasunak',
            },
        ),
        migrations.AddField(
            model_name='gameplaya',
            name='kategoria',
            field=models.ManyToManyField(related_name='gameplay', to='gameplaya.Kategoria'),
        ),
        migrations.AddField(
            model_name='gameplaya',
            name='plataforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameplay', to='jokoa.Plataforma'),
        ),
        migrations.AddField(
            model_name='gameplaya',
            name='zailtasuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameplay', to='gameplaya.Zailtasuna'),
        ),
    ]
