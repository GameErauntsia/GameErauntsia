# Generated by Django 2.2.2 on 2019-06-17 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("aurkezpenak", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aurkezpena",
            name="erabiltzailea",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
