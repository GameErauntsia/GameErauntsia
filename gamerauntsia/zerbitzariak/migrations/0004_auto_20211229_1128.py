# Generated by Django 2.2.24 on 2021-12-29 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zerbitzariak", "0003_auto_20201220_2147"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mc_whitelist",
            name="mc_user",
        ),
        migrations.RemoveField(
            model_name="mc_whitelist",
            name="uuid",
        ),
    ]
