# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:51
from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("photologue", "0010_auto_20160105_1307"),
        ("jokoa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bazkidea",
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
                ("paid", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("date_joined", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "expire_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2018, 3, 9, 7, 51, 26, 114457, tzinfo=utc
                        )
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Bazkidea",
                "verbose_name_plural": "Bazkideak",
            },
        ),
        migrations.CreateModel(
            name="Eskaera",
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
                ("added", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "bazkidea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bazkidetza.Bazkidea",
                    ),
                ),
            ],
            options={
                "verbose_name": "Eskaera",
                "verbose_name_plural": "Eskaerak",
            },
        ),
        migrations.CreateModel(
            name="Eskaintza",
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
                ("izena", models.CharField(max_length=150)),
                ("slug", models.SlugField()),
                ("deskribapena", models.TextField()),
                (
                    "mota",
                    models.IntegerField(
                        choices=[
                            (1, "Eskatzekoa"),
                            (2, "Parte hartzekoa"),
                            (3, "Eskubidea"),
                        ],
                        default=1,
                    ),
                ),
                ("activate_date", models.DateTimeField(auto_now_add=True)),
                ("expire_date", models.DateTimeField(blank=True, null=True)),
                ("is_public", models.BooleanField(default=False)),
                (
                    "irudia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="photologue.Photo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Eskaintza",
                "verbose_name_plural": "Eskaintza",
            },
        ),
        migrations.CreateModel(
            name="OparitzekoJokoak",
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
                ("key", models.CharField(max_length=250)),
                (
                    "non_aldatzeko",
                    models.IntegerField(
                        choices=[(1, "Steam"), (2, "Origin")], default=1
                    ),
                ),
                ("oparituta", models.BooleanField(default=False)),
                (
                    "pub_date",
                    models.DateTimeField(
                        default=timezone.now(), verbose_name="publikazio data"
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
                "verbose_name": "Oparitzeko jokoa",
                "verbose_name_plural": "Oparitzeko jokoak",
            },
        ),
        migrations.AddField(
            model_name="eskaera",
            name="eskaintza",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bazkidetza.Eskaintza"
            ),
        ),
    ]
