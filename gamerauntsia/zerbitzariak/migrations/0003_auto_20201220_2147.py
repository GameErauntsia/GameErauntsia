# Generated by Django 2.2.17 on 2020-12-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerbitzariak', '0002_auto_20190617_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mc_whitelist',
            name='rol',
            field=models.CharField(choices=[('g', 'Guest'), ('n', 'Normal'), ('v', 'VIP'), ('a', 'Administrator')], default='g', max_length=1),
        ),
    ]
