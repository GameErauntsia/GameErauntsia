# Generated by Django 2.2.17 on 2021-04-02 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gameplaya", "0003_auto_20190617_1316"),
    ]

    operations = [
        migrations.CreateModel(
            name="BideoPlataforma",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("izena", models.CharField(max_length=64)),
                ("embed_url", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Bideo plataforma",
                "verbose_name_plural": "Bideo plataformak",
            },
        ),
        migrations.AlterField(
            model_name="gameplaya",
            name="bideoa",
            field=models.CharField(
                blank=True,
                help_text="Bideoaren URL kodea. Youtube adb.: c21XAuI3aMo Peertube adb.: 544349f5-c7b3-4b31-92cb-a06c96eadfb6",
                max_length=100,
                null=True,
                verbose_name="Bideoaren URL kodea",
            ),
        ),
        migrations.AddField(
            model_name="gameplaya",
            name="bideo_plataforma",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="gameplaya.BideoPlataforma",
                verbose_name="Bideo plataforma",
            ),
        ),
    ]
