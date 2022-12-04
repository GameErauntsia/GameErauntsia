# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 08:59
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gameruser",
            name="added",
        ),
        migrations.RemoveField(
            model_name="gameruser",
            name="added_source",
        ),
        migrations.RemoveField(
            model_name="gameruser",
            name="is_admin",
        ),
        migrations.RemoveField(
            model_name="gameruser",
            name="modified",
        ),
        migrations.RemoveField(
            model_name="gameruser",
            name="usertype",
        ),
        migrations.AddField(
            model_name="gameruser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=30, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="gameruser",
            name="last_name",
            field=models.CharField(blank=True, max_length=30, verbose_name="last name"),
        ),
        migrations.AlterField(
            model_name="gameruser",
            name="bio",
            field=models.TextField(blank=True, null=True, verbose_name="Biografia"),
        ),
        migrations.AlterField(
            model_name="gameruser",
            name="fullname",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Izen abizenak"
            ),
        ),
        migrations.AlterField(
            model_name="gameruser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AlterField(
            model_name="gameruser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AlterField(
            model_name="gameruser",
            name="phone",
            field=models.CharField(
                blank=True, max_length=25, null=True, verbose_name="Telefonoa"
            ),
        ),
        migrations.AlterField(
            model_name="gameruser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.ASCIIUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
