# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:51
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
            name="Finished",
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
                ("jokoa", models.CharField(blank=True, max_length=100, null=True)),
                ("fetxa", models.DateTimeField(auto_now_add=True)),
                (
                    "nota",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=3, null=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="finished",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["fetxa"],
            },
        ),
    ]
