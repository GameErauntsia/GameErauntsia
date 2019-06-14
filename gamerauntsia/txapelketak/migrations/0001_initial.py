# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photologue', '0010_auto_20160105_1307'),
        ('jokoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partaidea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(blank=True, max_length=64, null=True)),
                ('irabazlea', models.BooleanField(default=False)),
                ('win', models.IntegerField(default=0, verbose_name='Irabazitakoak')),
                ('lose', models.IntegerField(default=0, verbose_name='Galdutakoak')),
                ('draw', models.IntegerField(default=0, verbose_name='Berdindutakoak')),
                ('matches', models.IntegerField(default=0, verbose_name='Jokatutakoak')),
                ('average', models.FloatField(default=0, verbose_name='Gorabeherakoa')),
                ('points', models.IntegerField(default=0, verbose_name='Puntuak')),
                ('irudia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo')),
                ('jokalariak', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Titularrak')),
                ('kapitaina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kapitaina', to=settings.AUTH_USER_MODEL)),
                ('ordezkoak', models.ManyToManyField(blank=True, related_name='ordezkoak', to=settings.AUTH_USER_MODEL, verbose_name='Ordezkoak')),
            ],
            options={
                'verbose_name': 'Partaidea',
                'verbose_name_plural': 'Partaideak',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jardunaldia', models.IntegerField(default=1, verbose_name='Jardunaldia')),
                ('emaitza', models.CharField(blank=True, max_length=50, null=True)),
                ('average', models.CharField(blank=True, max_length=50, null=True)),
                ('is_return', models.BooleanField(default=False, verbose_name='Itzulerakoa')),
                ('is_playoff', models.BooleanField(default=False, help_text='Markatu hau txapelketa konbinatu bateko playoff-aren partida bat bada', verbose_name='Playoff motakoa')),
                ('bideoa', models.CharField(blank=True, max_length=150, null=True)),
                ('start', models.IntegerField(blank=True, null=True, verbose_name='Hasiera')),
                ('end', models.IntegerField(blank=True, null=True, verbose_name='Bukaera')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='txapelketak.Partida')),
                ('partaideak', models.ManyToManyField(blank=True, to='txapelketak.Partaidea')),
            ],
            options={
                'verbose_name': 'Partida',
                'verbose_name_plural': 'Partidak',
            },
        ),
        migrations.CreateModel(
            name='Txapelketa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=64)),
                ('slug', models.SlugField(help_text='Eremu honetan kategoria honen URL helbidea zehazten ari zara.', unique=True)),
                ('desk', models.TextField(blank=True, max_length=256, null=True)),
                ('arauak', models.TextField(blank=True, max_length=256, null=True)),
                ('saria', models.TextField(blank=True, max_length=256, null=True)),
                ('mota', models.CharField(choices=[('0', 'Kanporaketa'), ('1', 'Liga'), ('2', 'Konbinatua')], default='0', max_length=1)),
                ('modalitatea', models.CharField(choices=[('0', 'Bakarka'), ('1', 'Taldeka')], default='0', max_length=1)),
                ('status', models.CharField(choices=[('0', 'Izen ematea zabalik'), ('1', 'Partidak sortzen'), ('2', 'Txapelketa jokuan'), ('3', 'Bukatuta')], default='0', max_length=1)),
                ('live_bideoa', models.CharField(blank=True, help_text='Eremu honetan bideoaren URL kodea itsatsi behar duzu. Adb.: c21XAuI3aMo', max_length=100, null=True)),
                ('twitch', models.BooleanField(default=False)),
                ('hashtag', models.CharField(blank=True, max_length=100, null=True)),
                ('irabazi', models.IntegerField(default=0, verbose_name='Puntuak irabaztean')),
                ('galdu', models.IntegerField(default=0, verbose_name='Puntuak galtzean')),
                ('berdinketa', models.IntegerField(default=0, verbose_name='Puntuak berdinketan')),
                ('publikoa_da', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Publikazio data')),
                ('insk_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Izen ematea')),
                ('shared', models.BooleanField(default=False)),
                ('adminak', models.ManyToManyField(related_name='tx_adminak', to=settings.AUTH_USER_MODEL, verbose_name='Egileak')),
                ('irudia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo')),
                ('jokalariak', models.ManyToManyField(blank=True, related_name='jokalariak', to=settings.AUTH_USER_MODEL, verbose_name='Inskripzioa')),
                ('jokoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jokoa.Jokoa')),
            ],
            options={
                'verbose_name': 'Txapelketa',
                'verbose_name_plural': 'Txapelketak',
            },
        ),
        migrations.AddField(
            model_name='partida',
            name='txapelketa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='txapelketak.Txapelketa'),
        ),
        migrations.AddField(
            model_name='partaidea',
            name='txapelketa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='txapelketak.Txapelketa'),
        ),
    ]
