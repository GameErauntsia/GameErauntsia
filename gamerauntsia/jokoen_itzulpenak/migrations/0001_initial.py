# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("photologue", "0010_auto_20160105_1307"),
        ("jokoa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Euskalinkak",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("izena", models.CharField(max_length=150, verbose_name="Izena")),
                ("url", models.URLField()),
                (
                    "publikoa_da",
                    models.BooleanField(default=False, verbose_name="Publikoa da"),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="publikazio data"
                    ),
                ),
                (
                    "irudia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="photologue.Photo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Euskal lotura",
                "verbose_name_plural": "Euskal loturak",
            },
        ),
        migrations.CreateModel(
            name="EuskarazkoJokoa",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "publikoa_da",
                    models.BooleanField(default=False, verbose_name="Publikoa da"),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="publikazio data"
                    ),
                ),
                (
                    "jokoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jokoa.Jokoa"
                    ),
                ),
                (
                    "plataforma",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jokoa.Plataforma",
                    ),
                ),
            ],
            options={
                "verbose_name": "Euskarazko jokoa",
                "verbose_name_plural": "Euskarazko jokoak",
            },
        ),
        migrations.CreateModel(
            name="Itzulpena",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("izena", models.CharField(max_length=150, verbose_name="Izena")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "Erdizka"),
                            ("1", "Probatzeko"),
                            ("2", "Amaituta"),
                        ],
                        default="0",
                        max_length=1,
                        verbose_name="Egoera",
                    ),
                ),
                ("ipsfile", models.FileField(upload_to="ips")),
                (
                    "publikoa_da",
                    models.BooleanField(default=False, verbose_name="Publikoa da"),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="publikazio data"
                    ),
                ),
                (
                    "mod_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="modifikazio data"
                    ),
                ),
                (
                    "jokoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jokoa.Jokoa"
                    ),
                ),
                (
                    "plataforma",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jokoa.Plataforma",
                    ),
                ),
            ],
            options={
                "verbose_name": "Itzulpen fitxategia",
                "verbose_name_plural": "Itzulpen fitxategiak",
            },
        ),
    ]