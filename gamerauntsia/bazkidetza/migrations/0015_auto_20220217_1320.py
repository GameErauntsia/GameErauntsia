# Generated by Django 2.2.26 on 2022-02-17 13:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bazkidetza', '0014_auto_20220217_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bazkidea',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 17, 13, 20, 31, 924457, tzinfo=utc)),
        ),
    ]
