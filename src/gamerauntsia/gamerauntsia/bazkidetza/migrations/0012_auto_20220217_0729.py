# Generated by Django 2.2.26 on 2022-02-17 07:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ("bazkidetza", "0011_auto_20220217_0728"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bazkidea",
            name="expire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 17, 7, 29, 54, 935198, tzinfo=utc)
            ),
        ),
    ]
