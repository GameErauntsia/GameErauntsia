# Generated by Django 2.2.17 on 2021-06-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("berriak", "0004_berria_azpititularra"),
    ]

    operations = [
        migrations.AlterField(
            model_name="berria",
            name="azpititularra",
            field=models.CharField(blank=True, max_length=170, null=True),
        ),
    ]
