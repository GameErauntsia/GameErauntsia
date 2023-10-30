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
        ("photologue", "0010_auto_20160105_1307"),
        ("jokoa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Berria",
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
                ("izenburua", models.CharField(max_length=150)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Eremu honetan berri honen URL helbidea zehazten ari zara.",
                        unique=True,
                    ),
                ),
                ("desk", models.TextField(max_length=256)),
                (
                    "publikoa_da",
                    models.BooleanField(
                        default=False, verbose_name="Publikatzeko prest"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("0", "Zirriborroa"), ("1", "Publikoa")],
                        default="0",
                        max_length=1,
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        default=timezone.now(), verbose_name="publikazio data"
                    ),
                ),
                (
                    "mod_date",
                    models.DateTimeField(
                        default=timezone.now(), verbose_name="modifikazio data"
                    ),
                ),
                (
                    "shared",
                    models.BooleanField(
                        default=False,
                        help_text="Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.",
                    ),
                ),
                (
                    "argazkia",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="photologue.Photo",
                    ),
                ),
                (
                    "erabiltzailea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="berriak",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "berria",
                "verbose_name_plural": "berriak",
            },
        ),
        migrations.CreateModel(
            name="Gaia",
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
                ("izena", models.CharField(max_length=64)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Eremu honetan gai honen URL helbidea zehazten ari zara.",
                        unique=True,
                    ),
                ),
                ("desk", models.TextField(blank=True, max_length=256, null=True)),
                (
                    "irudia",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="photologue.Photo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Gaia",
                "verbose_name_plural": "Gaiak",
            },
        ),
        migrations.AddField(
            model_name="berria",
            name="gaia",
            field=models.ManyToManyField(to="berriak.Gaia"),
        ),
        migrations.AddField(
            model_name="berria",
            name="jokoa",
            field=models.ForeignKey(
                blank=True,
                help_text="Artikulu honek joko zehaz batekin loturarik badu, adierazi hemen.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jokoa.Jokoa",
            ),
        ),
    ]
