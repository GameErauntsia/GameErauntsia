# Generated by Django 2.2.26 on 2022-06-04 08:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("joko_itzulpenak", "0003_auto_20220530_1933"),
    ]

    operations = [
        migrations.RenameField(
            model_name="itzulpenproiektua",
            old_name="url",
            new_name="external_url",
        ),
    ]
