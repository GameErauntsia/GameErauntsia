# Generated by Django 2.2.17 on 2020-12-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer', '0010_gameruser_channel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameruser',
            name='channel_description',
            field=models.TextField(blank=True, null=True, verbose_name='Kanalaren deskribapena'),
        ),
    ]