# Generated by Django 2.2.17 on 2021-01-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("berriak", "0003_auto_20190617_1316"),
    ]

    operations = [
        migrations.AddField(
            model_name="berria",
            name="azpititularra",
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
